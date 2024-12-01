import string
som_text = 'abcd efg, xyz'
numb =3
new_text = ''

for leter in som_text:
    if leter in string.ascii_lowercase:
        leters = string.ascii_lowercase.index(leter)
        print(leters)
        shifted_letter = string.ascii_lowercase[(leters + numb) % 26]
        new_text += shifted_letter
    else:
        new_text += leter
print(new_text)