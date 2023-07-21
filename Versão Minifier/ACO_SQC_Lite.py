X=str
L=open
O=True
N='Scripts'
K=range
J=None
G=len
F=int
from tkinter import filedialog as H,StringVar as M
import pandas as V
from ACOs import A as a
import os as D,base64 as Y,customtkinter as B,subprocess as s,shutil as R
I=''
E=[]
C=J
def t(lista,demanda_num,image_paths,Tamnaho_Coll):
	S=Tamnaho_Coll;J=image_paths;A=lista;global C
	if not D.path.exists(N):D.mkdir(N)
	E=D.path.join(N,f"Demanda_{demanda_num}");D.makedirs(E,exist_ok=O);R.copy(I,E)
	for B in J:R.copy(B,E)
	H=[];e=[];W=[]
	for M in D.listdir(E):
		if M.startswith('Script_')and M.endswith('-card.txt'):Z=M.split('-')[0].split('_')[1];W.append(F(Z))
	for B in K(G(A)):
		if A[B].Imagem not in[D.path.basename(A)for A in J]:H.append(F(A[B].num))
		if not J:T=''
		else:a=D.path.basename(A[B].Imagem);T=next((A for A in J if a==D.path.basename(A)),'')
		with L(T,'rb')as b:c=b.read();U=Y.b64encode(c).decode('utf-8')
		A[B].defini_banner();d=f"Script_{F(A[B].num)}-card.txt";V=D.path.join(E,d)
		if S==14:
			with L(V,'w')as P:Q='declare @str varchar(max) = \'%s\'\ndeclare @img varbinary(max) = (SELECT cast(\'\' as xml).value(\'xs:base64Binary(sql:variable( "@str"))\', \'varbinary(max)\'))\nINSERT INTO MENU_ACO_MBK (\nNUM_ACA,\nIDT_TIP_MNU,\nIDT_RCU_ITF,\nIDT_FUN,\nIDT_PRX_PAS,\nCTD_IMG_ACA,\nNOM_RCU_APA_MNU)\nVALUES (\n%d, \n7, \n%d, \n0, \n0, \n@img, \n\'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s"},"Navegacao":{"Metodo":"%s","Link":"%s","TituloPopUp":"","CodMensagemAlerta":"%s","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}\')'%(U,A[B].num,A[B].Banner,A[B].Titulo,A[B].Banner,A[B].num,A[B].Cor_Fundo_Inicial,A[B].Cor_Fundo_Final,A[B].Titulo_Cor,A[B].Subtitulo_Cor,A[B].CTA_Cor,A[B].CTA_Cor_Fundo,A[B].CTA_Cor_Borda,A[B].Subtitulo,A[B].Texto_CTA,A[B].Método_Red,A[B].Link,A[B].Código_Red);P.write(Q)
		elif S==15:
			with L(V,'w')as P:Q='declare @str varchar(max) = \'%s\'\ndeclare @img varbinary(max) = (SELECT cast(\'\' as xml).value(\'xs:base64Binary(sql:variable( "@str"))\', \'varbinary(max)\'))\nINSERT INTO INFORMAC_POPUP_ACO (\nNUM_ACA,\nIDT_TIP_MNU,\nIDT_RCU_ITF,\nIDT_FUN,\nIDT_PRX_PAS,\nCTD_IMG_ACA,\nDTA_GRV_REG,\nNOM_RCU_ACA_CMC )\n VALUES (\n%d, \n7, \n%d, \n0, \n0, \n@img, \ngetdate(),\n\'{"Titulo":"%s","Valor":{"ItemCard":{"IdTipoRecurso":%d,"ProximoPasso":0,"IdentificadorAcao":%d,"NumeroSequencialPessoa":0,"CodigoProduto":0,"IdentificadorMensagem":"","BotaoLimpar":{"Texto":"Apagar","Icone":"aco_close_icon.png","CorTexto":"%s"},"ImagemFundo":{"Imagem":null,"CorInicio":"%s","CorFim":"%s","CorTitulo":"%s","CorSubTitulo":"%s","CorTextoCta":"%s","CorFundoCta":"%s","CorBordaCta":"%s"},"Complemento":{"Icone":"","SubTitulo":"%s","TextoCta":"%s","TamanhoTitulo":%d,"TamanhoSubtitulo":%d},"Navegacao":{"Metodo":"%s","Link":"%s","TituloPopUp":"","CodMensagemAlerta":"%s","MensagemAlerta":"","Payload":{"IdtCat":0,"CodPdt":0,"NumDnd":0,"NumCta":0,"NumPes":0,"ExibirAlertaErro":true}}}},"Visivel":true}\')'%(U,A[B].num,A[B].Banner,A[B].Titulo,A[B].Banner,A[B].num,A[B].Cor_Botao_Fechar,A[B].Cor_Fundo_Inicial,A[B].Cor_Fundo_Inicial,A[B].Titulo_Cor,A[B].Subtitulo_Cor,A[B].CTA_Cor,A[B].CTA_Cor_Borda,A[B].CTA_Cor_Borda,A[B].Subtitulo,A[B].Texto_CTA,A[B].Tamanho_Titulo,A[B].Tamanho_Subtitulo,A[B].Método_Red,A[B].Link,A[B].Código_Red);P.write(Q)
	if H:H=[F(A)for A in H];C.set(f"Erro: Ações com nomes de imagens divergentes: {', '.join(map(X,H))}");return
	C.set(f"{G(A)} script(s) gerado(s) com sucesso.");return G(A)
