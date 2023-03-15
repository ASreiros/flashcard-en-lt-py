import pandas
import random


class Data:
	def __init__(self):
		self.data = {}
		self.get_data()
		self.word = ""
		self.translate = ""
		self.flag = False
		self.correct = 0
		self.tries = -1

	def get_data(self):
		try:
			pd = pandas.read_csv("./data/data en-lt.csv")
			self.data = {row.original: row.translate for (index, row) in pd.iterrows()}
		except FileNotFoundError:
			self.data = {}

	def get_word(self):
		if len(self.data) > 0:
			self.word = random.choice(list(self.data))
			self.translate = self.data[self.word]
			self.tries += 1
			return self.word
		else:
			return "|EXIT|"

	def correct_word(self):
		del self.data[self.word]
		self.correct += 1
