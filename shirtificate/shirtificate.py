"""
* CS50P Problem Set 8
* Shitificate
* by Samu Reinikainen 30.07.2022
"""

from fpdf import FPDF

def make_shirt(name)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, name)
    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter name: ").strip()

    if name.len() > 0:
        make_shirt(name)
    else:
        exit()

if __name__ == "__main__":
    main()
