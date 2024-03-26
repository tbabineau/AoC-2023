import string
kinds = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]

def get_num_true(arr):
    count = 0
    for i in range(5):
        if(arr[i]):
            count += 1
    return count


class Hand:
    def __init__(this, cards):
        this.cards = cards

        this.table = [False]*5
        for i in range(5):
            column = [False]*5
            for j in range(5):
                if(cards[i] == cards[j]):
                    column[j] = True
                this.table[i] = column

        matches = [0]*5
        for i in range(5):
            matches[i] = get_num_true(this.table[i])


        #5 of a kind
        if(matches[0] == 5):
            this.kind = "Five"
        
        #4 of a kind
        if(matches[0] == 4 or matches[1] == 4):
            this.kind = "Four"

        #full house
        if(matches[0] == 3 or matches[0] == 2):
            for i in range(1, 5):
                if((matches[i] == 2 or matches[i] == 3) and matches[i] != matches[0]):
                    this.kind = "Full"

        #3 of a kind
            
        
        #two pair
        

        #one pair
        

        #high card
        

            

    def compare_to(this, other):
        comparable = 0

    def __str__(this):
        return f"{this.cards[0]}\t{this.cards[1]}\t{this.cards[2]}\t{this.cards[3]}\t{this.cards[4]}\n{this.compare_table[0]}\n{this.compare_table[1]}\n{this.compare_table[2]}\n{this.compare_table[3]}\n{this.compare_table[4]}"

test = Hand("ABCDE")

print(test)