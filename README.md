# Meu BB
Testando se consigo acessar o BB usando o splinter de dentro de um container.

**OBS: ainda não tem nada pronto, apenas um container que já ta com o splinter configurado para entrar no BB**

# Instalação
## Requerimentos
 * [Docker](https://docs.docker.com/engine/installation/ "Instalar Docker")
 * [Docker-Compose](https://docs.docker.com/compose/install/#install-using-pip "Instalar Docker-Compose")
 * X11/Xorg (com env var $XAUTHORITY definida, caso seu OS já não faça isso)

## Certificado do BB como trusted
Na sua maquina entre no banco do brasil e quando ele perguntar se quer confiar no certificado, verifique se o certificado é valido, e se for, selecione que sim, e marque a opção para não perguntar isso novamente.

Em seguida copie o arquivo `trusted.certs`, que fica dentro da pasta `security` da sua [pasta do java deployments](http://docs.oracle.com/javase/7/docs/technotes/guides/jweb/jcp/properties.html#location), para dentro da pasta `java_conf/security/` na raiz do projeto.

**TODO:** fazer/usar algum script que leia o certificado do BB de `/data/java_confs/...` assim não precisa ficar buscando o `trusted.certs` da maquina host.

## Configurando firefox
Creio que não precisa??

## Preparando o Container
`docker-compose build app`
Caso de erro tentando copiar o `trusted.certs`, então é por que você esqueceu de fazer o passo [Certificado do BB como trusted](#certificado-do-bb-como-trusted)

# Rodando
`docker-compose run --rm python bb.py`

# Agradecimentos
Quero agradecer ao [@marioidival](https://github.com/marioidival) por me ajudar a encontrar o [tweet a respeito](https://twitter.com/henriquebastos/status/676335721125425152) disso, ao [@luzfcb](https://github.com/luzfcb) pela dica do Splinter, e ao [@henriquebastos](https://github.com/henriquebastos) por instigar a ideia.

#Licença
Distribuido sob licença MIT, veja o arquivo LICENSE para mais informações.