# AntiACO - Gerador de Scripts

<p align="center">
  <img src="https://github.com/ReisLucasF/ACO/blob/lusca/src/ACO.png" alt="Logo do AntiACO">
</p>

O AntiACO é um programa desenvolvido para facilitar a geração de scripts para uma aplicação de banco de dados, permitindo a importação de dados de uma planilha Excel e gerando os atributos necessários para serem interpretados pelo sistema.

## Funcionalidades

O programa foi atualizado para fornecer as seguintes funcionalidades:

1. **Interface Gráfica**: O AntiACO agora possui uma interface gráfica amigável, intuitiva e simples, tornando a interação com o programa mais fácil e rápida.

2. **Suporte para Múltiplas Ações Comerciais**: O programa agora suporta a importação de uma planilha com várias ações comerciais, permitindo a geração de scripts para cada uma delas.

3. **Suporte para Adição de Múltiplas Imagens**: O AntiACO permite o upload de várias imagens, e o programa identifica automaticamente qual ação comercial referencia cada imagem e atribui a ela os atributos correspondentes.

4. **Validação de Referência de Imagem na Planilha**: Antes de gerar os scripts, o programa verifica se todas as imagens adicionadas estão sendo corretamente referenciadas na planilha. Caso haja alguma ação com imagem não correspondente, uma mensagem de erro será exibida.

5. **Criação Automática de Pasta para Cada Demanda**: Ao gerar os scripts, o AntiACO cria automaticamente uma pasta com o número da demanda e inclui nela os scripts gerados. Os arquivos de script são nomeados de forma padronizada e com seu numero de ação para facilitar a identificação.

## Atualizações Futuras

O AntiACO está em constante evolução, e algumas atualizações futuras planejadas incluem:

| Melhorias                    | Descrição                                                     |
| ---------------------------- | ------------------------------------------------------------- |
| Geração de Scripts por Layout | Adicionar suporte para diferentes layouts de cards.         |
| Criação de Scripts para Popup | Implementar a funcionalidade de gerar scripts para popups.     |
| Criação de Scripts com Redirecionamento | Adicionar suporte para gerar scripts com redirecionamento via link.     |

## Instalação (Contribuição)

Para instalar o AntiACO, siga as instruções abaixo:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o comando `python -m pip install -r requirements.txt` para instalar as dependências necessárias.
4. Opcionalmente, instale o pacote `auto_py_to_exe` executando o comando `python -m pip install auto_py_to_exe`.

## Instalação (Usuário)

Para instalar o AntiACO e usufruir de suas funcionalidades, clique no botão a seguir e siga as instruções abaixo:<br>
[![Download](https://img.shields.io/badge/Download-ZIP-blue?style=for-the-badge&logo=github)](https://github.com/ReisLucasF/ACO/archive/refs/heads/Download.zip)


1. Descompacte o arquivo e selecione o seu melhor diretório.
2. Agora basta executar o AntiACO.exe
   
## Utilização

Para utilizar o AntiACO, siga as etapas abaixo:

1. Certifique-se de que a planilha a ser upada está com o formato de extensão`.xlsx`.
2. Para o upload de uma planilha com multiplas ações, cada ação deverá ser especificada em uma linha única da planilha. Ações com o campo ACO contendo mais de um número, ex: "3548, 24587" irão gerar erro.
3. Os resultados serão salvos em uma pasta com o número da demanda na pasta "Scripts" e assim que gerados, a pasta da respectiva demanda será aberta automaticamente para uma melhor visualização.

## Contribuição

Contribuições para aprimorar o AntiACO são bem-vindas! Se você tiver sugestões, melhorias ou problemas a relatar, abra uma [issue](https://github.com/ReisLucasF/ACO/issues) neste repositório.

O AntiACO é um projeto de código aberto mantido por [Lucas Reis](https://github.com/ReisLucasF) e [Uriel Andrade](https://github.com/UrielAnd). Sua participação é fundamental para tornar o programa cada vez melhor e mais útil para a comunidade.
