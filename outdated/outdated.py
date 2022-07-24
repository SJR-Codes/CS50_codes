"""
* CS50P Problem Set 3
* Outdated
* by Samu Reinikainen 24.07.2022
"""

def main():
    print("What date is it (\"(m/d/y)\")? ")
    odate = get_input("")

    #slist.sort()

    print_list(slist)

def get_input(prompt):
    x = []
    while True:
        udate = validate_date(input(prompt)):
        if udate != False:
            return convert_date(udate)

def validate_date(udate):
   # 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

main()