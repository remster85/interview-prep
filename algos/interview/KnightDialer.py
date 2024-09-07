#https://leetcode.com/problems/knight-dialer/
# Display the keypad layout first for visualization
def display_keypad():
    print("Phone Keypad Layout:\n")
    print("  1    2    3")
    print("  4    5    6")
    print("  7    8    9")
    print("       0")

# Call this function to display the keypad layout before executing the main logic
display_keypad()

MOD = 10**9 + 7

def knightDialer(n, validStartingDigits):
    # Corrected Knight move mapping from each key
    moves = {
        0: [4, 6],      # Knight can jump from 0 to 4 or 6
        1: [6, 8],      # Knight can jump from 1 to 6 or 8
        2: [7, 9],      # Knight can jump from 2 to 7 or 9
        3: [4, 8],      # Knight can jump from 3 to 4 or 8
        4: [0, 3, 9],   # Knight can jump from 4 to 0, 3, or 9
        5: [],          # 5 has no valid knight moves
        6: [0, 1, 7],   # Knight can jump from 6 to 0, 1, or 7
        7: [2, 6],      # Knight can jump from 7 to 2 or 6
        8: [1, 3],      # Knight can jump from 8 to 1 or 3
        9: [2, 4]       # Knight can jump from 9 to 2 or 4
    }

    # Initialize the array f based on valid starting digits
    f = [0] * 10
    for digit in validStartingDigits:
        f[digit] = 1
    
    # Iterate for each move (up to n-1 moves)
    for _ in range(n - 1):
        t = [0] * 10
        # Update t for each digit based on the current f and the knight moves
        for i in range(10):
            for move in moves[i]:
                t[i] = (t[i] + f[move]) % MOD
        f = t  # Move to the next state

    # Sum the counts for all keys to get the result
    return sum(f) % MOD

# Example usage:
validStartingDigits = [2, 3, 4, 5, 6, 7, 8, 9]  # Valid starting numbers between 2 and 9
n = 10  # Length of the number to be built

# Display the result
print(f"\nNumber of distinct phone numbers of length {n}: {knightDialer(n, validStartingDigits)}")
