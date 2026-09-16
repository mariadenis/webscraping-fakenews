# Web Scraping e Investigação Digital de Notícias

> ### Pergunta Principal:
> ## **Como rastrear a origem de uma fake news ou de uma notícia verdadeira usando Web Scraping?**

Bem-vindo(a) ao material didático e prático de **Web Scraping voltado para a investigação de notícias e circulação de informações na internet**!

Este repositório foi construído especialmente para **iniciantes** que nunca tiveram contato com programação ou raspagem de dados. Aqui você aprenderá, de maneira simples e progressiva, como usar **Python** para coletar dados de páginas web, comparar ocorrências de uma mesma matéria e construir linhas do tempo investigativas.

---

## 🧭 Como uma Notícia Circula na Web?

Quando uma informação surge e viraliza, ela se espalha em cadeia por diferentes veículos:

```text
Fonte A → publica em 10/09 (ex.: fórum ou blog desconhecido)
        ↓
Fonte B → reproduz em 11/09 (ex.: portal regional de notícias)
        ↓
Fonte C → reproduz em 12/09 (ex.: portal de grande audiência)
        ↓
Postagem em rede social → 13/09 (viralização com links e prints)
```

O **Web Scraping** permite visitar todas essas fontes automaticamente, recolher os títulos, datas, autores e textos, e organizar uma ordem cronológica dos fatos.

> [!IMPORTANT]
> ### Princípio Fundamental da Investigação
> **"A publicação mais antiga encontrada não é necessariamente a origem verdadeira da informação."**
> 
> Uma postagem mais antiga pode ter sido deletada, a informação pode ter nascido fora da internet (como em conversas privadas ou no rádio) ou pertencer a um site não indexado. O Web Scraping é uma ferramenta para **coletar evidências**, não um detector automático de veracidade.

---

## 🌐 O que é Web Scraping?

> **Web Scraping** é a técnica de coletar informações de páginas da internet automaticamente por meio de programas de computador, sem a necessidade de copiar e colar dados manualmente.

Em vez de abrir 50 notícias uma a uma no navegador:
1. O seu código Python faz uma **requisição HTTP** para a página;
2. Ele recebe o código **HTML** (a estrutura da página);
3. Um **parser** (BeautifulSoup) localiza as tags de título (`<h1>`), links (`<a>`), datas (`<time>`) e parágrafos (`<p>`);
4. Os dados são salvos de forma organizada para você analisar.

```text
Página da internet
       ↓
    HTML
       ↓
Programa Python
       ↓
Extrai informações
       ↓
Dados organizados
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.8+** (Linguagem de programação limpa e amigável)
* **Requests** (Biblioteca para conectar e baixar páginas da internet)
* **BeautifulSoup4** (Biblioteca para navegar pelo HTML e extrair os dados desejados)

---

## 🚀 Instalação e Preparação

Clone ou abra a pasta no terminal e instale as dependências:

```bash
pip install -r requirements.txt
```

*(Se o comando `pip` não for reconhecido no Windows, use `python -m pip install -r requirements.txt`)*

---

## 📚 Estrutura do Curso e das Aulas

O material está dividido de forma didática e progressiva:

| Aula | Conteúdo | Link |
| :--- | :--- | :--- |
| **Aula 01** | O que é Web Scraping, fluxo de notícias, conceitos de HTML e HTTP | [Ler Aula 01](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/01-o-que-e-web-scraping.md) |
| **Aula 02** | Primeiro código com `requests` e `BeautifulSoup` linha por linha | [Ler Aula 02](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/02-primeiro-web-scraping.md) |
| **Aula 03** | Aprendendo a extrair Título, Manchetes, Links, Datas, Autores e Textos | [Ler Aula 03](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/03-extraindo-dados.md) |
| **Aula 04** | Web Scraping aplicado à estrutura real de portais de notícias | [Ler Aula 04](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/04-web-scraping-noticias.md) |
| **Aula 05** | Rastreando Fake News: da coleta à linha do tempo, ética e limites | [Ler Aula 05](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/05-rastreando-fake-news.md) |

---

## 💻 Exemplos em Código Python (`exemplos/`)

Códigos prontos, comentados em detalhes e preparados para rodar no seu computador:

1. [`exemplos/01_titulo.py`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/01_titulo.py): Faz download de uma página e exibe seu título principal.
2. [`exemplos/02_links.py`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/02_links.py): Coleta todos os links, textos âncoras e resolve caminhos relativos.
3. [`exemplos/03_manchetes.py`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/03_manchetes.py): Coleta todas as manchetes de um feed de notícias.
4. [`exemplos/04_dados_noticia.py`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/04_dados_noticia.py): Estrutura dados completos de uma reportagem (Título, Data, Autor, Corpo e Links).
5. [`exemplos/05_rastreador.py`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/05_rastreador.py): Compara matérias fictícias em ordem cronológica e monta uma linha do tempo.

Execute qualquer exemplo com:
```bash
python exemplos/01_titulo.py
```

---

## 📝 Exercícios Práticos (`exercicios/`)

Cada exercício conta com **Objetivo**, **Instruções**, **Código Inicial**, **Dicas** e **Solução Comentada**:

* [Exercício 01 — Capturando o Título](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-01.md)
* [Exercício 02 — Encontrando Todos os Links](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-02.md)
* [Exercício 03 — Extraindo Todas as Manchetes](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-03.md)
* [Exercício 04 — Manchete + Link Combinados](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-04.md)
* [Exercício 05 — Tabela com Várias Notícias (Título \| Data \| Link)](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-05.md)
* [Exercício Final — Filtragem por Palavra-Chave e Comparação de Fontes](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios/exercicio-final.md)

---

## 🏆 Mini-Projeto Final: Rastreador de Notícias (`projeto/`)

O diretório [`projeto/`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/projeto/) contém um programa modular que:
* Recebe uma notícia de foco e outras ocorrências na web;
* Extrai metadados completos de cada uma;
* Ordena as ocorrências por data de publicação;
* Destaca a primeira publicação encontrada e renderiza a linha do tempo no terminal;
* Exibe o parecer metodológico de checagem.

Para rodar o projeto:
```bash
python projeto/rastreador_noticias.py
```

---

## 🛑 O que o Web Scraping NÃO Faz

> **Web Scraping não é um detector de Fake News.**

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     COLETA      │  ───► │     ANÁLISE     │  ───► │   VERIFICAÇÃO   │  ───► │    CONCLUSÃO    │
│  (Web Scraping) │       │ (Linha do Tempo)│       │ (Fontes Oficiais)│      │  (Fato ou Boato)│
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

* **Ele coleta dados, não julga:** O computador não sabe se uma afirmação médica ou política é real.
* **Datas podem ser republicadas:** Um boato antigo pode reaparecer com uma data recente sem que o texto seja novo.
* **Páginas dinâmicas ou apagadas:** Informações podem estar protegidas por JavaScript ou já terem sido removidas do ar.
* **Necessidade humana:** Toda investigação precisa de checadores humanos consultando fontes primárias (diários oficiais, especialistas e agências de checagem).

---

## ⚖️ Ética e Boas Práticas

Ao fazer Web Scraping, lembre-se:
1. **Respeite o `robots.txt`** dos sites visitados;
2. **Não sobrecarregue os servidores:** aplique intervalos entre requisições;
3. **Não acesse áreas restritas** nem tente burlar senhas ou CAPTCHAs;
4. **Respeite a privacidade:** não raspe dados pessoais desnecessariamente;
5. **Utilize páginas públicas e apropriadas** para o aprendizado e estudo de jornalismo de dados.
