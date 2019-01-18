#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import pymysql

# conn = pymysql.connect(host='185.74.252.15', port=3306, user='wladi984', passwd='uRvL98GUDi', db='wladi984_vkuser')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
cursor = conn.cursor()

i_group = "INSERT INTO groups (`id_group`, `name`) VALUES (%s,%s)"
s_group = "SELECT id_group FROM groups"
i_qeury = "INSERT INTO query (`text`) VALUES (%s)"
s_qeury = "SELECT text FROM query"



aut = [
    {
        'count': 0,
        'account': [
            {'login': '79056363387','pass': 'TU3IIU'},
            {'login': '79025000549','pass': 'gOvv5BJM'},
            {'login': '79782601923','pass': '4pIZeLBu0x'},
            {'login': '79520028738','pass': 'WTFnx7'},
        ]
    }
]