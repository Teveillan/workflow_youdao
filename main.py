#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urllib
import json
import sys
from workflow import Workflow, web
'''
parameters = { "keyfrom" : "teveillanus",
               "key" : "1663705644",
               "type" : "data",
               "doctype" : "json",
               "version" : "1.1",
               "q" : "你好"}
'''
#url = "http://fanyi.youdao.com/openapi.do?%s" % (urllib.urlencode(parameters))


class Youdao(object):
    def __init__(self):
        self.keyfrom = "teveillanus"
        self.key = "1663705644"
        self.type = "data"
        self.doctype = "json"
        self.version = "1.1"
        self.query = ""
        self.youdao_url = "http://fanyi.youdao.com/openapi.do?"

    def get_para(self, query_word=""):
        parameters = {"keyfrom": self.keyfrom,
                      "key": self.key,
                      "type": self.type,
                      "doctype": self.doctype,
                      "version": self.version,
                      "q": query_word}
        return parameters

    def get_url(self, query_word=""):
        parameters = self.get_para(query_word)
        url = "http://fanyi.youdao.com/openapi.do?%s" % (urllib.urlencode(parameters))
        return url

    def get_response(self, query_word=""):
        url = youdao.get_url(query_word)
        req = urllib.urlopen(url)
        return req.read()

def main(wf):
    youdao = Youdao()
    query_word = sys.argv[1]
    res = youdao.get_response(query_word)


if __name__ == "__main__":
    wf = Workflow()
    logger = wf.logger
    sys.exit(wf.run(main))

