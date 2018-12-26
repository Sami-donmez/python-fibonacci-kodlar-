def  forfibonacci(sinir):
    sayi1=0
    sayi2=1
    print(sayi1)
    print(sayi2)
    for i in range(sinir-2):
        sayi3=sayi1+sayi2
        print(sayi3)
        sayi1=sayi2
        sayi2=sayi3
def  whilefibonacci(sinir):
    sayi1=0
    sayi2=1
    print(sayi1)
    print(sayi2)
    i=0
    while(i<sinir-2):
        sayi3=sayi1+sayi2
        print(sayi3)
        sayi1=sayi2
        sayi2=sayi3
        i+=1
sinir=int(input("lütfen sayı giriniz"))
print("... for döngüsü için çıktı ....")
forfibonacci(sinir)
print("... while döngüsü için çıktı ....")
whilefibonacci(sinir)
