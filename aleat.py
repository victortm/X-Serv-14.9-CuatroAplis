#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

class aleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        randNum = (int(random.randrange(1,1001)) + int
                  (random.randrange(1,1001))) * 1000000
        resp = ("<html><body><h1> Acceso a pagina aleatoria" +
                "</h1>" "<a href= http:" + "/aleat/" + str(randNum) + 
                ">Dame otra</a> </body></html>\r\n")
        return ("200 OK", resp)
