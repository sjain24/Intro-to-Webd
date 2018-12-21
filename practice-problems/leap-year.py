def is_leap(year):
    if year < 1900 or year > 100000:
        print("Enter year between 1900 and 100000")
        return False

    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    # Write your logic here

    return leap


year = int(input())