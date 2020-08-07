"""Kahoot simulation program to determine the most important quality.
   Response time: The rate of answering questions
   Streak: The ability to maintain streaks
   Accuracy: The overall number of correct answers

   Questions
   Why streaks made the game terrible...now removed
   Gap between speed and accuracy

    Assumptions
    0. All questions have same time
    1. Player answers all questions
   """

import random
from models import Game


# Calculate if answer is correct 1 or incorrect 0
def calculate_answer():
    return random.randint(0, 1)


# Calculate player response time on question
def calculate_response_time(question_timer):
    return round(random.uniform(0, question_timer), 1)


def calculate_score(response_time, question_timer, points_possible):
    # Divide response time by question timer
    step_one = response_time / question_timer
    # Divide value by 2
    step_two = step_one / 2
    # Subtract step two from 1
    step_three = 1 - step_two
    # Multiply step three by step two
    step_four = points_possible * step_three
    # Round step four nearest whole number
    score = round(step_four)
    return score


def calculate_bonus(streak, points_possible):
    bonus = 0
    if points_possible == 0:
        return bonus
    else:
        if streak > 5:
            bonus = 500
        elif streak == 0:
            bonus = 0
        else:
            bonus = (streak - 1) * 100
    return bonus


if __name__ == "__main__":
    #  questions question_timer points_possible players
    game = Game.Game(10, 30, 1000, 2)
    # Loop players
    for player_index in range(len(game.player_list)):
        # Get the player for player list
        player = game.player_list[player_index]
        # Loop questions
        for question_index in range(game.questions):
            # Calculate player's response time for the question
            player_response_time = calculate_response_time(game.question_timer)
            # Log response time for the question
            player.response_times.append(player_response_time)
            # Calculate player's answer for the question
            answer = calculate_answer()
            # Log answer
            player.answers.append(answer)
            # If correct calculate score, bonus, points and increment streak
            if answer == 1:
                # Handle first question, streak is not set
                if question_index == 0:
                    player.streak = 0
                else:
                    player.streak = player.streaks[-1] + 1
                player.streaks.append(player.streak)
                player_score = calculate_score(player_response_time, game.question_timer, game.points_possible)
                player.scores.append(player_score)
                player_bonus = calculate_bonus(player.streak, game.points_possible)
                player.bonuses.append(player_bonus)
                player.points += player_score + player_bonus
            # Else incorrect score, bonus, streak 0 maintain points
            else:
                # Reset player streak
                player.streak = 0
                player.streaks.append(player.streak)
                player_score = 0
                player.scores.append(player_score)
                player_bonus = 0
                player.bonuses.append(player_bonus)
                player.points += player_score + player_bonus

    for index in range(len(game.player_list)):
        player = game.player_list[index]
        print("Player " + str(index) + " Points " + str(player.points))
        print("Scores")
        print(player.scores)
        print("Bonuses")
        print(player.bonuses)
        print("Streaks")
        print(player.streaks)
        print("Answers")
        print(player.answers)
        print("Response Times")
        print(player.response_times)
        print()
