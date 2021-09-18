def decode(string):
    if string == "": return ""
    on_the_run = None
    number = ""
    in_a_number = False
    res = ""
    for i, char in enumerate(string):
        if not char.isdigit():
            if number == "": res += char
            else:
                res += char * int(number)
                number = ""
        else:
            number += char
    return res
            


def encode(string):
    if string == "": return ""
    on_the_run = None
    count = 1
    res = ""

    for char in string:
        if on_the_run is None:
            on_the_run = char
        elif char != on_the_run:
            if count == 1: count = ""
            res += f"{count}{on_the_run}"
            on_the_run = char
            count = 1
        elif char == on_the_run:
            count += 1
    if count == 1: count = ""
    res += f"{count}{on_the_run}"
    return res
