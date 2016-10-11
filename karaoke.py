#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class KaraokeLocal():

    def __init__(self, fichero):

        parser = make_parser()
        MyHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(MyHandler)
        parser.parse(open(fichero))
        self.lista = MyHandler.get_tags()

    def __str__(self):
        for etiqueta in fichero:
            dicc_etiqueta = etiqueta[0]
            for atributo in etiqueta:
                dicc_atributo = atributo[0]

    if len(sys.argv) == 2:
        for datos in fichero:
            print(datos)
    else:
        print("usage: python3 karaoke.py file.smil.")


