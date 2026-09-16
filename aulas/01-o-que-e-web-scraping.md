# Aula 01 — O que é Web Scraping?

## Como rastrear a origem de uma fake news ou de uma notícia verdadeira usando Web Scraping?

Quando uma notícia ou boato começa a circular pela internet, raramente ele fica restrito a um único lugar. Em pouco tempo, dezenas ou centenas de páginas publicam versões muito parecidas daquela mesma história.

Observe como uma informação costuma se espalhar:

```text
Fonte A → publica em 10/09 (ex.: um blog desconhecido ou fórum)
        ↓
Fonte B → reproduz em 11/09 (ex.: um portal regional de notícias)
        ↓
Fonte C → reproduz em 12/09 (ex.: um agregador de notícias)
        ↓
Postagem em rede social → 13/09 (viralização com links e imagens)
```

Olhando para essa sequência, surge uma pergunta natural: **quem falou sobre isso primeiro? Onde tudo começou?**

É aqui que entra o **Web Scraping**. Essa técnica permite acessar automaticamente dezenas de páginas, coletar títulos, datas de publicação, autores e textos, para que você possa comparar as informações e montar um quebra-cabeça investigativo.

---

> [!IMPORTANT]
> ### Regra de Ouro da Investigação Digital
> **A publicação mais antiga encontrada NÃO é necessariamente a origem verdadeira da informação!**
> 
> * Pode existir uma postagem anterior que já foi **apagada**.
> * A informação pode ter surgido **fora da internet** (em uma conversa de rádio, num panfleto, num grupo fechado de mensagens).
> * O site mais antigo pode ter apenas copiado de uma fonte que o seu programa não encontrou.
> 
> O Web Scraping **não é um detector mágico de mentiras**. Ele é uma ferramenta de **coleta e organização de evidências** que você precisará checar em fontes confiáveis.

---

## 1. O que é Web Scraping de forma simples?

> **Web Scraping** (em português, *raspagem de dados na web*) é uma técnica utilizada para **coletar informações de páginas da internet automaticamente**, em vez de ter que copiar e colar os dados manualmente um por um.

Imagine que você precise levantar os títulos e datas das últimas 200 notícias sobre determinado assunto.

* **Modo manual:** você abre o navegador, entra em cada site, copia o título, cola em uma planilha, volta, copia a data, cola na planilha... Isso levaria horas e causaria cansaço.
* **Com Web Scraping:** você escreve um pequeno programa em Python. Ele visita as 200 páginas em poucos segundos, lê o código da página, separa o título e a data e salva tudo organizado em uma tabela.

Veja o fluxo visual do processo:

```text
  ┌─────────────────────────┐
  │   Página da Internet    │ (O que você vê no navegador)
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │       Código HTML       │ (A estrutura do texto e dos dados)
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │     Programa Python     │ (Faz o download e analisa o código)
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │   Extrai Informações    │ (Localiza títulos, links, autores, datas)
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │     Dados Organizados   │ (Prontos para análise e linha do tempo)
  └─────────────────────────┘
```

---

## 2. Conceitos Básicos Essenciais

Para conseguir fazer scraping sem medo, você só precisa entender alguns conceitos fundamentais da internet:

### A. O que é uma URL?
A **URL** (*Uniform Resource Locator*) é simplesmente o endereço de uma página na web.  
Exemplo: `https://exemplo.com/noticias/caso-123.html`

### B. O que é uma Requisição HTTP?
Quando você digita uma URL no seu navegador e aperta `Enter`, seu computador envia um pedido ao computador onde o site está guardado (o servidor). Esse pedido se chama **requisição HTTP** (*Request*). O servidor responde enviando o conteúdo da página (*Response*).

Fazer Web Scraping significa pedir ao Python para enviar essa mesma requisição e receber o conteúdo da página, sem precisar abrir uma janela visual de navegador.

### C. O que é HTML?
**HTML** (*HyperText Markup Language*) é a linguagem usada para construir e estruturar as páginas da internet. Ele não é uma linguagem de programação, e sim uma linguagem de marcação.

Pense no HTML como o "esqueleto" de uma página web. Ele diz ao navegador onde fica cada parágrafo, título, imagem ou link.

### D. O que são Tags HTML?
No HTML, tudo é marcado usando **tags** envolvidas por sinais de menor e maior (`<` e `>`). A maioria das tags tem uma abertura e um fechamento (com uma barra `/`):

* `<h1>Notícia Importante</h1>` → Título principal da página.
* `<h2>Subtítulo ou Manchete</h2>` → Título secundário.
* `<p>Este é um parágrafo com o texto da notícia.</p>` → Parágrafo comum.
* `<a href="https://site.com">Clique aqui</a>` → Um link que leva a outra página.

| Tag | Para que serve? | Exemplo |
| :--- | :--- | :--- |
| `<h1>` | Título de nível 1 (geralmente o título da notícia) | `<h1>Vacina é aprovada</h1>` |
| `<h2>`, `<h3>` | Subtítulos ou manchetes secundárias | `<h2>Especialistas comentam resultado</h2>` |
| `<p>` | Parágrafos de texto comum | `<p>Na manhã de ontem, pesquisadores...</p>` |
| `<a>` | Links que apontam para outras páginas | `<a href="/outra-pagina">Leia mais</a>` |
| `<time>` | Tag semântica usada em muitos sites para datas | `<time datetime="2026-09-10">10 de Setembro</time>` |
| `<span>` | Pequenos trechos de texto inline (ex: nome de autor) | `<span class="autor">Maria Silva</span>` |

### E. O que são Atributos?
Atributos são informações adicionais colocadas dentro da tag de abertura.  
No exemplo `<a href="https://noticia.com/texto">Link</a>`:
* `href` é o atributo que guarda o endereço de destino.
* `class` e `id` são atributos comuns usados para dar estilo ou identificar elementos específicos na página (ex: `<h1 class="titulo-noticia">`).

### F. O que é um Parser?
Quando o Python baixa o HTML de uma página, ele recebe apenas um bloco gigante de texto cru. O **Parser** (analisador) é o mecanismo que lê esse texto, entende onde cada tag abre e fecha, e transforma o HTML em uma árvore de objetos fácil de pesquisar (por exemplo: "encontre a tag `<h1>`" ou "encontre todos os links `<a>`").

Na próxima aula, vamos usar o **BeautifulSoup**, que é o parser mais popular e amigável para iniciantes em Python!

---

## Resumo da Aula 01

1. Web Scraping coleta dados de páginas automaticamente para você não ter que copiar à mão.
2. É uma ferramenta de **investigação e coleta de evidências**, não um detector de verdades.
3. Para fazer scraping, enviamos uma requisição HTTP, baixamos o HTML e usamos um parser para localizar tags como `<h1>`, `<p>`, `<a>` e `<time>`.
4. A data mais antiga que encontrarmos nos dá pistas de como o boato circulou, mas ainda precisamos checar fontes confiáveis.

👉 **Próximo passo:** [Aula 02 — Meu Primeiro Web Scraping](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/02-primeiro-web-scraping.md)
