import time
import random

# --- Game Functions ---
def play_game():
    """Runs a single instance of the virtual pet game."""
    print("\n🐾 Welcome to the Virtual Pet Game!")
    name = input("What would you like to name your pet? ")
    pet_type = input("What kind of pet is it? (dog, cat, alien, etc): ")

    hunger = 5  # 0 is full, 10 is starving
    happiness = 5  # 0 is sad, 10 is super happy
    possible_finds = [
        "ezra",
        "a mystery egg",
        "a ball",
        "a chewy toy",
        "a dog toy"
    ]

    print(f"\nYou adopted a {pet_type} named {name}! Take good care of it.")

    # Game loop (runs for 5 turns)
    start_time = time.time()
    for turn in range(5):
        print(f"\n--- Turn {turn + 1} ---")
        print(f"{name}'s stats: Hunger: {hunger}/10, Happiness: {happiness}/10")
        print("\nWhat would you like to do?")
        print("1 - Feed")
        print("2 - Play")
        print("3 - Do nothing")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            hunger = max(0, hunger - 2)
            print(f"You fed {name}. Hunger is now {hunger}.")
        elif choice == "2":
            happiness = min(10, happiness + 2)
            hunger = min(10, hunger + 1)  # playing makes it hungry
            print(f"You played with {name}. Happiness is now {happiness} 😜, but hunger is now {hunger} 🤤")
            if random.random() < 0.7:
                found_object = random.choice(possible_finds)
                print(f"While playing, {name} dug up {found_object} 🎉!")
        elif choice == "3":
            hunger = min(10, hunger + 2)
            happiness = max(0, happiness - 2)
            print(f"You did nothing. {name} looks bored and hungry... 😢")
        else:
            print("Invalid choice. Nothing happens.")

        # Check for game over conditions within the loop
        if hunger >= 10:
            print(f"\nOh no! {name} was too hungry and ran away in search of snacks. 🍟 Game Over!")
            return # End the current game
        elif happiness <= 0:
            print(f"\nOh no! {name} got too sad and hid in its pet bed. 🐾 Game Over!")
            return # End the current game

    # End of game after 5 turns
    print("\n🧾 Game Over!")
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print(f"You kept your pet alive for {elapsed_time} seconds.")
    print(f"You did a great job taking care of {name}! 🎉")

# --- Main Game Loop ---
while True:
    play_game() # Call the function to run a single game

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break # Exit the main loop if the user doesn't want to play again
