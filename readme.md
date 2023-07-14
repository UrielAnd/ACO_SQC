# AntiACO

<p align="center">
  <img src="https://github.com/ReisLucasF/ACO/blob/lusca/src/ACO.png" alt="Logo do AntiACO">
</p>

O AntiACO é um programa projetado para facilitar a geração de scripts, permitindo a importação de dados de uma planilha e gerando os atributos necessários para serem interpretados pelo banco de dados.

## Funcionalidades

O programa inclui um executável chamado `AntiACO.exe` que extrai os dados de uma planilha localizada na pasta "tests". A planilha deve ser nomeada como `teste.xlsx`. Além disso, o programa é capaz de identificar imagens presentes na pasta "imgs" e codificá-las em base64, desde que as referências estejam corretamente inseridas na planilha mencionada anteriormente.

## Instalação

Para instalar o AntiACO, siga as instruções abaixo:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o comando `python -m pip install -r requirements.txt` para instalar as dependências necessárias.
4. Opcionalmente, instale o pacote `auto_py_to_exe` executando o comando `python -m pip install auto_py_to_exe`.

## Utilização

Para utilizar o AntiACO, siga as etapas abaixo:

1. Certifique-se de que a planilha `teste.xlsx` está presente na pasta "tests".
2. Verifique se as imagens estão devidamente referenciadas na planilha e localizadas na pasta "imgs".
3. Execute o arquivo `AntiACO.exe` para iniciar o programa.
4. Aguarde enquanto os dados são extraídos da planilha e os atributos são gerados para o banco de dados.
5. Os resultados serão salvos em um arquivo de saída, conforme especificado nas configurações do programa.

## Atualizações Futuras

| Melhorias                    | Descrição                                                     |
| ---------------------------- | ------------------------------------------------------------- |
| Interface Gráfica            | Desenvolver uma interface amigável e intuitiva para o programa |
| Variações de Layouts         | Adicionar suporte para diferentes layouts de cards         |

## Contribuição

Contribuições para aprimorar o AntiACO são bem-vindas! Se você tiver sugestões, melhorias ou problemas a relatar, abra uma [issue](https://github.com/SeuNomeDeUsuário/Repositório/issues) neste repositório.

