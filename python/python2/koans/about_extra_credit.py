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

    HIGH_DICE_CAP = 4
    LOW_DICE_CAP = 2
    HIGH_POINTS_CAP = 800
    LOW_POINTS_CAP = 200

    def __init__(self, name, points = 0):
        self._name = name
        self._points = points
        self._dice = DiceSet()

    def __str__(self):
        return "{0}: {1}pts".format(self._name, self._points)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    def accumulate_points(self, points):
        self._points += points

    def roll(self, n):
        self._dice.roll(n)
        return self._dice.values

    def continue_roll(self, points, dices):
        stop = [
            points > Player.HIGH_POINTS_CAP and dices < Player.HIGH_DICE_CAP,
            points > Player.LOW_POINTS_CAP and dices < Player.LOW_DICE_CAP and self.points != 0,
            points > Game.ACCUMULATION_CAP and self.points == 0,
            self.points + points > Game.FINAL_CAP,
        ]

        return not (True in stop)

class Game(object):
    "Represents a game of Greed."

    ACCUMULATION_CAP = 300
    FINAL_CAP = 3000
    ITER_CAP = 30
    DICE_NUMBER = 5

    def __init__(self, players):
        self._players = players

    def __str__(self):
        return "players:[{0}]".format(", ".join([str(player) for player in self._players]))

    def __repr__(self):
        return str(self)

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
        roll_counter = 0
        roll = []
        dice_number = Game.DICE_NUMBER
        zero_roll = False
        continue_roll = True
        # The player may continue to roll as long as each roll scores points.
        while continue_roll and (not zero_roll) and roll_counter < Game.ITER_CAP:
            roll_points = 0
            roll_counter += 1
            roll = player.roll(dice_number)

            score_counter = score_hash(roll)
            for num, score in score_counter.iteritems():
                if score != 0:
                    roll_points += score
                    # After a player rolls and the score is calculated, the scoring dice are
                    # removed and the player has the option of rolling again using only the
                    # non-scoring dice.
                    dice_number -= 1
            points += roll_points
            zero_roll = roll_points == 0

            # If all of the thrown dice are scoring, then the
            # player may roll all 5 dice in the next roll.
            if dice_number == 0:
                dice_number = Game.DICE_NUMBER

            # If a roll has zero points, then the player loses not only their turn,
            # but also accumulated score for that turn.
            if zero_roll:
                points = 0

            continue_roll = player.continue_roll(points, dice_number)

            UI.display_roll(player.name, roll_counter, roll, points, dice_number, continue_roll)

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

        UI.display('START')

        # The count flag prevents infinite loop.
        while playing and round_counter < Game.ITER_CAP:
            round_counter += 1
            playing = self.play_round(self._players)
            UI.display_round(round_counter, False, self._players)

        # The winner is the player with the highest score after the final round.
        winner = self.play_last_round(self._players)
        UI.display_round(round_counter + 1, True, self._players)

        UI.display('END')
        UI.display('WINNER', winner)

        return winner


class UI(object):
    "Represents the user interface for a game of Greed"

    ITEMS = {
        'EN_SHORT': {
            'START': 'Start!',
            'END': 'End!',
            'LAST': 'Last Round Start!',
            'PLAYER': 'Player: {0}',
            'PLAYERS': 'Players: {0}',
            'WINNER': 'Winner: {0}',
            'BEST': 'Best: {0}',
            'POINTS': 'Points: {0}',
            'SCORE': 'Score: {0}',
            'ROUND': 'Round: {0}',
            'ROLL': 'Roll: {0}',
            'DICE': 'Dice: {0}',
        },
        'EN_LONG': {
            'ROLL': '│  {0} #{1} roll: {2}, {3}pts, {4}dcs, again? {5}',
            'ROUND': '├ Round #{0}! Last? {1}, Players! {2}',
        },
    }

    @staticmethod
    def output_short(item, val):
        return UI.ITEMS['EN_SHORT'][item].format(val)

    @staticmethod
    def display(item, val = None):
        print UI.output_short(item, val)

    @staticmethod
    def display_roll(name, roll_number, roll, points, dice, choice):
        print UI.ITEMS['EN_LONG']['ROLL'].format(name, roll_number, roll, points, dice, choice)

    @staticmethod
    def display_round(round_number, last_round, players):
        print UI.ITEMS['EN_LONG']['ROUND'].format(round_number, last_round, players)

