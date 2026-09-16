"""
Exemplo 03 — Como extrair manchetes de uma página ou portal
Curso: Web Scraping e Rastreamento de Notícias / Fake News
"""

from bs4 import BeautifulSoup

# Simulamos a página inicial de um portal de notícias
pagina_portal_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Portal Diário de Notícias</title>
</head>
<body>
  <header>
    <h1>Portal Diário de Notícias</h1>
  </header>

  <main>
    <section class="destaques">
      <h2>Governo anuncia novo plano para transição energética sustentável</h2>
      <p class="resumo">Medidas incluem incentivos fiscais para energia solar e eólica.</p>
    </section>

    <section class="geral">
      <h2>Atenção: Boato sobre bloqueio de contas bancárias volta a circular</h2>
      <p class="resumo">Banco Central emite nota alertando que mensagens são falsas.</p>

      <h2>Estudo revela aumento no número de leitores digitais no país</h2>
      <p class="resumo">Pesquisa aponta preferência por notícias no celular.</p>

      <h2>Equipe de resgate encontra animais perdidos após tempestade</h2>
      <p class="resumo">Operação comunitária durou mais de 48 horas.</p>
    </section>
  </main>
</body>
</html>
"""

# Inicializamos o parser
soup = BeautifulSoup(pagina_portal_html, "html.parser")

# Buscamos todas as manchetes na tag <h2>
manchetes = soup.find_all("h2")

print("=" * 65)
print(f"PORTAL DE NOTÍCIAS — {len(manchetes)} MANCHETES CAPTURADAS")
print("=" * 65)

for i, tag in enumerate(manchetes, start=1):
    texto_manchete = tag.get_text().strip()
    
    # Destacamos se a manchete contém palavras de alerta
    alerta = " [SUSPEITA / ALERTA]" if "boato" in texto_manchete.lower() else ""
    
    print(f"[{i:02d}] {texto_manchete}{alerta}")

print("=" * 65)
print("Dica: Em sites reais, você pode filtrar manchetes por palavras-chave")
print("para monitorar temas específicos ou notícias virais!")
