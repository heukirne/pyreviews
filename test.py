#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import pandas as pd

text = "O rato roeu a roupa do rei de Roma."

print text

objpl = pl.text(text)

objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))


 