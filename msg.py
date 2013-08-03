#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage: msg.py [options] <remetente> <grupo_e_mensagem>

Options:
    -d --debug      Mostra mensagens de debug
"""

import sys
from urllib import urlencode
from urllib2 import urlopen
import logging, logging.config

sys.path.append('/usr/share/python-support/python-mysqldb/')

import MySQLdb
from docopt import docopt

from config import CONFIG

# LOGGING

logfile_level = logging.DEBUG if CONFIG['msg']['debug'] else logging.INFO
stdout_level = logging.INFO

logger = logging.getLogger("msg")
logger.setLevel(logfile_level)

short_formatter = logging.Formatter('%(message)s')
long_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(CONFIG['msg']['logfile'])
fh.setLevel(logfile_level)
fh.setFormatter(long_formatter)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(stdout_level)
ch.setFormatter(short_formatter)

logger.addHandler(ch)
logger.addHandler(fh)

def contatos_do_grupo(codigo_grupo):
    """
    Retorna uma lista com os contatos de um grupo

    Argumentos:

    - codigo: uma string com o código do grupo, como cadastrado no playSMS
    """

    db = MySQLdb.connect(host=CONFIG['db']['host'], user=CONFIG['db']['user'], passwd=CONFIG['db']['pass'], db=CONFIG['db']['name'])

    group_table_name = CONFIG['db']['pref'] + '_toolsPhonebook_group'

    cur = db.cursor()

    command = 'SELECT id FROM %s WHERE code = %%s' % (group_table_name,)

    cur.execute(command, codigo_grupo.upper())

    try:
        gpid = cur.fetchone()[0]
    except TypeError:
        logger.info('O grupo "%s" não foi encontrado' % (codigo_grupo))
        exit(-1)

    contact_table_name = CONFIG['db']['pref'] + '_toolsPhonebook'

    command = 'SELECT mobile, name FROM %s WHERE gpid=%%s' % (contact_table_name,)

    cur.execute(command, gpid)

    return cur.fetchall()

def tem_voz(contato):
    if '#VOZ' in contato[1]:
        return True
    return False

def enviar_bc(codigo_grupo, mensagem):
    query = urlencode({
        'app': 'webservices',
        'u': CONFIG['webapp']['username'],
        'h': CONFIG['webapp']['token'],
        'ta': 'bc',
        'to': codigo_grupo,
        'msg': mensagem,
    })

    url = CONFIG['webapp']['url'] + '?' + query

    logger.debug('BC Webservices URL: ' + url)

    response = urlopen(url)
    logger.info(response.read())

def msg(remetente, codigo_grupo, mensagem):
    contatos = contatos_do_grupo(codigo_grupo)

    if len([c for c in contatos if c[0] == remetente]):
        contatos_voz = filter(tem_voz, contatos)
        if len([c for c in contatos_voz if c[0] == remetente]):
            logger.info('Enviando mensagem para grupo "%s"' % (codigo_grupo,))
            enviar_bc(codigo_grupo, mensagem)
        else:
            logger.info('O remetente "%s" não tem voz no grupo "%s"' % (remetente, codigo_grupo))
    else:
        logger.info('O remetente "%s" não é membro do grupo "%s"' % (remetente, codigo_grupo))

if __name__ == '__main__':
    args = docopt(__doc__)

    remetente = args['<remetente>']
    codigo_grupo, mensagem = args['<grupo_e_mensagem>'].split(None, 1)

    if args['--debug']:
        ch.setLevel(logging.DEBUG)

    logger.debug("SYS.ARGV: %s" % (str(sys.argv),))
    logger.debug("DOCOPT ARGS: %s" % (args,))
    msg(remetente, codigo_grupo, mensagem)
