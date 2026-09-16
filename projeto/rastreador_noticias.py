"""
Mini Projeto Final: Rastreador de Notícias
Curso: Web Scraping e Rastreamento de Notícias / Fake News

Este programa demonstra como utilizar Web Scraping para coletar dados de
uma notícia suspeita, comparar com outras ocorrências encontradas na web,
organizar tudo cronologicamente e gerar um relatório de investigação.
"""

import sys
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# Assegura que caracteres no Windows sejam impressos sem erro
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class RastreadorNoticias:
    """
    Classe responsável por coletar, analisar e organizar
    ocorrências de notícias em ordem cronológica.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "RastreadorEducativo/1.0 (+https://github.com/exemplo-didatico)"
        }

    def extrair_dados_html(self, html_conteudo, url=""):
        """
        Analisa o HTML de uma página e extrai metadados principais.
        """
        soup = BeautifulSoup(html_conteudo, "html.parser")

        # 1. Título
        tag_titulo = soup.find("h1") or soup.find("title")
        titulo = tag_titulo.get_text().strip() if tag_titulo else "Título não identificado"

        # 2. Data de publicação
        tag_data = soup.find("time") or soup.find(class_=["data", "date", "publicado-em"])
        data_iso = "2099-12-31"
        data_legivel = "Data não identificada"
        
        if tag_data:
            dt_attr = tag_data.get("datetime")
            texto_data = tag_data.get_text().strip()
            if dt_attr:
                data_iso = dt_attr.split("T")[0]
                data_legivel = texto_data or data_iso
            else:
                data_legivel = texto_data

        # 3. Autor
        tag_autor = soup.find(class_=["autor", "author", "por", "byline"])
        autor = tag_autor.get_text().replace("Por:", "").replace("Por", "").strip() if tag_autor else "Autor não informado"

        # 4. Texto completo
        conteiner = soup.find("article") or soup.find(class_=["conteudo", "texto-materia"]) or soup
        paragrafos = [p.get_text().strip() for p in conteiner.find_all("p") if p.get_text().strip()]
        texto = "\n".join(paragrafos) if paragrafos else "Sem texto disponível"

        # 5. Links encontrados
        links = []
        for a in conteiner.find_all("a"):
            href = a.get("href")
            txt = a.get_text().strip()
            if href and (href.startswith("http://") or href.startswith("https://")):
                links.append({"texto": txt or "Link", "url": href})

        return {
            "titulo": titulo,
            "autor": autor,
            "data_legivel": data_legivel,
            "data_iso": data_iso,
            "url": url,
            "texto": texto,
            "links": links
        }

    def raspar_url(self, url):
        """
        Faz a requisição para uma URL da internet e extrai os dados.
        Retorna None caso ocorra erro de conexão.
        """
        try:
            resp = requests.get(url, headers=self.headers, timeout=8)
            resp.raise_for_status()
            return self.extrair_dados_html(resp.text, url=url)
        except Exception as e:
            print(f"[Aviso] Não foi possível acessar '{url}': {e}")
            return None

    def gerar_relatorio(self, noticia_foco, outras_ocorrencias):
        """
        Gera a estrutura de relatório comparativo solicitada:
        1. Notícia analisada
        2. Outras ocorrências
        3. Linha do tempo cronológica
        """
        print("\n" + "=" * 75)
        print("NOTICIA ANALISADA")
        print("=" * 75)
        print(f"Titulo: {noticia_foco['titulo']}")
        print(f"Data  : {noticia_foco['data_legivel']}")
        print(f"Autor : {noticia_foco['autor']}")
        print(f"URL   : {noticia_foco['url']}")
        print(f"Texto (resumo): {noticia_foco['texto'][:180]}...")
        print(f"Links encontrados no texto: {len(noticia_foco['links'])}")

        print("\n" + "=" * 75)
        print("OUTRAS OCORRENCIAS ENCONTRADAS")
        print("=" * 75)

        for i, item in enumerate(outras_ocorrencias, start=1):
            print(f"{i}. {item.get('site_nome', 'Site Externo')}")
            print(f"   Data: {item['data_legivel']}")
            print(f"   URL : {item['url']}")
            print(f"   Titulo: {item['titulo']}")
            print()

        # Unimos todas as notícias para montar a linha do tempo cronológica
        todas = [noticia_foco] + outras_ocorrencias
        todas_ordenadas = sorted(todas, key=lambda x: x.get("data_iso", "2099-12-31"))

        print("=" * 75)
        print("LINHA DO TEMPO CRONOLOGICA (DA MAIS ANTIGA PARA A MAIS RECENTE):")
        print("=" * 75)

        for idx, item in enumerate(todas_ordenadas):
            identificador = "🥇 [PRIMEIRO REGISTRO ENCONTRADO]" if idx == 0 else f"↓ [Ocorrência {idx+1}]"
            print(f"{item['data_legivel']} ---> {item.get('site_nome', item['url'])}  {identificador}")
            print(f"   Titulo: \"{item['titulo']}\"")
            print(f"   URL   : {item['url']}")
            if idx < len(todas_ordenadas) - 1:
                print("   |")
                print("   v")

        print("\n" + "=" * 75)
        print("[!] PARECER METODOLOGICO SOBRE DESINFORMACAO:")
        print("-" * 75)
        primeira = todas_ordenadas[0]
        print(f"* Ocorrência mais antiga rastreada: {primeira['data_legivel']} ({primeira['url']}).")
        print("* ATENÇÃO: O Web Scraping é uma ferramenta para COLETAR evidências.")
        print("* A publicação mais antiga encontrada NÃO prova a autoria original da notícia,")
        print("  pois a mensagem pode ter sido gerada em fontes privadas, apagada de outras")
        print("  redes ou republicada com data alterada.")
        print("* Próximo passo obrigatório: checar fontes primárias e agências de checagem!")
        print("=" * 75)


def modo_demonstracao():
    """
    Executa uma demonstração guiada e realista com páginas fictícias,
    sem depender de conexão externa instável.
    """
    rastreador = RastreadorNoticias()

    # Notícia que motivou a denúncia
    html_foco = """
    <article>
      <h1>Suposta descoberta de cura milagrosa viraliza nas redes sociais</h1>
      <span class="autor">Por: Redação Curiosa</span>
      <time datetime="2026-09-13">13/09/2026</time>
      <div class="conteudo">
        <p>Uma mensagem compartilhada mais de 100 mil vezes alega que cientistas descobriram um composto caseiro revolucionário.</p>
        <p>A mensagem não cita nenhum hospital de pesquisa oficial.</p>
        <a href="https://blog-exemplo.com/materia-anterior">Veja a publicação anterior</a>
      </div>
    </article>
    """
    noticia_foco = rastreador.extrair_dados_html(html_foco, url="https://redesocial-viral.com/post/987123")
    noticia_foco["site_nome"] = "Rede Social Viral (Link Denunciado)"

    # Outras duas ocorrências achadas na internet sobre o mesmo caso
    html_site_a = """
    <article>
      <h1>Receita milagrosa caseira promete imunidade total</h1>
      <span class="autor">Desconhecido</span>
      <time datetime="2026-09-09">09/09/2026</time>
      <p>Texto inicial do boato em fórum...</p>
    </article>
    """
    item_a = rastreador.extrair_dados_html(html_site_a, url="https://forum-alternativo.net/topico/341")
    item_a["site_nome"] = "Site A (Fórum Alternativo)"

    html_site_b = """
    <article>
      <h1>Alerta de Saúde: Boato sobre receita milagrosa é perigoso</h1>
      <span class="autor">Dr. Roberto Lima</span>
      <time datetime="2026-09-11">11/09/2026</time>
      <p>Médicos alertam para os riscos do uso do composto caseiro...</p>
    </article>
    """
    item_b = rastreador.extrair_dados_html(html_site_b, url="https://portal-medicina-oficial.org/alertas/boato-receita")
    item_b["site_nome"] = "Site B (Portal de Saúde Oficial)"

    outras_ocorrencias = [item_a, item_b]

    rastreador.gerar_relatorio(noticia_foco, outras_ocorrencias)


if __name__ == "__main__":
    print("Iniciando Rastreador de Notícias...")
    modo_demonstracao()
