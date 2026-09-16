# Aula 04 — Web Scraping Aplicado a Notícias

Na aula anterior aprendemos a extrair cada elemento isoladamente: títulos, links, datas, autores e textos. Agora, vamos juntar essas peças para construir um **extrator completo de matérias jornalísticas**.

---

## 1. Como Portais de Notícias se Estruturam

Quase todos os sites de notícias modernos seguem uma estrutura HTML parecida:

```html
<article>
  <!-- Cabeçalho com Título e Metadados -->
  <header>
    <h1 class="titulo">Manchete Principal da Matéria</h1>
    <div class="meta">
      <span class="autor">Por Ana Souza</span>
      <time datetime="2026-09-12">12 de setembro de 2026</time>
    </div>
  </header>

  <!-- Conteúdo da Notícia -->
  <div class="conteudo">
    <p>Primeiro parágrafo com a notícia...</p>
    <p>Segundo parágrafo com citações e fontes...</p>
    <a href="https://fonte.com/documento">Documento de referência</a>
  </div>
</article>
```

Em um trabalho de investigação, nós queremos capturar todos esses dados de forma organizada para alimentar uma tabela comparativa.

---

## 2. A Importância dos "Fallbacks" (Valores Padrão)

Na internet real, muitas páginas não seguem um padrão perfeito. Uma notícia pode **não ter autor indicado**, ou a data pode estar em um formato diferente.

Se o seu código assumir que toda página sempre terá um autor e tentar chamar `.get_text()` em algo inexistente, o Python vai gerar um erro:
```text
AttributeError: 'NoneType' object has no attribute 'get_text'
```

Para evitar isso, criamos funções seguras que verificam a existência da tag antes de ler seu conteúdo:

```python
tag_autor = soup.find("span", class_="autor")
autor = tag_autor.get_text().strip() if tag_autor else "Autor não informado"
```

---

## 3. Código Completo: Extrator de Notícia

Veja como estruturar uma função que recebe uma página e devolve um dicionário Python com todos os dados:

```python
from bs4 import BeautifulSoup

def extrair_dados_noticia(html_conteudo, url_origem=""):
    """
    Recebe o código HTML de uma página e devolve os dados
    da notícia organizados em um dicionário.
    """
    soup = BeautifulSoup(html_conteudo, "html.parser")
    
    # 1. Título (procura h1 ou a tag title)
    tag_titulo = soup.find("h1") or soup.find("title")
    titulo = tag_titulo.get_text().strip() if tag_titulo else "Título não encontrado"
    
    # 2. Data de publicação (busca tag <time> ou classes comuns)
    tag_data = soup.find("time") or soup.find(class_=["data", "date", "publicado-em"])
    if tag_data:
        # Se tiver o atributo datetime usamos ele, senão o texto visível
        data = tag_data.get("datetime") or tag_data.get_text().strip()
    else:
        data = "Data não identificada"
        
    # 3. Autor da publicação
    tag_autor = soup.find(class_=["autor", "author", "por", "byline"])
    autor = tag_autor.get_text().replace("Por:", "").replace("Por", "").strip() if tag_autor else "Autor não informado"
    
    # 4. Corpo do texto (parágrafos)
    # Procuramos dentro da tag <article> ou no corpo geral
    conteiner = soup.find("article") or soup.find(class_=["conteudo", "texto-noticia", "post-body"]) or soup
    paragrafos = [p.get_text().strip() for p in conteiner.find_all("p") if p.get_text().strip()]
    texto_completo = "\n".join(paragrafos) if paragrafos else "Sem texto disponível"
    
    # 5. Links citados no texto da matéria
    links = []
    for a in conteiner.find_all("a"):
        href = a.get("href")
        texto_link = a.get_text().strip()
        if href and href.startswith("http"):
            links.append({"texto": texto_link or "Link", "url": href})
            
    return {
        "url": url_origem,
        "titulo": titulo,
        "data": data,
        "autor": autor,
        "texto": texto_completo,
        "links_citados": links
    }

# --- TESTE PRÁTICO COM UMA NOTÍCIA SIMULADA ---
html_exemplo = """
<article>
  <h1>Descoberta promete revolucionar baterias elétricas</h1>
  <div class="meta">
    <span class="autor">Por: Mariana Rocha</span>
    <time datetime="2026-09-11">11/09/2026</time>
  </div>
  <div class="conteudo">
    <p>Engenheiros apresentaram um protótipo com autonomia três vezes maior.</p>
    <p>O anúncio completo foi feito no simpósio de energia renovável.</p>
    <p>Mais detalhes podem ser vistos no <a href="https://instituto-energia.org/artigo">artigo oficial</a>.</p>
  </div>
</article>
"""

dados = extrair_dados_noticia(html_exemplo, url_origem="https://tecnologia-exemplo.com/noticia-bateria")

print("=" * 50)
print("DADOS COLETADOS DA NOTÍCIA:")
print("=" * 50)
print(f"Título: {dados['titulo']}")
print(f"Data:   {dados['data']}")
print(f"Autor:  {dados['autor']}")
print(f"URL:    {dados['url']}")
print(f"Links encontrados: {len(dados['links_citados'])}")
for link in dados['links_citados']:
    print(f"  └─ {link['texto']} -> {link['url']}")
print("-" * 50)
print("Primeiro parágrafo do texto:")
print(dados['texto'].splitlines()[0])
print("=" * 50)
```

---

## 4. O que Podemos Fazer com Esses Dados?

Quando você consegue transformar uma página em uma estrutura padronizada (um dicionário Python com `titulo`, `data`, `autor`, etc.), você abre portas para análises valiosas:

1. **Comparar versões:** Colocar o texto de duas matérias lado a lado para ver se uma copiou a outra integralmente.
2. **Checar citações:** Seguir os `links_citados` para ver se eles apontam para documentos legítimos ou para outros blogs sem credibilidade.
3. **Mapear a cronologia:** Se tivermos 5 notícias sobre o mesmo tema, podemos ordenar o dicionário pelo campo `data` e descobrir qual apareceu primeiro no tempo.

Esse é o código que você encontra pronto para rodar em:
👉 [exemplos/04_dados_noticia.py](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/04_dados_noticia.py)

---

👉 **Próximo passo:** [Aula 05 — Rastreando Fake News: Da Coleta à Linha do Tempo](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/05-rastreando-fake-news.md)
