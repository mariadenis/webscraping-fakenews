"""
Exemplo 05 — Rastreador de Circulação de Notícias e Linha do Tempo
Curso: Web Scraping e Rastreamento de Notícias / Fake News
"""

from bs4 import BeautifulSoup
from datetime import datetime

# 1. Três páginas fictícias que publicaram sobre o mesmo assunto em datas diferentes
paginas_ficticias = [
    {
        "site": "Site C (Portal Geral)",
        "url": "https://site-c.com/noticia-energia-revolucionaria",
        "html": """
        <html><body>
          <h1>Descoberta promete energia revolucionária: entenda a polêmica</h1>
          <time datetime="2026-09-13">13/09/2026</time>
          <span class="autor">Redação Central</span>
        </body></html>
        """
    },
    {
        "site": "Site A (Blog de Curiosidades)",
        "url": "https://site-a.blog/segredo-energia-revolucionaria",
        "html": """
        <html><body>
          <h1>Descoberta promete energia revolucionária sem custos</h1>
          <time datetime="2026-09-10">10/09/2026</time>
          <span class="autor">Anônimo</span>
        </body></html>
        """
    },
    {
        "site": "Site B (Notícias Regionais)",
        "url": "https://site-b-noticias.com/materia-energia",
        "html": """
        <html><body>
          <h1>Descoberta promete energia revolucionária em todo o país</h1>
          <time datetime="2026-09-11">11/09/2026</time>
          <span class="autor">Marcos Pereira</span>
        </body></html>
        """
    }
]

def raspar_dados_pagina(item):
    """
    Usa o BeautifulSoup para extrair título, data e autor do HTML.
    """
    soup = BeautifulSoup(item["html"], "html.parser")
    
    # Extrai o título
    titulo = soup.find("h1").get_text().strip()
    
    # Extrai a data ISO
    tag_tempo = soup.find("time")
    data_iso = tag_tempo.get("datetime") if tag_tempo else "2099-12-31"
    
    # Extrai o autor
    tag_autor = soup.find(class_="autor")
    autor = tag_autor.get_text().strip() if tag_autor else "Não informado"
    
    return {
        "site": item["site"],
        "url": item["url"],
        "titulo": titulo,
        "data_iso": data_iso,
        "autor": autor
    }

def formatar_data_br(data_iso):
    """Converte 'AAAA-MM-DD' para 'DD/MM/AAAA'"""
    try:
        dt = datetime.strptime(data_iso, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except ValueError:
        return data_iso

# Coletamos os dados de todas as páginas
publicacoes = [raspar_dados_pagina(p) for p in paginas_ficticias]

# Ordenamos a lista da data mais antiga para a mais recente
publicacoes_ordenadas = sorted(publicacoes, key=lambda x: x["data_iso"])

print("=" * 80)
print("RASTREAMENTO DE OCORRÊNCIAS — ORDEM CRONOLÓGICA")
print("=" * 80)
print(f"{'Data':<12} | {'Site':<26} | {'Título'}")
print("-" * 80)

for pub in publicacoes_ordenadas:
    data_formatada = formatar_data_br(pub["data_iso"])
    print(f"{data_formatada:<12} | {pub['site']:<26} | {pub['titulo']}")

print("=" * 80)

import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Construção visual da Linha do Tempo
print("\n" + "=" * 80)
print("LINHA DO TEMPO DA CIRCULACAO DA NOTICIA:")
print("=" * 80)

for i, pub in enumerate(publicacoes_ordenadas):
    data_formatada = formatar_data_br(pub["data_iso"])
    marcador = "[PRIMEIRA OCORRENCIA ENCONTRADA]" if i == 0 else f"[REPRODUZIDO - {i}o SALTO]"
    
    print(f"\n{data_formatada} ---> {pub['site']}  {marcador}")
    print(f"               +-- Titulo: \"{pub['titulo']}\"")
    print(f"               +-- Autor : {pub['autor']}")
    print(f"               +-- URL   : {pub['url']}")
    if i < len(publicacoes_ordenadas) - 1:
        print("               |")
        print("               v")

print("\n" + "=" * 80)
print("[!] AVISO IMPORTANTE DE CHECAGEM:")
print("A publicacao de 10/09/2026 (Site A) foi a mais antiga encontrada na nossa busca.")
print("POREM, isso NAO prova que o Site A criou o boato. Ele pode ter copiado de um")
print("grupo de mensagens, de uma postagem apagada ou de uma conversa offline.")
print("O scraping organiza as evidencias -- a checagem humana valida os fatos!")
print("=" * 80)

