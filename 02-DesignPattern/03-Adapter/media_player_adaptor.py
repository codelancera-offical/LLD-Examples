from abc import ABC, abstractmethod

# Target interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str):
        pass

# Native implementation
class Mp3Player(MediaPlayer):
    def play(self, filename: str):
        print(f"MP3 Player: Playing {filename}")

# External codec lib (Adaptees)
class VlcCodec:
    def play_vlc(self, filename: str):
        print(f"VLC Codec: Decoding and playing {filename}")

class Mp4Codec:
    def play_mp4(self, filename: str):
        print(f"MP4 Codec: Decoding and Playing {filename}")

# Adapters
class VlcPlayerAdapter(MediaPlayer):
    def __init__(self, codec: VlcCodec):
        self._codec = codec # adapter直接持有adaptee的引用

    def play(self, filename: str):
        self._codec.play_vlc(filename)

class Mp4PlayerAdapter(MediaPlayer):
    def __init__(self, codec: Mp4Codec):
        self._codec = codec

    def play(self, file_name: str):
        self._codec.play_mp4(file_name)

# Client
class Player:
    
    def play_file(self, filename: str):
        extension = filename.rsplit(".", 1)[-1].lower()

        players = {
            "mp3": lambda: Mp3Player(), # lambda 到底返回个啥
            "vlc": lambda: VlcPlayerAdapter(VlcCodec()),
            "mp4": lambda: Mp4PlayerAdapter(Mp4Codec()),
        }

        creator = players.get(extension)
        if creator is None:
            print(f"Unsupported format: {extension}")
            return
    
        creator().play(filename)

if __name__ == "__main__":
    player = Player()
    player.play_file("song.mp3")
    player.play_file("movie.mp4")
    player.play_file("documentary.vlc")
    player.play_file("image.png")