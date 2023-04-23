"""
File: validEmailAddress.py
Name: 
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	count = 0  # distinguish valid and invalid
	score = 0
	correct_email = 0  # correct identification
	maybe_email_list = read_in_data()
	for maybe_email in maybe_email_list:
		count += 1
		feature_vector = feature_extractor(maybe_email)
		for i in range(len(WEIGHT)):
			score += feature_vector[i] * WEIGHT[i][0]
		if count <= 13:
			if score < 0:
				correct_email += 1
		else:
			if score > 0:
				correct_email += 1
		score = 0
	print('The accuracy is ', round(correct_email / 26, 5))



def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:  # only check when @ in the str
				feature_vector[i] = 1 if '.' not in maybe_email.split('@', 1)[0] else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@', 1)[0] else 0
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@', 1)[1] else 0
		elif i == 4:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@', 1)[1] else 0
		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email[-4:] == '.com' else 0
		elif i == 7:
			feature_vector[i] = 1 if maybe_email[-4:] == '.edu' else 0
		elif i == 8:
			feature_vector[i] = 1 if maybe_email[-3:] == '.tw' else 0
		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	email_lst = []
	with open(DATA_FILE, 'r') as f:
		for line in f:
			email_lst.append(line)
	return email_lst


if __name__ == '__main__':
	main()
