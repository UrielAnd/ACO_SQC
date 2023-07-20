from tkinter import filedialog, messagebox, StringVar
import pandas as pd
from Excel_file import Excel_file
from ACOs import ACOs
import os
import base64
import customtkinter
import subprocess


# Variáveis globais para armazenar o caminho do arquivo Excel e da imagem
excel_path = ""
image_paths = []

# Variável global para armazenar a mensagem de status
status_message = None


# Função para gerar o script a partir dos dados da planilha e das imagens selecionadas na janela
def gerar_script_gerado(lista, demanda_num, image_paths, Tamnaho_Coll):
    global status_message

    if not os.path.exists("Scripts"):
        os.mkdir("Scripts")

    demand_folder = os.path.join("Scripts", f"Demanda_{demanda_num}")
    os.makedirs(demand_folder, exist_ok=True)

    divergent_actions = []  # Lista para armazenar ações com nomes de imagens divergentes
    updated_actions = []  # Lista para armazenar ações que foram atualizadas

    # Verificar quais ações já existem na pasta e adicioná-las a uma lista
    existing_actions = []
    for file in os.listdir(demand_folder):
        if file.startswith("Script_") and file.endswith("-card.txt"):
            action_number = file.split("-")[0].split("_")[1]
            existing_actions.append(int(action_number))

    for index in range(len(lista)):
        # Validar se o nome da imagem coincide com o nome na planilha
        if lista[index].Imagem not in [os.path.basename(image_path) for image_path in image_paths]:
            divergent_actions.append(int(lista[index].num))

        if not image_paths:  # Se a lista de imagens está vazia, atribuir a mesma imagem para todas as ações
            image_path = ""  # Caminho vazio
        else:
            # Encontrar a imagem com o nome correto na lista de imagens selecionadas
            image_name = os.path.basename(lista[index].Imagem)
            image_path = next((image_path for image_path in image_paths if image_name == os.path.basename(image_path)), "")

        with open(image_path, "rb") as img_file:
            # Ler a imagem em formato binário e converter para base64
            image_data = img_file.read()
            image_base64 = base64.b64encode(image_data).decode("utf-8")

        lista[index].defini_banner()
        lista[index].print()

        script_file_name = f"Script_{int(lista[index].num)}-card.txt"
        script_file_path = os.path.join(demand_folder, script_file_name)

        # Verificar se o arquivo de script já existe
        if os.path.exists(script_file_path):
            updated_actions.append(int(lista[index].num))

        if Tamnaho_Coll == 14:
            with open(script_file_path, "w") as arquivo:
                script = """declare @str varchar(max) = '%s'
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
'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s"},"Navegacao":{"Metodo":"%s","Link":"%s","TituloPopUp":"","CodMensagemAlerta":"%s","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}')""" % (
                image_base64, lista[index].num, lista[index].Banner, lista[index].Titulo, lista[index].Banner,
                lista[index].num, lista[index].Cor_Fundo_Inicial, lista[index].Cor_Fundo_Final, lista[index].Titulo_Cor,
                lista[index].Subtitulo_Cor, lista[index].CTA_Cor, lista[index].CTA_Cor_Fundo, lista[index].CTA_Cor_Borda,
                lista[index].Subtitulo, lista[index].Texto_CTA, lista[index].Método_Red, lista[index].Link, lista[index].Código_Red)
                arquivo.write(script)

        elif Tamnaho_Coll == 15:
            with open(script_file_path, "w") as arquivo:
                script = """declare @str varchar(max) = '%s'
declare @img varbinary(max) = (SELECT cast('' as xml).value('xs:base64Binary(sql:variable( "@str"))', 'varbinary(max)'))
INSERT INTO INFORMAC_POPUP_ACO (
NUM_ACA,
IDT_TIP_MNU,
IDT_RCU_ITF,
IDT_FUN,
IDT_PRX_PAS,
CTD_IMG_ACA,
DTA_GRV_REG,
NOM_RCU_ACA_CMC )
 VALUES (
%d, 
7, 
%d, 
0, 
0, 
@img, 
getdate(),
'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png","CorTexto":"%s"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s","TamanhoTitulo":%s,"TamanhoSubtitulo":"%s"},"Navegacao":{"Metodo":"%s","Link":"%s","TituloPopUp":"","CodMensagemAlerta":"%s","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}')""" % (
                image_base64, lista[index].num, lista[index].Banner, lista[index].Titulo, lista[index].Banner, lista[index].num, 
                lista[index].Cor_botao_fechar, lista[index].Cor_Fundo_Inicial, lista[index].Cor_Fundo_Inicial, lista[index].Titulo_Cor, lista[index].Subtitulo_Cor,
                lista[index].CTA_Cor, lista[index].CTA_Cor_Borda, lista[index].CTA_Cor_Borda, lista[index].Subtitulo, lista[index].Texto_CTA,
                lista[index].Tamanho_Titulo, lista[index].Tamanho_Subtitulo, lista[index].Método_Red, lista[index].Link, lista[index].Código_Red)

                arquivo.write(script)

    if divergent_actions:
        divergent_actions = [int(action) for action in divergent_actions]
        status_message.set(f"Erro: Ações com nomes de imagens divergentes: {', '.join(map(str, divergent_actions))}")
        return

    status_message.set(f"{len(lista)} script(s) gerado(s) com sucesso.")

    return len(lista)


