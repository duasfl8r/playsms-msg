Script pro comando MSG no playSMS
=================================

Dependências
------------

(além do playSMS, claro)

- Python 2.5, 2.6 ou 2.7
- Dependências do python:
    - MySQL-python
    - docopt: 

Instalação
----------

1. Na tela *My Account > Preferências*, habilitar os campos:
    - New webservices token
    - Enable webservices

2. Ao salvar as preferências, o seu *token de webservices*, um código de letras
e números, vai aparecer no campo *Webservices token*. Copie-o pra usar no
próximo passo.

3. Copiar o arquivo `config-dist.py` pra `config.py` e preencher seus campos de configuração.

4. Na tela *Recursos > Administrar comandos*, criar um novo comando:

    - Configurar "Palavra-chave do comando SMS"  para ``MSG``
    - Configurar "Comando executado"  pra ``msg.py {SMSSENDER} {COMMANDPARAM}``
"MSG" (ou outro, se preferir).
    - Marcar "Make return as reply".
    - Copiar caminho presente em *Caminho de execução do comando SMS* para usar no próximo passo

5. Copiar os arquivos `config.py` e `msg.py` pro diretório copiado no passo
anterior -- por exemplo, `/var/lib/playsms/sms_command/1/`

