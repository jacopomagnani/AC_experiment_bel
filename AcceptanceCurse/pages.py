from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        if self.subsession.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
        self.subsession.initialize_round()
        self.group.initialize_group()


class Page1Active(Page):

    timeout_seconds = 60

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


class Page1Passive(Page):

    timeout_seconds = 30

    def vars_for_template(self):
        return {'prob': Constants.prob_Haccept[self.subsession.game]}

    def is_displayed(self):
        return self.player.status == 1


class MyWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.get_outcome()


class Page2(Page):

    timeout_seconds = 10


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'paying_round': self.session.vars['paying_round']
        }


page_sequence = [
    Intro,
    MyWaitPage1,
    Page1Active,
    Page1Passive,
    MyWaitPage2,
    Page2,
    FinalPage
]
