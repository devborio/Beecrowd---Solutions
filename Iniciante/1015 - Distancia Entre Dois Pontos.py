pontoUmX, pontoUmY = input().split()
pontoDoisX, pontoDoisY = input().split()

pontoUmX = float(pontoUmX)
pontoUmY = float(pontoUmY)
pontoDoisX = float(pontoDoisX)
pontoDoisY = float(pontoDoisY)

distancia = ((pontoDoisX - pontoUmX)**2 + (pontoDoisY - pontoUmY)**2)**0.5

print("%.4f" %distancia)