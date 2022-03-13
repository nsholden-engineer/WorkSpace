import typing

def validate(guess: str, wordlen: int, wordlist: typing.Set[str]) -> typing.Tuple[str, str]:

    guess_upper = guess.upper()

    if len(guess_upper) != wordlen:
        return f"Guess must be of length {wordlen}", guess_upper
    
    if guess_upper not in wordlist:
        return "Guess must be a valid word", guess_upper

    return None, guess_upper

def get_user_guess(wordlen: int, wordlist: typing.Set[str]) -> str:

    while True:
        guess = input("Guess: ")

        error, guess = validate(guess=guess, wordlen=wordlen, wordlist=wordlist)


        if error is None:
            break

        print(error)
    return guess

def compare(expected: str, guess: str) -> typing.List[str]:

    output = ["_"] * len(expected)

    for index, (expected_char, guess_char) in enumerate(zip(expected, guess)):
        if expected_char == guess_char:
            output[index] = "*"

    return output


if __name__ == '__main__':
    
    WORD = "TESTS"
    GAME_WORD_LENGTH = len(WORD)
    GUESS_WORDLIST = [WORD, "GAMES", "FRONT", "TILES"]

    print("\n",
    compare("steer", "stirs"),"\n",
    compare("steer", "floss"),"\n",
    compare("pains", "stirs"),"\n",
    compare("creep", "enter"),"\n",
    compare("crape", "enter"),"\n",
    compare("ennui", "enter"),"\n")

    try:
        while True:
            GUESS = get_user_guess(GAME_WORD_LENGTH, GUESS_WORDLIST)
            if WORD == GUESS:
                print("You won!")
                break
    except KeyboardInterrupt:
        print("You exited the game.")
