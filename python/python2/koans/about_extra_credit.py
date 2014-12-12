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
    "Represents a player of the Greed Game. He has a name, points, and the ability to roll dices."

    def __init__(self, name, points = 0):
        self._name = name
        self._points = points
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
        # TODO Number of dices rolled should be parameterized.
        self._dice.roll(5)
        return self._dice.values



class Game(object):
    "Represents a game of Greed."

    ACCUMULATION_CAP = 300
    FINAL_CAP = 3000

    def __init__(self, players):
        self._players = players

    def __str__(self):
        return "players:[{0}]".format(", ".join([str(player) for player in self._players]))

    def pick_best_player(self, players):
        "Pick the best player: the one with the most points."
        best = players[0]
        for player in players:
            if player.points > best.points:
                best = player
        return best

    def play_turn(self, player):
        "One turn: actions of a single player in a round."
        points = 0
        # TODO: Implement
        points += score(player.roll())
        return points

    def play_round(self, players):
        "One round: a turn for each player."
        game_ongoing = True

        for player in players:
            points = self.play_turn(player)
            # Before a player is allowed to accumulate points, they must get at
            # least 300 points in a single turn. Once they have achieved 300 points
            # in a single turn, the points earned in that turn and each following
            # turn will be counted toward their total score.
            if (player.points >= Game.ACCUMULATION_CAP) or (points >= Game.ACCUMULATION_CAP):
                player.accumulate_points(points)

            # Once a player reaches 3000 (or more) points, the game enters the final
            # round where each of the other players gets one more turn.
            game_ongoing = game_ongoing and (player.points < Game.FINAL_CAP)

        return game_ongoing

    def play_last_round(self, players):
        "End game: last round for all but the best player."

        best_player = self.pick_best_player(players)
        players.remove(best_player)
        self.play_round(players)
        players.append(best_player)

        return self.pick_best_player(players)

    def play(self):
        "Plays a game of Greed."
        playing = True
        round_counter = 0

        # The count flag prevents infinite loop.
        while playing and round_counter < 100:
            round_counter += 1
            playing = self.play_round(self._players)

        # The winner is the player with the highest score after the final round.
        winner = self.play_last_round(self._players)

        return winner


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

    def test_player_initialization(self):
        p1 = Player("p1")
        self.assertEqual(p1.name, "p1")
        self.assertEqual(p1.points, 0)

        p2 = Player("p2", 500)
        self.assertEqual(p2.name, "p2")
        self.assertEqual(p2.points, 500)

    def test_player_points_couting(self):
        p = Player("p")
        self.assertEqual(p.points, 0)
        p.accumulate_points(100)
        self.assertEqual(p.points, 100)
        p.accumulate_points(100)
        self.assertEqual(p.points, 200)

    def test_player_dice_rolling(self):
        p = Player("p")
        roll = p.roll()

        self.assertEqual(type(roll), list)
        self.assertEqual(len(roll), 5)

        self.assertFalse(roll == p.roll())

    def test_game_initialization(self):
        g = Game([Player("p1"), Player("p2"), Player("p3")])
        self.assertEqual(type(g), Game)
        self.assertEquals(str(g), "players:[p1: 0pts, p2: 0pts, p3: 0pts]")

    def test_game_best_player_pick(self):
        best = Player("ppp", 300)
        players = [Player("p", 100), Player("pp", 200), best]
        g = Game(players)
        self.assertEqual(g.pick_best_player(players), best)
        self.assertEqual(g.pick_best_player(players).points, best.points)

    def test_game_play_turn(self):
        p1 = Player("p1")
        g = Game([p1, Player("p2"), Player("p3")])
        self.assertEqual(type(g.play_turn(p1)), int)

    def test_game_play_round(self):
        p1 = Player("p1")
        players = [p1, Player("p2"), Player("p3")]
        g = Game(players)
        self.assertEqual(type(g.play_round(players)), bool)

    def test_game_play_last_round(self):
        p1 = Player("p1")
        players = [p1, Player("p2"), Player("p3")]
        g = Game(players)
        self.assertEqual(type(g.play_last_round(players)), Player)

    def test_game_play(self):
        p1 = Player("p1")
        players = [p1, Player("p2"), Player("p3")]
        g = Game(players)
        self.assertEqual(type(g.play()), Player)


