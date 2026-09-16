# Aula 03 — Aprendendo a Extrair Informações

Quando estamos investigando uma notícia suspeita, precisamos de mais do que apenas o título da página. Precisamos reunir **manchetes**, **links citados**, **datas de publicação**, **autores** e o **corpo do texto**.

Nesta aula, você aprenderá a extrair cada um desses elementos passo a passo, usando métodos fundamentais do BeautifulSoup:
* `soup.find()`: localiza a **primeira** ocorrência de uma tag;
* `soup.find_all()`: localiza **todas** as ocorrências de uma tag e devolve uma lista.

---

## Exemplo 1 — Título da Página

### Objetivo:
Capturar o título principal de uma notícia, geralmente localizado na tag `<h1>` ou na tag `<title>`.

### Código:
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")

# Encontra a tag de título principal
titulo = soup.find("h1").get_text().strip()

print(f"Título: {titulo}")
```

### Explicação do Código:
* `.strip()`: remove espaços em branco ou quebras de linha desnecessárias no início e no final do texto extraído.

### Resultado Esperado:
```text
Título: Example Domain
```

### Exercício Rápido:
> Como você alteraria a linha para buscar a tag `<title>` caso a página não tenha `<h1>`?

---

## Exemplo 2 — Múltiplas Manchetes

### Objetivo:
Em um portal ou página de busca, existem várias notícias listadas. Queremos coletar **todas** as manchetes da página de uma só vez.

### Código:
```python
from bs4 import BeautifulSoup

# Simulando o HTML de uma página com várias notícias
html_noticias = """
<html>
  <body>
    <h2>Cientistas descobrem nova espécie na Amazônia</h2>
    <h2>Mercado financeiro fecha em alta nesta terça</h2>
    <h2>Boato sobre nova lei viraliza em grupos de mensagens</h2>
  </body>
</html>
"""

soup = BeautifulSoup(html_noticias, "html.parser")

# soup.find_all retorna uma lista com todas as tags <h2>
manchetes = soup.find_all("h2")

print(f"Total de manchetes encontradas: {len(manchetes)}\n")

for i, tag in enumerate(manchetes, start=1):
    texto_manchete = tag.get_text().strip()
    print(f"{i}. {texto_manchete}")
```

### Explicação do Código:
* `soup.find_all("h2")`: vasculha todo o HTML e devolve uma lista contendo todos os elementos `<h2>`.
* `for i, tag in enumerate(manchetes, start=1)`: percorre a lista elemento por elemento, numerando de 1 em diante.
* `tag.get_text().strip()`: limpa o texto de cada manchete individual.

### Resultado Esperado:
```text
Total de manchetes encontradas: 3

1. Cientistas descobrem nova espécie na Amazônia
2. Mercado financeiro fecha em alta nesta terça
3. Boato sobre nova lei viraliza em grupos de mensagens
```

### Exercício Rápido:
> Se o portal usasse tags `<h3>` para notícias secundárias, como você adaptaria o código para listar as tags `<h3>`?

---

## Exemplo 3 — Links (Texto e URL)

### Objetivo:
Notícias frequentemente citam ou direcionam para outras páginas. Para rastrear a circulação de uma informação, precisamos extrair tanto o **texto do link** quanto o **endereço de destino (URL)**.

### Código:
```python
from bs4 import BeautifulSoup

html_links = """
<div>
  <a href="https://noticia-original.com/estudo">Veja o estudo original</a>
  <a href="https://governo.exemplo.gov/nota">Nota oficial do ministério</a>
  <a href="https://redesocial.exemplo.com/post-viral">Postagem nas redes</a>
</div>
"""

soup = BeautifulSoup(html_links, "html.parser")

# Procura todas as tags <a> (hiperlinks)
links = soup.find_all("a")

for link in links:
    texto = link.get_text().strip()
    url_destino = link.get("href")  # Obtém o atributo href
    print(f"Texto: {texto} | URL: {url_destino}")
```

### Explicação do Código:
* No HTML, o endereço do link fica no atributo `href`: `<a href="DESTINO">TEXTO</a>`.
* `link.get("href")`: acessa o valor do atributo `href`. Se a tag não tiver o atributo, retorna `None` de forma segura sem travar o programa.

### Resultado Esperado:
```text
Texto: Veja o estudo original | URL: https://noticia-original.com/estudo
Texto: Nota oficial do ministério | URL: https://governo.exemplo.gov/nota
Texto: Postagem nas redes | URL: https://redesocial.exemplo.com/post-viral
```

### Exercício Rápido:
> Como você filtraria apenas os links cujo endereço comece com `"https://"`?

---

## Exemplo 4 — Data de Publicação

### Objetivo:
A data é a peça mais importante para investigar a ordem cronológica em que uma informação apareceu. Os sites costumam guardar a data na tag `<time>` ou em tags com classes especiais (como `class="data"`).

### Código:
```python
from bs4 import BeautifulSoup

