#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

fich = sys.argv[-1]

parser = make_parser()
MyHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(MyHandler)
parser.parse(open(fich))
fichero = MyHandler.get_tags()

if len(sys.argv) == 2:
    for datos in fichero:
        print(datos)
else:
    print("usage: python3 karaoke.py file.smil.")


