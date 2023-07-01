from fpdf import FPDF

class PDF(FPDF):
    def get_shirt(self, name):
        self.add_page()
        self.set_font('helvetica', "B", size=25)
        self.cell(0, 10, "CS50 Shirtificate", align = "C")
        self.image("shirtificate.png", x=0, y=60)
        self.set_text_color(255,255,255)
        self.text(70, 150, f"{name} took CS50")
        self.output("shirtificate.pdf")

pdf = PDF()
name = input("Name: ")
pdf.get_shirt(name)


