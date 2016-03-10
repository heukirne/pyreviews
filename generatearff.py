#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
from os import walk

count = 0
noheader = 0
arff = open('cellphone-reviews.arff', 'w')
arff.write('@RELATION reviews\n')

mypath = "reviews/Celular_e_Smartphone/5.0/"
for (dirpath, dirnames, filenames) in walk(mypath):
    print('Total: %s' %len(filenames))
    total = len(filenames)
    for (reviewfile) in filenames:
        count += 1
        if '.xml' in reviewfile:
            # READ XML
            objreview = rp.parseit(mypath + reviewfile)

            if objreview.thumbsup != objreview.thumbsdown and len(objreview.opinion) > 10:

                # READ XML
                objpl = pl.text(objreview.opinion)
                objpl.language = "pt-br";

                # WRITE HEADER
                if noheader == 0:
                    for attr in objpl.getFeatures():
                        arff.write('@ATTRIBUTE ' + attr + '\tNUMERIC\n')
                    arff.write('@ATTRIBUTE thumbsup\tNUMERIC\n')
                    arff.write('@ATTRIBUTE thumbsdown\tNUMERIC\n')
                    arff.write('@DATA\n')
                    noheader = 1

                # WRITE ATTRIBUTES
                attributes = ""
                for attr in objpl.getFeatures():
                    attributes += str(objpl.getFeatures()[attr]) + ','
                attributes += objreview.thumbsup + ','
                attributes += objreview.thumbsdown

                arff.write(attributes + '\n');

                if count % 100 == 0:
                    sys.stdout.write(str(total - count))
                    sys.stdout.write(',')
                    sys.stdout.flush()

            # DEBUG
            break

    arff.close();
    break