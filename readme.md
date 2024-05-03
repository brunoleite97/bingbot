# BINGBOT

Automatizar obtenção de pontos de pesquisa no bing

## Pré-requisitos

Para rodar esse projeto, faz-se necessário instalar o [GIT](https://git-scm.com/downloads) e o [Python](https://www.python.org/).



## Instalação

Instale as dependências de [Python](https://www.python.org/), é necessario criar um ambiente, com o seguinte comando:
```
python -m venv nome-do-ambiente
```

Para iniciar o ambiente use o seguinte comando:
```
nome-do-ambiente\scripts\python
```

Instale as dependências de Python do projeto, no prompt com o comando:
```
pip install -r requirements.txt
```

Aguarde até finalizar.

## Ajustes
Altere a quantidade de pesquisas a ser realizada no trecho:

```
keywords = [fake.word() for _ in range(30)]
```

Altere o navegador no trecho
```
    pyautogui.write('Microsoft Edge')
```

## Iniciar pesquisas
Tenha login realizado no bing do navegador a ser utilizado.


Para iniciar as pesquisas, execute o comando:
```
python bot.py
```

Ele irá buscar em sua barra de pesquisas do windows, o navegador definido. Ele irá abrir o navegador e digitar o dado na barra de pesquisa.

## Tecnologias utilizadas

Abaixo seguem as tecnologias utilizadas:

* [GIT](https://git-scm.com/) - Aplicação utilizada para controle de versionamento de código.
* [Python](https://python.org) - Linguagem de programação utilizada para geração dos dados para o teste.
* [Faker](https://faker.readthedocs.io/en/master/) - Biblioteca utilizada para geração dos dados falsos utilizados no teste.
* [Pyautogui](https://pyautogui.readthedocs.io/en/latest/) - PyAutoGUI permite que seus scripts Python controlem o mouse e o teclado para automatizar as interações com outros aplicativos.