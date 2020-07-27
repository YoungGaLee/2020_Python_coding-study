def is_leap(year):
    leap = False

    if year % 4 is 0:
        if year % 100 is 0:
            if year % 400 is 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap