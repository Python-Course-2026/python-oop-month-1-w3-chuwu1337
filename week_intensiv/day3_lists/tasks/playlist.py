class Playlist:
    """ЗАДАЧА: Подсчет общей длительности песен (track_list - список секунд)"""
    def __init__(self): self.tracks = []
    def get_duration(self):
        len = 0
        for track in self.tracks:
            len += track.duration
        return len