# Exercício 02 — Encontrando Todos os Links da Página

## Objetivo
Criar um programa em Python que localize todas as tags de hiperlink (`<a>`) em uma página, exibindo na tela o texto âncora do link e a URL de destino (`href`).

---

## Instruções
1. Importe as bibliotecas necessárias.
2. Acesse a página ou utilize um bloco HTML com links.
3. Use o método `soup.find_all("a")` para obter todas as tags de link.
4. Crie um loop `for` para percorrer cada link.
5. Para cada link, extraia o texto com `.get_text()` e o atributo `href` com `.get("href")`.

---

## Código Inicial

```python
from bs4 import BeautifulSoup

# Exemplo de HTML com links de fontes de notícias
html_teste = """
<nav>
  <a href="https://portal-noticias.org">Página Inicial</a>
  <a href="https://portal-noticias.org/checagem">Agência de Checagem</a>
  <a href="https://portal-noticias.org/contato">Fale com a Redação</a>
</nav>
"""

soup = BeautifulSoup(html_teste, "html.parser")

# COMPLETE AQUI: Encontre todos os links
# links = ...

# COMPLETE AQUI: Percorra a lista e exiba o texto e o href de cada um
# for link in links:
#     ...
```

---

## Dica
* Lembre-se que `soup.find()` retorna apenas um elemento, enquanto `soup.find_all()` retorna uma **lista** com todos os elementos encontrados.
* Para pegar o valor de um atributo HTML (como `href="https://..."`), use `link.get("href")`.

---

## Solução Comentada

```python
from bs4 import BeautifulSoup

html_teste = """
<nav>
  <a href="https://portal-noticias.org">Página Inicial</a>
  <a href="https://portal-noticias.org/checagem">Agência de Checagem</a>
  <a href="https://portal-noticias.org/contato">Fale com a Redação</a>
</nav>
"""

soup = BeautifulSoup(html_teste, "html.parser")

# Encontra todas as tags <a> da página
todos_os_links = soup.find_all("a")

print(f"Foram encontrados {len(todos_os_links)} links:")
print("-" * 50)

# Percorremos cada link e extraímos seus dados
for i, link in enumerate(todos_os_links, start=1):
    texto = link.get_text().strip()
    destino = link.get("href")
    
    print(f"Link {i}:")
    print(f"  Texto  : {texto}")
    print(f"  Destino: {destino}")
    print("-" * 50)
```
