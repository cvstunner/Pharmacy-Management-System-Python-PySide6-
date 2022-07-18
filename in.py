from pdf_gen import Invoice 
class a:
    def __init__(self):
        details = [(1, 'Chetan Shigvan', '1234567890', 'Mumbai 33', '04/18/2022, 00:26:57', 'temp2', 'A-Quin', '157', '3', '471')]
        Invoice.set_drugs_details(details)
        print("Hi")

obj = a()