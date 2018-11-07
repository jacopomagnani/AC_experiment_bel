from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class MyWaitPage(WaitPage):
    wait_for_all_groups = True


page_sequence = [
    MyPage,
    MyWaitPage
]
