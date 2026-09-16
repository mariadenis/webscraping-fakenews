# Exercício Final — Investigação, Filtro por Palavra-Chave e Comparação de Fontes

Este exercício final consolida duas habilidades vitais para investigar notícias falsas e desinformação:
1. **Filtragem por Palavra-Chave:** monitorar notícias que mencionem termos suspeitos ou tópicos sob apuração.
2. **Comparação entre Fontes:** coletar títulos de duas páginas diferentes e comparar as narrativas.

---

## Parte 1 — Filtrando Notícias por Palavra-Chave

### Objetivo:
Criar um programa que receba uma lista de notícias e filtre apenas aquelas que mencionem determinada palavra-chave (exemplo: `"boato"`, `"vacina"`, `"alerta"` ou `"urgente"`).

### Código Inicial:
```python
from bs4 import BeautifulSoup

html_noticias = """
<ul>
  <li>Descoberta de nova jazida de lítio impulsiona setor automotivo</li>
  <li>URGENTE: Mensagem falsa sobre cancelamento de títulos eleitorais volta a circular</li>
  <li>Campeonato regional define finalistas após rodada emocionante</li>
  <li>ALERTA: Especialistas desmentem boato sobre contaminação de água pública</li>
</ul>
"""

soup = BeautifulSoup(html_noticias, "html.parser")

palavra_chave = "boato"

# COMPLETE AQUI: Percorra todas as tags <li> e filtre apenas aquelas
# que contenham a palavra_chave (dica: converta para minúsculas com .lower())
```

### Dica:
* Use `if palavra_chave.lower() in texto.lower():` para garantir que a busca não diferencie maiúsculas de minúsculas.

### Solução da Parte 1:
```python
from bs4 import BeautifulSoup

html_noticias = """
<ul>
  <li>Descoberta de nova jazida de lítio impulsiona setor automotivo</li>
  <li>URGENTE: Mensagem falsa sobre cancelamento de títulos eleitorais volta a circular</li>
  <li>Campeonato regional define finalistas após rodada emocionante</li>
  <li>ALERTA: Especialistas desmentem boato sobre contaminação de água pública</li>
</ul>
"""

soup = BeautifulSoup(html_noticias, "html.parser")
palavra_chave = "boato"

itens = soup.find_all("li")

print(f"Notícias filtradas contendo o termo '{palavra_chave.upper()}':")
print("=" * 60)

encontrados = 0
for li in itens:
    texto = li.get_text().strip()
    if palavra_chave.lower() in texto.lower():
        encontrados += 1
        print(f"[{encontrados}] {texto}")

if encontrados == 0:
    print("Nenhuma notícia encontrada com essa palavra-chave.")
print("=" * 60)
```

---

## Parte 2 — Comparação de Títulos entre Duas Páginas

### Objetivo:
Raspar duas páginas distintas (por exemplo, um portal de notícias oficial e um blog que reproduziu a notícia) e comparar os títulos para investigar como a manchete mudou.

### Código Inicial:
```python
from bs4 import BeautifulSoup

# Página 1: Fonte original
html_pagina_1 = """
<article>
  <h1>Estudo preliminar aponta necessidade de novos testes em medicamento</h1>
  <time datetime="2026-09-05">05/09/2026</time>
</article>
"""

# Página 2: Blog que modificou a informação para gerar cliques (clickbait/boato)
html_pagina_2 = """
<article>
  <h1>BOMBA: Medicamento é proibido às pressas por apresentar riscos gravíssimos!</h1>
  <time datetime="2026-09-07">07/09/2026</time>
</article>
"""

# COMPLETE AQUI: Extraia o título e a data de cada página e exiba uma comparação lado a lado!
```

### Dica:
* Crie uma função auxiliar `extrair_resumo(html)` que retorne um dicionário `{ "titulo": ..., "data": ... }`. Assim você não repete código!

### Solução da Parte 2:
```python
from bs4 import BeautifulSoup

html_pagina_1 = """
<article>
  <h1>Estudo preliminar aponta necessidade de novos testes em medicamento</h1>
  <time datetime="2026-09-05">05/09/2026</time>
</article>
"""

html_pagina_2 = """
<article>
  <h1>BOMBA: Medicamento é proibido às pressas por apresentar riscos gravíssimos!</h1>
  <time datetime="2026-09-07">07/09/2026</time>
</article>
"""

def extrair_resumo(html):
    soup = BeautifulSoup(html, "html.parser")
    tag_h1 = soup.find("h1")
    tag_time = soup.find("time")
    
    return {
        "titulo": tag_h1.get_text().strip() if tag_h1 else "Sem título",
        "data": tag_time.get_text().strip() if tag_time else "Sem data"
    }

fonte_1 = extrair_resumo(html_pagina_1)
fonte_2 = extrair_resumo(html_pagina_2)

print("=" * 70)
print("COMPARAÇÃO DE VERSÕES DA NOTÍCIA")
print("=" * 70)
print(f"[FONTE 1 - DATA: {fonte_1['data']}]")
print(f"Manchete: {fonte_1['titulo']}\n")

print(f"[FONTE 2 - DATA: {fonte_2['data']}]")
print(f"Manchete: {fonte_2['titulo']}\n")

print("-" * 70)
print("ANÁLISE DE DESINFORMAÇÃO:")
print("Observe como a Fonte 2 (mais recente) exagerou o título da Fonte 1,")
print("transformando um 'estudo preliminar com novos testes' em um alarde 'BOMBA'.")
print("Essa técnica de comparação é fundamental para identificar descontextualizações!")
print("=" * 70)
```