# Função para gerar o script
def gerar_script():
    global excel_path, image_paths, status_message

    if not excel_path:
        status_message.set("Erro: Nenhum arquivo Excel selecionado.")
        return

    if not image_paths:
        status_message.set("Erro: Nenhuma imagem selecionada.")
        return

    if not demand_number_entry.get().isdigit():
        status_message.set("Erro: Número da demanda inválido ou vazio.")
        return

    try:
        demand_number = int(demand_number_entry.get())

        # Criar instância da classe Excel_file com o caminho do arquivo Excel
        file = Excel_file(excel_path)
        lista = []

        # Ler a planilha
        Arq = pd.read_excel(file.caminho)
        Arq = Arq.drop(0, axis=0)
        Arq.reset_index(drop=True, inplace=True)
        Arq.fillna('', inplace=True)
        #print(Arq.shape[1])
        Tamnaho_Coll = Arq.shape[1]
        if Tamnaho_Coll == 14:
            Arq = Arq.rename(columns={"Unnamed: 3": "Titulo cor", "Unnamed: 5": "Subtitulo cor", "Unnamed: 7": "CTA cor",
                                    "Unnamed: 9": "Cor fundo inicial",
                                    "Unnamed: 10": "Cor fundo Final", "CTA": "CTA Cor do fundo",
                                    "CTA.1": "CTA Cor da borda", "Fundo": "Imagem", "Redirecionamento externo": "Link" })
            for index in range(len(Arq)):
                if pd.isna(Arq["ACO"][index]):
                    continue  # Ignorar o cabeçalho e linhas em branco
                else:
                    ACO = ACOs(Arq["ACO"][index], Arq["Tipo de Layout"][index], Arq["Titulo"][index],
                            Arq["Titulo cor"][index], Arq["Subtitulo"][index], Arq["Subtitulo cor"][index],
                            Arq["Texto CTA"][index],
                            Arq["CTA cor"][index], Arq["Imagem"][index], Arq["Cor fundo inicial"][index],
                            Arq["Cor fundo Final"][index], Arq["CTA Cor do fundo"][index],
                            Arq["CTA Cor da borda"][index], Arq["Link"][index], None, None, None)
                    lista.append(ACO)

        elif Tamnaho_Coll == 15:
            Arq = Arq.rename(columns={"Unnamed: 3": "Titulo tamanho", "Unnamed: 4": "Titulo cor", "Unnamed: 6": "Subtitulo tamanho",
                          "Unnamed: 7": "Subtitulo cor",
                          "Unnamed: 9": "CTA cor", "Unnamed: 11": "Cor fundo",
                          "Fundo": "Imagem", "Redirecionamento externo": "Link"})
            for index in range(len(Arq)):
                if pd.isna(Arq["ACO"][index]):
                    continue  # Ignorar o cabeçalho e linhas em branco
                else:
                    ACO = ACOs(Arq["ACO"][index], Arq["Tipo de Layout"][index], Arq["Titulo"][index],
                            Arq["Titulo cor"][index], Arq["Subtitulo"][index], Arq["Subtitulo cor"][index],
                            Arq["Texto CTA"][index],
                            Arq["CTA cor"][index], Arq["Imagem"][index], Arq["Cor fundo"][index],
                            None, Arq["Fundo CTA"][index],
                            None, Arq["Link"][index], Arq["Titulo tamanho"][index],
                            Arq["Subtitulo tamanho"][index], Arq["Botão fechar"][index])
                    lista.append(ACO)
            

        print(Arq)

        # Verificar se há nomes de imagem divergentes
        divergent_actions = []
        for index in range(len(lista)):
            if lista[index].Imagem not in [os.path.basename(image_path) for image_path in image_paths]:
                divergent_actions.append(int(lista[index].num))

        if divergent_actions:
            divergent_actions = [int(action) for action in divergent_actions]
            status_message.set(f"Erro: Ações com nomes de imagens divergentes: {', '.join(map(str, divergent_actions))}")
            return

        # Número de ações comerciais encontradas na planilha
        num_acos = gerar_script_gerado(lista, demand_number, image_paths, Tamnaho_Coll)

        if num_acos == 0:
            status_message.set("Nenhuma ação comercial encontrada na planilha.")
            return

        #if num_acos > len(image_paths):
            #status_message.set("Erro: O número de imagens é menor que o número de ações comerciais.")
            #return

        # Associar cada imagem à ação correspondente na planilha
        for i in range(num_acos):
            ACO = lista[i]

            # Encontrar a imagem com o nome correto na lista de imagens selecionadas
            image_name = os.path.basename(ACO.Imagem)
            image_path = next(image_path for image_path in image_paths if image_name == os.path.basename(image_path))

        status_message.set(f"{num_acos} script(s) gerado(s) com sucesso.")

        # Abrir a pasta da demanda que foi criada
        demand_folder_path = os.path.join("Scripts", f"Demanda_{demand_number}")
        subprocess.Popen(["explorer", demand_folder_path])

    except Exception as error:
        status_message.set(f"Erro: {str(error)}")
        #traceback.print_exc()

