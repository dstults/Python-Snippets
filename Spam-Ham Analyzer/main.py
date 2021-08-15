import pandas as pd

# ===============================================================================
# Customize your Usage Here
# ===============================================================================

# Note: The sample spam blog-post data included in this repository is too short
#       to be of any use, you will need to acquire your own similar data for this
#       to be of any value. It's just to demonstrate the format.

# The path to the list of already-classified known spam and ham messages
trainedData = 'sms-collection-training-short.txt'

# The list of things you want to see if they are spam or not
testData = 'sms-collection-test.txt'

# ===============================================================================
# Prepare the Training Data
# ===============================================================================

# TODO: This needs a try-catch or using for file not found / etc.
def getSanitizedDataFromTrainingFile(fileName):
	print("Loading Training File: " + fileName)
	data = pd.read_csv(fileName, sep="\t", header=None)
	data_clean = pd.DataFrame(data)
	data_clean.columns = ['0label', '0text']
	data_clean['0text'] = sanitizeText(data_clean['0text'])
	return data_clean

# TODO: This needs a try-catch or using for file not found / etc.
def getTestFile(fileName):
	print("Loading Test File: " + fileName)
	data = pd.read_csv(fileName, sep="\t", header=None)
	data_clean = pd.DataFrame(data)
	data_clean.columns = ['0text']
	data_clean['0text'] = sanitizeText(data_clean['0text'])
	return data_clean

def sanitizeText(text):
	print("Sanitizing text...")
	text = text.str.replace('\W+', ' ').str.replace('\s+', ' ').str.strip()
	text = text.str.lower()
	text = text.str.split()
	return text

print('Commencing training file input process.')

trainingData = getSanitizedDataFromTrainingFile(trainedData)
# TODO: Get it to append multiple files to the same massive training data clean var
#training_data &= getSanitizedDataFromTrainingFile('SMSSpamCollection2.short')

print('Training files loaded and sanitized.')

# ===============================================================================
# Train the Data
# ===============================================================================

print('Training the data, this might take a while...')

# Create frequency table
vocabulary = list(set(trainingData['0text'].sum()))
word_counts_per_sms = pd.DataFrame([
	[row[1].count(word) for word in vocabulary]
	for _, row in trainingData.iterrows()], columns=vocabulary)
trainingData = pd.concat([trainingData.reset_index(), word_counts_per_sms], axis=1).iloc[:,1:]
# print(train_data.style)
# print(tabulate(train_data, headers='keys', tablefmt='psql'))
probabilityOfSpam = trainingData['0label'].value_counts()['spam'] / trainingData.shape[0]
probabilityOfHam = trainingData['0label'].value_counts()['ham'] / trainingData.shape[0]
numberSpam = trainingData.loc[trainingData['0label'] == 'spam', '0text'].apply(len).sum()
numberHam = trainingData.loc[trainingData['0label'] == 'ham', '0text'].apply(len).sum()
vocabularySize = len(trainingData.columns) - 3
# print(test_data)

print('Data training complete.')

# ===============================================================================
# Test the Trained Data against Real Messages
# ===============================================================================

def probabilityWordIsSpam(word):
	# alpha = priming coefficient for when no data or word
	alpha = 1
	if word in trainingData.columns:
		# BUG: this will throw an error if the "word" is the same as trainingData column names
		#      needs further research to prevent: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
		return (trainingData.loc[trainingData['0label'] == 'spam', word].sum() + alpha) / (numberSpam + alpha * vocabularySize)
	else:
		return 1

def probabilityWordIsHam(word):
	# alpha = priming coefficient for when no data or word
	alpha = 1
	if word in trainingData.columns:
		# BUG: this will throw an error if the "word" is the same as trainingData column names
		#      needs further research to prevent: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
		return (trainingData.loc[trainingData['0label'] == 'ham', word].sum() + alpha) / (numberHam + alpha * vocabularySize)
	else:
		return 1

def classifyAsSpamOrHam(message):
	pSpamForMessage = probabilityOfSpam
	pHamForMessage = probabilityOfHam
	for word in message:
		try:
			pSpamForMessage *= probabilityWordIsSpam(word)
			pHamForMessage *= probabilityWordIsHam(word)
		except:
			print("Error classifying word:", word)
			print("Error with message:", message)
			exit()
	if pHamForMessage > pSpamForMessage:
		return 'ham'
	elif pHamForMessage < pSpamForMessage:
		return 'spam'
	else:
		return 'needs human classification'

# For readability below
def listToString(rowData):
	return ' '.join(rowData)

print('Getting real data to test against the trained data.')

test_data = getTestFile(testData)

print('Testing the trained data against the real data.')

for _, row in test_data.iterrows():
	print(classifyAsSpamOrHam(row['0text']) + " | MSG: " + listToString(row['0text']))

# TODO: Output to somewhere for production purposes

print('\nProgram gracefully terminated.\n')
