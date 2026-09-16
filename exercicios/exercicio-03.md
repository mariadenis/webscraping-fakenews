# Exercício 03 — Extraindo Todas as Manchetes

## Objetivo
Coletar todas as manchetes de uma página ou portal jornalístico (geralmente estruturadas em tags `<h2>` ou `<h3>`), exibindo-as em uma lista numerada.

---

## Instruções
1. Crie ou acesse o HTML de um portal de notícias.
2. Utilize `soup.find_all("h2")` para capturar os títulos das matérias.
3. Use a função `enumerate()` do Python para numerar as manchetes de 1 até o total encontrado.
4. Garanta que o texto esteja limpo, sem espaços extras.

---

## Código Inicial

```python
from bs4 import BeautifulSoup

html_portal = """
<section class="noticias-do-dia">
  <h2>Novo telescópio espacial envia primeiras imagens em alta definição</h2>
  <h2>Previsão do tempo indica chegada de frente fria no fim de semana</h2>
  <h2>Pesquisa revela hábito de leitura de notícias dos jovens brasileiros</h2>
  <h2>Ministério emite alerta sobre golpe financeiro no aplicativo de mensagens</h2>
</section>
"""

soup = BeautifulSoup(html_portal, "html.parser")

# COMPLETE AQUI: Colete todas as manchetes da tag <h2>
# lista_manchetes = ...

# COMPLETE AQUI: Imprima cada manchete numerada
# for numero, tag in enumerate(..., start=1):
#     print(...)
```

---

## Dica
* O método `.strip()` é fundamental para remover quebras de linha e espaços antes e depois do texto.
* Se quiser contar quantas manchetes foram encontradas, basta usar `len(lista_manchetes)`.

---

## Solução Comentada

```python
from bs4 import BeautifulSoup

html_portal = """
<section class="noticias-do-dia">
  <h2>Novo telescópio espacial envia primeiras imagens em alta definição</h2>
  <h2>Previsão do tempo indica chegada de frente fria no fim de semana</h2>
  <h2>Pesquisa revela hábito de leitura de notícias dos jovens brasileiros</h2>
  <h2>Ministério emite alerta sobre golpe financeiro no aplicativo de mensagens</h2>
</section>
"""

soup = BeautifulSoup(html_portal, "html.parser")

# 1. Buscamos todas as ocorrências de <h2>
manchetes = soup.find_all("h2")

print("=" * 60)
print(f"TOTAL DE MANCHETES CAPTURADAS: {len(manchetes)}")
print("=" * 60)

# 2. Percorremos e imprimimos cada uma numerada
for numero, tag in enumerate(manchetes, start=1):
    titulo = tag.get_text().strip()
    print(f"[{numero:02d}] {titulo}")

print("=" * 60)
```
