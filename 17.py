co=float(input("Digite o cateto oposto: "))
ca=float(input("Digite o cateto adjacente: "))

hi=(ca ** 2 + co ** 2) ** ( 1/2 )

print (" O cateto adijacente é {} e o cateto oposto é {} então a Hipotenusa é {:.2f}".format(ca,co,hi))

ou

#utilisando biblioteca math
import math
co=float(input("Digite o cateto oposto: "))
ca=float(input("Digite o cateto adjacente: "))

hi=math.hypot(co,ca)

print (" O cateto adijacente é {} e o cateto oposto é {} então a Hipotenusa é {:.2f}".format(ca,co,hi))