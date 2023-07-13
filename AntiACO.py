import pandas as pd
import math
from Excel_file import Excel_file
from ACOs import ACOs
from datetime import datetime
import os
import base64
from PIL import Image

def Gera_Script(lista):
        Moment = datetime.now().microsecond

        if not os.path.exists("Scripts"):
                os.mkdir("Scripts")
        #Local_Script_ACO = "nome_do_diretorio"

        #caminho_completo = os.path.join(os.getcwd(), nome_diretorio)
        
        for index in range(len(lista)):

                with open(f"imgs/{lista[index].Imagem}", "rb") as Imagem:
                        # Codificar a imagem em Base64
                        Imagem = base64.b64encode(Imagem.read())
                        Imagem64 = Imagem.decode("utf-8")
                Layout_Value = 0
                if lista[index].Tipo_de_layout == "Cartão com imagem à esquerda - Título, subtítulo e CTA à direita":
                        Layout_Value = 319
                elif ...:
                        ...

                lista[index].print()
                
                #print("Teste")
                with open(f"Scripts/Script_{int(lista[index].num)}-{Moment}.txt", "w") as arquivo:
                        arquivo.write("""declare @str varchar(max) = %s
declare @img varbinary(max) = (SELECT cast('' as xml).value('xs:base64Binary(sql:variable( "@str"))', 'varbinary(max)'))
INSERT INTO MENU_ACO_MBK (
NUM_ACA,
IDT_TIP_MNU,
IDT_RCU_ITF,
IDT_FUN,
IDT_PRX_PAS,
CTD_IMG_ACA,
NOM_RCU_APA_MNU)
VALUES (
%d,
7,
%d,
0,
0,
@img,
'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s"},"Navegacao":{"Metodo":"Link","Link":"https://bancomercantil.com.br/Voce/Investimentos/programa-de-indicacao-premiada/Paginas/default.aspx","TituloPopUp":"","CodMensagemAlerta":"https://bancomercantil.com.br/Voce/Investimentos/programa-de-indicacao-premiada/Paginas/default.aspx","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}')""" % (Imagem64, lista[index].num, Layout_Value, lista[index].Titulo, Layout_Value, lista[index].num, lista[index].Cor_Fundo_Inicial, lista[index].Cor_Fundo_Final, lista[index].Titulo_Cor, lista[index].Subtitulo_Cor, lista[index].CTA_Cor, lista[index].CTA_Cor_Fundo, lista[index].CTA_Cor_Borda, lista[index].Subtitulo, lista[index].Texto_CTA))

                arquivo.close()
try:

        lista = []

        file = Excel_file("tests/Teste.xlsx")

        Arq = pd.read_excel(file.caminho, sheet_name="Planilha1")
        Arq. dropna()
        Arq = Arq.rename(columns={"Unnamed: 4": "Titulo cor", "Unnamed: 6": "Subtitulo cor", "Unnamed: 8": "CTA cor", "Unnamed: 10": "Cor fundo inicial",
                                "Unnamed: 11": "Cor fundo Final", "CTA": "CTA Cor do fundo", "CTA.1": "CTA Cor da borda", "Fundo": "Imagem" })
        #print(Arq)

        for index in range(len(Arq)):
                if math.isnan(Arq["ACO"][index]):
                        ...
                else:
                        #teste =Arq["ACO"][index] 
                        #print(teste)
                        ACO = ACOs(Arq["ACO"][index], Arq["Tipo de layout"][index],Arq["Banner"][index], Arq["Titulo"][index], Arq["Titulo cor"][index], Arq["Subtitulo"][index], Arq["Subtitulo cor"][index], Arq["Texto CTA"][index],
                                Arq["CTA cor"][index], Arq["Imagem"][index], Arq["Cor fundo inicial"][index], Arq["Cor fundo Final"][index], Arq["CTA Cor do fundo"][index], Arq["CTA Cor da borda"][index] )
                        #print(ACO.num)
                        lista.append(ACO)
                        #print(lista)
        #lista[0].print()

        Gera_Script(lista)
except Exception as error:
        print(error)


