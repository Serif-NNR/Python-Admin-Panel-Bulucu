##
##  LapRooz - Admin Panel Bulucu
##
##  Copyright (C) 2017 - Şerif İnanır
##  e-mail: sheriffnnr[at]gmail.com
##
##  LapRooz is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## LapRooz is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################


#  PROGRAM AÇIKLAMASI
#
#  Elinizde ki admin panel listesini satır satır okur
#  ve her satırı, girdiğiniz URL'nin sonuna ekleyerek
#  bağlantı kurmaya çalışır. Bağlantı sonucunda
#  olumlu cevap dönerse 'Admin Panel Bulundu' ibaresini
#  ekrana basar.
#
#  İllegal işlerde kullanılmaz :)


#-*- coding: utf-8 -*-
import requests
from tkinter import*
from tkinter import filedialog


imza="""
      ########
       #######
        ######    ALKÜ
         #####   ######   ###   ###### ##### ##### ######
         ##############  ## ##  ##  ## ##    ## ## ######
        ############### ####### ###### ##    #####   ######
                                ##           Şerif   İnanır
                                ##
    """


print(imza)

_url_=input("\t# Hedef URL    : ")

def toplam_dork(dosya_uzantısı):
    d=0
    try:
        aç2=open(dosya_uzantısı)
        toplam_satır=aç2.readlines()
        for dork in toplam_satır:
            d+=1
        aç2.close()
        print("[+] Seçilen liste uzunluğu:      ",end="")
        print(d,end="\n\n")
        return d
    except:
        a=".txt dosyaları dene!"
        return a

def site_cevap(url="https://google.com",panel=""):
    durum=requests.get(url+panel)
    geri_dönen_cevap=durum.status_code
    return print(geri_dönen_cevap)

def server_durumu(url):
    oo=requests.get(url)
    oos=oo.status_code
    if oos==200:
        print("Site ile bağlantı kuruldu")
    else:
        print("Sunucuya Bağlanamadı")

def dork_sec():
    dosya=filedialog.askopenfilename()
    dosya_uzantısı=dosya
    dosya_yeri["text"]=dosya_uzantısı
    denenecek_sayısı["text"]=toplam_dork(dosya_uzantısı)

def url_islem():
    try:
        son["text"]=""
        dosya_uzantısı=dosya_yeri["text"]
        aç=open(dosya_uzantısı)
        satir_oku=aç.readlines()
        başarılı="\n\n\tBulunan Admin Panel Linkleri\n"+"="*60+"\n"
        kaç=1
        kaçıncı_=0
        tüm=denenecek_sayısı["text"]
        for dork in satir_oku:
            bağlantı=requests.get(_url_+dork)
            drmm=bağlantı.status_code

            if drmm==200:
                başarılı+="\t[+]  "+_url_+dork
                kaçıncı_+=1
                print("########################################### {}. Admin Panel Bulundu\n({} / {}): BULUNDU: {}###########################################".format(kaçıncı_,kaç,tüm,dork))
                son["text"]+="\n"+dork
            else:
                print("({} / {}): Bulunamadı: {}".format(kaç,tüm,dork),end="")
            kaç += 1
        print(başarılı)

    except:
        print("Panel listesi belirlenmedi yada yanlış belirlendi.")
        son["text"]="Panel Listesi\nSeçilmedi"


try:
    bağ=requests.get(_url_)
    lan=bağ.status_code
    if lan==200:
        print("Bağantı Kuruldu")
        win = Tk()
        win.title("AdminPanel | LapRooz")
        win.geometry("520x490+650+80")
        win.resizable(False, False)





        site_adresi=Label(text="Hedef Site:            "+_url_)
        site_adresi.place(x=15,y=5)

        ayraç2=Label(text="#"*100,fg="red")
        ayraç2.place(x=-5,y=25)

        dork_dosya_yazısı=Label(text="Panel Listesi:")
        dork_dosya_yazısı.place(x=15,y=40)
        dosya_aç=Button(text="Dosya Aç",command=dork_sec,cursor="hand1",fg="red")
        dosya_aç.place(x=5,y=60)
        dosya_yeri=Label(text="Dosya konumu belirlenmedi")
        dosya_yeri.place(x=70,y=63)
        ayraç=Label(text="#"*100,fg="red")
        ayraç.place(x=-5,y=90)

        denenecek=Label(text="Panel Sayısı: ")
        denenecek.place(x=15,y=110)
        denenecek_sayısı=Label(text="Bilinmiyor")
        denenecek_sayısı.place(x=110,y=110)
        ayraç3=Label(text="#"*40,fg="red")
        ayraç3.place(x=-5,y=130)

        bulunan=Label(text="BULUNAN PANELLER:",fg="green")
        bulunan.place(x=370,y=110)

        ay=Label(text="-"*50,fg="green")
        ay.place(x=300,y=125)

        aayy=Label(text="#\n"*23,fg="red")
        aayy.place(x=270,y=105)

        footer=Label(text="#"*100,fg="red")
        footer.place(x=-3,y=450)

        AUTHOUR=Label(text="Şerif İnanır | AlanyaAlaaddinKeykubatÜniversitesi")
        AUTHOUR.place(x=280,y=465)

        başlat=Button(text="Atağı\nBaşlat",width=35,height=7,cursor="hand1",bg="black",fg="red",command=url_islem)
        başlat.place(x=10,y=155)

        son=Label(text="Bulunamadı")
        son.place(x=300,y=140)


        açıklama=Label(text="AÇIKLAMA\n==============================\nSızma testleri için kodlandı.\nSade ve olabildiğince hızlı\nbir program felsefesi ile yazılmıştır.\nHer hangi bir yere zararınız sonucunda\nsorumluluk tamamiyle size aittir.\nSorularınız için e-Posta:\nsheriffnnr@gmail.com")
        açıklama.place(x=15,y=315)
        mainloop()
    else:
        print("Bağlantı Başarısız")
except:
    print("\n   Hata oluştu.")
    print("   Aşağıdaki çözümler işinize yarayabilir:\n\t[+] İnternet bağlantınızı kontrol edin\n\t[+] Bağlantı hızınızı kontrol edin\n\t[+] Örnek kullanım https://google.com")
    input()

