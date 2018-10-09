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
    game_sequence = [0, 4]
    type_space = [1, 2, 3]
    type_labels = ["X", "Y", "Z"]
    status_space = [0, 1]
    status_labels = ["active", "passive"]
    match_value = [160, 80, 40]
    reservation_value = [100, 75, 25]
    signal_space = [1, 2, 3]
    signal_names = ["red", "yellow", "blue"]
    pL = [0, 1/2, 1/2]
    pM = [0, 1, 0]
    pH = [1/2, 1/2, 0]
    game_space = [0, 1, 2, 3, 4]
    game_labels= ["A", "B", "C", "D", "E"]
    prob_Haccept = [100, 75, 50, 25, 0]


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
    status = models.IntegerField()
    status_name = models.StringField()
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
        # assign type, status, assign random partner's type and generate signal
        for t in range(1, Constants.num_rounds+1):
            if t == 1:
                self.in_round(t).type = 2
                self.in_round(t).status = Constants.status_space[0]
                self.in_round(t).status_name = Constants.status_labels[Constants.status_space.index(self.in_round(t).status)]
                self.in_round(t).partner_type = random.choice(Constants.type_space)
                if self.in_round(t).partner_type == 1:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pH)
                elif self.in_round(t).partner_type == 2:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pM)
                elif self.in_round(t).partner_type == 3:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pL)
            elif t == 2:
                self.in_round(t).type = random.choice(Constants.type_space)
                self.in_round(t).status = Constants.status_space[1]
                self.in_round(t).status_name = Constants.status_labels[
                    Constants.status_space.index(self.in_round(t).status)]
                self.in_round(t).partner_type = 2
                if self.in_round(t).partner_type == 1:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pH)
                elif self.in_round(t).partner_type == 2:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pM)
                elif self.in_round(t).partner_type == 3:
                    self.in_round(t).signal = numpy.random.choice(Constants.signal_space, p=Constants.pL)

    def get_outcome(self):
        match_value = Constants.match_value
        reservation_value = Constants.reservation_value
        if self.status == 0:
            if self.partner_type == 2 or self.partner_type == 3:
                self.partner_choice = 1
            else:
                self.partner_choice = numpy.random.choice([0, 1], p=[1 - Constants.prob_Haccept[self.subsession.game] / 100,
                                                          Constants.prob_Haccept[self.subsession.game] / 100])
        elif self.status == 1:
            self.partner_choice = random.choice([0, 1])
            if self.type == 2 or self.type == 3:
                self.choice = 1
            else:
                self.choice = numpy.random.choice([0, 1], p=[1 - Constants.prob_Haccept[self.subsession.game] / 100,
                                                             Constants.prob_Haccept[self.subsession.game] / 100])
        self.match = self.choice * self.partner_choice
        self.points = self.match * match_value[self.partner_type-1] + (1 - self.match) * reservation_value[self.type-1]