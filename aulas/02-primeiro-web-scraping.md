# Aula 02 — Primeiro Web Scraping em Python

Agora que você já entendeu o que é Web Scraping e como uma página web é estruturada com tags HTML, vamos colocar a mão na massa com nosso primeiro código em **Python**!

---

## 1. As Ferramentas que Vamos Usar

Para fazer Web Scraping em Python sem complicação, usamos duas bibliotecas principais:

```bash
requests
beautifulsoup4
```

### Para que serve a biblioteca `requests`?
A biblioteca `requests` funciona como o seu navegador web, só que dentro do código. Ela é responsável por:
* Conectar-se ao servidor do site;
* Enviar a requisição HTTP;
* Baixar o código HTML da página.

### Para que serve a biblioteca `beautifulsoup4` (BeautifulSoup)?
Depois que o `requests` baixa o HTML, ele chega como uma montanha de texto corrido. O `beautifulsoup4` atua como um navegador inteligente:
* Ele lê e organiza esse HTML (faz o *parse*);
* Permite que você faça buscas fáceis como: *"me dê o título da página"*, *"encontre todos os links"* ou *"busque o texto do parágrafo"*.

---

## 2. Instalação das Bibliotecas

Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) e execute:

```bash
pip install -r requirements.txt
```

*(Ou se preferir instalar manualmente: `pip install requests beautifulsoup4`)*

---

## 3. O Primeiro Código Passo a Passo

Nosso objetivo neste primeiro exemplo é:
1. Conectar-se a uma página web;
2. Baixar o código HTML dela;
3. Localizar o título da página;
4. Imprimir o resultado na tela.

Aqui está o código completo:

```python
import requests
from bs4 import BeautifulSoup

# Passo 1: Definir o endereço da página que queremos visitar
url = "https://example.com"

# Passo 2: Fazer a requisição HTTP para baixar a página
resposta = requests.get(url)

# Passo 3: Passar o conteúdo HTML baixado para o BeautifulSoup organizar
soup = BeautifulSoup(resposta.text, "html.parser")

# Passo 4: Localizar a tag do título da página
tag_titulo = soup.find("h1")

# Passo 5: Extrair apenas o texto limpo de dentro da tag
titulo_limpo = tag_titulo.get_text()

# Passo 6: Exibir o resultado final
print("Título da página encontrado:")
print(titulo_limpo)
```

---

## 4. Explicação Linha por Linha

Vamos entender exatamente o que cada instrução está fazendo:

* `import requests`: traz para o programa as ferramentas necessárias para navegar e fazer requisições pela internet.
* `from bs4 import BeautifulSoup`: importa a ferramenta `BeautifulSoup`, que vai ler e navegar pelo código HTML.
* `url = "https://example.com"`: guarda em uma variável o endereço que queremos raspar. O site `example.com` é um domínio oficial mantido pela IANA para testes e exemplos.
* `resposta = requests.get(url)`: o método `.get()` faz o pedido da página para o servidor. A variável `resposta` guarda o resultado retornado (código de status como 200 para sucesso, cabeçalhos e o conteúdo da página).
* `soup = BeautifulSoup(resposta.text, "html.parser")`: aqui o BeautifulSoup lê todo o texto recebido (`resposta.text`) usando o interpretador padrão de HTML do Python (`"html.parser"`). A partir dessa linha, a variável `soup` permite buscar qualquer elemento da página!
* `tag_titulo = soup.find("h1")`: o método `.find("nome_da_tag")` procura a **primeira ocorrência** da tag indicada. Aqui ele procura `<h1>`.
* `titulo_limpo = tag_titulo.get_text()`: a tag completa é `<h1>Example Domain</h1>`. O método `.get_text()` remove as tags `<>` e deixa apenas as palavras `Example Domain`.
* `print(...)`: mostra o texto na tela para você ver o resultado.

### Resultado Esperado no Terminal:
```text
Título da página encontrado:
Example Domain
```

---

## 5. Arquivo de Exemplo Pronto para Rodar

Você encontra este código pronto para execução no arquivo:
👉 [exemplos/01_titulo.py](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/exemplos/01_titulo.py)

Para testar no seu terminal, basta rodar:
```bash
python exemplos/01_titulo.py
```

---

## 6. Mini Exercício de Fixação

> **Exercício Rápido:**
> Modifique o código acima para extrair o título da tag `<title>` (a que aparece na aba do navegador) em vez da tag `<h1>`.
> 
> **Dica:** Basta trocar `soup.find("h1")` por `soup.find("title")`!

---

👉 **Próximo passo:** [Aula 03 — Aprendendo a Extrair Diferentes Tipos de Dados](file:///c:/Users/maria/OneDrive/Desktop/webscraping/webscraping-fakenews/aulas/03-extraindo-dados.md)
