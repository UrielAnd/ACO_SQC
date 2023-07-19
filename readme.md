# ACO-SQC - Gerador de Scripts

<p align="center">
  <img src="https://github.com/ReisLucasF/ACO/blob/lusca/src/ACO.png" alt="Logo do ACO-SQC">
</p>

O ACO-SQC é um programa desenvolvido para facilitar a geração de scripts para uma aplicação de banco de dados, permitindo a importação de dados de uma planilha Excel e gerando os atributos necessários para serem interpretados pelo sistema.

## Funcionalidades

O programa foi atualizado para fornecer as seguintes funcionalidades:

1. **Interface Gráfica**: O ACO-SQC agora possui uma interface gráfica amigável, intuitiva e simples, tornando a interação com o programa mais fácil e rápida.

2. **Suporte para Múltiplas Ações Comerciais**: O programa agora suporta a importação de uma planilha com várias ações comerciais, permitindo a geração de scripts para cada uma delas.

3. **Suporte para Adição de Múltiplas Imagens**: O ACO-SQC permite o upload de várias imagens, e o programa identifica automaticamente qual ação comercial referencia cada imagem e atribui a ela os atributos correspondentes.

4. **Validação de Referência de Imagem na Planilha**: Antes de gerar os scripts, o programa verifica se todas as imagens adicionadas estão sendo corretamente referenciadas na planilha. Caso haja alguma ação com imagem não correspondente, uma mensagem de erro será exibida.

5. **Criação Automática de Pasta para Cada Demanda**: Ao gerar os scripts, o ACO-SQC cria automaticamente uma pasta com o número da demanda e inclui nela os scripts gerados. Os arquivos de script são nomeados de forma padronizada e com seu numero de ação para facilitar a identificação.

## Apresentação do ACO-SQC

Assista a uma breve apresentação do ACO-SQC para entender como utilizar o programa e suas principais funcionalidades.

[![Assista ao vídeo](https://img.shields.io/badge/Assista%20ao%20v%C3%ADdeo-ACO--SQC%20Presentation-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1i7iUSBXucPpfW0DzPlcGkgknCEoA1FJl/view?usp=drive_link)

Neste vídeo, você terá uma visão geral do ACO-SQC e aprenderá como utilizar as principais funcionalidades do programa.

## Atualizações Futuras

O ACO-SQC está em constante evolução, e algumas atualizações futuras planejadas incluem:

| Melhorias                    | Descrição                                                     |
| ---------------------------- | ------------------------------------------------------------- |
| Criação de Scripts para Popup | Implementar a funcionalidade de gerar scripts para popups.     |
| Criação de Scripts com Redirecionamento | Adicionar suporte para gerar scripts com redirecionamento via link.     |

## Instalação (Contribuição)

Para instalar o ACO-SQC e contribuir com o projeto, siga as instruções abaixo:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o comando `python -m pip install -r requirements.txt` para instalar as dependências necessárias.
4. Opcionalmente, instale o pacote `auto_py_to_exe` executando o comando `python -m pip install auto_py_to_exe`.

## Instalação (Usuário)

Para instalar o ACO-SQC e usufruir de suas funcionalidades, clique no botão abaixo para baixar o instalador da aplicação:

[![Download](https://img.shields.io/badge/Download%20via%20Google%20Drive-Install%20ACO--SQC-blue?style=for-the-badge&logo=googledrive)](https://drive.google.com/drive/u/0/folders/1YUcHqGUGfik-Db-RriX6n2Mknq9UN-Bs)

1. Após baixar o instalador, execute-o em sua máquina.
2. Siga as instruções de instalação fornecidas pelo instalador.
3. Após a conclusão da instalação, o ACO-SQC estará pronto para uso.

## Utilização

Para utilizar o ACO-SQC, siga as etapas abaixo:

1. Certifique-se de que a planilha a ser upada está com o formato de extensão `.xlsx`.
2. Para o upload de uma planilha com múltiplas ações, cada ação deverá ser especificada em uma linha única da planilha. Ações com o campo ACO contendo mais de um número, ex: "3548, 24587" irão gerar erro.
3. Os resultados serão salvos em uma pasta com o número da demanda na pasta "Scripts" e assim que gerados, a pasta da respectiva demanda será aberta automaticamente para uma melhor visualização.

<p align="center">
  <img src="https://github.com/ReisLucasF/ACO/blob/master/imgs/ScreenRecorderProject4.gif?raw=true">
</p>

## Contribuição

Contribuições para aprimorar o ACO-SQC são bem-vindas! Se você tiver sugestões, melhorias ou problemas a relatar, abra uma [issue](https://github.com/ReisLucasF/ACO/issues) neste repositório.

O ACO-SQC é um projeto de código aberto mantido por [Lucas Reis](https://github.com/ReisLucasF) e [Uriel Andrade](https://github.com/UrielAnd). Sua participação é fundamental para tornar o programa cada vez melhor e mais útil para a comunidade.
