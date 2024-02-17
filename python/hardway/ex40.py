class Song(object):

	"""docstring for Song"""

	def __init__(self, lyrics_1, lyrics_2):
		self.lyrics_1 = lyrics_1
		self.lyrics_2 = lyrics_2

	def sing_me_a_song(self):
		for line, linex in zip(self.lyrics_1, self.lyrics_2):
			print(line, linex)


lyrics_1 = ["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"]

lyrics_2 = ["They rally around tha family",
						"With pockets full of shells"]

happy_bday = Song(lyrics_1, lyrics_2)

bulls_on_parade = Song(lyrics_2, lyrics_1)


happy_bday.sing_me_a_song()

print("")

bulls_on_parade.sing_me_a_song()

		