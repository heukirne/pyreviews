
import sys, gzip, json, datetime
sys.path.append("../pylinguistics/pylinguistics/")

import Pylinguistics as pl
import descriptive
import pandas as pd
import numpy as np

df = {}
i = 0 

g = gzip.open('reviews-amazon.json.gz', 'r')
for l in g:
	review_json = json.loads(l)

	date = int(datetime.datetime.strptime(review_json['reviewTime'], "%m %d, %Y").strftime("%Y%m%d"))

	if date > 20050915 and date < 20130924:
		try:
			objpl = pl.text(review_json['reviewText'])

			review_pd = []
			review_pd.append(descriptive.word_count(objpl))
			review_pd.append(review_json['helpful'][0])
			review_pd.append(review_json['helpful'][1])
			review_pd.append(int(review_json['overall']))

			df[i] = review_pd

			i += 1
			sys.stdout.write(str(i))
		except:
			sys.stdout.write('e')

	if i > 35000:
		break

reviews = pd.DataFrame.from_dict(df, orient='index')
reviews.columns = ['word_count','thumbsup','thumbsdown','stars']
reviews.to_csv('experiments/amazon-help.csv.gz', compression='gzip')