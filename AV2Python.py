TEMPMIN=999999999
TEMPMAX=0
TEMPHOJE=0
for DIA in range(1,8):
 TEMPHOJE = float(input("Digite a temperatura do dia: . . ."))
 print("Dia",DIA)
 if TEMPHOJE > TEMPMAX: #FOR MAIOR
     TEMPMAX = TEMPHOJE
     print("TEMPMAX",TEMPMAX)
 elif TEMPHOJE < TEMPMIN : #FOR MENOR
     TEMPMIN = TEMPHOJE
     print("TEMPMIN",TEMPMIN)
print("A tempratura Maxima do dia é:{:.2f} e a temperatura minima é:{:.2f}".format(TEMPMAX,TEMPMIN))
