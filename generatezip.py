#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, gzip, chardet

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
from os import walk

noheader = 0
index = 0
csvgz = gzip.open('experiments/reviews.csv.gz', 'wb')

mypath = "reviews/"
for (dirnone, categories, filenone) in walk(mypath):
    for category in categories:
        categorypath = mypath + category + '/'
        for (dirnull, versions, filenull) in walk(categorypath):
            for version in versions:
                versionpath = categorypath + version + '/'
                for (dirpath, dirnames, filenames) in walk(versionpath):
                    print("\nTotal %s files in %s  " % (len(filenames), versionpath))
                    total = len(filenames)
                    count = 0
                    for (reviewfile) in filenames:
                        count += 1
                        if '.xml' in reviewfile:
                            # READ XML
                            #reviewfile = '2_42055.xml'
                            #print reviewfile
                            try:
                                objreview = rp.parseit(versionpath + reviewfile)
                            except:
                                objreview = 0

                            if objreview != 0 and objreview.thumbsup != objreview.thumbsdown and len(objreview.opinion) > 10:

                                # READ XML
                                objpl = pl.text(objreview.opinion)
                                objpl.language = "pt-br";

                                # WRITE HEADER
                                if noheader == 0:
                                    for attr in objpl.getFeatures():
                                        csvgz.write(',' + attr)
                                    # WITH VALUES
                                    csvgz.write(',thumbsup,thumbsdown,stars,user,category,evaluation_date,recommends\n')
                                    noheader = 1

                                # WRITE ATTRIBUTES
                                index += 1
                                attributes = str(index) + ","
                                for attr in objpl.getFeatures():
                                    attributes += str(objpl.getFeatures()[attr]) + ','
                                # WITH VALUES
                                attributes += objreview.thumbsup + ','
                                attributes += objreview.thumbsdown + ','
                                attributes += objreview.stars + ','
                                attributes += objreview.user + ','
                                attributes += objreview.category + ','
                                attributes += objreview.evaluation_date + ','
                                attributes += objreview.recommends

                                csvgz.write(attributes + '\n');

                                if count % 100 == 0:
                                    sys.stdout.write(str(total - count))
                                    sys.stdout.write(',')
                                    sys.stdout.flush()

                        break #file
                break #version
        #break #category

csvgz.close();