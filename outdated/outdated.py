"""
* CS50P Problem Set 3
* Outdated
* by Samu Reinikainen 24.07.2022
"""

def main():
    print("What date is it (\"(m/d/y)\")? ")
    odate = get_input("")

    #slist.sort()

    #print_list(slist)

def get_input(prompt):
    x = []
    while True:
        udate = convert_date(input(prompt))
        if udate != False:
            return udate

def convert_date(udate):
   # 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    if udate.count("/") == 2:
        return conv_num_date(udate)
    else:
        for month in months:
            if month in udate:
                return conv_mon_date(udate)

    return False

def conv_num_date(udate):
    parts = udate.split("/")
    print(parts)

main()