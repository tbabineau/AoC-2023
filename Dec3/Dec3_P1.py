import string
fIn = open("input.txt", "r")

fText = fIn.read()
fText = fText.split("\n")

def findNum(array, row, col):
    minCol = col
    maxCol = col
    max = len(array[0]) - 1

    while((minCol > 0) and (array[row][minCol] in string.digits)):
        minCol -= 1
    while((maxCol < max) and (array[row][maxCol] in string.digits)):
        maxCol += 1

    if(array[row][minCol] not in string.digits):
        minCol += 1
    if(array[row][maxCol] not in string.digits):
        maxCol -= 1
    return [minCol, maxCol]

partSum = 0

for i in range(len(fText)):
    for j in range(len(fText[i])):
        currCell = fText[i][j]
        if(currCell != "." and (not (currCell in string.digits))):
            if(i > 0):
                if(fText[i-1][j] in string.digits):
                    num = findNum(fText, i-1, j)
                    partSum += int(fText[i-1][num[0]:num[1]+1:1])
                else:
                    if(j > 0 and fText[i-1][j-1] in string.digits):
                        num = findNum(fText, i-1, j-1)
                        partSum += int(fText[i-1][num[0]:num[1]+1:1])
                    if(j < len(fText[0]) and fText[i-1][j+1] in string.digits):
                        num = findNum(fText, i-1, j+1)
                        partSum += int(fText[i-1][num[0]:num[1]+1:1])
            if(i < len(fText[0]) - 1):
                if(fText[i+1][j] in string.digits):
                    num = findNum(fText, i+1, j)
                    partSum += int(fText[i+1][num[0]:num[1]+1:1])
                else:
                    if(j > 0 and fText[i+1][j-1] in string.digits):
                        num = findNum(fText, i+1, j-1)
                        partSum += int(fText[i+1][num[0]:num[1] + 1: 1])
                    if(j < len(fText[0]) and fText[i+1][j+1] in string.digits):
                        num = findNum(fText, i+1, j+1)
                        partSum += int(fText[i+1][num[0]:num[1] + 1:1])
            if(j > 0 and fText[i][j-1] in string.digits):
                num = findNum(fText, i, j-1)
                partSum += int(fText[i][num[0]:num[1]+1:1])
            if(j < len(fText[0]) - 1 and fText[i][j+1] in string.digits):
                num = findNum(fText, i, j+1)
                partSum += int(fText[i][num[0]:num[1]+1])

print(partSum)