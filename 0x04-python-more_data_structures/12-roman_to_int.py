def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    table = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    num = 0
    i = 0
    while i < len(roman_string):
        for pair in table:
            temp = 0
            if roman_string[i] == pair[0]:
                temp=pair[1]
            elif i + 1 < len(roman_string):
                if roman_string[i:i+2]==pair[0]:
                    temp = pair[1]
                    i += 1
            num += temp
        i +=1
    return num
