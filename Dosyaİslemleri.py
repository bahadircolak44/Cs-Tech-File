import re

def f_komutu(kelime):
    
    # aratilacak kelimede - karakteri var is regex icin . ile degistir. 
    if "-" in kelime:
        kelime = kelime.replace("-",".")
        result = re.findall(kelime,f.read())
        print(len(result)," tane eslesme bulundu.")
        print (result)
        
    # kelimenin basindaki ve sonunda ki * lar silinip textin icindeki kelimelerde bu substringi içeren olup olmadigini arar.
    elif "*" in kelime:
        kelime = kelime.replace("*","")
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
        print (i," tane eslesme bulundu.")
try:              
    f = open('input.txt','r')
    f_komutu("*lan*")
except IOError:
    print ("Dosya bulunamadi.")
    

