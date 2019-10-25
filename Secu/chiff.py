# moodle sécu

# ex1 : 
text = "JE MANGE DANS UNE SALLE"
text_chiff = []
for car in text:  
    if ord(car) >= 65 and ord(car) + 13 <= 90:
        car = ord(car) + 13        
    elif ord(car) == 32:
        car = ord(car)
    elif ord(car) + 13 > 90:
        car = ord(car) - 12 # +13 -25
    text_chiff.append(chr(int(car)))
text_chiff = ''.join(text_chiff)
print(text_chiff)


# ex2 : 
mess = "fzmxfcjaan(kmdixdkz)"
for i in range (1 , 25):
    mess_clair = []
    for car in mess:
        if ord(car) == 40 or ord(car) == 41:
            car  = ord(car)
        elif ord(car) >= 97 and ord(car) + i <= 122:
            car = ord(car) + i
        elif ord(car) + i > 122:
            car = ord(car) + i - 26
        mess_clair.append(chr(int(car)))
    mess_clair = ''.join(mess_clair)
    print(mess_clair)


# ex3 : 
