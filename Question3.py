def play_card_game():
    try:
        # Read input for player names and initial health
        player1, player2 = input().split()
        health1, health2 = map(int, input().split())
        damages = list(map(int, input().split()))  # Read the list of damages for each card

        score1, score2 = 0, 0  # Initialize scores for both players
        card_mapping = {"A": 0, "B": 1, "C": 2}  # Define a mapping of cards to their index in the damages list

        # Play 3 rounds of the card game
        for _ in range(3):
            card1, card2 = input().split()  # Read the cards played by both players
            damage1, damage2 = damages[card_mapping[card1]], damages[card_mapping[card2]]  # Get the damage values for the played cards

            # Update the health of both players based on the damage dealt by the opponent's card
            health1 -= damage2
            health2 -= damage1

            # Update the scores based on the comparison of damage values
            if damage1 > damage2:
                score1 += 1
            elif damage2 > damage1:
                score2 += 1

        # Print the scores and remaining health for both players
        print(f"{player1} -> Score: {score1}, Health: {health1}")
        print(f"{player2} -> Score: {score2}, Health: {health2}")

    except ValueError: 
        print("Invalid Command.")  # Handle ValueError if input format is incorrect

play_card_game()  # Call the function to play the card game