# Função upload do arquivo Excel
def upload_excel():
    global excel_path, status_message

    excel_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    status_message.set("Arquivo Excel selecionado.")


# Função para fazer o upload de várias imagens
def upload_images():
    global image_paths, status_message

    image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if image_paths:
        status_message.set(f"{len(image_paths)} imagem(ns) selecionada(s).")
    else:
        status_message.set("Nenhuma imagem selecionada.")


# Janela principal
janela = customtkinter.CTk()
janela.geometry("400x350")
janela.title("ACO_SQC")

# Define o ícone da janela
icon_path = "src/ACO.ico"
janela.iconbitmap(icon_path)

# Cria a variável para armazenar a mensagem de status
status_message = StringVar()

# Campo de texto para o número da demanda
demand_number_label = customtkinter.CTkLabel(janela, text="Número da demanda:")
demand_number_label.pack(padx=10, pady=10)

demand_number_entry = customtkinter.CTkEntry(janela)
demand_number_entry.pack()

# Rótulos e botões
file_label = customtkinter.CTkLabel(janela, text="Selecione a planilha Excel:")
file_label.pack(padx=10, pady=10)

file_button = customtkinter.CTkButton(janela, text="Escolher arquivo", command=upload_excel)
file_button.pack()

image_label = customtkinter.CTkLabel(janela, text="Selecione a(s) imagem(ns):")
image_label.pack(padx=10, pady=10)

image_button = customtkinter.CTkButton(janela, text="Escolher imagem(ns)", command=upload_images)
image_button.pack()

generate_button = customtkinter.CTkButton(janela, text="Gerar script(s)", command=gerar_script)
generate_button.pack(padx=10, pady=10)

status_label = customtkinter.CTkLabel(janela, textvariable=status_message)
status_label.pack()

# Inicia o loop principal do Tkinter
janela.mainloop()