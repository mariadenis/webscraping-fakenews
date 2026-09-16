"""
Exemplo 04 — Extração estruturada de uma notícia completa
Curso: Web Scraping e Rastreamento de Notícias / Fake News
"""

from bs4 import BeautifulSoup

def analisar_noticia(html_texto, url="https://portal-exemplo.com/noticias/caso-123"):
    """
    Extrai de forma segura todos os dados essenciais de uma página jornalística.
    """
    soup = BeautifulSoup(html_texto, "html.parser")

    # 1. TÍTULO
    tag_titulo = soup.find("h1") or soup.find("title")
    titulo = tag_titulo.get_text().strip() if tag_titulo else "Sem título"

    # 2. DATA
    tag_data = soup.find("time") or soup.find(class_=["data", "publicado-em", "date"])
    if tag_data:
        data = tag_data.get("datetime") or tag_data.get_text().strip()
    else:
        data = "Data não informada"

    # 3. AUTOR
    tag_autor = soup.find(class_=["autor", "author", "byline"])
    if tag_autor:
        autor = tag_autor.get_text().replace("Por:", "").replace("Por", "").strip()
    else:
        autor = "Não informado (Atenção: comum em desinformação)"

    # 4. CORPO DO TEXTO
    corpo = soup.find("article") or soup.find(class_=["conteudo", "texto-materia"]) or soup
    paragrafos = [p.get_text().strip() for p in corpo.find_all("p") if p.get_text().strip()]
    texto_artigo = "\n".join(paragrafos)

    # 5. LINKS CITADOS NA MATÉRIA
    links = []
    for a in corpo.find_all("a"):
        href = a.get("href")
        texto_link = a.get_text().strip()
        if href and href.startswith("http"):
            links.append({"texto": texto_link or "Link sem texto", "url": href})

    return {
        "url": url,
        "titulo": titulo,
        "data": data,
        "autor": autor,
        "texto": texto_artigo,
        "links": links
    }


# Exemplo simulando uma matéria com metadados reais
html_materia = """
<article>
  <header>
    <h1>Cientistas emitem nota sobre imagem gerada por IA atribuída a telescópio</h1>
    <div class="metadados">
      <span class="autor">Por: Juliana Nogueira</span>
      <time datetime="2026-09-12">12 de Setembro de 2026</time>
    </div>
  </header>
  <div class="conteudo">
    <p>Uma imagem astronômica impressionante que circulou em redes sociais como foto real foi criada por inteligência artificial.</p>
    <p>A agência espacial publicou um esclarecimento confirmando que a imagem não pertence ao seu catálogo oficial.</p>
    <p>O comunicado completo pode ser lido na <a href="https://agencia-espacial.gov/comunicados/ia-foto">página oficial de comunicados</a>.</p>
  </div>
</article>
"""

import sys

# Garante compatibilidade de saída em consoles com diferentes encodings
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

if __name__ == "__main__":
    resultado = analisar_noticia(html_materia)

    print("=" * 65)
    print("RELATORIO DE EXTRACAO DA NOTICIA")
    print("=" * 65)
    print(f"[*] TITULO: {resultado['titulo']}")
    print(f"[*] DATA  : {resultado['data']}")
    print(f"[*] AUTOR : {resultado['autor']}")
    print(f"[*] URL   : {resultado['url']}")
    print("-" * 65)
    print("CONTEUDO DA MATERIA:")
    print(resultado['texto'])
    print("-" * 65)
    print(f"LINKS CITADOS ({len(resultado['links'])}):")
    for link in resultado['links']:
        print(f"   -> {link['texto']} ({link['url']})")
    print("=" * 65)

