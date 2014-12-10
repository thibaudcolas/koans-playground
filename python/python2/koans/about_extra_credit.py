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
        self._round = 0
        self._playing = False
        self._winner = None
        self._accumulation_cap = 300
        self._final_cap = 3000

    def __str__(self):
        return "r:{0}, p:{1}, w:{2}, players:[{3}]".format(self._round, self._playing, self._winner, ", ".join([str(player) for player in self._players]))

    @staticmethod
    def best_player(players):
        best = player[0]
        for player in players:
            if player.points > best.points:
                best = player
        return best

    def play_turn(self, player):
        points = 0
        # TODO: Implement
        return points

    def play_round(self, players):
        self._round += 1
        final_cap_reached = False

        for player in players:
            points = self.play_turn(player)
            if points >= self._accumulation_cap: player.accumulate_points(points)
            final_cap_reached = final_cap_reached or (points >= self._final_cap)

        return final_cap_reached

    def play(self):
        self._playing = True

        while self._playing:
            self._playing = not self.play_round(self._players)

        player_over_cap = self.best_player(self._players)
        self._players.remove(player_over_cap)
        self.play_round(self._players)
        self._players.add(player_over_cap)

        self._winner = self.best_player(self._players)


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
        g1 = Game([Player('p1'), Player('p2'), Player('p3')])
        self.assertEqual(type(g), Game)
        self.assertEquals(str(g), 'r:0, p:False, w:None, players:[p1: 0pts, p2: 0pts, p3: 0pts]')


