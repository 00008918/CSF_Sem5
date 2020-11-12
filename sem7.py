Marks = dict()
Marks["CSF"] = int(input("CSF: "))
Marks["FunPro"] = int(input("FunPro: "))
Marks["WebDesign"] = int(input("WebDesign: "))

def calculate(d):
    all_marks = d.values()
    total = sum(all_marks)
    average = total/len(d)
    return average

print(calculate(Marks))




