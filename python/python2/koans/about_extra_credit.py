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

    def turn(self, player):
        pass

    def play(self):
        turn = 0
        playing = True
        final_round = False
        winner = None

        while playing:
            turn += 1
            for player in players:
                self.turn(player)
            playing = False
            pass

        return winner


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

