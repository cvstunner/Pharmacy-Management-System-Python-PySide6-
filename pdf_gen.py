from reportlab.pdfgen import canvas

class Invoice():
    def __init__(self):
        super(Invoice, self).__init__()
        self.invoice_number = 0
    def createInvoice(self, details):
        for index, drug in enumerate(details):
            invoice_number = str(drug[0])
            break;
        self.c = canvas.Canvas(("C:/MediMan/Invoice"+str(invoice_number)+".pdf"), pagesize=(300,400))
        self.c.setFont("Times-BoldItalic",18)

        self.c.drawString(20, 370, "MediMan")
        self.c.line(20, 365, 280, 365)

        self.c.setFont("Courier",6)
        self.c.drawString(20, 340, "Name:")
        self.c.drawString(20, 330, "Phone:")
        self.c.drawString(20, 320, "Address:")
        self.c.drawString(20, 310, "Bill-id:")

        self.c.setFont("Courier",5)
        self.c.setLineWidth(.2)
        self.c.line(20, 290, 280, 290)
        self.c.drawString(30, 283, "Sr No.")
        self.c.line(60, 280, 60, 290)
        self.c.drawString(73, 283, "Drug")
        self.c.line(100, 280, 100, 290)
        self.c.drawString(114, 283, "Company")
        self.c.line(150, 280, 150, 290)
        self.c.drawString(162, 283, "Price")
        self.c.line(190, 280, 190, 290)
        self.c.drawString(202, 283, "Quantity")
        self.c.line(240, 280, 240, 290)
        self.c.drawString(253, 283, "Total")
        self.c.line(20, 280, 280, 280)

        self.c.drawString(35, 270, "1.")
        self.c.drawString(35, 260, "2.")
        self.c.drawString(35, 250, "3.")
        self.c.drawString(35, 240, "4.")
        self.c.drawString(35, 230, "5.")
        self.c.drawString(35, 220, "6.")
        self.c.drawString(35, 210, "7.")
        self.c.drawString(35, 200, "8.")
        self.c.drawString(35, 190, "9.")
        self.c.drawString(33, 180, "10.")
        self.c.line(20, 170, 280, 170)
        self.c.drawString(30, 163, "TOtal")
        self.c.line(20, 160, 280, 160)

        # print(self.c.getAvailableFonts())
        # self.details = [(1, 'Chetan Shigvan', '1234567890', 'Mumbai 33', '04/18/2022, 00:26:57', 'temp2', 'A-Quin', '157', '3', '471')]
        # self.set_drugs_details(self.details)
        # print("class")
        # self.c.save()

    # def set_user_details(self, details):
    #     for index, drug in enumerate(details):
    #         print(index, drug)
    #         self.c.drawString(40, 340, drug[1])
    #         self.c.drawString(43, 330, drug[2])
    #         self.c.drawString(51, 320, drug[3])
    #         self.c.drawString(51, 310, str(drug[0]))
    #         break;

    # def set_drugs_details(self, details):
    #     row = 270
    #     for index, drug in enumerate(details):
    #         self.c.drawString(63, row, drug[5])
    #         self.c.drawString(114, row, drug[6])
    #         self.c.drawString(162, row, drug[7])
    #         self.c.drawString(210, row, drug[8])
    #         self.c.drawString(253, row, drug[9])
    #         row-=10
    #         print(row, index)
    #     print("Done")

    def dumpInvoice(self, details):
        row = 270
        grand_total = 0
        for index, drug in enumerate(details):
            print(index, drug)
            self.c.drawString(40, 340, drug[1])
            self.c.drawString(43, 330, drug[2])
            self.c.drawString(51, 320, drug[3])
            self.c.drawString(51, 310, str(drug[0]))
            break;
        for index, drug in enumerate(details):
            self.c.drawString(63, row, drug[5])
            self.c.drawString(114, row, drug[6])
            self.c.drawString(162, row, drug[7])
            self.c.drawString(210, row, drug[8])
            self.c.drawString(253, row, drug[9])
            grand_total = grand_total + int(drug[9])
            row-=10
        self.c.drawString(253, 163, str(grand_total))
        self.c.save()