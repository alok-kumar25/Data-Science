# is to create a room that contains 100 boxes of random number with random numbers on it 
import random

def generate_prisoners():
    prisoners = []
    while len(prisoners) < 100:
        prisoner = random.randint(1,100)
        if prisoner not in prisoners:
            prisoners.append(prisoner)
    return prisoners

def generate_key_val():
    key = random.randint(1,100)
    val = random.randint(1,100)
    return key,val

def generate_room():
    room = {}
    while len(room) < 100:
        key,val = generate_key_val()   
        if key not in room and val not in room.values():
            room[key] = val
    return room

def random_searching(room, prisoners):
    found = 0
    for prisoner in prisoners:
        searched_boxes = set()
        for _ in range(50):
            # pick a random box
            box = random.randint(1, 100)
            if box not in searched_boxes:
                searched_boxes.add(box)
                if room[box] == prisoner:
                    found += 1
                    break  # prisoner found their number
    return found == 100




def strategic_searching(room, prisoners):
    found = 0
    for prisoner in prisoners:
        current_box = prisoner
        for _ in range(50):
            if room[current_box] == prisoner:
                found +=1 
                break
            else:
                current_box = room[current_box]
    return found == 100

num = 0
for i in range(1000):
    prisoners = generate_prisoners()
    room = generate_room()
    if strategic_searching(room,prisoners):
        num +=1
print("success rate :"+num)

# An another method is listed below 
"""
def random_searching(room, prisoners: list):
    found = 0
    while len(prisoners) > 0:
        random_turn = random.randint(1,100)
        if random_turn in prisoners:
            number_of_turns = 50
            searched_boxes = []
            while number_of_turns > 0 and len(searched_boxes) < 50:
                random_box = random.randint(1,100)
                if random_box not in searched_boxes:
                    if room[random_box] == random_turn:
                        found += 1
                        break
                    else:
                        number_of_turns -=1
                        searched_boxes.append(random_box)
            prisoners.remove(random_turn)
    return found == 100
"""


"""
# Uncomment this block to run large-scale trials in parallel
def run_single_trial(_):
    prisoners = generate_prisoners()
    room = generate_room()
    return strategic_searching(room, prisoners)

if __name__ == "__main__":
    num_trials = 100000  # total number of simulations
    num_cores = cpu_count()  # use all available CPU cores

    with Pool(processes=num_cores) as pool:
        results = pool.map(run_single_trial, range(num_trials))

    total_successes = sum(results)
    print(f"Total successes: {total_successes}/{num_trials}")
    print(f"Empirical probability: {total_successes / num_trials:.5f}")
"""