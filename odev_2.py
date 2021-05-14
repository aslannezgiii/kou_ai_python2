"""
Paylaşılan .txt dosyasındaki verilerin içinden sayıları ve özel karakterleri sildirip
.txt dosyasının temiz halini tekrardan yazdırmanız gerekmekte.
"""
import os
data = open("odev.txt","r",encoding="utf-8")
read_data = data.read()
#print(read_data)
#print(read_data[8])
#print((' '))

#for satir in read_data:
#   print(satir)
new_data = os.open ('new_data.txt',os.O_RDWR|os.O_CREAT)

#[print(chr(i)) for i in range(ord('a'),ord('z')+1)]
alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h','ı','i', 'j', 'k', 'l', 'm', 'n',
 'o','ö','p', 'q', 'r', 's','ş', 't', 'u','ü', 'v', 'w', 'x', 'y', 'z']

for row in read_data:
    if row == '\n': #boşluğa eşitse
        #a=3 #kontrol - if çalışıyor mu diye
        os.write(new_data,"\n".encode())
    else:
        for letter in alphabet:
            if row == letter:
                os.write(new_data, row.encode())

os.close(new_data)

data_new = open("new_data.txt","r",encoding="utf-8")
read_data_new = data_new.read()
print(read_data_new)

#print(a) #if çalışıyor mu kontrolü
