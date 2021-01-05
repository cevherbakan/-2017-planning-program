#!/usr/bin/env python
global sToplam
global oToplam
global aToplam
global yapayMatris
global dizi

dosya=open("D:/sabah.txt","w")
dosya.close()
dosya=open("D:/ogle.txt","w")
dosya.close()
dosya=open("D:/aksam.txt","w")
dosya.close()
dosya=open("D:/notime.txt","w")
dosya.close()


print("HOÞ GELDÝNÝZ")

kontrol=raw_input("Planlarý görmek için 0 a basýn")
while(kontrol != "0"):

    name=raw_input("Plan Adi girin:")
    minute=raw_input("Plan Yaklaþýk Süresi:")
    puan=raw_input("0-100 arasýnda Önem Derecesi giriniz(#Küçük olan daha deðerli#)")
    time=raw_input("Vakit giriniz (Sabah=1, Ogle=2,Aksam=3, Zamansýz=0): ")
    
    if(name != '' or minute != '') or (puan != '' or time != ''):
        yaz=open("D:/planlama2.txt","a")
        yaz.write("\n")
        yaz.write(name+"-")
        yaz.write(minute+"-")
        yaz.write(puan+"-")
        yaz.write(time+"-")
        yaz.close()

        dosya=open("D:/planlama2.txt","r")
        dizi=dosya.readlines()
        for i in range(len(dizi)):
            sutun=dizi[i].split('-')
            for j in range(2):
                print sutun[j],
                if j==1:
                    print "dakika"
            print "__________________________"
        print "\n"
                    
                
    kontrol=raw_input("Planlarý görmek için 0 a basýn")




dosya=open("D:/planlama2.txt","r")
dizi=dosya.readlines()
sutun=dizi[1].split('-')

yapayMatris=[[0 for j in range(5)] for i in range(len(dizi)-1)]

for k in range(len(dizi)-1):
    
    for l in range(5):
        
        yenidizi=dizi[k+1].split('-')
        yapayMatris[k][l]=yenidizi[l]
        
    yapayMatris[k][4]=int(yapayMatris[k][1])*int(yapayMatris[k][2])

sToplam=0
oToplam=0
aToplam=0



def dosyaOku():
    global sabah
    global ogle
    global aksam
    dosya=open("D:/planlama.txt","r")
    dizi=dosya.readlines()
    vakitler=dizi[0].split('=')

    
    vakit1=vakitler[1].split(' ')
    vakit2=vakitler[2].split(' ')
    vakit3=vakitler[3].split(' ')

    sabah=vakit1[0]
    ogle=vakit2[0]
    aksam=vakit3[0]

    if int(sabah)+int(ogle)+int(aksam)>720:
        print "Zaman cok yuksek !!!! ********"
        return False

    

def vakitKontrol():
    global sToplam
    global oToplam
    global aToplam
    global yapayMatris

    
    for i in range(len(yapayMatris)):
    
        if yapayMatris[i][3]=='1': 
            sToplam=sToplam+int(yapayMatris[i][1])

        elif yapayMatris[i][3]=='2':        
            oToplam=oToplam+int(yapayMatris[i][1])


        elif yapayMatris[i][3]=='3':      
            aToplam=aToplam+int(yapayMatris[i][1])

        else:
            pass

        if(sToplam > int(sabah)):
            print "sabah için sýnýr aþýldý"
            return False

        if(oToplam > int(ogle)):
            print "ogle için sýnýr aþýldý"
            return False

        if(aToplam > int(aksam)):
            print "aksam için sýnýr aþýldý"
            return False
                            
                                