class AboutExtraCredit(Koan):

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
        roll = p.roll(Game.DICE_NUMBER)

        self.assertEqual(type(roll), list)
        self.assertEqual(len(roll), 5)

        self.assertFalse(roll == p.roll(Game.DICE_NUMBER))

    def test_player_continue_roll_choice(self):
        p1 = Player("p1")
        self.assertEqual(True, p1.continue_roll(250, 1))
        self.assertEqual(True, p1.continue_roll(250, 4))

        self.assertEqual(False, p1.continue_roll(1000, 5))
        self.assertEqual(False, p1.continue_roll(1000, 2))

        self.assertEqual(False, p1.continue_roll(350, 5))
        self.assertEqual(False, p1.continue_roll(350, 1))

        self.assertEqual(False, p1.continue_roll(3100, 1))
        self.assertEqual(False, p1.continue_roll(3100, 5))

        p2 = Player("p2", 500)
        self.assertEqual(False, p2.continue_roll(250, 1))
        self.assertEqual(True, p2.continue_roll(250, 4))

        self.assertEqual(True, p2.continue_roll(1000, 5))
        self.assertEqual(False, p2.continue_roll(1000, 2))

        self.assertEqual(True, p2.continue_roll(350, 5))
        self.assertEqual(False, p2.continue_roll(350, 1))

        self.assertEqual(False, p2.continue_roll(2800, 2))
        self.assertEqual(False, p2.continue_roll(2800, 5))

    def test_game_initialization(self):
        g = Game([Player("p1"), Player("p2"), Player("p3")])
        self.assertEqual(type(g), Game)
        self.assertEqual(str(g), "players:[p1: 0pts, p2: 0pts, p3: 0pts]")

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

    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 0, '4': 0, '6': 0}, score_hash([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 50, '4': 0, '6': 0}, score_hash([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual({'1': 100, '3': 0, '2': 0, '5': 0, '4': 0, '6': 0}, score_hash([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual({'1': 200, '3': 0, '2': 0, '5': 100, '4': 0, '6': 0}, score_hash([1, 5, 5, 1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 0, '4': 0, '6': 0}, score_hash([2, 3, 4, 6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual({'1': 1000, '3': 0, '2': 0, '5': 0, '4': 0, '6': 0}, score_hash([1, 1, 1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual({'1': 0, '3': 0, '2': 200, '5': 0, '4': 0, '6': 0}, score_hash([2, 2, 2]))
        self.assertEqual({'1': 0, '3': 300, '2': 0, '5': 0, '4': 0, '6': 0}, score_hash([3, 3, 3]))
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 0, '4': 400, '6': 0}, score_hash([4, 4, 4]))
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 500, '4': 0, '6': 0}, score_hash([5, 5, 5]))
        self.assertEqual({'1': 0, '3': 0, '2': 0, '5': 0, '4': 0, '6': 600}, score_hash([6, 6, 6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual({'1': 0, '2': 200, '3': 0, '4': 0, '5': 50, '6': 0}, score_hash([2, 5, 2, 2, 3]))
        self.assertEqual({'1': 0, '2': 0, '3': 0, '4': 0, '5': 550, '6': 0}, score_hash([5, 5, 5, 5]))
        self.assertEqual({'1': 1100, '3': 0, '2': 0, '5': 50, '4': 0, '6': 0}, score_hash([1, 1, 1, 5, 1]))

    def test_ones_not_left_out(self):
        self.assertEqual({'1': 100, '3': 0, '2': 200, '5': 0, '4': 0, '6': 0}, score_hash([1, 2, 2, 2]))
        self.assertEqual({'1': 100, '3': 0, '2': 200, '5': 50, '4': 0, '6': 0}, score_hash([1, 5, 2, 2, 2]))
