# Exercício 04 — Manchete + Link

## Objetivo
Combinar o título de uma matéria com o seu respectivo link de acesso, gerando uma lista estruturada no formato:
`Título | Link`

---

## Instruções
1. No HTML dos portais de notícias, a manchete geralmente fica dentro de uma tag `<a>` ou possui uma tag `<a>` dentro do `<h2>` (exemplo: `<h2><a href="...">Título</a></h2>`).
2. Utilize o BeautifulSoup para localizar esses blocos de notícia.
3. Extraia o texto do título e a URL do link.
4. Exiba cada notícia no formato padronizado `Título | Link`.

---

## Código Inicial

```python
from bs4 import BeautifulSoup

html_feed = """
<div class="feed">
  <article>
    <h2><a href="https://noticias.com/economia/dolar-hoje">Dólar fecha em queda de 0,8%</a></h2>
  </article>
  <article>
    <h2><a href="https://noticias.com/saude/nova-campanha-vacinacao">Iniciada nova etapa de vacinação nacional</a></h2>
  </article>
  <article>
    <h2><a href="https://noticias.com/tecnologia/novo-satelite">Lançamento de satélite de monitoramento ambiental</a></h2>
  </article>
</div>
"""

soup = BeautifulSoup(html_feed, "html.parser")

# COMPLETE AQUI: Encontre todos os artigos ou todos os links dentro de h2
# materias = ...

# COMPLETE AQUI: Extraia o texto e o href e mostre no formato:
# print(f"{titulo} | {link}")
```

---

## Dica
* Você pode buscar todas as tags `<h2>` com `soup.find_all("h2")` e, dentro de cada uma delas, buscar o link com `h2.find("a")`.
* Assim você garante que está pegando exatamente o link correspondente àquele título!

---

## Solução Comentada

```python
from bs4 import BeautifulSoup

html_feed = """
<div class="feed">
  <article>
    <h2><a href="https://noticias.com/economia/dolar-hoje">Dólar fecha em queda de 0,8%</a></h2>
  </article>
  <article>
    <h2><a href="https://noticias.com/saude/nova-campanha-vacinacao">Iniciada nova etapa de vacinação nacional</a></h2>
  </article>
  <article>
    <h2><a href="https://noticias.com/tecnologia/novo-satelite">Lançamento de satélite de monitoramento ambiental</a></h2>
  </article>
</div>
"""

soup = BeautifulSoup(html_feed, "html.parser")

print("=" * 80)
print("LISTA DE NOTÍCIAS (TÍTULO | LINK)")
print("=" * 80)

# Buscamos todas as tags <h2>
tags_h2 = soup.find_all("h2")

for tag in tags_h2:
    # Dentro de cada h2, localizamos a tag <a>
    link_tag = tag.find("a")
    
    if link_tag:
        titulo = link_tag.get_text().strip()
        link_url = link_tag.get("href")
        print(f"{titulo} | {link_url}")

print("=" * 80)
```
