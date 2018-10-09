from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = ['answer1', 'answer2', 'answer3']

    def before_next_page(self):
        k = 0
        if self.player.answer1 == 5:
            k = k+1
        if self.player.answer2 == 5:
            k = k+1
        if self.player.answer3 == 47:
            k = k+1
        self.player.num_correct = k
        self.player.payoff = k*2

    def vars_for_template(self):
        rate = self.session.config['real_world_currency_per_point']
        return {
            'rate': c(rate).to_real_world_currency(self.session)
        }

class Results(Page):
    pass


page_sequence = [
    Intro,
    Page1,
    Results
]
