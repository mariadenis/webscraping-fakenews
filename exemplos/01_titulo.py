"""
Exemplo 01 — Como extrair o título de uma página com Web Scraping
Curso: Web Scraping e Rastreamento de Notícias / Fake News
"""

import requests
from bs4 import BeautifulSoup

# URL de teste da internet (site mantido pela IANA para testes e exemplos)
url = "https://example.com"

print(f"1. Conectando ao endereço: {url} ...")

try:
    # Fazemos a requisição HTTP para o servidor
    resposta = requests.get(url, timeout=10)
    
    # Verificamos se a requisição foi bem-sucedida (código 200)
    resposta.raise_for_status()
    conteudo_html = resposta.text

except requests.exceptions.RequestException as erro:
    # Se houver problema de conexão ou o site estiver fora do ar,
    # usamos um HTML de demonstração para que o exemplo sempre funcione
    print(f"\n[Aviso] Não foi possível conectar à internet ({erro}).")
    print("Usando HTML local de demonstração para o aprendizado...\n")
    conteudo_html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Notícia Exemplo — Portal de Teste</title>
      </head>
      <body>
        <h1>Título da Notícia: Descoberta Científica Anunciada</h1>
        <p>Texto do primeiro parágrafo...</p>
      </body>
    </html>
    """

# 2. Criamos o objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(conteudo_html, "html.parser")

# 3. Localizamos a tag <h1> (título principal)
tag_h1 = soup.find("h1")

# Também podemos verificar a tag <title> (título que aparece na aba do navegador)
tag_title = soup.find("title")

# 4. Exibimos os resultados
print("\n" + "=" * 50)
print("RESULTADOS DA EXTRAÇÃO:")
print("=" * 50)

if tag_h1:
    print(f"Tag <h1> encontrada : {tag_h1.get_text().strip()}")
else:
    print("Tag <h1> não encontrada.")

if tag_title:
    print(f"Tag <title> da página: {tag_title.get_text().strip()}")
else:
    print("Tag <title> não encontrada.")

print("=" * 50)
