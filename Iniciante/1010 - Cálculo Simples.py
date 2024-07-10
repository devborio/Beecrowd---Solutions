# Utilizar o: .split()
umCod, umNum, umVal = input().split()
umCod = int(umCod)
umNum = int(umNum)
umVal = float(umVal)

doisCod, doisNum, doisVal = input().split()
doisCod = int(doisCod)
doisNum = int(doisNum)
doisVal = float(doisVal)

print("VALOR A PAGAR: R$ %.2f" %(umNum * umVal + doisNum * doisVal))