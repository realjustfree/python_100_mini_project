import random, sys

class DoorGraph:
    ALL_CLOSED = """
    +------+  +------+  +------+
    |      |  |      |  |      |
    |   1  |  |   2  |  |   3  |
    |      |  |      |  |      |
    |      |  |      |  |      |
    |      |  |      |  |      |
    +------+  +------+  +------+"""

    FIRST_GOAT = """
    +------+  +------+  +------+
    |  ((  |  |      |  |      |
    |  oo  |  |   2  |  |   3  |
    | /_/|_|  |      |  |      |
    |    | |  |      |  |      |
    |GOAT|||  |      |  |      |
    +------+  +------+  +------+"""

    SECOND_GOAT = """
    +------+  +------+  +------+
    |      |  |  ((  |  |      |
    |   1  |  |  oo  |  |   3  |
    |      |  | /_/|_|  |      |
    |      |  |    | |  |      |
    |      |  |GOAT|||  |      |
    +------+  +------+  +------+"""

    THIRD_GOAT = """
    +------+  +------+  +------+
    |      |  |      |  |  ((  |
    |   1  |  |   2  |  |  oo  |
    |      |  |      |  | /_/|_|
    |      |  |      |  |    | |
    |      |  |      |  |GOAT|||
    +------+  +------+  +------+"""

    FIRST_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    | CAR! |  |  ((  |  |  ((  |
    |    __|  |  oo  |  |  oo  |
    |  _/  |  | /_/|_|  | /_/|_|
    | /_ __|  |    | |  |    | |
    |   O  |  |GOAT|||  |GOAT|||
    +------+  +------+  +------+"""

    SECOND_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    |  ((  |  | CAR! |  |  ((  |
    |  oo  |  |    __|  |  oo  |
    | /_/|_|  |  _/  |  | /_/|_|
    |    | |  | /_ __|  |    | |
    |GOAT|||  |   O  |  |GOAT|||
    +------+  +------+  +------+"""

    THIRD_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    |  ((  |  |  ((  |  | CAR! |
    |  oo  |  |  oo  |  |    __|
    | /_/|_|  | /_/|_|  |  _/  |
    |    | |  |    | |  | /_ __|
    |GOAT|||  |GOAT|||  |   O  |
    +------+  +------+  +------+"""

door_graph = DoorGraph()

# getting user input, and decide list value

def get_user_choice():
    while True:
        user_input = input("choose between doors 1, 2, or 3: ")
        if user_input in ["1", "2", "3"]:
            break
    user_input=int(user_input)-1 # to convert to 0 index
    return user_input

def doors_init(user_choice):
    doors = ["0","0","0"]
    doors[user_choice] = random.choice("gc")

    if doors[user_choice] == "c":
        for index, value in enumerate(doors):
            if value != "c":
                doors[index] = "g"
    else: # if doors[user_input] == "g"
        for index, value in enumerate(doors):
            if value == "0":
                doors[index] = random.choice("gc")
            if doors[index] == "c":
                for index, value in enumerate(doors):
                    if value == "0":
                        doors[index] = "g"
            if doors[index] == "g":
                for index, value in enumerate(doors):
                    if value == "0":
                        doors[index] = "c"
    # car_position = "".join(str(doors)).find("c")
    car_position = doors.index("c")

    print("doors: ", doors)
    print("car_position :", car_position)
    return doors, car_position

"""
copilot offer. it's better than my code.

def doors_init():
    doors = ['0', '0', '0']  # Step 1: Initialize doors
    car_position = random.randint(0, 2)  # Step 2: Randomly assign a car
    doors[car_position] = 'c'  # Mark the car's position
    
    # Step 3: Assign goats to the remaining doors
    for i in range(len(doors)):
        if doors[i] != 'c':  # If the door doesn't have a car
            doors[i] = 'g'  # Assign a goat to the door
    
    return doors 
"""

def make_choose(doors_situation, user_choice, car_position, swap):
    # open one door with goat
    # the door not car and not user's choice
    opened_door = [index for index, value in enumerate(doors_situation) if index != user_choice and index != car_position][0]
    remained_door = [index for index, value in enumerate(doors_situation) if index != user_choice and index != opened_door][0]

    if opened_door == 0:
        print(door_graph.FIRST_GOAT)
    elif opened_door == 1:
        print(door_graph.SECOND_GOAT)
    else:
        print(door_graph.THIRD_GOAT)
    print("showing one door with goat")
    print("you choose {}th door".format(user_choice+1))

    # offer to change the user's choice
    while True:
        want_to_change = input("Do you want to change your choice? (y or n)\
(changing from {} to {}) : ".format(user_choice+1, remained_door+1)).lower().strip()
        if want_to_change in ["y", "n"]:
            break

    if want_to_change == "y":
        swap = 1
        for index, value in enumerate(doors_situation):
            if index != user_choice and index != opened_door:
                temp = opened_door
                opened_door = user_choice
                user_choice = temp


    else:
        swap = 0

    return user_choice, swap

def result_judge(user_choice, car_position, total_games):
    total_games += 1

    if car_position == 0:
        print(door_graph.FIRST_CAR_OTHERS_GOAT)
    elif car_position == 1:
        print(door_graph.SECOND_CAR_OTHERS_GOAT)
    else:
        print(door_graph.THIRD_CAR_OTHERS_GOAT)

    if user_choice == car_position:
        print("You win! The car was behind the door!")
        return 1, total_games
    else:
        print("You lose! The car was behind the door!")
        return 0, total_games

def result_cal(result, swap, swap_win, swap_loss, stay_win, stay_loss, total_games):
    if swap == 1:
        if result == 1:
            swap_win += 1
        else:
            swap_loss += 1
    else:
        if result == 1:
            stay_win += 1
        else:
            stay_loss += 1

    print("")
    print("swap : winning: {}, loss: {}".format(swap_win, swap_loss))
    print("stay : winning: {}, loss: {}".format(stay_win, stay_loss))
    print("\n\ntotal winning rate: ")
    print("swap : ", swap_win/total_games*100)
    print("stay : ", stay_win/total_games*100)

    return swap_win, swap_loss, stay_win, stay_loss




def main():
    swap = 0
    swap_win = 0
    swap_loss = 0
    stay_win = 0
    stay_loss = 0
    total_games = 0

    continue_playing = True

    while continue_playing:
        print(door_graph.ALL_CLOSED)

        user_choice = get_user_choice()
        doors_situation, car_position = doors_init(user_choice)
        user_choice, swap = make_choose(doors_situation, user_choice, car_position, swap)
        result, total_games = result_judge(user_choice, car_position, total_games)
        swap_win,swap_loss, stay_win, stay_loss = result_cal(result, swap, swap_win, swap_loss, stay_win, stay_loss, total_games)

        while True:
            want_to_again = input("Do you want to play again? (y or n): ").lower().strip()
            if want_to_again in ["y", "n"]:
                if want_to_again == "n":
                    continue_playing = False
                break






if __name__ == "__main__":
    main()
