def list_func():
    return ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


def gen_func():
    yield "A"
    yield "K"
    yield "Q"
    yield "J"
    yield "10"
    yield "9"
    yield "8"
    yield "7"
    yield "6"
    yield "5"
    yield "4"
    yield "3"
    yield "2"


for card in list_func():
    print(f"{card} of Hearts")

for card in gen_func():
    print(f"{card} of Hearts")
