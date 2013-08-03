Script pro comando MSG no playSMS
=================================

Por padrão, o playSMS só aceita que um dos membros de um grupo mande SMS pra
todo mundo -– o que criou o grupo na interface web. 

Esse script permite criar uma palavra-chave pra que um membro de um grupo com o
código "#VOZ" no nome possa mandar mensagens pra todos os outros membros,
através do seu próprio celular.

Por enquanto, o script só suporta mensagens sem acentuação.

Dependências
------------

(além do playSMS, claro)

- Python 2.5, 2.6 ou 2.7
- Dependências do python:
    - MySQL-python
    - docopt

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
    - Marcar "Make return as reply".
    - Copiar caminho presente em *Caminho de execução do comando SMS* para usar no próximo passo

5. Copiar os arquivos `config.py` e `msg.py` pro diretório copiado no passo
anterior -- por exemplo, `/var/lib/playsms/sms_command/1/`


Uso
---

Para dar a um celular a permissão pra mandar mensagens pra todos os membros de
um grupo, adicione o celular ao grupo com o código `#VOZ` no nome (por exemplo,
"Robertinho #VOZ").

Robertinho pode então falar com todo o grupo mandando um SMS no seguinte formato:

```
msg <codigo_grupo> <mensagem>
```

Por exemplo:

```
msg turma reuniao as 5h
```
