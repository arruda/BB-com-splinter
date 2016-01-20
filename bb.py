# -*- coding: utf-8 -*-
import os
import time
import datetime
from splinter import Browser

AG = os.environ.get('AG')
CC = os.environ.get('CC')
SE = os.environ.get('SE')
DOWNLOAD_DIR = os.environ.get('EXTRATOS_DIR', '/data/extratos')


def login_bb(browser):
    browser.visit('https://www2.bancobrasil.com.br/aapf/login.jsp')

    time.sleep(10)
    browser.fill('dependenciaOrigem', AG)
    browser.fill('numeroContratoOrigem', CC)
    browser.fill('senhaConta', SE)
    browser.find_by_id('botaoEntrar').click()
    time.sleep(10)
    #dando reload no lugar de tentar fechar o modal, pois algumas vezes o modal pode ficar com o bt escondido
    # o proprio reload fecha esse modal.
    browser.reload()


def renomear_extrato():
    downloaded_file_name = os.path.join(DOWNLOAD_DIR, 'extrato.csv')
    novo_nome = os.path.join(DOWNLOAD_DIR,
                             'extrato_{}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    os.rename(downloaded_file_name, novo_nome)
    print("Extrato salvo em: {}".format(novo_nome))


def download_extrato(browser):
    time.sleep(2)
    browser.find_by_css(
        "div.conteudo:nth-child(4) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1)"
    ).mouse_over()

    time.sleep(4)
    browser.find_by_css(
        "div.conteudo:nth-child(4) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)"
    ).click()

    time.sleep(4)

    browser.find_by_css(".botaoToolBarSalvar").click()
    time.sleep(1)
    browser.find_by_css(".csv").click()
    time.sleep(4)


def open_browser():
    prefs = {
        'security.enable_java': True,
        'plugin.state.java': 2,
        'browser.download.folderList': 2,
        'browser.download.saveLinkAsFilenameTimeout': 1,
        'browser.download.manager.showWhenStarting': False,
        'browser.download.dir': DOWNLOAD_DIR,
        'browser.download.downloadDir': DOWNLOAD_DIR,
        'browser.download.defaultFolder': DOWNLOAD_DIR,
        'browser.helperApps.neverAsk.saveToDisk': "text/csv,application/pdf,application/x-pdf,application/octet-stream",
        'pdfjs.disabled': True,
        'plugin.scan.plid.all': False,
        'plugin.scan.Acrobat': "99.0"
    }
    with Browser('firefox', profile_preferences=prefs) as browser:
        try:
            #setando tamanho minimo da tela
            browser.driver.set_window_size(1000, 800)
            login_bb(browser)
            download_extrato(browser)
            renomear_extrato()
        except:
            browser.windows[0].close()
            browser.quit()

if __name__ == "__main__":
    open_browser()
