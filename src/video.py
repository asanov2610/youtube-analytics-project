import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build("youtube", "v3", developerKey=api_key)

    def __init__(self, id_video: str):
        try:
            if any(map(str.isdigit, id_video)):
                self.channel_id = id_video
            else:
                self.channel_info = None
                self.title = None
                self.url = None
                self.view_count = None
                self.like_count = None
                raise ValueError
        except ValueError:
            print("Неверный ID")
        else:
            self.id_video = id_video
            self.channel = self.youtube.videos().list(id=self.id_video, part='snippet,statistics').execute()
            self.url = f"https://www.youtube.com/channel/{self.id_video}"
            self.title = self.channel["items"][0]["snippet"]["title"]
            self.view_count = self.channel["items"][0]["statistics"]["viewCount"]
            self.like = self.channel["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.playlist = self.youtube.playlistItems().list(id=self.id_playlist, part='snippet').execute()