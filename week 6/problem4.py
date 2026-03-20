#Static Method
class Kitchen:

    @staticmethod
    def cups_to_ml(cups):
        return round(cups * 236.588, 1)
    
    @staticmethod
    def tbsp_to_ml(tbsp):
        return round(tbsp * 14.787, 1)

print(Kitchen.cups_to_ml(2))
print(Kitchen.cups_to_ml(0.5))
print(Kitchen.tbsp_to_ml(3))
print(Kitchen.tbsp_to_ml(10))