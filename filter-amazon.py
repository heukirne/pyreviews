
import sys, gzip, json, datetime
sys.path.append("./pylinguistics/pylinguistics/")

import Pylinguistics as pl
import descriptive
import pandas as pd
import numpy as np

df = {}
i = 0 
columns = []

g = gzip.open('reviews-amazon.json.gz', 'r')
for l in g:
	review_json = json.loads(l)

	date = int(datetime.datetime.strptime(review_json['reviewTime'], "%m %d, %Y").strftime("%Y%m%d"))
	thumbs = int(review_json['helpful'][0]) + int(review_json['helpful'][1])

	if date > 20050915 and date < 20130924 and thumbs > 0:
		try:
			review_pd = []

			objpl = pl.text(review_json['reviewText'],'en')
			#print objpl.getFeatures()

			if columns == []:
				for attr in objpl.getFeatures():
					columns.append(attr)

			for attr in objpl.getFeatures():
				review_pd.append(str(objpl.getFeatures()[attr]))

			review_pd.append(review_json['helpful'][0])
			review_pd.append(review_json['helpful'][1])
			review_pd.append(int(review_json['overall']))

			df[i] = review_pd

			sys.stdout.write(str(i))
		except:
			sys.stdout.write('e')

	i += 1
	if i > 35000:
		break

reviews = pd.DataFrame.from_dict(df, orient='index')
columns.extend(['thumbsup','thumbsdown','stars'])
reviews.columns = columns
reviews.to_csv('experiments/amazon-help.csv.gz', compression='gzip')