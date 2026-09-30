class Playlist(object):
  def __init__(self):
    self.songs = []

  def contains(self , song):
    return song in self.songs

  def add(self,song):
    if not self.contains(song):
      self.songs.append(song)

  def remove(self, song):
    if self.contains(song):
      self.songs.remove(song)
    else:
      raise ValueError("Song not found in playlist")

  def __add__(self, other):
    new_playlist = Playlist()
    for song in self.songs:
      new_playlist.add(song)
    for song in other.songs:
      new_playlist.add(song)
    return new_playlist
  
  def __str__(self):
    return ", ".join(self.songs)

# p = Playlist()
# p.add("Jazz")
# p.add("Rock")
# p.remove("Jazz")

# print(p)
# print(p.contains("Jazz"))