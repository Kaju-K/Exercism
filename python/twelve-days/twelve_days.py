days = {1: "first", 2: "second", 3: "third", 4: "fourth", 5:"fifth", 6:"sixth", 7: "seventh",
        8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}

gifts = ["twelve Drummers Drumming, ", "eleven Pipers Piping, ", "ten Lords-a-Leaping, ", "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ", "six Geese-a-Laying, ", "five Gold Rings, ",
        "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, and ", "a Partridge in a Pear Tree."]

def recite(start_verse, end_verse):
    song = []
    for verse in range(start_verse, end_verse+1):
        song.append(f"On the {days.get(verse)} day of Christmas my true love gave to me: " + "".join(gifts[-verse:]))
    return song
