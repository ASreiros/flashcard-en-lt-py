import pandas
import random


class Data:
	def __init__(self):
		self.data = {}
		self.known_data = {}
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
		else:
			try:
				kw = pandas.read_csv("./data/known_words.csv")
				self.known_data = {row.original: row.translate for (index, row) in kw.iterrows()}
			except FileNotFoundError:
				print("no known words")
			else:
				known_list = list(self.known_data)
				for word in known_list:
					del self.data[word]
				print(len(self.data))

	def get_word(self):
		if len(self.data) > 0:
			self.word = random.choice(list(self.data))
			self.translate = self.data[self.word]
			self.tries += 1
			return self.word
		else:
			return "|EXIT|"

	def correct_word(self):
		self.known_data[self.word] = self.data[self.word]
		info = pandas.DataFrame(list(self.known_data.items()), columns=["original", "translate"])
		info.to_csv("data/known_words.csv")
		del self.data[self.word]
		self.correct += 1

	def new_list(self):
		self.known_data = {}
		info = pandas.DataFrame(list(self.known_data.items()), columns=["original", "translate"])
		info.to_csv("data/known_words.csv")
		self.correct = 0
		self.tries = -1
		try:
			pd = pandas.read_csv("./data/data en-lt.csv")
			self.data = {row.original: row.translate for (index, row) in pd.iterrows()}
		except FileNotFoundError:
			self.data = {}
