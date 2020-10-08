#make_chocolate
def make_chocolate(small, big, goal):
    bar = goal / 5

    if big >= bar:
        if small >= (goal - bar * 5):
            return goal - bar * 5

    if big < bar:
        if small >= (goal - big * 5):
            return goal - big * 5

    return -1