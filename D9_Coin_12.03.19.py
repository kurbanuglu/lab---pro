

#Girilen bir paranın listedeki bozuk paralara göre bolunmesi


def kurus(a):
    bozuk=[100,50,25,10,5,1]
    sonuc=[]
    sonuc2=[]
    n=a
    for i in range(6):
        if(a%bozuk[i]==0):
             while(a>0):
                 a=a-bozuk[i]
                 sonuc.append(bozuk[i])

    while(n!=0):
        for i in range(0,6):
            while(n>=bozuk[i]):
                n=n-bozuk[i]
                sonuc2.append(bozuk[i])

    if(len(sonuc)<len(sonuc2)):
        return sonuc
    else:
        return sonuc2

x=int(input("bir sayı giriniz:"))
print("sonuc:",kurus(x))