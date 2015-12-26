from apscheduler.schedulers.background import BackgroundScheduler
from urllib.request import urlopen

class Matches():
    """Contains and updates list of dota 2 pro-matches"""
    def __init__(self):
        self.__update_frequency_minutes = 10
        self.__scheduler = BackgroundScheduler()
        self.__list_of_matches = ''
        self.__request_url = 'http://dailydota2.com/match-api'


    @property
    def list_of_matches(self):
        return self.__list_of_matches


    def get_updated_match_schedule(self):
        """Retrieve an updated copy of the latest pro dota 2 matches"""
        print("updating")
        response = urlopen(self.__request_url)
        self.__list_of_matches = response.read().decode('utf-8')
        print(self.__list_of_matches)


    def start(self):
        """Starts the match retriever"""
        self.get_updated_match_schedule()
        self.__scheduler.add_job(self.get_updated_match_schedule, 'interval', minutes = self.__update_frequency_minutes)
        self.__scheduler.start()


    def stop(self):
        self.__scheduler.shutdown()
