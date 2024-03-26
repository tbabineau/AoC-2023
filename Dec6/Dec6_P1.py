fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")

for i in range(len(text)):
    text[i] = text[i].split()
    for j in range(1, len(text[i])):
        text[i][j] = int(text[i][j])

result = [0]* (len(text[0]) -1)
start_found = False

for i in range(1, len(text[0])):
    for j in range(text[0][i] + 1):
        if(not start_found):
            if(j * (text[0][i] - j) > text[1][i]):
                start_found = True
                result[i-1] = -j
        else:
            if(j * (text[0][i] - j) <= text[1][i]):
                start_found = False
                result[i-1] += j
                break 

total = 1

for num in result:
    total *= num
print(total)
