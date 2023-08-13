
import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""
    API_KEY : str = os.getenv('API_KEY')



    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.dict_to_print = {}
        self.youtube = None

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.youtube = youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.printj(channel)

    def printj(self, dict_to_print):
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))



