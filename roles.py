#-*-coding:utf8;-*-
#qpy:3
# CODED BY HUNTER FOLLOW :)

import random, os, time

os.system("cls")
print("\n")
path = str(input("Path to the players file : "))
def main():
    os.system("cls")
    print("\n")

    os.system("cls")

    print("\n")

    file = open(path, "r").readlines()


    players = list(random.sample(file, k=len(file)))

    try:
        wolfs_num = int(input("How many wolfs ? : "))
    
    except:
        print("[!] invalid, please enter a number")
        wolfs_num = int(input("How many wolfs ? : "))
    
    print("\n" + str(len(file)), "players,", wolfs_num, "wolfs,", "6 roles,", len(file) - wolfs_num - 6, "Villagers\n")


    s = 0

    for player in players:
        try:
            if player == players[wolfs_num]:
                break
        except:
            print("too many wolfs!")
            exit()
        
        s = s + 1
        print("wolf", s, " : ", player, end="\r")
        players.remove(player)
        time.sleep(0.2)


    print("\n")

    roles = [
    "seeker",
    "hunter",
    "witch",
    "salva",
    "crow",
    "sniper",
    ]

    j = list(random.sample(players, k=6))


    for player in j:
        x = random.choice(roles)
        print(x, ":", player, end="\r")
        roles.remove(x)
        time.sleep(0.2)



    print("\n")



def rerun():
    os.system("cls")
    print("\n")

    file = open(path, "r").readlines()


    players = list(random.sample(file, k=len(file)))

    try:
        wolfs_num = int(input("How many wolfs ? : "))
    
    except:
        print("[!] invalid, please enter a number")
        wolfs_num = int(input("How many wolfs ? : "))
    
    print("\n" + str(len(file)), "players,", wolfs_num, "wolfs,", "6 roles,", len(file) - wolfs_num - 6, "Villagers\n")


    s = 0

    for player in players:
        try:
            if player == players[wolfs_num]:
                break
        except:
            print("too many wolfs!")
            exit()
        
        s = s + 1
        print("wolf", s, " : ", player, end="\r")
        players.remove(player)
        time.sleep(0.2)


    print("\n")

    roles = [
    "seeker",
    "hunter",
    "witch",
    "salva",
    "crow",
    "sniper",
    ]

    j = list(random.sample(players, k=6))


    for player in j:
        x = random.choice(roles)
        print(x, ":", player, end="\r")
        roles.remove(x)
        time.sleep(0.2)



    print("\n")



main()
while True:
    choice = str(input("\n[0]exit    [1]re-run\n\n>> : "))
    if choice == "0":
        exit()
    elif choice == "1":
        rerun()
    else:
        print("[!]invalid")
        
