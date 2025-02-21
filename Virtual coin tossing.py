import random

def coin_toss():
    """Simulate a coin toss and return the result."""
    return random.choice(['Heads', 'Tails'])

def main():
    print("Welcome to the Virtual Coin Toss Simulator!")
    
    while True:
        try:
            # Get user input for the number of tosses
            num_tosses = int(input("How many times would you like to toss the coin? (Enter a positive integer): "))
            
            if num_tosses <= 0:
                print("Please enter a positive integer.")
                continue
            
            # Initialize counters for heads and tails
            heads_count = 0
            tails_count = 0
            
            # Perform the coin tosses
            for _ in range(num_tosses):
                result = coin_toss()
                if result == 'Heads':
                    heads_count += 1
                else:
                    tails_count += 1
            
            # Display the results
            print(f"\nResults after {num_tosses} tosses:")
            print(f"Heads: {heads_count}")
            print(f"Tails: {tails_count}")
            print(f"Total Tosses: {heads_count + tails_count}")
            
            # Ask if the user wants to toss again
            toss_again = input("\nWould you like to toss again? (yes/no): ").strip().lower()
            if toss_again != 'yes':
                print("Thank you for using the Virtual Coin Toss Simulator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
