fIn = open("input.txt", "r")

fText = fIn.read()
fText = fText.split("\n")
nRed = 12
nGreen = 13
nBlue = 14
game_count = 0
possible_games = 0

for line in fText:
    game_count += 1
    possible = True
    line = line.split(";")
    for set in line:
        for delimiter in [" ", ", "]:
            set = " ".join(set.split(delimiter))
        set = set.split()
        for i in range(len(set)):
            if(set[i] == "blue"):
                if(int(set[i-1]) > nBlue):
                    possible = False
            if(set[i] == "red"):
                if(int(set[i-1]) > nRed):
                    possible = False
            if(set[i] == "green"):
                if(int(set[i-1]) > nGreen):
                    possible = False
    if(possible):
        possible_games += game_count
print(possible_games)