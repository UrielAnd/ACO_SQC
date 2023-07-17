class ACOs:
    num = None
    Tipo_de_layout = None
    Banner = 0
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
    


    def __init__ (self, num, Tipo_de_layout, Titulo, Titulo_Cor, Subtitulo, Subtitulo_Cor, Texto_CTA, CTA_Cor, Imagem, Cor_Fundo_Inicial, Cor_Fundo_Final, CTA_Cor_borda, CTA_Cor_Fundo,) -> None:
        self.num = num
        self.Tipo_de_layout = Tipo_de_layout
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

    def defini_banner(self):
        if self.Tipo_de_layout == "Cartão com imagem à esquerda - Título, subtítulo e CTA à direita":
                self.Banner = 319
        elif self.Tipo_de_layout == "Cartão com imagem à esquerda - Título e CTA à direita":
                self.Banner = 320
        elif self.Tipo_de_layout == "Cartão com imagem à esquerda - Subtítulo e CTA à direita":
                self.Banner = 321
        elif self.Tipo_de_layout == "Cartão com imagem à esquerda - Título e subtítulo à direita":
                self.Banner = 271
        elif self.Tipo_de_layout == "Cartão com imagem à direita - Título, subtítulo e CTA à esquerda":
                self.Banner = 322
        elif self.Tipo_de_layout == "Cartão com imagem à direita - Título e CTA à esquerda":
                self.Banner = 323
        elif self.Tipo_de_layout == "Cartão com imagem à direita - Subtítulo e CTA à esquerda":
                self.Banner = 324
        elif self.Tipo_de_layout == "Cartão com imagem à direita - Título e subtítulo à esquerda":
                self.Banner = 275
        #elif lista[index].Tipo_de_layout == "Cartão sem imagem - Título, subtítulo e CTA":
        #        Layout_Value = 303
        #elif lista[index].Tipo_de_layout == "Cartão sem imagem - Título e CTA":
        #        Layout_Value = 304
        #elif lista[index].Tipo_de_layout == "Cartão sem imagem - Título e subtítulo":
        #        Layout_Value = 305
        #elif lista[index].Tipo_de_layout == "Cartão sem imagem - Subtítulo e CTA":
        #        Layout_Value = 306

    def print(self):
        return print(self.num, self.Tipo_de_layout, self.Banner, self.Titulo, self.Titulo_Cor, self.Subtitulo, self.Subtitulo_Cor,
                      self.Texto_CTA, self.CTA_Cor, self.Imagem, self.Cor_Fundo_Inicial, self. Cor_Fundo_Final, self.CTA_Cor_Fundo, self.CTA_Cor_Borda)
