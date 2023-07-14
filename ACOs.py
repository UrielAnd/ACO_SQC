class ACOs:
    num = None
    Tipo_de_layout = None
    Banner = None
    Titulo = None
    Titulo_Cor = None
    Cor_Fundo_Inicial= None
    Cor_Fundo_Final = None
    CTA_Cor = None
    CTA_Cor_Borda = None
    CTA_Cor_Fundo = None
    Subtitulo = None
    Subtitulo_Cor = None
    Texto_CTA = None
    Imagem = None
    


    def __init__ (self, num, Tipo_de_layout, Banner, Titulo, Titulo_Cor, Subtitulo, Subtitulo_Cor, Texto_CTA, CTA_Cor, Imagem, Cor_Fundo_Inicial, Cor_Fundo_Final, CTA_Cor_borda, CTA_Cor_Fundo,) -> None:
        self.num = num
        self.Tipo_de_layout = Tipo_de_layout
        self.Banner = Banner
        self.Titulo = Titulo
        self.Titulo_Cor = Titulo_Cor
        self.Subtitulo = Subtitulo
        self.Subtitulo_Cor = Subtitulo_Cor
        self.Texto_CTA = Texto_CTA
        self.CTA_Cor = CTA_Cor
        self.Imagem = Imagem
        self.Cor_Fundo_Inicial = Cor_Fundo_Inicial
        self.Cor_Fundo_Final = Cor_Fundo_Final
        self.CTA_Cor_Fundo = CTA_Cor_Fundo
        self.CTA_Cor_Borda = CTA_Cor_borda


    def print(self):
        return print(self.num, self.Tipo_de_layout, self.Banner, self.Titulo, self.Titulo_Cor, self.Subtitulo, self.Subtitulo_Cor,
                      self.Texto_CTA, self.CTA_Cor, self.Imagem, self.Cor_Fundo_Inicial, self. Cor_Fundo_Final, self.CTA_Cor_Fundo, self.CTA_Cor_Borda)