html_data = """
<article>
  <h1>Descoberta arqueológica surpreende pesquisadores</h1>
  <time datetime="2026-09-10T14:30:00">10 de setembro de 2026</time>
</article>
"""

soup = BeautifulSoup(html_data, "html.parser")

tag_tempo = soup.find("time")

if tag_tempo:
    # Podemos pegar tanto o texto visível quanto o atributo datetime padronizado
    data_legivel = tag_tempo.get_text().strip()
    data_padrao = tag_tempo.get("datetime")
    print(f"Data legível: {data_legivel}")
    print(f"Data padronizada (datetime): {data_padrao}")
else:
    print("Data não encontrada na página.")
```

### Explicação do Código:
* `soup.find("time")`: busca a tag semântica de data.
* Sempre usamos `if tag_tempo:` para verificar se a tag realmente foi encontrada antes de chamar `.get_text()`, evitando erros se a página não tiver data explícita.
* O atributo `datetime` frequentemente contém a data no formato ISO (`AAAA-MM-DD`), excelente para ordenar no Python!

### Resultado Esperado:
```text
Data legível: 10 de setembro de 2026
Data padronizada (datetime): 2026-09-10T14:30:00
```

### Exercício Rápido:
> Em alguns sites, a data está em um parágrafo como `<p class="data-publicacao">11/09/2026</p>`. Como você usaria `soup.find("p", class_="data-publicacao")` para capturá-la?

---

## Exemplo 5 — Autor da Notícia

### Objetivo:
Identificar quem escreveu a publicação. Desinformações e fake news muitas vezes **não possuem autor identificado** ou usam nomes genéricos como "Redação" ou "Administrador".

### Código:
```python
from bs4 import BeautifulSoup

html_autor = """
<div class="meta-noticia">
  <span class="autor">Por: Carlos Eduardo Mendes</span>
  <span class="cargo">Jornalista Investigativo</span>
</div>
"""

soup = BeautifulSoup(html_autor, "html.parser")

# Buscamos a tag span que possui a classe 'autor'
tag_autor = soup.find("span", class_="autor")

if tag_autor:
    # Limpamos o prefixo "Por: " para isolar apenas o nome
    nome_autor = tag_autor.get_text().replace("Por:", "").strip()
    print(f"Autor identificado: {nome_autor}")
else:
    print("Autor não especificado.")
```

### Explicação do Código:
* No BeautifulSoup, para buscar por classe CSS usamos o parâmetro `class_` (com sublinhado no final, pois `class` é uma palavra reservada do Python).
* `.replace("Por:", "")`: remove a palavra "Por:" para termos um dado mais limpo.

### Resultado Esperado:
```text
Autor identificado: Carlos Eduardo Mendes
```

### Exercício Rápido:
> Se o autor estiver dentro de um link `<a class="author-name">Ana Lima</a>`, qual comando você utilizaria para extraí-lo?

---

## Exemplo 6 — Texto Completo da Notícia

### Objetivo:
Extrair o conteúdo dos parágrafos que compõem a reportagem para permitir comparações de texto ou buscas por termos suspeitos.

### Código:
```python
from bs4 import BeautifulSoup

html_corpo = """
<div class="corpo-noticia">
  <p>Uma mensagem alarmante começou a circular hoje em grupos de conversa.</p>
  <p>O texto alega falsamente que um novo imposto será cobrado a partir de amanhã.</p>
  <p>Órgãos oficiais e especialistas desmentiram a informação imediatamente.</p>
</div>
"""

soup = BeautifulSoup(html_corpo, "html.parser")

# Localizamos a área principal da notícia
area_noticia = soup.find("div", class_="corpo-noticia")

# Extraímos todos os parágrafos de dentro dessa área
paragrafos = area_noticia.find_all("p")

# Juntamos o texto de cada parágrafo com quebras de linha
texto_completo = "\n".join([p.get_text().strip() for p in paragrafos])

print("--- TEXTO DA NOTÍCIA EXTRAÍDO ---")
print(texto_completo)
```

### Explicação do Código:
* Primeiro encontramos a `div` que contém a matéria (`area_noticia`), para evitar pegar textos de rodapés, menus ou anúncios.
* Depois chamamos `find_all("p")` apenas dentro dessa área.
* `"\n".join(...)`: une todos os parágrafos em um único texto contínuo, separando-os por uma linha em branco.

### Resultado Esperado:
```text
--- TEXTO DA NOTÍCIA EXTRAÍDO ---
Uma mensagem alarmante começou a circular hoje em grupos de conversa.
O texto alega falsamente que um novo imposto será cobrado a partir de amanhã.
Órgãos oficiais e especialistas desmentiram a informação imediatamente.
```

### Exercício Rápido:
> Como contar quantas palavras existem no texto extraído usando `.split()` em Python?

---

👉 **Próximo passo:** [Aula 04 — Web Scraping Aplicado a Portais de Notícias](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/04-web-scraping-noticias.md)
