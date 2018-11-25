from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class page1(Page):

    form_model = 'player'
    form_fields = ['sex', 'major']

    def sex_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please choose an answer.'

    def major_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please choose an answer.'


page_sequence = [
    Intro,
    page1
]
