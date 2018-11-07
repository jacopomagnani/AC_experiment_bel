from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import socket


class MyPage(Page):
    def before_next_page(self):
        self.player.pc_ip = self.request.META['REMOTE_ADDR']
        self.player.pc_name = socket.gethostbyaddr(self.player.pc_ip)[0].split('.')[0]


page_sequence = [
    MyPage,
]
