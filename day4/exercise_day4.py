# =====================================================
# Python course (Fall 2016)
# Homework exercise
# Day 4 (2016/10/17)
# Exercise 1
# A program that creates "Song" objects using the
# information from a CSV file
#
# By Ka Lok Li
# =====================================================

# Modules used in the code
import warnings
import webbrowser
import os
import csv

# Define the "Song" class
class Song(object):
	""" A class that describes songs """
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist

		# Try to convert "duration" into an integer
		try:
			# Give no error if "duration" is a positive or a negative integer
			self.duration = int(duration)
			
			if duration.isdigit() == True:
				# If "duration" is a positive integer
				self.duration = int(duration)
			else:
				# If "duration" is a negative integer
				raise Exception("Input duration is a negative integer.")

		except ValueError:
			# Have error if "duration" is neither a positive nor a negative integer
			self.duration = 0
			warnings.warn("Input duration is not an integer.")
			
	def pretty_duration(self):
		""" Return the duration in a pretty way """
		hour = self.duration / 3600
		minute = (self.duration - hour*3600 ) / 60
		second = self.duration - hour*3600 - minute*60
		return "%02d hours %02d minutes %02d seconds" % (hour, minute, second)

	def play(self):
		""" Automatically open a webpage on the computer with a youtube search for the title """
		url = "https://www.youtube.com/results?search_query=%s" % self.title
		webbrowser.open_new(url)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# For Windows
# In Windows the $HOME variable is called %HOMEPATH%
home_var = os.environ.get('HOMEPATH')
# Full path to the original CSV file
# csv_path = '%s\lulu_mix_16.csv' % home_var
# Full path to the modified CSV file (songs with negative duration removed)
csv_path = '%s\lulu_mix_16_fixed.csv' % home_var
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # For Linux
# home_var = os.environ.get('HOME')
# # Full path to the original CSV file
# csv_path = '%s/lulu_mix_16.csv' % home_var
# # Full path to the modified CSV file (songs with negative duration removed)
# csv_path = '%s/lulu_mix_16_fixed.csv' % home_var
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# A list which contains all "Song" instances
songs = []
# A list which holds all information in the csv file
song_list_csv = []

# Read all information from the csv file
with open(csv_path, 'r') as f_handle:
	temp = csv.reader(f_handle)
	
	for row in temp:
		song_list_csv.append(row) 

# Create a new "Song" instance for each song and append it to the "songs" list
for row in song_list_csv[1:]:
	songs.append(Song(row[0], row[1], row[2]))

# Codes in the question
for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()
