try:
    a = int(input("������� ����� �� 1 �� 999 999: "))
except ValueError:
    a = int(input("������� �����: "))
ed1 = ["����", "���", "���", "������", "����", "�����", "����", "������", "������"]
ed2 = ["����", "���", "���", "������", "����", "�����", "����", "������", "������"]
ch = ["�����������", "����������", "����������", "������������", "����������", "�����������", "����������", "������������", "������������"]
dec = ["������", "��������", "��������", "�����", "���������", "����������", "���������", "�����������", "���������"]
sotn = ["���", "������", "������", "���������", "�������", "��������", "�������", "���������", "���������"]
tys = ["������", "������", "�����"]
rub = ["�����", "�����", "������"]

a1 = a // 100000
a2 = (a // 10000) % 10
a3 = (a // 1000) % 10
a4 = (a // 100) % 10
a5 = (a // 10) % 10
a6 = a % 10

chislo = ""
if a1 != 0:
    i1 = a1 - 1
    chislo += sotn[i1] + " "

if a2 == 1 and a3 == 0:
    chislo += dec[0] + " "

if a2 != 1:
    if a2 != 0:
        i2 = a2 - 1
        chislo += dec[i2] + " "

if a3 != 0:
    if a2 == 1:
        i3 = a3 - 1
        chislo += ch[i3] + " " + tys[2] + " "
    else:
        i3 = a3 - 1
        chislo += ed2[i3] + " "
        if a3 == 1:
            chislo += tys[0] + " "
        elif 1 < a3 < 5:
            chislo += tys[1] + " "
        else:
            chislo += tys[2] + " "

if (a3 == 0) and (a2 or a1 != 0):
    chislo += tys[2] + " "

if a4 != 0:
    i4 = a4 - 1
    chislo += sotn[i4] + " "

if a5 == 1 and a6 == 0:
    chislo += dec[0] + " "

if a5 != 1:
    if a5 != 0:
        i5 = a5 - 1
        chislo += dec[i5] + " "

if a6 != 0:
    if a5 == 1:
        i6 = a6 - 1
        chislo += ch[i6] + " " + rub[2]
    else:
        i6 = a6 - 1
        chislo += ed1[i6] + " "
        if a6 == 1:
            chislo += rub[0] + " "
        elif 1 < a6 < 5:
            chislo += rub[1] + " "
        else:
            chislo += rub[2] + " "

if (a6 == 0) and (a5 or a4 or a3 or a2 or a1 !=0):
    chislo += rub[2]

chislo = chislo.capitalize()
print(chislo)


