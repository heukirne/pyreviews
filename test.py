#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, chardet

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp

if 'TRAVIS' in os.environ:
    #SAMPLE TEXT
    text = "O rato roeu a roupa do rei de Roma."
    print text
    objpl = pl.text(text)
else:
    # READ FILE
    file = open('reviews/Celular e Smartphone/5.0/0_100112.txt', 'r')
    text = file.read()
    print('Charset: %s' %chardet.detect(text))
    objpl = pl.text(text.decode(chardet.detect(text)['encoding']))

    # READ XML
    objreview = rp.parseit("reviews/Celular e Smartphone/5.0/0_100112.xml")
    objpl = pl.text(objreview.opinion)

objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))