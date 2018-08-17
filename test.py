#Autor: Raquel Collado Islas
#Fecha:17 Ago. 2018
#

def Primo(x):
   if x<2:
      flag=False
   elif p==2:
      flag=True
   else:
      flag=True
      for n in range (2,x-1):
         if x%n==0:
            flag= False
            break
   return flag

p=input("Numero p: ")
if Primo(p):
   print("Es primo")
else:
   print("No es primo")

