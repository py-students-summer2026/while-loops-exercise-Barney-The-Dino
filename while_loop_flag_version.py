"""
Sings "99 Bottles of Beer on the Wall" using a while loop controlled by a flag
variable.
"""


def get_starting_number():
    """
    Asks the user how many bottles of beer to start with, repeating the
    question until they enter a valid response (any integer 1 or greater).
    Returns the integer the user entered.
    """

    while True:
        response = input("How many bottles of beer on the wall? ")
        try:
            number = int(response)
        except ValueError:
            continue
        if number >= 1:
            return number


def bottle_phrase(count):
    """
    Returns the grammatically correct phrase for a given number of bottles,
    e.g. "no more bottles", "1 bottle", or "5 bottles".
    """

    if count == 0:
        return "no more bottles"
    elif count == 1:
        return "1 bottle"
    else:
        return f"{count} bottles"


def sing(num_bottles):
    """
    Outputs the lyrics to the song, starting from num_bottles, using a while
    loop controlled by a flag that signals when to stop singing.
    """

    count = num_bottles
    still_singing = True
    while still_singing:
        current = bottle_phrase(count)
        remaining = bottle_phrase(count - 1)

        print(f"{current} of beer on the wall, {current} of beer.")
        if count > 1:
            print(f"Take one down, pass it around, {remaining} of beer on the wall.")
        else:
            print(f"Take it down, pass it around, {remaining} of beer on the wall!")
        print()

        count -= 1

        # lower the flag once the last bottle has been sung
        if count == 0:
            still_singing = False
