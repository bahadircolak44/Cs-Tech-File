import re

def f_komutu(text,fileName):
    f = open(fileName,'r')
    i = 0
    # aratilacak kelimede - karakteri var is regex icin . ile degistir. 
    if "-" in text:
        text = text.replace('-','.')
        for x in f:
            for word in x.split():
                if re.fullmatch(text,word):
                    i = i+1
                    print(word)
        print(i,' tane eslesme bulundu.')

    # kelimenin basindaki ve sonunda ki * lar silinip textin icindeki kelimelerde bu substringi içeren olup olmadigini arar.
    elif "*" in text:
        text = text.replace('*','[a-zA-Z]+')
        for x in f:
            for word in x.split():
                if re.fullmatch(text, word):
                    i = i + 1
                    print(word)

    #"-" veya "*" icermiyorsa
    else:
        i = 0
        for x in f:
            for word in x.split():
                if text == word:
                    i = i + 1
        print (i,' tane eslesme bulundu.')

def r_komutu(text1,text2,fileName):
    f = open(fileName, 'r')
    s = ' '
    for x in f:
        for word in x.split():
            if word == text1:
                word = text2
                s = s+word + ' '
            else:
                s = s + word + ' '

    with open(fileName, "w") as f:
        f.write(s)
def d_komutu(text,fileName):
    try:
        f = open(fileName, 'r')
        s = ' '
        for x in f:
            for word in x.split():
                if word == text:
                    continue
                else:
                    s = s + word + ' '

        with open(fileName, "w") as f:
            f.write(s)

    except IOError:
        print('Dosya bulunamadi.')

fileName = 'input.txt'
f_komutu('*an',fileName)
#r_komutu('a', '1', fileName)
#d_komutu('ilk',fileName)

    

