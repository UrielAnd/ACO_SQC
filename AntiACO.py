import pandas as pd
import math
from Excel_file import Excel_file
from ACOs import ACOs
from datetime import datetime
import os
import base64
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Variáveis globais para armazenar o caminho do arquivo Excel e da imagem
excel_path = ""
image_paths = []

# Variável global para armazenar o valor de Moment
Moment = None

# Função para gerar o script a partir dos dados da planilha e imagens selecionadas na janela
def gerar_script_gerado(lista, demanda_num, image_paths):
    global Moment

    if not os.path.exists("Scripts"):
        os.mkdir("Scripts")

    demand_folder = os.path.join("Scripts", f"Demanda_{demanda_num}")
    os.makedirs(demand_folder, exist_ok=True)

    divergent_actions = []  # Lista para armazenar ações com nomes de imagens divergentes

    for index in range(len(lista)):
        # Validar se o nome da imagem coincide com o nome na planilha
        if lista[index].Imagem not in [os.path.basename(image_path) for image_path in image_paths]:
            divergent_actions.append(lista[index].num)

        with open(image_paths[index], "rb") as img_file:
            # Ler a imagem em formato binário e converter para base64
            image_data = img_file.read()
            image_base64 = base64.b64encode(image_data).decode("utf-8")

        Layout_Value = 0
        if lista[index].Tipo_de_layout == "Cartão com imagem à esquerda - Título, subtítulo e CTA à direita":
            Layout_Value = 319
        # Adicione outras condições para os diferentes tipos de layout, se necessário

        lista[index].print()

        with open(os.path.join(demand_folder, f"Script_{int(lista[index].num)}-{Moment}-card.txt"), "w") as arquivo:
            script = """declare @str varchar(max) = '%s /n'
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
'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s"},"Navegacao":{"Metodo":"Link","Link":"https://bancomercantil.com.br/Voce/Investimentos/programa-de-indicacao-premiada/Paginas/default.aspx","TituloPopUp":"","CodMensagemAlerta":"https://bancomercantil.com.br/Voce/Investimentos/programa-de-indicacao-premiada/Paginas/default.aspx","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}')""" % (image_base64, lista[index].num, Layout_Value, lista[index].Titulo, Layout_Value, lista[index].num, lista[index].Cor_Fundo_Inicial, lista[index].Cor_Fundo_Final, lista[index].Titulo_Cor, lista[index].Subtitulo_Cor, lista[index].CTA_Cor, lista[index].CTA_Cor_Fundo, lista[index].CTA_Cor_Borda, lista[index].Subtitulo, lista[index].Texto_CTA)

            arquivo.write(script)

    if divergent_actions:
        status_label.config(text=f"Erro: Ações com nomes de imagem divergentes: {', '.join(map(str, divergent_actions))}", fg="red")
        return

    return len(lista)

