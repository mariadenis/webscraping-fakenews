# Exercício 01 — Capturando o Título de uma Página

## Objetivo
Criar um programa em Python com `requests` e `BeautifulSoup` que acesse uma página da internet e extraia o seu título principal (`<h1>`), exibindo-o limpo no terminal.

---

## Instruções
1. Importe as bibliotecas `requests` e `BeautifulSoup`.
2. Defina a URL `https://example.com` (ou outra de sua preferência).
3. Faça a requisição HTTP com `requests.get()`.
4. Use o BeautifulSoup para analisar o HTML.
5. Localize a tag `<h1>` e imprima apenas o texto na tela.

---

## Código Inicial

Copie este esqueleto e complete onde indicado pelos comentários:

```python
import requests
from bs4 import BeautifulSoup

# 1. Defina a URL desejada
url = "https://example.com"

# 2. Faça a requisição HTTP
resposta = requests.get(url)

# 3. Analise o HTML com BeautifulSoup
soup = BeautifulSoup(resposta.text, "html.parser")

# 4. COMPLETE AQUI: Encontre a tag <h1>
# tag_titulo = ...

# 5. COMPLETE AQUI: Extraia o texto limpo e imprima
# print(...)
```

---

## Dica
* Use o método `soup.find("h1")` para localizar a tag.
* Use o método `.get_text().strip()` para pegar apenas as palavras, removendo espaços e quebras de linha em excesso.

---

## Solução Comentada

```python
import requests
from bs4 import BeautifulSoup

# 1. Endereço da página alvo
url = "https://example.com"

# 2. Fazemos o download do conteúdo da página
resposta = requests.get(url)

# 3. Criamos o analisador (parser) BeautifulSoup
soup = BeautifulSoup(resposta.text, "html.parser")

# 4. Buscamos a primeira tag <h1> encontrada na página
tag_titulo = soup.find("h1")

# 5. Verificamos se a tag existe antes de extrair o texto
if tag_titulo:
    titulo_limpo = tag_titulo.get_text().strip()
    print("Título encontrado com sucesso:")
    print(f"-> {titulo_limpo}")
else:
    print("Nenhuma tag <h1> foi encontrada nesta página.")
```
