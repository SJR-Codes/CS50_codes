"""
* CS50P Problem Set 8
* Shitificate
* by Samu Reinikainen 30.07.2022
"""

from fpdf import FPDF

def make_shirt(name)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, "CS50 Shirtificate")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter name: ").strip()

    if name.len() > 0:
        make_shirt(name)
    else:
        exit()

if __name__ == "__main__":
    main()
