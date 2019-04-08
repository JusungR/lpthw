class Song(object) :

    def __init__(self, lyrics) :
        self.lyrics = lyrics

    def sing_me_a_song(self) :
        for line in self.lyrics :
            print(line)

happy_bday = Song(["Happy birth day to you",
                    "I don't want to get sued.",
                    "So I'll stop right there."])

happy_ending = Song("We live the last of our life but not togeter".split())

happy_bday.sing_me_a_song()
happy_ending.sing_me_a_song()
