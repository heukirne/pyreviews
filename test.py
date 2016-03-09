#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, chardet

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
import numpy as np

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
    print('ThumbsUp: %s' %objreview.thumbsup)
    print('ThumbsDown: %s' %objreview.thumbsdown)

objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))
a = [1,4,6]
b = [1,2,3] 
print np.correlate(a, b)
print np.corrcoef(a,b)