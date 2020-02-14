class Song:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = []

    def add_tags(self,*args):
        self.tags.extend(args)

song1 = Song("Aria", "Shtil")
song1.add_tags("Rock", 'Russian')

song2 = Song("Pink", "Rock it")
song2.add_tags("American", "Punk")

print(song2.tags)