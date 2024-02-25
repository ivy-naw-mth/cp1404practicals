def main():
    """Score Classification Program"""
    score = float(input("Enter score: "))
    print(decide_condition(score))

def decide_condition(score):
    """Deciding score condition"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()