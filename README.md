# Meu BB
Testando se consigo acessar o BB usando o splinter de dentro de um container.

# O que ele faz?
Loga no BB, e baixa o extrato da sua conta corrente (mes atual), no formato `.csv` na pasta `extratos`, com nome de `extrato_XXXXX.csv` (onde *XXXXX* é o timestamp de quando foi baixado o extrato).

# Instalação
## Requerimentos
 * [Docker](https://docs.docker.com/engine/installation/ "Instalar Docker")
 * [Docker-Compose](https://docs.docker.com/compose/install/#install-using-pip "Instalar Docker-Compose")
 * X11/Xorg (com env var $XAUTHORITY definida, caso seu OS já não faça isso)

## Certificado do BB como trusted
Na sua maquina entre no banco do brasil e quando ele perguntar se quer confiar no certificado, verifique se o certificado é valido, e se for, selecione que sim, e marque o checkbox para não perguntar isso novamente.
Isso vai fazer com que o certificado do Banco do brasil fique salvo em sua maquina.

Em seguida copie o arquivo `trusted.certs`, que fica dentro da pasta `security` da sua [pasta do java deployments](http://docs.oracle.com/javase/7/docs/technotes/guides/jweb/jcp/properties.html#location), para dentro da pasta `java_conf/security/` na raiz do projeto.

**TODO:** fazer/usar algum script que leia o certificado do BB de `/data/java_confs/...` assim não precisa ficar buscando o `trusted.certs` da maquina host.

## Configurando firefox
Creio que não precisa??

## Preparando o Container
`docker-compose build app`
Caso de erro tentando copiar o `trusted.certs`, então é por que você esqueceu de fazer o passo [Certificado do BB como trusted](#certificado-do-bb-como-trusted)

# Rodando
Basta setar as variaveis de ambiente `AG`, `CC`, `SE` para sua **agencia**, **conta corrente**, e **senha da internet** respectivamente, antes de iniciar o container, ex:

`AG='XXXXXX' CC='XXXXXX' SE='XXXXXXXX'docker-compose run --rm python bb.py`

# Agradecimentos
Quero agradecer ao [@marioidival](https://github.com/marioidival) por me ajudar a encontrar o [tweet a respeito](https://twitter.com/henriquebastos/status/676335721125425152) disso, ao [@luzfcb](https://github.com/luzfcb) pela dica do Splinter e snippet de codigo, e ao [@henriquebastos](https://github.com/henriquebastos) por instigar a ideia.

#Licença
Distribuido sob licença MIT, veja o arquivo LICENSE para mais informações.