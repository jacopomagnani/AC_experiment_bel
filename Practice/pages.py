from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.initialize()



class Page1Active(Page):

    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        return {'prob': Constants.prob_Haccept[self.subsession.game]}

    def is_displayed(self):
        return self.player.status == 0

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            flip = random.randint(0,1)
            if flip ==0:
                self.player.choice = False
            else:
                self.player.choice = True
        self.player.get_outcome()


class Page1Passive(Page):

    def vars_for_template(self):
        return {'prob': Constants.prob_Haccept[self.subsession.game]}

    def is_displayed(self):
        return self.player.status == 1

    def before_next_page(self):
        self.player.get_outcome()


class Page2(Page):
    pass

class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Page1Active,
    Page1Passive,
    Page2,
    FinalPage
]
