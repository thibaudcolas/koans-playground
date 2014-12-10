#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *
from about_scoring_project import *
from about_dice_project import *


class Player(object):
    def __init__(self, name):
        self._name = name
        self._points = 0
        self._dice = DiceSet()

    def __str__(self):
        return "{0}: {1}pts".format(self._name, self._points)

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    def accumulate_points(self, points):
        self._points += points

    def roll(self):
        self._dice.roll(5)
        return self._dice.values

class Game(object):
    def __init__(self, players):
        self._players = players
        self._turn = 0
        self._playing = False
        self._final_round = False
        self._winner = None

    def __str__(self):
        return "t:{0}, p:{1}, fr:{2}, w:{3}, players:[{4}]".format(self._turn, self._playing, self._final_round, self._winner, ", ".join([str(player) for player in self._players]))

    def play_turn(self, player):
        pass

    def play(self):
        self._playing = True

        while playing:
            turn += 1
            for player in players:
                self.play_turn(player)
            playing = False
            pass

        self._winner = None


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

    def test_player_initialization(self):
        p1 = Player('p1')
        self.assertEqual(p1.name, 'p1')
        self.assertEqual(p1.points, 0)

        p2 = Player('p2')
        self.assertEqual(p2.name, 'p2')
        self.assertEqual(p2.points, 0)

    def test_player_methods(self):
        p = Player('p')
        self.assertEqual(p.points, 0)
        p.accumulate_points(100)
        self.assertEqual(p.points, 100)

        roll = p.roll()

        self.assertEqual(type(roll), list)
        self.assertEqual(len(roll), 5)

        self.assertFalse(roll == p.roll())

    def test_game_initialization(self):
        g = Game([Player('p1'), Player('p2'), Player('p3')])
        self.assertEqual(type(g), Game)
        self.assertEquals(str(g), 't:0, p:False, fr:False, w:None, players:[p1: 0pts, p2: 0pts, p3: 0pts]')


