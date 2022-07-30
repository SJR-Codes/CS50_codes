"""
* CS50P Problem Set 8
* Shitificate
* by Samu Reinikainen 30.07.2022
"""

from fpdf import FPDF

def make_shirt(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 0, "CS50 Shirtificate", align="C", new_x="LEFT")
    pdf.image("shirtificate.png", w=pdf.epw, h=0)
    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter name: ").strip()

    if len(name) > 0:
        make_shirt(name)
    else:
        exit()

if __name__ == "__main__":
    main()
