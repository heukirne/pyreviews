#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
import numpy as np
from os import walk

listReadUp = []
listReadDown = []
listUp = []
listDown = []
count = 0

mypath = "reviews/Celular e Smartphone/5.0/"
for (dirpath, dirnames, filenames) in walk(mypath):
    print('Total: %s' %len(filenames))
    total = len(filenames)
    for (reviewfile) in filenames:
        count += 1
        if '.xml' in reviewfile:
            # DEBUG
            #reviewfile = 'minus_11_406309.xml'

            # READ XML
            objreview = rp.parseit(mypath + reviewfile)
            objpl = pl.text(objreview.opinion)
            objpl.language = "pt-br";

            # DEBUG
            #print reviewfile
            #print len(objreview.opinion) > 10
            #print objreview.opinion
            #print('Redability: %s' %objpl.getFeatures()['redability'])
            #print('ThumbsUp: %s' %objreview.thumbsup)
            #print('ThumbsDown: %s' %objreview.thumbsdown)

            # APPEND LISTS
            if len(objreview.opinion) > 10 and int(objreview.thumbsup) > 0:
                listReadUp.append(float(objpl.getFeatures()['redability']))
                listUp.append(int(objreview.thumbsup))

            if len(objreview.opinion) > 10 and int(objreview.thumbsup) > 0:
                listReadDown.append(float(objpl.getFeatures()['redability']))
                listDown.append(int(objreview.thumbsdown))

            if count % 100 == 0:
                sys.stdout.write(str(total - count))
                sys.stdout.write(',')
                sys.stdout.flush()

            # DEBUG
            #break

    print ' '
    print 'Redability x ThumbsUp Cross-Correlation'
    print np.correlate(listReadUp, listUp)
    print 'Redability x ThumbsUp Pearson Correlation Coefficients'
    print np.corrcoef(listReadUp,listUp)
    print 'Redability x ThumbsDown Cross-Correlation'
    print np.correlate(listReadDown, listDown)
    print 'Redability x ThumbsDown Pearson Correlation Coefficients'
    print np.corrcoef(listReadDown,listDown)

    break