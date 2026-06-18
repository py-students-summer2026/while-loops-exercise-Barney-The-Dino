"""
Sings "99 Bottles of Beer on the Wall" using a while loop controlled by an
accumulator variable.
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
    loop controlled by an accumulator (count) that counts down to 0.
    """

    count = num_bottles
    while count > 0:
        current = bottle_phrase(count)
        remaining = bottle_phrase(count - 1)

        print(f"{current} of beer on the wall, {current} of beer.")
        if count > 1:
            print(f"Take one down, pass it around, {remaining} of beer on the wall.")
        else:
            print(f"Take it down, pass it around, {remaining} of beer on the wall!")
        print()

        # update the accumulator so the loop eventually terminates
        count -= 1
