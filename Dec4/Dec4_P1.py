fIn = open("input.txt", "r")
text = fIn.read()
text = text.split("\n")

total_points = 0

for card in text:
    card_wins = -1
    card = card.split(" | ")
    winning_nums = card[0][8:len(card[0])].split()
    my_nums = card[1].split()

    for winning_num in winning_nums:
        for my_num in my_nums:
            if(my_num == winning_num):
                card_wins += 1

    if(card_wins >=0):
        total_points += 2**card_wins

print(total_points)