"""
File: validEmailAddress_2.py
Name: 
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  '@' in the email
feature2:  '.' before @
feature3:  '..' in the email
feature4:  some string before @
feature5:  if '@' not in the email
feature6:  if '.@' in the email
feature7:  there is popular domain name in the email
feature8:  there is some strange mark and space in the str
feature9:  . before the @
feature10: length of email more then 10

Accuracy of your model: TODO:
"""
import numpy as np

WEIGHT = np.array([               # The weight vector selected by you
	[0.2],
	[-0.1],
	[-0.5],
	[0.5],
	[-1],
	[-1.2],
	[1],
	[-0.8],
	[0.7],
	[-1.1]
])

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	weight_vector = WEIGHT.T
	is_email_arr = np.zeros(len(maybe_email_list))
	is_email_arr[13:] = 1
	is_correct_arr = np.zeros(len(maybe_email_list))  # 0/1 for wrong/correct

	for i, maybe_email in enumerate(maybe_email_list):
		feature_vector = feature_extractor(maybe_email)
		score = weight_vector.dot(feature_vector)
		if is_email_arr[i] and score > 0 or not is_email_arr[i] and score < 0:
			is_correct_arr[i] = 1
	print('Accuracy of this model: %.5f' % (np.mean(is_correct_arr)))

def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	strange_mark1 = '#:%\\[]$ '
	top_level_domains = ['.net', '.org', '.edu', '.tw']
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@', 1)[0] else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if '..' in maybe_email else 0
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@', 1)[0] else 0
		elif i == 4:
			feature_vector[i] = 1 if '@' not in maybe_email else 0
		elif i == 5:
			feature_vector[i] = 1 if '.@' in maybe_email else 0
		elif i == 6:
			for ch in top_level_domains:
				if ch in maybe_email:
					feature_vector[i] = 1
					break
				else:
					feature_vector[i] = 0
		elif i == 7:
			for ch in strange_mark1:
				if ch in maybe_email:
					feature_vector[i] = 1
					break
				else:
					feature_vector[i] = 0
		elif i == 8:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@', 1)[1] else 0
		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	email_lst = []
	with open(DATA_FILE, 'r') as f:
		for line in f:
			email_lst.append(line)
	return email_lst


if __name__ == '__main__':
	main()