def P():
	r='Cor fundo';q='Subtitulo tamanho';p='Titulo tamanho';o='Texto CTA';n='Subtitulo';m='Titulo';l='Tipo de Layout';k='CTA Cor da borda';j='CTA Cor do fundo';i='Cor fundo Final';h='Cor fundo inicial';g='Redirecionamento externo';f='Fundo';e='Unnamed: 9';d='Unnamed: 7';c='Unnamed: 3';U='ACO';T='Link';S='Imagem';R='CTA cor';Q='Subtitulo cor';P='Titulo cor';global I,E,C
	if not I:C.set('Erro: Nenhum arquivo Excel selecionado.');return
	if not E:C.set('Erro: Nenhuma imagem selecionada.');return
	if not W.get().isdigit():C.set('Erro: Número da demanda inválido ou vazio.');return
	try:
		b=F(W.get());u=I;H=[];A=V.read_excel(u);A=A.drop(0,axis=0);A.reset_index(drop=O,inplace=O);A.fillna('',inplace=O);Y=A.shape[1]
		if Y==14:
			A=A.rename(columns={c:P,'Unnamed: 5':Q,d:R,e:h,'Unnamed: 10':i,'CTA':j,'CTA.1':k,f:S,g:T})
			for B in K(G(A)):
				if V.isna(A[U][B]):continue
				else:L=a(A[U][B],A[l][B],A[m][B],A[P][B],A[n][B],A[Q][B],A[o][B],A[R][B],A[S][B],A[h][B],A[i][B],A[j][B],A[k][B],A[T][B],J,J,J);H.append(L)
		elif Y==15:
			A=A.rename(columns={c:p,'Unnamed: 4':P,'Unnamed: 6':q,d:Q,e:R,'Unnamed: 11':r,f:S,g:T})
			for B in K(G(A)):
				if V.isna(A[U][B]):continue
				else:L=a(A[U][B],A[l][B],A[m][B],A[P][B],A[n][B],A[Q][B],A[o][B],A[R][B],A[S][B],A[r][B],J,A['Fundo CTA'][B],J,A[T][B],A[p][B],A[q][B],A['Botão fechar'][B]);H.append(L)
		M=[]
		for B in K(G(H)):
			if H[B].Imagem not in[D.path.basename(A)for A in E]:M.append(F(H[B].num))
		if M:M=[F(A)for A in M];C.set(f"Erro: Ações com nomes de imagens divergentes: {', '.join(map(X,M))}");return
		Z=t(H,b,E,Y)
		if Z==0:C.set('Nenhuma ação comercial encontrada na planilha.');return
		for v in K(Z):L=H[v];w=D.path.basename(L.Imagem);z=next(A for A in E if w==D.path.basename(A))
		C.set(f"{Z} script(s) gerado(s) com sucesso.");x=D.path.join(N,f"Demanda_{b}");s.Popen(['explorer',x])
	except Exception as y:C.set(f"Erro: {X(y)}")
def Q():global I,C;I=H.askopenfilename(filetypes=[('Excel Files','*.xlsx')]);C.set('Arquivo Excel selecionado.')
def S():
	global E,C;E=H.askopenfilenames(filetypes=[('Image Files','.png;.jpg;*.jpeg')])
	if E:C.set(f"{G(E)} imagem(ns) selecionada(s).")
	else:C.set('Nenhuma imagem selecionada.')
A=B.CTk()
A.geometry('400x350')
A.title('ACO_SQC')
T='src/ACO.ico'
A.iconbitmap(T)
C=M()
U=B.CTkLabel(A,text='Número da demanda:')
U.pack(padx=10,pady=10)
W=B.CTkEntry(A)
W.pack()
Z=B.CTkLabel(A,text='Selecione a planilha Excel:')
Z.pack(padx=10,pady=10)
b=B.CTkButton(A,text='Escolher arquivo',command=Q)
b.pack()
c=B.CTkLabel(A,text='Selecione a(s) imagem(ns):')
c.pack(padx=10,pady=10)
d=B.CTkButton(A,text='Escolher imagem(ns)',command=S)
d.pack()
e=B.CTkButton(A,text='Gerar script(s)',command=P)
e.pack(padx=10,pady=10)
f=B.CTkLabel(A,textvariable=C)
f.pack()
A.mainloop()