from pprint import pprint
import random
import math


TIMESTAMPS_COUNT = 50000
PROBABILITY_SCORE_CHANGED = 0.0001
PROBABILITY_HOME_SCORE = 0.45
OFFSET_MAX_STEP = 3
INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}

def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1
    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }
  
def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)
    return stamps


def get_score(game_stamps, offset):
    home = 0
    away = 0
    for record in game_stamps:
        if (record["offset"] == offset
                or record["offset"] == offset + 1
                or record["offset"] == offset + 2):
            home = record['score']['home']
            away = record['score']['away']
    return home, away


if __name__ == '__main__':
    game_stamps = generate_game()
    # f = open("score.txt", "w")
    # for line in game_stamps:
    #     f.write(str(line)+'\n')
    # f.close()
    offset = math.floor(random.random() * TIMESTAMPS_COUNT * (OFFSET_MAX_STEP - 1))
    home, away = get_score(game_stamps, offset)
    pprint(game_stamps)
    print(offset, home, away)
