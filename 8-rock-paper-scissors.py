rule = {
    "rock": 
        {
            "scissor": "win",
            "paper": "lose",
            "rock": "draw",
        },
    "paper": 
        {
            "rock": "win",
            "scissor": "lose",
            "paper": "draw",
        },
    "scissor":
        {
            "paper": "win",
            "rock": "lose",
            "scissor": "draw",
        },
}

play = True
while play:

    player1 = input("Wybierz jedno: rock, paper, scissor: ")
    player2 = input("Wybierz jedno: rock, paper, scissor: ")

    print(rule[player1][player2])
    if player1 == 'q' or player2 == 'q':
        play = False

