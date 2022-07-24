"""
* CS50P Problem Set 3
* Outdated
* by Samu Reinikainen 24.07.2022
"""

def main():
    print("What date is it (\"(m/d/y)\")? ", end="")
    udate = get_input("")

    #slist.sort()

    print(udate)

def get_input(prompt):
    x = []
    while True:
        udate = convert_date(input(prompt))
        if udate != False:
            return udate

def convert_date(udate):
    # 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

    if udate.count("/") == 2:
        return conv_num_date(udate)
    elif udate.count(",") == 1:
        return conv_mon_date(udate)
    else:
        return False

def conv_num_date(udate):
    parts = udate.split("/")
    #print(parts)

    try:
        day = int(parts[1])
        mon = int(parts[0])
        year = int(parts[2])
    except ValueError:
        return False

    if 0 >= day > 31: # or 0 <= mon < 12:
        print(day)
        return False

    return str(day).zfill(2) + "-" + str(mon).zfill(2) + "-" + str(year)


def conv_mon_date(udate):
    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    parts = udate.split(",")
    year = parts[1].strip()
    parts = parts[0].split(" ")
    mon = parts[0].strip().lower().title()
    day = parts[1].strip()

    if mon not in months:
        return False

    mon = str(months.index(mon)+1)

    tdate = mon + "/" + day + "/" + year

    return conv_num_date(tdate)

main()