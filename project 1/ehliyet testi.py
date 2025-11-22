cevap = input('Yolda önüne üzerinde üç farklı yol yazan bir taş çıkacak. Hangi yöne gitmek istiyorsun: sol, düz ya da sağ?')
if cevap == 'duz': print('Yüzük taşına ulaştın.')
if cevap == 'sol': print('Eşkıyalarla çıktı.')
if cevap == 'sag': print('Süpriz hediye aldın')

cevap = int(input('Kaç yaşındasınız?'))
if cevap >= 18: print("Ehliyet alabilirsiniz!")
else: print("Henüz ehliyet alamazsınız!")

import turtle
cevap = input('Şu anda hangi trafik lambası yanıyor?')
if cevap == 'yesil':
    print('Yoldan karşıya geçebilirsiniz')
    turtle.color('green'); turtle.circle(100)
if cevap == 'sari':
    print('Sakın böyle bir riske girme')
    turtle.color('yellow'); turtle.circle(100)
if cevap == 'kirmizi':
    print('Şu anda karşıya geçemezsin!')
    turtle.color('red'); turtle.circle(100) 