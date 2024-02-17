formatter = "{} {} {} {}"
a_phrase = ["You", "know", "me", "well"]

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format(
    a_phrase[0], a_phrase[1], a_phrase[2], a_phrase[3]),
    formatter.format(a_phrase[2], a_phrase[3], a_phrase[0], a_phrase[1]),
    formatter.format(a_phrase[1], a_phrase[0], a_phrase[3], a_phrase[2]),
    formatter.format(a_phrase[3], a_phrase[2], a_phrase[1], a_phrase[0])))

print("")
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
