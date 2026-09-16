# Aula 05 — Rastreando Fake News: Da Coleta à Linha do Tempo

Chegamos ao ponto central do nosso estudo:

> **Como rastrear a origem de uma fake news ou de uma notícia verdadeira usando Web Scraping?**

Nesta aula, conectaremos todas as técnicas de scraping aprendidas até aqui a uma metodologia sólida de investigação de informação online.

---

## 1. O Fluxo Completo de Investigação

Quando surge uma alegação viral ou suspeita, nós nunca tiramos conclusões com base em um único link. Em vez disso, aplicamos o seguinte fluxo:

```text
       ┌─────────────────────────────┐
       │      Notícia Suspeita       │ (Um link compartilhado em redes)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │     Coletar Informações     │ (Título, data, autor, texto, links citados)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │ Encontrar Páginas Parecidas │ (Buscar trechos do texto em outros sites)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │    Coletar URLs e Datas     │ (Fazer scraping de todas as páginas achadas)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │     Comparar Conteúdos      │ (Ver semelhanças nos textos e frases)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │  Organizar Cronologicamente │ (Ordenar da data mais antiga à mais recente)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │  Identificar Ocorrência     │ (Qual foi o primeiro registro localizado?)
       │        Mais Antiga          │
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │  Investigar Fontes Citadas  │ (Seguir os links originais e documentos)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │   Verificar em Fontes       │ (Consultar agências de checagem e diários oficiais)
       │        Confiáveis           │
       └─────────────────────────────┘
```

---

## 2. Exemplo Prático com Notícias Fictícias

Para entender o processo sem depender de links externos instáveis, vamos trabalhar com um cenário fictício:

Um boato sobre uma "descoberta revolucionária" começou a circular. Nosso programa fez a raspagem em três páginas diferentes que publicaram a matéria:

* **Site A:** Título *"Nova tecnologia promete energia infinita"*, Data: `2026-09-10`
* **Site B:** Título *"Cientistas descobrem fórmula de energia infinita"*, Data: `2026-09-11`
* **Site C:** Título *"Nova tecnologia promete energia infinita: entenda o caso"*, Data: `2026-09-13`

### Tabela Organizada pelo Programa:

| Data       | Site   | Título                                               | Status da Circulação |
| :--------- | :----- | :--------------------------------------------------- | :------------------- |
| **10/09/2026** | Site A | Nova tecnologia promete energia infinita             | 🥇 Ocorrência mais antiga |
| **11/09/2026** | Site B | Cientistas descobrem fórmula de energia infinita     | 🥈 Reprodução 1 dia depois |
| **13/09/2026** | Site C | Nova tecnologia promete energia infinita: entenda... | 🥉 Viralização tardia |

### Linha do Tempo Gerada:

```text
10/09/2026 ── Site A (Possível propagador inicial na web)
     │
     ▼
11/09/2026 ── Site B (Reproduziu com pequena alteração de título)
     │
     ▼
13/09/2026 ── Site C (Portal maior que republicou o boato já viral)
```

O código que implementa essa lógica completa de coleta, ordenação por datas e geração de linha do tempo está disponível em:  
👉 [exemplos/05_rastreador.py](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/05_rastreador.py)

---

## 3. Web Scraping NÃO é um Detector de Fake News

Esta é a lição mais importante de todo o material:

> **Web Scraping não consegue determinar sozinho se uma notícia é verdadeira ou falsa.**  
> Ele é uma ferramenta de **coleta e automação**, não um árbitro da verdade.

Entenda as razões:

1. **A publicação mais antiga encontrada não garante que aquela seja a fonte original:**
   * O autor original pode ter publicado em uma rede social fechada (como grupos de mensagens), e um blog só copiou dias depois.
   * A postagem original mais antiga pode ter sido **apagada** pelo autor após repercussão negativa.
   * O seu crawler de scraping pode simplesmente não ter encontrado todas as páginas existentes.

2. **Datas podem ser manipuladas ou imprecisas:**
   * Alguns sites alteram a data para parecerem mais novos ou mais antigos.
   * Uma notícia antiga e verdadeira de 2015 pode ser republicada hoje sem data, fazendo as pessoas acreditarem que é um fato recente (descontextualização).

3. **Sites dinâmicos e páginas removidas:**
   * Algumas páginas usam JavaScript pesado que não é carregado com um simples `requests.get()`.
   * Links quebram ou saem do ar (*Link Rot*).

### O Papel do Analista Humano:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     COLETA      │       │     ANÁLISE     │       │   VERIFICAÇÃO   │       │    CONCLUSÃO    │
│  (Web Scraping) │  ───► │  (Linha do      │  ───► │  (Consulta a    │  ───► │ (Determinar se  │
│                 │       │   Tempo / Datas)│       │   Especialistas)│       │   é boato/fato) │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

O Web Scraping faz a **COLETA** rapidamente. Cabe a você fazer a **ANÁLISE**, consultar fontes primárias para a **VERIFICAÇÃO** e só então chegar a uma **CONCLUSÃO**.

---

## 4. Ética e Boas Práticas no Web Scraping

Fazer scraping é uma habilidade poderosa, mas deve ser executada com responsabilidade e respeito aos donos dos sites:

* **Respeite o arquivo `robots.txt`:** Quase todos os sites possuem um arquivo no endereço `/robots.txt` (ex: `https://site.com/robots.txt`) que indica quais partes da página podem ou não ser raspadas por robôs.
* **Não sobrecarregue os servidores (Rate Limiting):** Nunca faça centenas de requisições por segundo. Em programas reais, use pequenos intervalos (como `time.sleep(1)` ou `time.sleep(2)`) entre requisições para agir como um visitante humano gentil.
* **Não tente burlar proteções:** Não contorne CAPTCHAs ou sistemas de autenticação privada. Limite-se a dados que estejam publicamente disponíveis para leitura.
* **Proteja dados pessoais:** Evite coletar telefones, documentos ou e-mails de pessoas comuns sem justificativa legal ou consentimento (observando leis de proteção de dados como a LGPD).
* **Consulte os Termos de Serviço:** Sempre verifique as diretrizes do portal antes de coletar dados em larga escala.

---

## Parabéns!

Você completou a parte teórica fundamental do curso! Agora você tem toda a base conceitual para:
1. Resolver os exercícios práticos em [`exercicios/`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exercicios);
2. Conhecer e rodar o mini projeto final em [`projeto/`](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/projeto).
