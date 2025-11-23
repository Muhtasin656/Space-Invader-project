class integertoroman:
    def __init__(self):
        
        self.values = [

        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),

        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),

        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),

        (1, "I")

    ] 
def converter(self,num):
    roman=""
    for value, symbol in self.value:
        while num >=value:
            roman += symbol
            num -=value
    return roman 
obj=integertoroman()
number=int(input("enter a number"))   
print("Roman numeral:",obj.convert(number))    