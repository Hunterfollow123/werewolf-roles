#-*-coding:utf8;-*-
#qpy:3
# CODED BY HUNTER FOLLOW :)

import random, os, time

os.system("cls")
print("\n")

path = str(input("Path to the players file : "))
os.system("clear")
print("\n")
file = open(path, "r").readlines()


players = list(random.sample(file, k=len(file)))


s = 0
for player in players:
    if player == players[2]:
        break
    s = s + 1
    print("wolf", s, " : ", player, end="\r")
    players.remove(player)
    time.sleep(0.2)


print("\n")

s = 0
for player in players:
    if player == players[6]:
        break
    s = s + 1
    print("role", s, ":", player, end="\r")
    players.remove(player)
    time.sleep(0.2)

print("\n")

print("""role 1 = seeker
role 2 = hunter
role 3 = witch
role 4 = salva
role 5 = crow
role 6 = sniper
""")


