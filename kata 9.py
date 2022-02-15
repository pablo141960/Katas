


def informe(tanque1, tanque2, tanque3):
    promedio_total = (tanque1 + tanque2 + tanque3) / 3
    return f"""Fuel Report:
    Total Average: {promedio_total}%
    Main tank: {tanque1}%
    External tank: {tanque2}%
    Hydrogen tank: {tanque3}% 
    """
print(informe(80, 70, 85))



def promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

promedio([80, 85, 81]) 
def informe(tanque1, tanque2, tanque3):
    return f"""Fuel Report:
    Total Average: {promedio([tanque1, tanque2, tanque3])}%
    Main tank: {tanque1}%
    External tank: {tanque2}%
    Hydrogen tank: {tanque3}% 
    """
print(informe(88, 76, 70))









