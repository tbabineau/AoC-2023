fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")

def get_length(x):
    count = 0
    while(x - (x % 10**count) != 0):
        count += 1
    return count

for i in range(len(text)):
    text[i] = text[i].split()
    for j in range(1, len(text[i])):
        text[i][j] = int(text[i][j])

time = 0
dist = 0
for i in range(1, len(text[0])):
    time = time * (10**get_length(text[0][i]))
    time += text[0][i]
    
    dist = dist * (10**get_length(text[1][i]))
    dist += text[1][i]


result = 0
start_found = False

for i in range(time):
    print(i)
    if(not start_found):
        if(i * (time - i) > dist):
            result = -i
            start_found = True
    else:
        if(i * (time - i) <= dist):
            result += i
            break
print(result)