class Card:
    won_cards = None
    spare_count = 0

    def __init__(this, num, winning_nums, card_nums):
        this.num = num
        this.won_cards = []
        
        matches = 0
        for winning_num in winning_nums:
            for card_num in card_nums:
                if(winning_num == card_num):
                    matches += 1
        for i in range(matches):
            this.won_cards.append(int(num) + i +1)

    def get_won_cards(this):
        return this.won_cards
    
    def increment_count(this):
        this.spare_count += 1
    
    def __str__(this):
        return f"{this.num}"


fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")

cards = []
count = 0

for card in text:
    count += 1
    card = card.split(" | ")
    winning_nums = card[0][8:len(card[0])].split()
    card_nums = card[1].split()
    

    cards.append(Card(count, winning_nums, card_nums))


for card in cards:
    if(len(card.get_won_cards()) != 0):
        for won_card in card.get_won_cards():
            cards.append(cards[won_card - 1])

print(len(cards))
