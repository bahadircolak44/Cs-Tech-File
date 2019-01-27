import re

def f_komutu(kelime,fileName):
    f = open(fileName,'r')
    # aratilacak kelimede - karakteri var is regex icin . ile degistir. 
    if "-" in kelime:
        kelime = kelime.replace('-','.')
        result = re.findall(kelime,f.read())
        print(len(result),' tane eslesme bulundu.')

    # kelimenin basindaki ve sonunda ki * lar silinip textin icindeki kelimelerde bu substringi içeren olup olmadigini arar.
    elif "*" in kelime:
        kelime = kelime.replace('*','')
        for x in f:
            for word in x.split():
                if kelime in word:
                    print(word)
                    
    #"-" veya "*" icermiyorsa
    else:
        i = 0
        for x in f:
            for word in x.split():
                if kelime == word:
                    i = i + 1
        print (i,' tane eslesme bulundu.')

def r_komutu(word1,word2,fileName):
    f = open(fileName, 'r')
    s = ' '
    for x in f:
        for word in x.split():
            if word == word1:
                word = word2
                s = s+word + ' '
            else:
                s = s + word + ' '

    with open(fileName, "w") as f:
        f.write(s)
try:
    fileName = 'input.txt'
    r_komutu('a', '1', fileName)
except IOError:
    print('Dosya bulunamadi.')
    

