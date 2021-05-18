"""
Paylaşılan .txt dosyasındaki verilerin içinden sayıları ve özel karakterleri sildirip
.txt dosyasının temiz halini tekrardan yazdırmanız gerekmekte.
"""
import os
data = open("odev.txt","r",encoding="utf-8")
read_data = data.read()
new_data = os.open ('new_data.txt',os.O_RDWR|os.O_CREAT)

for row in read_data:
    if row == '\n':
        os.write(new_data,"\n".encode())
    else:
            if row.isalpha():
                os.write(new_data, row.encode())

os.close(new_data)

data_new = open("new_data.txt","r",encoding="utf-8")
read_data_new = data_new.read()
print(read_data_new)
