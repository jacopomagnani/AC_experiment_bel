from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = ['answer1', 'answer2', 'answer3']

    def before_next_page(self):
        self.player.get_outcome()

    def vars_for_template(self):
        return {
            'rate': self.session.config['real_world_currency_per_point']
        }

class Results(Page):
    pass


page_sequence = [
    Intro,
    Page1,
    Results
]
