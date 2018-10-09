from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy



author = 'Jacopo Magnani'

doc = """
Matching Game with noisy signals
"""


class Constants(BaseConstants):
    name_in_url = 'practice'
    players_per_group = None
    num_rounds = 2
    game_space = [0, 1]
    game_labels = ["A", "B"]
    game_sequence = [0, 1]
    type_space = [1, 2, 3]
    type_labels = ["X", "Y", "Z"]
    A_match_value = [160, 80, 40]
    A_reservation_value = [100, 75, 25]
    B_match_value = [160, 80, 40]
    B_reservation_value = [80, 75, 25]
    signal_space = [1, 2, 3]
    signal_names = ["red", "yellow", "blue"]
    pL = [0, 1/2, 1/2]
    pM = [0, 1, 0]
    pH = [1/2, 1/2, 0]


class Subsession(BaseSubsession):

    game = models.IntegerField()
    game_name = models.StringField()

    def creating_session(self):
        #game sequence
        if self.round_number == 1:
            for t in range(1, Constants.num_rounds+1):
                self.in_round(t).game = Constants.game_sequence[t-1]
                self.in_round(t).game_name = Constants.game_labels[self.in_round(t).game]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    type = models.IntegerField()
    partner_type = models.IntegerField()
    signal = models.IntegerField()
    choice = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    partner_choice = models.IntegerField()
    match = models.IntegerField()
    late = models.IntegerField()
    points = models.IntegerField()

    def initialize(self):
        # assign type, assign random partner's type and generate signal
        for t in range(1, Constants.num_rounds+1):
            self.in_round(t).type = random.choice(Constants.type_space)
            self.in_round(t).partner_type = random.choice(Constants.type_space)
            if self.in_round(t).partner_type == 1:
                self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pH)
            elif self.in_round(t).partner_type == 2:
                self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pM)
            elif self.in_round(t).partner_type == 3:
                self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pL)

    def get_outcome(self):
        if self.subsession.game == 0:
            match_value = Constants.A_match_value
            reservation_value = Constants.A_reservation_value
        elif self.subsession.game == 1:
            match_value = Constants.B_match_value
            reservation_value = Constants.B_reservation_value
        self.partner_choice = random.choice([0, 1])
        self.match = self.choice * self.partner_choice
        self.points = self.match * match_value[self.partner_type-1] + (1 - self.match) * reservation_value[self.type-1]