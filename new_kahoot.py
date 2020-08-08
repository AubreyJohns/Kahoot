"""Kahoot simulation program to determine the most important quality.
   Response time: The rate of answering questions
   Accuracy: The overall number of correct answers

   Questions
   Streaks removed

   Gap between speed and accuracy
   What happens if your slower

    Assumptions
    0. All questions have same time
    1. Player answers all questions
   """
import csv
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


def calculate_average_response_time(times_list, answers_list):
    averages = []
    for x in range(len(answers_list)):
        if answers_list[x] == 1:
            averages.append(times_list[x])
    if len(averages) == 0:
        return 0
    else:
        return round(sum(averages) / len(averages), 1)


def calculate_total_response_time(time_list):
    return round(sum(time_list), 1)


def calculate_total_answers(answer_list):
    return sum(answer_list)


# number of questions
def calculate_accuracy(answer_list, questions):
    correct = 0
    for x in range(len(answer_list)):
        if answer_list[x] == 1:
            correct += 1
    return correct / questions


def get_points(sort_player):
    return sort_player.points


# List of answers
# calculate answer
# check against the list

if __name__ == "__main__":
    #  questions question_timer points_possible players
    game = Game.Game(30, 30, 1000, 10000)
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
                player_score = calculate_score(player_response_time, game.question_timer, game.points_possible)
                player.scores.append(player_score)
                player.points += player_score
            # Else incorrect score, bonus, streak 0 maintain points
            else:
                player_score = 0
                player.scores.append(player_score)
                player.points += player_score

    # Generate dataset
    with open('new_kahoot_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Points", "Accuracy", "Total Response Time"])
        for index in range(len(game.player_list)):
            print(index)
            player = game.player_list[index]
            writer.writerow([player.points,
                             calculate_accuracy(player.answers, game.questions),
                             calculate_total_response_time(player.response_times)])

    # Generate question dataset
    with open('kahoot_score_time_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Score", "Response Time"])
        for index in range(len(game.player_list)):
            print(index)
            player = game.player_list[index]
            for check in range(len(player.scores)):
                # Check correct answers
                if player.scores[check] == 0:
                    continue
                else:
                    writer.writerow([player.scores[check], player.response_times[check]])
