# =====================================================
# Python course (Fall 2016)
# Homework exercise
# Day 5 (2016/10/18)
# Exercise 1
# Create a class for parsing FASTA files
#
# By Ka Lok Li
# =====================================================

import matplotlib.pyplot as plt
import os

class FastaParser(object):
	""" A class for parsing a FASTA file """
	def __init__(self, path = ""):
		""" Read and parse the FASTA file """

		# If "path" is an empty string, it means that the user does not input any path or
		# the user input an empty path. In both cases, raise TypeError
		if path == "":
			raise TypeError("File path is missing.")
		# If the path does not exist, raise IOError 
		elif not os.path.exists(path):
			raise IOError('File path "%s" does not exist.' % path)

		# A list which stores the ID of all sequences
		key_list = []
		# A dictionary which stores the actual sequences
		sequence = {}

		# Open the FASTA file
		f_handle = open(path, 'r')

		# Loop through each line in the file
		for line in f_handle:
			# If the line starts with ">", it is an ID
			if line.startswith('>') == True:
				name = line[1:].strip('\n')
				# Append the name to the "key_list"
				key_list.append(name)
				# Initialize a dictionary entry with "name" as the key
				sequence[name] = ''
			else:
				# Add the sequence to the dictionary entry
				sequence[name] += line.strip('\n')

		# Close the file
		f_handle.close()

		self.key_list = key_list
		self.sequence = sequence

		# Set the total number of sequences
		self.count = len(key_list)

	def __len__(self):
		""" To implement the built-in function "len()".
		    This method returns the total number of sequences. """
		return self.count

	def __getitem__(self, index):
		""" To implement evaluation of "self[index]".
		    If "index" is an integer, the method returns the sequence which has that index.
		    If "index" is a string, the method returns the sequence which has that ID """
		if type(index) == int:
			if index >= self.count:
				raise IndexError("Index out of range.")
				
			key = self.key_list[index]
			return self.sequence[key]

		elif type(index) == str:
			if index not in self.key_list:
				raise KeyError('No ID called "%s".' % index)

			return self.sequence[index]

	def extract_length(self, max_len):
		""" Given an integer "max_len", the method returns all sequences that are shorter
		    than "max_len". The output is a list. """
		shorter_list = []

		for item in self.sequence:
			cur_sequence = self.sequence[item]

			if len(cur_sequence) < max_len:
				shorter_list.append(cur_sequence)

		return shorter_list

	def length_dist(self, location):
		""" The method creates a histogram of the length distribution of the sequences.
		    The figure is saved as a PDF file in "location". """

		# A list holding the length of all sequences
		sequence_len = []
		for item in self.sequence:
			sequence_len.append(len(self.sequence[item]))

		# Plot the histogram
		plt.hist(sequence_len)
		plt.title('The histogram of the length distribution of the sequences')
		plt.xlabel('Sequence length')
		plt.ylabel('Frequency')
		plt.savefig(location, dpi = 300)
