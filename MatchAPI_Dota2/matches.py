import ast
import json
import traceback
from urllib.error import URLError

from apscheduler.schedulers.background import BackgroundScheduler
from urllib.request import urlopen

from .common import log


class Matches:
    """Contains and updates list of dota 2 pro-matches"""

    def __init__(self):
        self.REQUEST_URL = "http://dailydota2.com/match-api"
        self.SLEEP_TIME = 30

        self.update_frequency_minutes = 10
        self.scheduler = BackgroundScheduler()
        self.list_of_matches = ""

    def get_updated_match_schedule(self):
        """Retrieve an updated copy of the latest pro Dota 2 matches"""
        number_of_attempts = 5
        attempt = 1
        error_free = False
        while error_free is False and attempt < (number_of_attempts + 1):
            try:
                response = urlopen(self.REQUEST_URL)
                self.list_of_matches = json.loads(response.read().decode("utf-8"))
                log("Successfully retrieved match log")
                error_free = True
            except URLError as e:
                log("Failed to obtain latest match schedule, sleeping {0} seconds:\n{2}".format(self.SLEEP_TIME, e))
                traceback.print_tb(e.__traceback__)

    def start(self):
        """Starts the match retriever"""
        self.get_updated_match_schedule()
        self.scheduler.add_job(self.get_updated_match_schedule, "interval", minutes=self.update_frequency_minutes)
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
