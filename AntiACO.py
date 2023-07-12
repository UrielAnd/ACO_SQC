import pandas as pd
import math
from Excel_file import Excel_file
from ACOs import ACOs

lista = []

file = Excel_file("Teste.xlsx")

Arq = pd.read_excel(file.caminho, sheet_name="Planilha1")
#print(Arq)

for index in range(len(Arq)):
        if math.isnan(Arq["ACO"][index]):
                ...
        else:
                teste =Arq["ACO"][index] 
                #print(teste)
                ACO = ACOs(teste)
                #print(ACO1.num)
                lista.append(ACO)
                #print(lista)


        #Tipo_de_layout = Arq["Tipo de layout"][index]


