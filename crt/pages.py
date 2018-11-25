from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = ['answer1', 'answer2', 'answer3']

    def answer1_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please enter an answer.'

    def answer2_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please enter an answer.'

    def answer3_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please enter an answer.'

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
