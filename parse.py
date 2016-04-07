import argparse
import json
import codecs
import os
import itertools
from collections import defaultdict
from nltk import word_tokenize, sent_tokenize



def main(datadir):
	testing = ['2016', '2008', '1976']
	megadict = defaultdict(lambda: {})
	for filename in os.listdir(datadir):
		year = filename.split('_')[0]
		f = open(datadir + '/' + filename, 'r')
		data = json.load(f)
		f.close()
		if year not in testing:
			for name, v in dict.iteritems(data):
				for date, text in dict.iteritems(v):
					sentences = sent_tokenize("".join(text))
					words = [word_tokenize(t) for t in sentences]
					for index, w in enumerate(words):
						words[index] = [x.lower() for x in w]
					megadict[name][date] = words
	newf = open(datadir + '/parsed.json' , 'w')
	newf.write(json.dumps(megadict))
	newf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("datadir", help="directory where dataset is located", type=str)
	args = parser.parse_args()

	main(args.datadir)