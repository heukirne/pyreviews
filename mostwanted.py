#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
import numpy as np
from os import walk

count = 0

mostUpcount = 0
mostUpfile = ""

mostDowncount = 0
mostDownfile = ""

mypath = "reviews/Celular e Smartphone/5.0/"
for (dirpath, dirnames, filenames) in walk(mypath):
    print('Total: %s' %len(filenames))
    total = len(filenames)
    for (reviewfile) in filenames:
        count += 1
        if '.xml' in reviewfile:
            # READ XML
            objreview = rp.parseit(mypath + reviewfile)

            if objreview.thumbsup != objreview.thumbsdown:
                if objreview.thumbsup > mostUpcount:
                    mostUpcount = objreview.thumbsup
                    mostUpfile = reviewfile

                if objreview.thumbsdown > mostDowncount:
                    mostDowncount = objreview.thumbsdown
                    mostDownfile = reviewfile

                if count % 100 == 0:
                    sys.stdout.write(str(total - count))
                    sys.stdout.write(',')
                    sys.stdout.flush()

            # DEBUG
            #break

    print ' '
    print ' '
    print('Most Up Review: %s' %mostUpcount)
    print mostUpfile
    objreview = rp.parseit(mypath + mostUpfile)
    objpl = pl.text(objreview.opinion)
    objpl.language = "pt-br";
    print objreview.opinion
    print('Features: %s' %objpl.getFeatures())
    print('POS_TAGS: %s' %objpl.postag)

    print ' '
    print('Most Down Review: %s' %mostDowncount)
    print mostDownfile
    objreview = rp.parseit(mypath + mostDownfile)
    objpl = pl.text(objreview.opinion)
    objpl.language = "pt-br";
    print objreview.opinion
    print('Features: %s' %objpl.getFeatures())
    print('POS_TAGS: %s' %objpl.postag)

    break