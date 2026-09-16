"""
Exemplo 02 — Como extrair links (URLs e textos) de uma página
Curso: Web Scraping e Rastreamento de Notícias / Fake News
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Endereço que será analisado
url = "https://example.com"

print(f"1. Acessando: {url} ...")

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    conteudo_html = resposta.text
except requests.exceptions.RequestException:
    print("[Aviso] Modo demonstração local ativado.")
    conteudo_html = """
    <html>
      <body>
        <h1>Artigo sobre Desinformação</h1>
        <p>Confira as fontes citadas abaixo:</p>
        <a href="https://agencia-noticias.org/materia-original">Matéria Original da Agência</a><br>
        <a href="https://dados.gov.br/relatorio">Relatório Oficial de Dados</a><br>
        <a href="/contato">Fale com a Redação</a>
      </body>
    </html>
    """

# Criamos o parser com BeautifulSoup
soup = BeautifulSoup(conteudo_html, "html.parser")

# soup.find_all("a") retorna uma lista com TODAS as tags <a> da página
todos_os_links = soup.find_all("a")

print("\n" + "=" * 60)
print(f"TOTAL DE LINKS ENCONTRADOS: {len(todos_os_links)}")
print("=" * 60)

for indice, tag_a in enumerate(todos_os_links, start=1):
    texto = tag_a.get_text().strip() or "[Sem texto]"
    href = tag_a.get("href")  # Obtém o destino do link
    
    # Se o link for relativo (ex: /contato), urljoin transforma em URL completa
    url_completa = urljoin(url, href) if href else "[Sem URL]"
    
    print(f"{indice}. Texto : {texto}")
    print(f"   Destino: {url_completa}")
    print("-" * 60)
