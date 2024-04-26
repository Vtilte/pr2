class Printer:
    def __init__(self, printer_name, manufacturer_country, printer_color, price, text_color, manufacture_date, paper_type):
        self.printer_name = printer_name
        self.manufacturer_country = manufacturer_country
        self.printer_color = printer_color
        self.price = price
        self.text_color = text_color
        self.manufacture_date = manufacture_date
        self.paper_type = paper_type

    def display_data(self):
        print("Printer Data:")
        print(f"{'Printer name':<20} {self.printer_name}")
        print(f"{'Manufacturer country':<20} {self.manufacturer_country}")
        print(f"{'Printer color':<20} {self.printer_color}")
        print(f"{'Price':<20} {self.price}")
        print(f"{'Text color':<20} {self.text_color}")
        print(f"{'Manufacture date':<20} {self.manufacture_date}")
        print(f"{'Paper type':<20} {self.paper_type}")

printer_name = input("Enter printer name: ")
manufacturer_country = input("Enter manufacturer country: ")
printer_color = input("Enter printer color: ")
price = float(input("Enter printer price: "))
text_color = input("Enter text color: ")
manufacture_date = input("Enter manufacture date: ")
paper_type = input("Enter paper type: ")

# Create an instance of the Printer class
printer = Printer(printer_name, manufacturer_country, printer_color, price, text_color, manufacture_date, paper_type)

# Display the printer data
printer.display_data()