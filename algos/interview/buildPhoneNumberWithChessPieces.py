def buildNumber(startingDigits, keyboardDigits, transitionRules, length):
    """
    Build numbers starting with digits from `startingDigits`, using only digits in `keyboardDigits`,
    and respecting the `transitionRules`.
    
    :param startingDigits: List of allowed starting digits.
    :param keyboardDigits: List of allowed digits on the keyboard.
    :param transitionRules: Dictionary defining valid transitions (e.g., {1: [2, 3], 2: [4]})
    :param length: Desired length of the number.
    :return: List of valid numbers as strings.
    """
    def isValidTransition(prev_digit, next_digit):
        """ Check if the transition from prev_digit to next_digit is valid. """
        return next_digit in transitionRules.get(prev_digit, [])
    
    def backtrack(current, remaining_length):
        """ Use backtracking to build valid numbers. """
        if remaining_length == 0:
            result.append("".join(current))
            return
        
        last_digit = int(current[-1]) if current else None
        
        for digit in keyboardDigits:
            if last_digit is None or isValidTransition(last_digit, digit):
                backtrack(current + [str(digit)], remaining_length - 1)

    result = []
    
    for start_digit in startingDigits:
        if start_digit in keyboardDigits:
            backtrack([str(start_digit)], length - 1)
    
    return result

# Example usage
startingDigits = [1, 2, 3]
keyboardDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
transitionRules = {1: [2, 3], 2: [4], 3: [1, 5]}
length = 4

valid_numbers = buildNumber(startingDigits, keyboardDigits, transitionRules, length)
print(valid_numbers)
