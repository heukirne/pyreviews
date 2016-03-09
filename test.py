#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import chardet

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import pandas as pd

if 'TRAVIS' in os.environ and os.environ['TRAVIS'] == 'yes':
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


objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))