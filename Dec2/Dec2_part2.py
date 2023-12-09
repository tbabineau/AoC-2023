import math
fIn = open("input.txt", "r")

fText = fIn.read()
fText = fText.split("\n")
min_red = 0
min_blue = 0
min_green = 0

cube_power = 0

for line in fText:
    line = line.split(";")
    min_red = 0
    min_blue = 0
    min_green = 0
    for set in line:

        for delimiter in [" ", ", "]:
            set = " ".join(set.split(delimiter))
        set = set.split()
        for i in range(len(set)):
            if(set[i] == "blue"):
                if(int(set[i - 1]) > min_blue):
                    min_blue = int(set[i-1])
            if(set[i] == "red"):
                if(int(set[i - 1]) > min_red):
                    min_red = int(set[i-1])
            if(set[i] == "green"):
                if(int(set[i - 1]) > min_green):
                    min_green = int(set[i-1])

    cube_power += min_red * min_blue * min_green

print(cube_power)