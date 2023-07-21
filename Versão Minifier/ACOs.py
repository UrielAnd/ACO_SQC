B=None
class A:
	num=B;Tipo_de_layout=B;Banner=0;Titulo=B;Titulo_Cor=B;Cor_Fundo_Inicial=B;Cor_Fundo_Final=B;CTA_Cor=B;CTA_Cor_Borda=B;CTA_Cor_Fundo=B;Subtitulo=B;Subtitulo_Cor=B;Texto_CTA=B;Imagem=B;Link=B;Método_Red='';Código_Red='';Tamanho_Titulo=B;Tamanho_Subtitulo=B;Cor_Botao_Fechar=B
	def __init__(A,num,Tipo_de_layout,Titulo,Titulo_Cor,Subtitulo,Subtitulo_Cor,Texto_CTA,CTA_Cor,Imagem,Cor_Fundo_Inicial,Cor_Fundo_Final,CTA_Cor_borda,CTA_Cor_Fundo,Link,Tamanho_Titulo,Tamanho_Subtitulo,Cor_Botao_Fechar):
		G='GRANDE';F='MEDIO';E='PEQUENO';D=Tamanho_Subtitulo;C=Tamanho_Titulo;A.num=num;A.Tipo_de_layout=Tipo_de_layout.upper();A.Titulo=Titulo;A.Titulo_Cor=Titulo_Cor;A.Subtitulo=Subtitulo;A.Subtitulo_Cor=Subtitulo_Cor;A.Texto_CTA=Texto_CTA;A.CTA_Cor=CTA_Cor;A.Imagem=Imagem;A.Cor_Fundo_Inicial=Cor_Fundo_Inicial;A.Cor_Fundo_Final=Cor_Fundo_Final;A.CTA_Cor_Fundo=CTA_Cor_Fundo;A.CTA_Cor_Borda=CTA_Cor_borda;A.Link=Link;A.Tamanho_Titulo=C;A.Tamanho_Subtitulo=D;A.Cor_Botao_Fechar=Cor_Botao_Fechar
		if Link=='':...
		else:A.Código_Red='23172';A.Método_Red='Link'
		if C==B:...
		elif C.upper()==E:A.Tamanho_Titulo=1
		elif C.upper()==F:A.Tamanho_Titulo=2
		elif C.upper()==G:A.Tamanho_Titulo=3
		if D==B:...
		elif D.upper()==E:A.Tamanho_Subtitulo=1
		elif D.upper()==F:A.Tamanho_Subtitulo=2
		elif D.upper()==G:A.Tamanho_Subtitulo=3
	def defini_banner(A):
		if A.Tipo_de_layout=='CARTÃO COM IMAGEM À ESQUERDA - TÍTULO, SUBTÍTULO E CTA À DIREITA':A.Banner=319
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À ESQUERDA - TÍTULO E CTA À DIREITA':A.Banner=320
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À ESQUERDA - SUBTÍTULO E CTA À DIREITA':A.Banner=321
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À ESQUERDA - TÍTULO E SUBTÍTULO À DIREITA':A.Banner=271
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À DIREITA - TÍTULO, SUBTÍTULO E CTA À ESQUERDA':A.Banner=322
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À DIREITA - TÍTULO E CTA À ESQUERDA':A.Banner=323
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À DIREITA - SUBTÍTULO E CTA À ESQUERDA':A.Banner=324
		elif A.Tipo_de_layout=='CARTÃO COM IMAGEM À DIREITA - TÍTULO E SUBTÍTULO À ESQUERDA':A.Banner=275
		elif A.Tipo_de_layout=='POPUP COM IMAGEM SUPERIOR - TITULO, SUBTÍTULO, TEXTO CTA (BOTÃO)':A.Banner=333
		elif A.Tipo_de_layout=='POPUP COM IMAGEM INFERIOR - TITULO, SUBTÍTULO, TEXTO CTA (BOTÃO)':A.Banner=334
		elif A.Tipo_de_layout=='POPUP COM IMAGEM LIVRE (TEXTOS JÁ FIXOS NA IMAGEM)':A.Banner=335
		else:A.Banner=0
	def print(A):return print(A.num,A.Tipo_de_layout,A.Banner,A.Titulo,A.Titulo_Cor,A.Subtitulo,A.Subtitulo_Cor,A.Texto_CTA,A.CTA_Cor,A.Imagem,A.Cor_Fundo_Inicial,A.Cor_Fundo_Final,A.CTA_Cor_Fundo,A.CTA_Cor_Borda,A.Link)