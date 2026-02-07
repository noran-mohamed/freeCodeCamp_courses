import re

def verify_card_number(digs: str)->bool:
    # Removing any non-digit characters
    digs = re.sub(r"\D", "", digs)
    summ = 0
    i = 0
    for c in digs[::-1]:
        if i %2:
            temp = int(c) * 2
        else:
            temp = int(c)
        if temp > 9:
            temp -= 9
        summ += temp
        i += 1
    if summ % 10 == 0 :
        return "VALID!"
    else:
        return "INVALID!"
        
print(verify_card_number('1234 5678 9012 3456'))
