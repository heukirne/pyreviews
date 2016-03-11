#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, chardet

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
import pandas as pd

if 'TRAVIS' in os.environ:
    #SAMPLE TEXT
    text = "O rato roeu a roupa do rei de Roma."
    print text
    objpl = pl.text(text)
else:
    # READ XML
    objreview = rp.parseit("reviews/Celular_e_Smartphone/5.0/0_100112.xml")
    objpl = pl.text(objreview.opinion)
    print('ThumbsUp: %s' %objreview.thumbsup)
    print('ThumbsDown: %s' %objreview.thumbsdown)

    # READ CSV
    reviewscsv = pd.read_csv('experiments/reviews.csv')
    reviewscsv.get('word_count')

objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))