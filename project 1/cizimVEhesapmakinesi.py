import turtle
t = turtle.Turtle()
shape = input('Ne çizilmesini istersiniz: bir kare, bir üçgen veya bir daire?')
if shape == 'kare':
    t.forward(100); t.left(90);t.forward(100);t.left(90)
    t.forward(100); t.left(90);t.forward(100);t.left(90)
if shape == 'ucgen':
    t.forward(100); t.left(120); t.forward(100)
    t.left(120); t.forward(100); t.left(120)
if shape == 'daire': t.circle(100)
input()

print("Lütfen yapmak istediğiniz işlemi seçin:")
print("1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\n5. Çıkış")
seçim = input("Seçiminiz (1/2/3/4/5): ")

if seçim !='5':
    sayi1 = int(input("Birinci sayıyı girin : "))
    sayi2 = int(input("İkinci sayıyı girin  : "))

if seçim == '1':   print(f"{sayi1} + {sayi2} = {sayi1+sayi2}")
elif seçim == '2': print(f"{sayi1} - {sayi2} = {sayi1-sayi2}")
elif seçim == '3': print(f"{sayi1} x {sayi2} = {sayi1*sayi2}")
elif seçim == '4':
    if sayi2 == 0: print("Bölme işlemi için payda sıfır olamaz.")
    else: print(f"{sayi1} / {sayi2} = {sayi1/sayi2}")
elif seçim == '5': print("Programdan çıkılıyor...")
else: print("Geçersiz seçim, lütfen tekrar deneyin.") 
