import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.dict_to_print = {}
        self.youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.printj(channel)

    def printj(self, dict_to_print):
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @property
    def title(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["snippet"]["title"]

    @property
    def description(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["snippet"]["description"]

    @property
    def url(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["snippet"]["customUrl"]

    @property
    def subscriber_count(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["statistics"]["subscriberCount"]

    @property
    def video_count(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["statistics"]["videoCount"]

    @property
    def view_count(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["statistics"]["viewCount"]

    @property
    def channel_id(self):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            return i["id"]

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.API_KEY)

    def to_json(self, filename):
        data = {
            "id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "view_count": self.view_count,
            "channel_id": self.channel_id,
            "video_count": self.video_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
