import re
a = tuple("aбвгдеёжзийклмнопрстуфхцчшщъыьэюя")
wordChip = []
wordDechip = []
s = 'Здесь должен быть текст'
#s = s.lower()


def redact_str(list_):
    cipher = (str(list_))
    cipher = re.sub(' ', '', cipher)
    cipher = re.sub('\'', '', cipher)
    cipher = re.sub(',', '', cipher)
    cipher = re.sub('\[', '', cipher)
    cipher = re.sub(']', '', cipher)
    cipher = re.sub('_', ' ', cipher)
    return cipher


def cipher(strChip, x):
    strChip = strChip.lower()
    if x > 33:
        x = x % 33
    for i in range(len(strChip)):
        for j in range(33):
            try:
                if strChip[i] == a[j]:
                    z = strChip.replace(strChip[i], a[j+x])
                    wordChip.append(z[i])
            except:
                if s[i] == a[j]:
                    z = strChip.replace(strChip[i], a[j-(33-x)])
                    wordChip.append(z[i])
        if strChip[i] == ' ':
            wordChip.append('_')
    return wordChip


def decipher(strDechip, x):
    if x > 33:
        x = x % 33
    for i in range(len(strDechip)):
        for j in range(33):
            try:
                if strDechip[i] == a[j]:
                    z = strDechip.replace(strDechip[i], a[j-x])
                    wordDechip.append(z[i])
            except:
                if s[i] == a[j]:
                    z = s.replace(strDechip[i], a[j+(33-x)])
                    wordDechip.append(z[i])
        if strDechip[i] == ' ':
            wordDechip.append('_')
    return wordDechip


print(redact_str(cipher(s, 40)))
print(redact_str(decipher('оклшг кхтнлф звщг щлсшщ', 40)))
