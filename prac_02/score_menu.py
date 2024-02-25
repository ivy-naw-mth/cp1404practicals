MINIMUM_SCORE = 0
PASSING_SCORE = 50
HIGH_SCORE = 90
MAXIMUM_SCORE = 100

MENU = """
G - Get a valid score (must be 0 - 100 inclusive)
P - Print Result
S - Show stars (as many stars as the score)
Q - Quit
"""

def main():
    """Score menu program main function"""
    score = ""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            score_feedback = decide_score_condition(score)
            print(score_feedback)
        elif choice == "S":
            print(stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thanks for using our program, goodbye!")

def get_valid_score():
    """Function to get the valid score"""
    score = int(input("Please enter a valid score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Please enter a valid score: "))
    return score

def decide_score_condition(score):
    """Function to decide the score input"""
    if score >= HIGH_SCORE:
        return "Excellent"
    elif score >= PASSING_SCORE:
        return "Passable"
    else:
        return "Bad"

def stars(score_result):
    """Convert score into stars"""
    return "*" * score_result

main()
