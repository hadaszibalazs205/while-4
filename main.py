'''
4. Feladat
Írj egy programot while ciklussal, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
'''
mit = input("Mit írjon ki a képernyőre? ")
hanyszor = int(input("Hányszor írja ki a képernyőre? "))

while hanyszor > 0:
  print(mit)
  hanyszor -= 1