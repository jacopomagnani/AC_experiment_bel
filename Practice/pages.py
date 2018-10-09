from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.initialize()


class Page1(Page):

    form_model = 'player'
    form_fields = ['choice']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            flip = random.randint(0,1)
            if flip ==0:
                self.player.choice = 0
            else:
                self.player.choice = 1
        self.player.get_outcome()


class Page2(Page):
    pass

class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Page1,
    Page2,
    FinalPage
]
