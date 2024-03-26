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
    def __init__(this, val):
        this.val = val
        this.next = val
        this.placed = False

    def isPlaced(this):
        return this.placed
    
    def setPlaced(this, placed):
        this.placed = placed

    def getSeed(this):
        return this.val

    def __str__(this):
        return f"{this.val} corresponds to {this.next}"
    
    def setNext(this, val):
        this.next = val

    def getNext(this):
        return this.next

fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")
seeds = text[0][7:len(text[0])].split()
destination = [0]*len(seeds)

for i in range(len(seeds)):
    seeds[i] = Seed(int(seeds[i]))

ranges = []
    
for i in range(3, len(text)):
    if(text[i] == "" or text[i][0] in string.ascii_letters):
        for range in ranges:
            for seed in seeds:
                if(not seed.isPlaced()):
                    result = range.is_in_range(seed.getNext())
                    if(result > 0):
                        seed.setNext(result)
                        seed.setPlaced(True)

        ranges = []
        for seed in seeds:
            seed.setPlaced(False)
    else:
        nums = text[i].split()
        ranges.append(Range(int(nums[0]), int(nums[1]), int(nums[2])))

for range in ranges:
            for seed in seeds:
                if(not seed.isPlaced()):
                    result = range.is_in_range(seed.getNext())
                    if(result > 0):
                        seed.setNext(result)
                        seed.setPlaced(True)
min_location = seeds[0].getNext()

for seed in seeds:
    if(min_location > seed.getNext()):
        min_location = seed.getNext()

print(min_location)
