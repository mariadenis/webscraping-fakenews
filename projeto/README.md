# Projeto: Rastreador de Notícias

O **Rastreador de Notícias** é o mini-projeto prático de conclusão do curso. Ele sintetiza todas as técnicas de Web Scraping aprendidas para responder à pergunta fundamental:

> **Como rastrear a origem de uma fake news ou de uma notícia verdadeira usando Web Scraping?**

---

## 1. O que o Projeto Faz?

O projeto recebe uma notícia analisada (URL ou código HTML) e a compara com outras ocorrências encontradas na internet sobre o mesmo caso.

Para cada página raspada, o programa extrai:
* 📌 **Título** (`<h1>` ou `<title>`);
* 📅 **Data de Publicação** (`<time>` ou atributos `datetime`);
* ✍️ **Autor** (`class="autor"`, `author`, etc.);
* 🔗 **URL de Origem**;
* 📄 **Corpo do Texto** (parágrafos `<p>`);
* 🌐 **Links Citados** (fontes ou referências externas).

Em seguida, o programa:
1. Agrupa todas as matérias;
2. Ordena os registros cronologicamente (da data mais antiga para a mais recente);
3. Identifica a **ocorrência mais antiga registrada**;
4. Imprime uma **linha do tempo no terminal**;
5. Emite um parecer metodológico de checagem.

---

## 2. Estrutura do Relatório Gerado

O script produz uma saída padronizada e legível:

```text
===========================================================================
NOTICIA ANALISADA
===========================================================================
Titulo: Suposta descoberta de cura milagrosa viraliza nas redes sociais
Data  : 13/09/2026
Autor : Redação Curiosa
URL   : https://redesocial-viral.com/post/987123
Texto (resumo): Uma mensagem compartilhada mais de 100 mil vezes...
Links encontrados no texto: 1

===========================================================================
OUTRAS OCORRENCIAS ENCONTRADAS
===========================================================================
1. Site A (Fórum Alternativo)
   Data: 09/09/2026
   URL : https://forum-alternativo.net/topico/341
   Titulo: Receita milagrosa caseira promete imunidade total

2. Site B (Portal de Saúde Oficial)
   Data: 11/09/2026
   URL : https://portal-medicina-oficial.org/alertas/boato-receita
   Titulo: Alerta de Saúde: Boato sobre receita milagrosa é perigoso

===========================================================================
LINHA DO TEMPO CRONOLOGICA (DA MAIS ANTIGA PARA A MAIS RECENTE):
===========================================================================
09/09/2026 ---> Site A (Fórum Alternativo)  🥇 [PRIMEIRO REGISTRO ENCONTRADO]
   Titulo: "Receita milagrosa caseira promete imunidade total"
   URL   : https://forum-alternativo.net/topico/341
   |
   v
11/09/2026 ---> Site B (Portal de Saúde Oficial)  ↓ [Ocorrência 2]
   Titulo: "Alerta de Saúde: Boato sobre receita milagrosa é perigoso"
   URL   : https://portal-medicina-oficial.org/alertas/boato-receita
   |
   v
13/09/2026 ---> Rede Social Viral (Link Denunciado)  ↓ [Ocorrência 3]
   Titulo: "Suposta descoberta de cura milagrosa viraliza nas redes sociais"
   URL   : https://redesocial-viral.com/post/987123
```

---

## 3. Como Executar

No diretório raiz `webscraping-fakenews`, execute:

```bash
python projeto/rastreador_noticias.py
```

Por padrão, o script roda no **modo de demonstração guiada**, utilizando dados fictícios estruturados que simulam um caso clássico de propagação de boato de saúde.

---

## 4. O que o Web Scraping NÃO Faz (Aviso Crucial)

> [!WARNING]
> **Web Scraping NÃO é um detector de Fake News!**
> 
> * **Coleta não é verificação:** O programa organiza as ocorrências e aponta qual foi a mais antiga encontrada, mas isso **não prova** que aquele site seja o autor do boato.
> * **Conteúdos apagados:** O criador do boato pode ter postado em redes sociais ou fóruns e apagado o conteúdo antes do rastreador encontrá-lo.
> * **Datas alteradas:** Sites de desinformação podem alterar intencionalmente o carimbo de data para induzir os leitores a erro.
> 
> O Web Scraping é a primeira etapa (coleta e organização de evidências). A conclusão final sempre exigirá consulta a fontes primárias e checadores de fatos humanos.
