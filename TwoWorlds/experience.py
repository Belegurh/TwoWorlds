# character-levels
lvl_player = 1


# experience points
nxt_lvl = [10, 100, 500, 2000, 5000, 10000]
ep_player = 0


# increase experience points and lvl up
def exp(increase_ep):
    global ep_player
    global lvl_player
    global nxt_lvl

    ep_player += increase_ep

    if ep_player >= nxt_lvl[0]:
        lvl_player += 1
        del nxt_lvl[0]
        print(f"ep + {increase_ep}")
        print("Congratulations, Your character level has been increased.")
        print(f"You are now lvl {lvl_player}.")
    else:
        print(f"ep + {increase_ep}")
