
print ("**** Merhabalar 4 Şıktan Oluşan Genel Kültür Bilgi Yarışmasına ****\n\t\t ...HOŞGELDİNİZ...")

SoruCevap=["Mehmet Akif Ersoy İstiklal Marşının ödülünü hangi kuruma bağışlamıştır?",["A-)Darulfunün","B-)Darulbedai","C-)Daruleytam","D-)Darulmesai"],"D",
           "Hangi Türk filmi Oscar adayı olmamıştır ?",["A-)Tabutta Rövaşata","B-)Sivas ","C-)Mavi Sürgün","D-)Manisa Tarzanı"],"A",
           "Tarihçilerin kutbu olarak bilinen dünyaca ünlü tarihçimiz kimdir ?",["A-)İlber Ortaylı ","B-)Halil İnalcık ","C-)Mehmet Fuat Köprülü","D-)Cemal Kafadar "],"B",
           "Fransız ihtilali hangi yıllar arasında gerçekleşmiştir ?",["A-)1789-1799","B-)1768-1787","C-)1867-1889","D-)1862-1867"],"A",
           "Klasik müziğin en çok bilinen eserlerinden olan 4 konçertodan oluşan Dört Mevsim kimin eseridir ?",["A-)Beethoven","B-)Mozart","C-)Vivaldi","D-)Revaldi"],"A"]
counter=0
for i in range (0,14,3):
    print(SoruCevap[i])
    for k in SoruCevap[i+1]:
        print (k)
    answer = input("Lütfen Cevabınızı giriniz :");
    if(answer.upper()==SoruCevap[i+2]):
        counter+=20

print (counter)