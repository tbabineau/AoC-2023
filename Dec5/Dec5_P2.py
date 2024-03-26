import string

class Range:
    def __init__(this, dest, source, length):
        this.dest = dest
        this.source = source
        this.length = length

    def __str__(this):
        return f"{this.dest} {this.source} {this.length}"
    
    def is_in_range(this, seed):
        if(this.source <= seed and seed <= this.source + this.length - 1):
            return seed - this.source + this.dest
        else:
            return -1
        
class Seed:
    def __init__(this, val, length):
        this.val = val
        this.length = length
        this.next = []
        for i in range(val, val+length):
            this.next.append(i)
        this.placed = [False]*length

    def isPlaced(this, pos):
        return this.placed[pos]
    
    def setPlaced(this, placed, pos):
        this.placed[pos] = placed

    def getSeed(this):
        return this.val

    def __str__(this):
        return f"{this.val} corresponds to {this.next}"
    
    def setNext(this, val, pos):
        this.next[pos] = val

    def getNext(this, pos):
        return this.next[pos]
    
    def getLength(this):
        return this.getLength

fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")
nums = text[0][7:len(text[0])].split()
seeds = []

for i in range(0, len(nums), 2):
    seeds.append(Seed(int(nums[i]), int(nums[i+1])))


ranges = []
    
for i in range(3, len(text)):
    if(text[i] == "" or text[i][0] in string.ascii_letters):
        for area in ranges:
            for seed in seeds:
                for j in range(seed.getSeed(), seed.val + seed.length):
                    if(not seed.isPlaced(j - seed.getSeed())):
                        result = area.is_in_range(seed.getNext(j - seed.val))
                        if(result > 0):
                            seed.setNext(result, j - seed.val)
                            seed.setPlaced(True, j - seed.val)

        ranges = []
        for seed in seeds:
            for i in range(seed.length):
                seed.setPlaced(False, i)
    else:
        nums = text[i].split()
        ranges.append(Range(int(nums[0]), int(nums[1]), int(nums[2])))

for area in ranges:
            for seed in seeds:
                for j in range(seed.getSeed(), seed.val + seed.length):
                    if(not seed.isPlaced(j - seed.getSeed())):
                        result = area.is_in_range(seed.getNext(j - seed.val))
                        if(result > 0):
                            seed.setNext(result, j - seed.val)
                            seed.setPlaced(True, j - seed.val)

min_location = seeds[0].getNext(0)

for seed in seeds:
    for i in range(seed.length):
        if(min_location > seed.getNext(i)):
            min_location = seed.getNext(i)

print(min_location)
