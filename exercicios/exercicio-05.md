# Exercício 05 — Tabela com Várias Notícias (Título | Data | Link)

## Objetivo
Coletar dados de múltiplos artigos e apresentá-los no formato de uma tabela alinhada contendo:
`Título | Data | Link`

---

## Instruções
1. Itere sobre os blocos de matérias (`<article>`).
2. Para cada artigo, extraia:
   * O título da matéria (`<h2>` ou `<a>`);
   * A data de publicação (`<time>`);
   * O link (`<a href="...">`).
3. Formate a saída como uma tabela limpa e fácil de ler no terminal.

---

## Código Inicial

```python
from bs4 import BeautifulSoup

html_artigos = """
<div class="arquivo-noticias">
  <article>
    <h3><a href="https://noticia.org/clima-seca">Seca histórica afeta reservatórios do interior</a></h3>
    <time datetime="2026-09-08">08/09/2026</time>
  </article>

  <article>
    <h3><a href="https://noticia.org/nova-vacina">Aprovada nova fórmula de vacina contra gripe</a></h3>
    <time datetime="2026-09-10">10/09/2026</time>
  </article>

  <article>
    <h3><a href="https://noticia.org/alerta-boato">Nota de esclarecimento sobre mensagem falsa nas redes</a></h3>
    <time datetime="2026-09-12">12/09/2026</time>
  </article>
</div>
"""

soup = BeautifulSoup(html_artigos, "html.parser")

# COMPLETE AQUI: Encontre todos os elementos <article>
# artigos = ...

# COMPLETE AQUI: Para cada artigo, extraia titulo, data e link e imprima como tabela
```

---

## Dica
* Use formatação de strings do Python como `f"{titulo:<40} | {data:<10} | {link}"` para alinhar as colunas da tabela!
* Verifique se `<time>` e `<a>` existem com um `if` para evitar erros caso falte algum dado.

---

## Solução Comentada

```python
from bs4 import BeautifulSoup

html_artigos = """
<div class="arquivo-noticias">
  <article>
    <h3><a href="https://noticia.org/clima-seca">Seca histórica afeta reservatórios do interior</a></h3>
    <time datetime="2026-09-08">08/09/2026</time>
  </article>

  <article>
    <h3><a href="https://noticia.org/nova-vacina">Aprovada nova fórmula de vacina contra gripe</a></h3>
    <time datetime="2026-09-10">10/09/2026</time>
  </article>

  <article>
    <h3><a href="https://noticia.org/alerta-boato">Nota de esclarecimento sobre mensagem falsa nas redes</a></h3>
    <time datetime="2026-09-12">12/09/2026</time>
  </article>
</div>
"""

soup = BeautifulSoup(html_artigos, "html.parser")

artigos = soup.find_all("article")

print("=" * 95)
print(f"{'Título':<52} | {'Data':<12} | {'Link'}")
print("=" * 95)

for art in artigos:
    tag_link = art.find("a")
    tag_data = art.find("time")
    
    titulo = tag_link.get_text().strip() if tag_link else "Sem título"
    link = tag_link.get("href") if tag_link else "Sem link"
    data = tag_data.get_text().strip() if tag_data else "Sem data"
    
    # Exibe formatado em colunas
    print(f"{titulo:<52} | {data:<12} | {link}")

print("=" * 95)
```
