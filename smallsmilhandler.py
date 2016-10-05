#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.Lista = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.root_layout = {'width': attrs.get('width', ""),
                                'height': attrs.get('height',""),
                                'background-color': attrs.get('background-color',"")}
            self.Lista.append(self.root_layout)

        elif name == 'region':
            self.region = {'id': attrs.get('id', ""),
                           'top': attrs.get('top',""),
                           'bottom': attrs.get('bottom',""),
                           'left': attrs.get('left',""),
                           'right': attrs.get('right',"")}
            self.Lista.append(self.region)

    def get_tags(self):

        return self.Lista
      
if __name__ == "__main__":


    parser = make_parser()
    MyHandler = SmallSMILHandler()
    parser.setContentHandler(MyHandler)
    parser.parse(open('karaoke.smil'))
    Listado = MyHandler.get_tags()

    for infor in Listado:
        print(infor)
