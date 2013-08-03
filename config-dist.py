#!/usr/bin/env python
# -*- coding: utf-8 -*-
CONFIG = {
    # configurações do msg.py
    'msg': {
        'debug': False,
        'logfile': '/var/log/playsms/sms.log',
    },


    # configurações do banco de dados - copie do config.php do playSMS
    'db': {
        'host': '', # host
        'port': '', # porta
        'user': '', # usuário
        'pass': '', # senha
        'name': '', # nome do banco de dados
        'pref': '', # prefixo das tabelas
    },

    # configurações da interface web do playSMS
    'webapp': {
        'username': '',
        'token': '',
        'url': 'http://example.com/playsms/',
    }
}en
