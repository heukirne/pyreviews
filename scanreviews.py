#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
import numpy as np
import datetime
from os import walk

listReadUp = []
listReadDown = []
listUp = []
listDown = []
count = 0
countThumbs = 0

date_ini = 20160101
date_end = 0

mypath = "reviews/Celular_e_Smartphone/5.0/"
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

            objreview.evaluation_date
            date = int(datetime.datetime.strptime(objreview.evaluation_date, "%d/%m/%Y").strftime("%Y%m%d"))

            if date > date_end: #20130924
                date_end = date
            if date < date_ini: #20050915
                date_ini = date

            objpl = pl.text(objreview.opinion)
            objpl.language = "pt";

            # DEBUG
            #print reviewfile
            #print objpl.summary()
            #print len(objreview.opinion) > 10
            #print objreview.opinion
            #print('Redability: %s' %objpl.getFeatures()['redability'])
            #print('ThumbsUp: %s' %objreview.thumbsup)
            #print('ThumbsDown: %s' %objreview.thumbsdown)

            # APPEND LISTS
            if objreview.thumbsup != objreview.thumbsdown:
                countThumbs += 1
                if len(objreview.opinion) > 10 and int(objreview.thumbsup) > 0:
                    listReadUp.append(float(objpl.getFeatures()['redability']))
                    listUp.append(int(objreview.thumbsup))

                if len(objreview.opinion) > 10 and int(objreview.thumbsdown) > 0:
                    listReadDown.append(float(objpl.getFeatures()['redability']))
                    listDown.append(int(objreview.thumbsdown))

                if count % 100 == 0:
                    sys.stdout.write(str(total - count))
                    sys.stdout.write(',')
                    sys.stdout.flush()

            # DEBUG
            #break

    print ' '
    print('Count Thumbs: %s' %countThumbs)
    print ' '
    print 'Redability x ThumbsUp Pearson Correlation Coefficients'
    print np.corrcoef(listReadUp,listUp)
    print 'Redability x ThumbsDown Pearson Correlation Coefficients'
    print np.corrcoef(listReadDown,listDown)

    print('Date Ini: %i' %date_ini)
    print('Date End: %i' %date_end)

    break