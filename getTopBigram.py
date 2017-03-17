import pickle
from collections import OrderedDict
import heapq # for getting top 5

pickleDumps = "pickleDumps/"
conditionalProbabilityFile = pickleDumps+"conditionalProbabilityDict.p"
bigramsListPath = pickleDumps + "bigramsList.p"

file = open(conditionalProbabilityFile,"rb")
conditionalProbabilityDict = pickle.load(file)

file = open(bigramsListPath,"rb")
bigramsList = pickle.load(file)

while True:
	checkForThisBigram = raw_input("Enter a word to predict its next probable words ('rikenrocks' for stopping) : ")

	if checkForThisBigram == "rikenrocks":
		break;

	# empty the list, for new iteration
	matchedBigrams = [] # all bigrams that starts with the inputted word
	for bigram in bigramsList:
		if checkForThisBigram == bigram[1]:
			matchedBigrams.append(bigram[1]+" "+bigram[2])

	# print matchedBigrams
	topDict = {}
	for singleBigram in matchedBigrams:
		topDict[singleBigram] = conditionalProbabilityDict[singleBigram]

	topBigrams = heapq.nlargest(5, topDict, key=topDict.get)
	for b in topBigrams:
		print b+" : "+str(topDict[b])+"\n"

	print "\n" + "____________________" + "\n"
