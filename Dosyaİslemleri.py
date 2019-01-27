import re
import os


def f_komutu(text, f):
    i = 0
    # aratilacak kelimede - karakteri var is regex icin . ile degistir.
    if "-" in text:
        text = text.replace('-', '.')
        for x in f:
            for word in x.split():
                if re.fullmatch(text, word):
                    i = i + 1
                    print(word)
        print(i, ' tane eslesme bulundu.')

    # kelimenin basindaki ve sonunda ki * lar silinip textin icindeki kelimelerde bu substringi içeren olup olmadigini arar.
    elif "*" in text:
        text = text.replace('*', '[a-zA-Z]+')
        for x in f:
            for word in x.split():
                if re.fullmatch(text, word):
                    i = i + 1
                    print(word)

    # "-" veya "*" icermiyorsa
    else:
        i = 0
        for x in f:
            for word in x.split():
                if text == word:
                    i = i + 1
        print(i, ' tane eslesme bulundu.')


# text1 parametresi ile gelen kelime metin icinde bulunursa text2 parametresi ile degistirilip s ye append edilir ve toplu olarak geri yazilir.
def r_komutu(text1, text2, f, fileName):
    s = ' '
    for x in f:
        for word in x.split():
            if word == text1:
                word = text2
                s = s + word + ' '
            else:
                s = s + word + ' '

    with open(fileName, "w") as f:
        f.write(s)


# Eger silinmek istenen tam kelime bulunamazsa, o kelimeyi s ye append eder. Bulursa s icine dahil etmeden continue eder.
def d_komutu(text, f):
    s = ' '
    for x in f:
        for word in x.split():
            if word == text:
                continue
            else:
                s = s + word + ' '

    with open(fileName, "w") as f:
        f.write(s)


while (True):
    fileName = input("Lutfen dosya yolunu giriniz: ")
    try:
        f = open(fileName, 'r')
    except IOError:
        print("Dosya okunurken bir hata olustu.")
        continue
    except ValueError:
        print("Dosya okunurken bir hata olustu.")
        continue
    komut = str(input("Lutfen komut giriniz: "))
    command = komut.split()[0]

    if command.upper() == 'F':
        try:
            f_komutu(komut.split()[1], f)
        except IndexError:
            print("Eksik parametre girildi")

    elif command.upper() == 'R':
        try:
            r_komutu(komut.split()[1], input.split()[2], f, fileName)
        except IndexError:
            print("Eksik parametre girildi")

    elif command.upper() == 'D':
        try:
            d_komutu(komut.split()[1], f)
        except IndexError:
            print("Eksik parametre girildi")

    else:
        print('Girdiginiz komut bulunamamaktadir! Lutfen tekrar giriniz.')




