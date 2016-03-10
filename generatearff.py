#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import reviewparser as rp
from os import walk

noheader = 0
arff = open('cellphone-reviews.arff', 'w')
arff.write('@RELATION reviews\n')

mypath = "reviews/Celular_e_Smartphone/"
for (dirnone, subdirs, filenone) in walk(mypath):
    for subdir in subdirs:
        #subdir = '4.0'
        for (dirpath, dirnames, filenames) in walk(mypath + subdir):
            print("\nTotal %s files in %s  " % (len(filenames), subdir))
            total = len(filenames)
            count = 0
            for (reviewfile) in filenames:
                count += 1
                if '.xml' in reviewfile:
                    # READ XML
                    #reviewfile = '2_42055.xml'
                    #print reviewfile
                    try:
                        objreview = rp.parseit(mypath + subdir + '/' + reviewfile)
                    except:
                        objreview = 0

                    if objreview != 0 and objreview.thumbsup != objreview.thumbsdown and len(objreview.opinion) > 10:

                        # READ XML
                        objpl = pl.text(objreview.opinion)
                        objpl.language = "pt-br";

                        # WRITE HEADER
                        if noheader == 0:
                            for attr in objpl.getFeatures():
                                arff.write('@ATTRIBUTE ' + attr + '\tNUMERIC\n')
                            # WITH VALUES
                            arff.write('@ATTRIBUTE thumbsup\tNUMERIC\n')
                            arff.write('@ATTRIBUTE thumbsdown\tNUMERIC\n')
                            # WITH CLASS
                            arff.write('@ATTRIBUTE class\t{up,down}\n')
                            arff.write('@DATA\n')
                            noheader = 1

                        # WRITE ATTRIBUTES
                        attributes = ""
                        for attr in objpl.getFeatures():
                            attributes += str(objpl.getFeatures()[attr]) + ','
                        # WITH VALUES
                        attributes += objreview.thumbsup + ','
                        attributes += objreview.thumbsdown + ','
                        # WITH CLASS
                        if objreview.thumbsup > objreview.thumbsdown:
                            attributes += 'up'
                        else:
                            attributes += 'down'

                        arff.write(attributes + '\n');

                        if count % 100 == 0:
                            sys.stdout.write(str(total - count))
                            sys.stdout.write(',')
                            sys.stdout.flush()

                #break #file
        #break #subdir

arff.close();