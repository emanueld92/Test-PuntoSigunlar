a = 0
while a == 0 or a > 1000:
    a = int(input("introuzca un numero entre 1 y 1000 : "))

    unidad = {1: 'I', 2: 'II', 3: 'III', 4: 'IV',
              5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

    decena = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
              5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}

    centena = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC',
               8: 'DCCC', 9: 'CM'}

ro = []
u = a % 10
d = (a//10 % 10)
c = (a//100)

if c == 0:
    ro.append('')
else:
    ro.append(centena.get(c))

if d == 0:
    ro.append('')
else:
    ro.append(decena.get(d))


if u == 0:
    ro.append('')
else:
    ro.append(unidad.get(u))

print(a, 'En romanos = ', ''.join(ro))

