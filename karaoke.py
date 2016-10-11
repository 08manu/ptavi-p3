#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

#fich = sys.argv[-1]

def imprimir(fich):
    parser = make_parser()
    MyHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(MyHandler)
    parser.parse(open(fich))
    fichero = MyHandler.get_tags()

if __name__ == '__main__':

    fich = sys.argv[-1]
    print(imprimir(fich))
    for datos in fichero:
        print(datos)