# Função para gerar o script
def gerar_script():
    global Moment

    if not excel_path:
        status_label.config(text="Erro: Nenhum arquivo Excel selecionado.", fg="red")
        return

    if not image_paths:
        status_label.config(text="Erro: Nenhuma imagem selecionada.", fg="red")
        return

    if not demand_number_entry.get().isdigit():
        status_label.config(text="Erro: Número da demanda inválido.", fg="red")
        return

    try:
        demand_number = int(demand_number_entry.get())

        # Atualizar o valor de Moment com o datetime atual antes de gerar o script
        Moment = datetime.now().microsecond

        # Criar instância da classe Excel_file com o caminho do arquivo Excel
        file = Excel_file(excel_path)

        # Ler a planilha
        Arq = pd.read_excel(file.caminho, sheet_name="Planilha1")
        Arq.dropna()
        Arq = Arq.rename(columns={"Unnamed: 4": "Titulo cor", "Unnamed: 6": "Subtitulo cor", "Unnamed: 8": "CTA cor", "Unnamed: 10": "Cor fundo inicial",
                                "Unnamed: 11": "Cor fundo Final", "CTA": "CTA Cor do fundo", "CTA.1": "CTA Cor da borda", "Fundo": "Imagem" })

        lista = []

        for index in range(len(Arq)):
            if math.isnan(Arq["ACO"][index]):
                continue  # Ignorar o cabeçalho e linhas em branco
            else:
                ACO = ACOs(Arq["ACO"][index], Arq["Tipo de layout"][index], Arq["Banner"][index], Arq["Titulo"][index], Arq["Titulo cor"][index], Arq["Subtitulo"][index], Arq["Subtitulo cor"][index], Arq["Texto CTA"][index],
                            Arq["CTA cor"][index], Arq["Imagem"][index], Arq["Cor fundo inicial"][index], Arq["Cor fundo Final"][index], Arq["CTA Cor do fundo"][index], Arq["CTA Cor da borda"][index])
                lista.append(ACO)

        # Número de ações comerciais encontradas na planilha
        num_acos = gerar_script_gerado(lista, demand_number, image_paths)

        if num_acos == 0:
            status_label.config(text="Nenhuma ação comercial encontrada na planilha.", fg="red")
            return

        if num_acos > len(image_paths):
            status_label.config(text="Erro: O número de imagens é menor que o número de ações comerciais.", fg="red")
            return

        # Associar cada imagem à ação correspondente na planilha
        for i in range(num_acos):
            ACO = lista[i]

            # Encontrar a imagem com o nome correto na lista de imagens selecionadas
            image_name = os.path.basename(ACO.Imagem)
            image_path = next(image_path for image_path in image_paths if image_name == os.path.basename(image_path))

        status_label.config(text=f"{num_acos} script(s) gerado(s) com sucesso.", fg="green")

        # Abrir a pasta da demanda que foi criada
        demand_folder_path = os.path.join("Scripts", f"Demanda_{demand_number}")
        subprocess.Popen(["explorer", demand_folder_path])

    except Exception as error:
        status_label.config(text=f"Erro: {str(error)}", fg="red")

        # Gerar o script com base nos dados da planilha e imagem upados
        script = gerar_script_gerado(lista, demand_number, image_paths)

        # Criar a subpasta com o nome da demanda no diretório "Scripts"
        demand_folder = os.path.join("Scripts", f"Demanda_{demand_number}")
        os.makedirs(demand_folder, exist_ok=True)

        # Caminho do arquivo de script dentro da subpasta da demanda
        script_file_path = os.path.join(demand_folder, f"Script_{demand_number}-{datetime.now().microsecond}-card.txt")

        # Salvar o script no arquivo de texto dentro da subpasta da demanda
        with open(script_file_path, "w") as script_file:
            script_file.write(script)

        # Abrir o arquivo em um programa que interprete .txt
        subprocess.Popen(["notepad.exe", script_file_path])

        status_label.config(text="Script gerado com sucesso.", fg="green")

# Função upload do arquivo Excel
def upload_excel():
    global excel_path
    excel_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    status_label.config(text="Arquivo Excel selecionado.", fg="black")

# Função para fazer o upload de várias imagens
def upload_images():
    global image_paths
    image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_paths:
        status_label.config(text=f"{len(image_paths)} imagem(ns) selecionada(s).", fg="black")
    else:
        status_label.config(text="Nenhuma imagem selecionada.", fg="red")


# Janela principal
root = tk.Tk()
root.title("Anti-ACO")

# Define o ícone da janela
icon_path = "src/ACO.ico"
root.iconbitmap(icon_path)

# Campo de texto para o número da demanda
demand_number_label = tk.Label(root, text="Número da demanda:")
demand_number_label.pack()

demand_number_entry = tk.Entry(root)
demand_number_entry.pack()

# rótulos e botões
file_label = tk.Label(root, text="Selecione a planilha Excel:")
file_label.pack()

file_button = tk.Button(root, text="Escolher arquivo", command=upload_excel)
file_button.pack()

image_label = tk.Label(root, text="Selecione a(s) imagem(ns):")
image_label.pack()

image_button = tk.Button(root, text="Escolher imagem(ns)", command=upload_images)
image_button.pack()

generate_button = tk.Button(root, text="Gerar script(s)", command=gerar_script)
generate_button.pack()

script_label = tk.Label(root, text="Script(s) gerado(os):")
script_label.pack()

script_text = tk.Text(root, width=50, height=10)
script_text.pack()

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

# Inicia o loop principal do Tkinter
root.mainloop()
