# -*- coding: utf-8 -*-
import os
from splinter import Browser

AG = os.environ.get('AG')
CC = os.environ.get('CC')
SE = os.environ.get('SE')


if __name__ == "__main__":
    b = Browser(
        'firefox',
        profile_preferences={
            'security.enable_java': True,
            'plugin.state.java': 2,
        }
    )
    import ipdb; ipdb.set_trace()
    b.driver.set_page_load_timeout(8)
    # driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
    b.visit('https://www2.bancobrasil.com.br/aapf/login.jsp')

    b.fill('dependenciaOrigem', AG)
    b.fill('numeroContratoOrigem', CC)
    b.fill('senhaConta', SE)
    b.find_by_id('botaoEntrar').click()
    import ipdb; ipdb.set_trace()
    b.windows[0].close()

    # form = b.find_by_id('aapfModal').first
    # bt_fechar_modal = form.find_by_css('.botaoToolBarFechar').first
