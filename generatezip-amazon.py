#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, gzip, chardet, json, datetime

sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl

noheader = 0
i = 0
csvgz = gzip.open('experiments/reviews-amazon.csv.gz', 'wb')

g = gzip.open('reviews-amazon.json.gz', 'r')
for l in g:
    review_json = json.loads(l)

    date = int(datetime.datetime.strptime(review_json['reviewTime'], "%m %d, %Y").strftime("%Y%m%d"))
    thumbs = int(review_json['helpful'][0]) + int(review_json['helpful'][1])

    if date > 20050915 and date < 20130924 and thumbs > 0:

            try:
                objpl = pl.text(review_json['reviewText'],'en')

                # WRITE HEADER
                if noheader == 0:
                    for attr in objpl.getFeatures():
                        csvgz.write(',' + attr)
                    # WITH VALUES
                    csvgz.write(',thumbsup,thumbsdown,stars\n')
                    noheader = 1

                # WRITE ATTRIBUTES
                attributes = str(i) + ","
                for attr in objpl.getFeatures():
                    attributes += str(objpl.getFeatures()[attr]) + ','
                # WITH VALUES
                attributes += str(review_json['helpful'][0])  + ','
                attributes += str(review_json['helpful'][1])  + ','
                attributes += str(review_json['overall'])

                csvgz.write(attributes + '\n');
                sys.stdout.write(str(i))
                i += 1
            except:
                sys.stdout.write('e')

    if i > 35000:
        break

g.close();
csvgz.close();