def sirala():
    global sabah
    global sToplam
    global ogle
    global oToplam
    global aksam
    global aToplam


    for i in range(1,len(dizi)):
        satir=dizi[i].split('-')
        if satir[3]=='0':

            sure=int(sabah)-int(sToplam)
            sure2=int(ogle)-int(oToplam)
            sure3=int(aksam)-int(aToplam)
            zaman=int(satir[1])

            
            if (sure>int(satir[1]))and((zaman+sToplam)<int(sabah)):
                sToplam=sToplam+int(satir[1])
                
                dosya=open("D:/sabah.txt","a")
                dosya.write(str(dizi[i]))
                dosya.close

            
            
            elif (sure2> int(satir[1]))and ((zaman+oToplam)<int(ogle)):
                oToplam=oToplam+int(satir[1])
                
                dosya=open("D:/ogle.txt","a")
                dosya.write(str(dizi[i]))
                dosya.close



            
            elif sure3>int(satir[1])and((zaman+aToplam)<int(aksam)):
                
                aToplam=aToplam+int(satir[1])
                
                dosya=open("D:/aksam.txt","a")
                dosya.write(str(dizi[i]))
                dosya.close
                
            else:
                print "zamanlama yerleþtirilemedi"
                return False
    




    
    sayac=0
    for i in range(0,len(dizi)-1):
        sayac=sayac+1
        if yapayMatris[i][3]=='1':
            
            dosya=open("D:/sabah.txt","a")
            yazi=dizi[sayac]
            dosya.write(str(yazi))
            dosya.close

    dosya=open("D:/sabah.txt","r")
    dizi2=dosya.readlines()

    
    sMatris=[[0 for j in range(5)] for i in range(len(dizi2))]

    for i in range(len(dizi2)):
        sutun=dizi2[i].split("-")
        for j in range(5):
            if j==4:
                sMatris[i][4]=int(sMatris[i][1])*int(sMatris[i][2])
            else:
                sMatris[i][j]=sutun[j]




    
    sayac=0
    for i in range(0,len(dizi)-1):
        sayac=sayac+1
        if yapayMatris[i][3]=='2':
            
            dosya=open("D:/ogle.txt","a")
            yazi=dizi[sayac]
            dosya.write(str(yazi))
            dosya.close

    dosya=open("D:/ogle.txt","r")
    dizi3=dosya.readlines()


    
    oMatris=[[0 for j in range(5)] for i in range(len(dizi3))]

    for i in range(len(dizi3)):
        sutun2=dizi3[i].split("-")
        for j in range(5):
            if j==4:
                oMatris[i][4]=int(oMatris[i][1])*int(oMatris[i][2])
            else:
                oMatris[i][j]=sutun2[j]
    





            
    sayac=0
    for i in range(0,len(dizi)-1):
        sayac=sayac+1
        if yapayMatris[i][3]=='3':
            
            dosya=open("D:/aksam.txt","a")
            yazi=dizi[sayac]
            dosya.write(str(yazi))
            dosya.close

        
    dosya=open("D:/aksam.txt","r")
    dizi4=dosya.readlines()

    aMatris=[[0 for j in range(5)] for i in range(len(dizi4))]

    for i in range(len(dizi4)):
        sutun3=dizi4[i].split("-")
        for j in range(5):
            if j==4:
                aMatris[i][4]=int(aMatris[i][1])*int(aMatris[i][2])
            else:
                aMatris[i][j]=sutun3[j]




        
    sayac=0
    for i in range(0,len(dizi)-1):
        sayac=sayac+1
        if yapayMatris[i][3]=='0':
            
            dosya=open("D:/notime.txt","a")
            yazi=dizi[sayac]
            dosya.write(str(yazi))
            dosya.close
    

    dosya=open("D:/notime.txt","r")
    dizi4=dosya.readlines()
    
    nMatris=[[0 for j in range(5)] for i in range(len(dizi4))]

    for i in range(len(dizi4)):
        sutun4=dizi4[i].split("-")
        for j in range(5):
            if j==4:
                nMatris[i][4]=int(nMatris[i][1])*int(nMatris[i][2])
            else:
                nMatris[i][j]=sutun4[j]
    



    for j in range(len(sMatris)-1):
        for i in range(1,len(sMatris)):
            if(sMatris[i][4]<sMatris[i-1][4]):

                degis=sMatris[i-1]
                sMatris[i-1]=sMatris[i]
                sMatris[i]=degis
                

    for j in range(len(oMatris)-1):
        for i in range(1,len(oMatris)):
            if(oMatris[i][4]<oMatris[i-1][4]):
                
                degis=oMatris[i-1]
                oMatris[i-1]=oMatris[i]
                oMatris[i]=degis


    for j in range(len(aMatris)-1):
        for i in range(1,len(aMatris)):
            if(aMatris[i][4]<aMatris[i-1][4]):
                
                degis=aMatris[i-1]
                aMatris[i-1]=aMatris[i]
                aMatris[i]=degis

    for j in range(len(nMatris)-1):
        for i in range(1,len(nMatris)):
            if(nMatris[i][4]<nMatris[i-1][4]):
                
                degis=nMatris[i-1]
                nMatris[i-1]=nMatris[i]
                nMatris[i]=degis

              
                



    print "______________________SABAH____________________________"
    for i in range(len(sMatris)):
        for j in range(2):
            print sMatris[i][j],
            if j==1:
                print "dakika"
        print "----------------------------------"
    print "\n"
        

    print "_____________________OGLE______________________________"
    
    for i in range(len(oMatris)):
        for j in range(2):
            print oMatris[i][j],
            if j==1:
                print "dakika"
        print "----------------------------------"
    print "\n"

    print "______________________AKSAM____________________________"
    for i in range(len(aMatris)):
        for j in range(2):
            print aMatris[i][j],
            if j==1:
                print "dakika"
        print "----------------------------------"
    print "\n"

    print "__________________________________________________________"




input()
if dosyaOku()==False:
    print "kesildi"
else:
    if vakitKontrol()==False:
        print "Vakit kontrol kesildi"
    
    else:
        sirala()
