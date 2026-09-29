# 📘 Manual do Usuário — Jybóia IDE 2.0

> **Jybóia IDE** é um ambiente de programação para iniciantes que permite escrever código em **Português Estruturado** (arquivos `.jy`) e executá-lo diretamente, sem precisar aprender inglês para começar a programar.

---

## Sumário

1. [Instalação](#1-instalação)
2. [Primeiros Passos na IDE](#2-primeiros-passos-na-ide)
3. [Criando e Executando seu Primeiro Programa](#3-criando-e-executando-seu-primeiro-programa)
4. [Painel de Variáveis](#4-painel-de-variáveis)
5. [Exemplos Prontos](#5-exemplos-prontos)
6. [Referência Completa da Linguagem](#6-referência-completa-da-linguagem)
   - [6.1 Palavras-chave de Controle de Fluxo](#61-palavras-chave-de-controle-de-fluxo)
   - [6.2 Funções e Definições](#62-funções-e-definições)
   - [6.3 Valores e Operadores Lógicos](#63-valores-e-operadores-lógicos)
   - [6.4 Tratamento de Erros](#64-tratamento-de-erros)
   - [6.5 Módulos e Contexto](#65-módulos-e-contexto)
   - [6.6 Funções Embutidas](#66-funções-embutidas)
   - [6.7 Métodos de Lista](#67-métodos-de-lista)
   - [6.8 Métodos de Dicionário](#68-métodos-de-dicionário)
   - [6.9 Métodos de Conjunto (set)](#69-métodos-de-conjunto-set)
   - [6.10 Métodos de Texto (str)](#610-métodos-de-texto-str)
   - [6.11 Métodos de Arquivo](#611-métodos-de-arquivo)
7. [Dicas e Boas Práticas](#7-dicas-e-boas-práticas)
8. [Mensagens de Erro Comuns](#8-mensagens-de-erro-comuns)

---

## 1. Instalação

Escolha o modo que se encaixa na sua situação:

### 🟢 Opção A — Portable (sem instalar nada) — *Recomendado para alunos no Windows*

> Funciona em qualquer Windows 10 ou 11, sem instalar Python.

1. Acesse a página de **Releases** no GitHub do projeto
2. Baixe o arquivo **`Jyboia-Portable-Windows.zip`**
3. Extraia o `.zip` em qualquer pasta (Desktop, pen drive, etc.)
4. Abra a pasta e dê duplo clique em **`Jyboia.exe`**

> 💡 **Dica para professores:** copie a pasta extraída para um pen drive e leve para o laboratório. Funciona em qualquer computador Windows sem instalar nada.

---

### 🟡 Opção B — Versão Leve Universal (Para quem já tem Python instalado — Windows e Linux)

> Pacote leve de execução que detecta automaticamente a instalação correta do Python.

1. Baixe o arquivo **`Jyboia-Universal.zip`**
2. Extraia o arquivo no seu computador
3. **No Windows:**
   - Dê duplo clique em **`iniciar_jyboia.bat`**. O arquivo identifica a melhor instalação do Python 3.9+ no sistema (via `py -3`, PATH, AppData, Program Files ou Registro) e valida o suporte a Tkinter.
4. **No Linux ou macOS:**
   - No terminal, dê permissão e execute:
     ```bash
     chmod +x iniciar_jyboia.sh
     ./iniciar_jyboia.sh
     ```
   - O inicializador valida a presença do Python 3 e do módulo `python3-tk`.

---

### 🔵 Opção C — Via pip (para quem tem Python instalado)

> Compatível com Windows, Linux e macOS. Requer Python 3.9 ou superior.

Abra o terminal e execute:

```bash
pip install .
```

Após a instalação, basta digitar no terminal:

```bash
jyboia
```

---

### 🛠️ Opção D — Pelo código-fonte (para desenvolvedores)

No Windows, dê duplo clique em `iniciar_jyboia.bat`  
Ou pelo terminal (Windows/Linux/macOS):

```bash
python iniciar_jyboia.py
```

---

## 2. Primeiros Passos na IDE

Ao abrir o Jybóia IDE, você verá:

```
┌─────────────────────────────────────────────────────────────┐
│  Jybóia IDE 2.0                            [_] [□] [X]      │
├──────────────────────────────┬──────────────────────────────┤
│                              │                              │
│    📝 Editor (.jy)           │   🐍 Código Python Gerado    │
│    (onde você escreve)       │   (tradução automática)      │
│                              │                              │
├──────────────────────────────┴──────────────────────────────┤
│    🖥️ Shell / Console (saída do programa)                   │
├─────────────────────────────────────────────────────────────┤
│    📊 Monitor de Variáveis                                  │
└─────────────────────────────────────────────────────────────┘
```

| Painel | Função |
|---|---|
| **Editor (.jy)** | Onde você escreve seu código em Português Estruturado |
| **Código Python Gerado** | Mostra em tempo real como seu código ficaria em Python |
| **Shell / Console** | Exibe a saída do programa e mensagens de erro |
| **Monitor de Variáveis** | Mostra o valor de cada variável enquanto o programa roda |

---

## 3. Criando e Executando seu Primeiro Programa

### Passo 1 — Criar um novo arquivo

- Menu **Arquivo → Novo** (ou `Ctrl+N`)
- O arquivo começa com a extensão `.jy` por padrão

### Passo 2 — Escrever o código

```
nome = leia("Qual é o seu nome? ")
escreva("Olá,", nome, "! Bem-vindo ao Jybóia!")
```

### Passo 3 — Salvar

- `Ctrl+S` para salvar
- Escolha um nome como `meu_programa.jy` (a extensão `.jy` é preenchida por padrão)
- O arquivo `.py` espelho correspondente é gerado automaticamente

### Passo 4 — Executar

- Pressione **F5** ou clique no botão ▶ **Executar**
- **Execução de código novo sem salvar:** Por padrão, o Jybóia solicita que você salve o arquivo antes de rodar, abrindo o diálogo "Salvar Como". Se você cancelar ou preferir executar direto sem nome, o Jybóia salva automaticamente o conteúdo como `unsaved.jy` na pasta do projeto e o executa com todas as funções didáticas (`escreva()`, `leia()`, etc.) ativas.
- A saída aparece no painel **Shell** abaixo

### Passo 5 — Observar as variáveis

- Enquanto o programa roda, o **Monitor de Variáveis** mostra o nome, tipo e valor de cada variável

---

## 4. Painel de Variáveis

O **Monitor de Variáveis** é uma das ferramentas mais importantes para aprender a programar.

Ele mostra, para cada variável criada no programa:

| Coluna | O que mostra |
|---|---|
| **Nome** | O nome da variável (`nota1`, `nome`, `contador`, ...) |
| **Tipo** | O tipo do dado (`int`, `float`, `str`, `list`, ...) |
| **Valor** | O valor atual da variável |

**Exemplo:** ao executar o código abaixo, o Monitor de Variáveis exibirá:

```
nota1 = 8.5
nota2 = 7.0
media = (nota1 + nota2) / 2
escreva("Média:", media)
```

| Nome | Tipo | Valor |
|---|---|---|
| `nota1` | float | 8.5 |
| `nota2` | float | 7.0 |
| `media` | float | 7.75 |

---

## 5. Exemplos Prontos

A pasta `samples/` contém exemplos prontos para abrir e executar:

| Arquivo | O que demonstra |
|---|---|
| `ola_mundo.jy` | Saída de texto com `escreva`, variáveis de texto |
| `calculo_media.jy` | Condicional `se / senaose / senao` |
| `tabuada.jy` | Laço `para ... em intervalo(...)` |
| `monitor_variaveis_demo.jy` | Laço `enquanto`, listas e o Monitor de Variáveis |

Para abrir: **Arquivo → Abrir** e navegue até a pasta `samples/`.

---

## 6. Referência Completa da Linguagem

### 6.1 Palavras-chave de Controle de Fluxo

#### Condicional

```
se <condição>:
    # bloco executado se a condição for verdadeira
senaose <outra condição>:
    # bloco executado se a segunda condição for verdadeira
senao:
    # bloco executado se nenhuma condição for verdadeira
```

**Exemplo:**

```
nota = leia_real("Digite a nota: ")

se nota >= 7.0:
    escreva("Aprovado!")
senaose nota >= 5.0:
    escreva("Em Recuperação!")
senao:
    escreva("Reprovado.")
```

| Português | Python | Descrição |
|:---|:---|:---|
| `se` | `if` | Se a condição for verdadeira |
| `senaose` / `senão se` | `elif` | Caso contrário, se... |
| `senao` / `senão` | `else` | Caso contrário |

---

#### Laços de Repetição

**Laço `para` (quantidade definida de repetições):**

```
para i em intervalo(1, 11):
    escreva("Linha", i)
```

**Laço `enquanto` (repete enquanto a condição for verdadeira):**

```
contador = 0
enquanto contador < 5:
    escreva("Contando:", contador)
    contador = contador + 1
```

| Português | Python | Descrição |
|:---|:---|:---|
| `para` | `for` | Laço com quantidade definida |
| `em` | `in` | Pertencimento / iteração |
| `enquanto` | `while` | Laço condicional |
| `intervalo(inicio, fim)` | `range(inicio, fim)` | Sequência de números |
| `pare` / `interrompa` | `break` | Interrompe o laço imediatamente |
| `continue` / `próximo` | `continue` | Pula para a próxima iteração |
| `passe` | `pass` | Bloco vazio (não faz nada) |
| `retorne` / `retorna` | `return` | Retorna valor de uma função |

---

### 6.2 Funções e Definições

```
funcao saudacao(nome):
    escreva("Olá,", nome)
    retorne "ok"

saudacao("Ana")
```

| Português | Python | Descrição |
|:---|:---|:---|
| `funcao` / `função` / `defina` | `def` | Declarar uma função |
| `metodo` / `método` | `def` | Declarar um método (dentro de classe) |
| `classe` | `class` | Declarar uma classe |
| `retorne` / `retorna` | `return` | Retornar um valor |
| `lambda` / `anonima` | `lambda` | Função anônima de uma linha |
| `global` | `global` | Usar variável global dentro da função |
| `nao_local` / `não_local` | `nonlocal` | Usar variável do escopo superior |

---

### 6.3 Valores e Operadores Lógicos

| Português | Python | Descrição |
|:---|:---|:---|
| `Verdadeiro` | `True` | Valor booleano verdadeiro |
| `Falso` | `False` | Valor booleano falso |
| `Nulo` / `Vazio` | `None` | Ausência de valor |
| `e` | `and` | E lógico |
| `ou` | `or` | Ou lógico |
| `nao` / `não` | `not` | Negação lógica |
| `eh` / `é` | `is` | Identidade (mesmo objeto) |
| `nao em` / `não em` | `not in` | Não pertence à coleção |
| `eh nao` / `é não` | `is not` | Não é o mesmo objeto |

**Exemplo:**

```
ativo = Verdadeiro
bloqueado = Falso

se ativo e nao bloqueado:
    escreva("Usuário pode entrar!")
```

---

### 6.4 Tratamento de Erros

```
tente:
    resultado = 10 / 0
exceto:
    escreva("Erro: divisão por zero!")
finalmente:
    escreva("Bloco sempre executado.")
```

| Português | Python | Descrição |
|:---|:---|:---|
| `tente` | `try` | Tenta executar um bloco |
| `exceto` / `trate` | `except` | Captura um erro |
| `finalmente` | `finally` | Executa sempre, com ou sem erro |
| `lance` / `dispare` | `raise` | Lança um erro propositalmente |
| `afirme` / `assegure` | `assert` | Verifica uma condição |

---

### 6.5 Módulos e Contexto

| Português | Python | Descrição |
|:---|:---|:---|
| `importe` / `importar` | `import` | Importar um módulo |
| `de` | `from` | Importar de um módulo específico |
| `como` | `as` | Renomear ao importar |
| `com` | `with` | Gerenciador de contexto |
| `produza` / `gere` | `yield` | Gerar valor em um gerador |
| `assincrono` / `assíncrono` | `async` | Função assíncrona |
| `aguarde` | `await` | Aguardar resultado assíncrono |

**Exemplo:**

```
importe matematica
escreva(matematica.pi)

de matematica importe sqrt como raiz_quadrada
escreva(raiz_quadrada(16))
```

---

### 6.6 Funções Embutidas

Funções que funcionam diretamente, sem precisar importar nada:

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `escreva(...)` | `print(...)` | Exibe texto na tela | `escreva("Oi!")` |
| `imprima(...)` | `print(...)` | Alias de escreva | `imprima(42)` |
| `leia(...)` | `input(...)` | Lê texto digitado | `nome = leia("Nome: ")` |
| `leia_inteiro(...)` | — | Lê e converte para inteiro | `n = leia_inteiro("Número: ")` |
| `leia_real(...)` | — | Lê e converte para decimal | `x = leia_real("Valor: ")` |
| `inteiro(x)` | `int(x)` | Converte para número inteiro | `inteiro("42")` |
| `real(x)` | `float(x)` | Converte para número decimal | `real("3.14")` |
| `texto(x)` | `str(x)` | Converte para texto | `texto(100)` |
| `booleano(x)` | `bool(x)` | Converte para verdadeiro/falso | `booleano(0)` |
| `tamanho(x)` | `len(x)` | Comprimento de lista ou texto | `tamanho("Jybóia")` |
| `comprimento(x)` | `len(x)` | Alias de tamanho | `comprimento([1,2,3])` |
| `soma(lista)` | `sum(lista)` | Soma os itens de uma lista | `soma([1, 2, 3])` |
| `minimo(x, y)` | `min(x, y)` | Menor valor | `minimo(5, 3)` |
| `maximo(x, y)` | `max(x, y)` | Maior valor | `maximo(5, 3)` |
| `absoluto(x)` | `abs(x)` | Valor absoluto (sem sinal) | `absoluto(-7)` |
| `arredonde(x, n)` | `round(x, n)` | Arredonda um número | `arredonde(3.567, 2)` |
| `tipo(x)` | `type(x)` | Tipo do dado | `tipo(42)` |
| `intervalo(...)` | `range(...)` | Sequência de números | `intervalo(1, 11)` |
| `lista(...)` | `list(...)` | Cria uma lista | `lista(intervalo(5))` |
| `tupla(...)` | `tuple(...)` | Cria uma tupla | `tupla([1, 2, 3])` |
| `dicionario(...)` | `dict(...)` | Cria um dicionário | `dicionario()` |
| `conjunto(...)` | `set(...)` | Cria um conjunto | `conjunto([1,1,2,3])` |
| `ordene(lista)` | `sorted(lista)` | Retorna lista ordenada | `ordene([3,1,2])` |
| `invertido(lista)` | `reversed(lista)` | Retorna iterador invertido | `invertido([1,2,3])` |
| `enumere(lista)` | `enumerate(lista)` | Retorna índice + valor | `enumere(["a","b"])` |
| `abrir(arquivo)` | `open(arquivo)` | Abre um arquivo | `abrir("dados.txt", "r")` |
| `ajuda(x)` | `help(x)` | Exibe ajuda sobre algo | `ajuda(lista)` |

---

### 6.7 Métodos de Lista

> Métodos são chamados com ponto após o nome da variável: `minha_lista.adicionar(5)`

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.adicionar(x)` | `.append(x)` | Adiciona item no final | `notas.adicionar(8.5)` |
| `.acrescentar(x)` | `.append(x)` | Alias de adicionar | `notas.acrescentar(7.0)` |
| `.inserir(i, x)` | `.insert(i, x)` | Insere item na posição `i` | `notas.inserir(0, 10)` |
| `.estender(outra)` | `.extend(outra)` | Une outra lista no final | `notas.estender([6, 7])` |
| `.remover(x)` | `.remove(x)` | Remove a primeira ocorrência de `x` | `notas.remover(5)` |
| `.retirar()` | `.pop()` | Remove e retorna o último item | `ultimo = notas.retirar()` |
| `.retirar(i)` | `.pop(i)` | Remove e retorna o item na posição `i` | `notas.retirar(0)` |
| `.desempilhar()` | `.pop()` | Alias de retirar | `notas.desempilhar()` |
| `.limpar()` | `.clear()` | Remove todos os itens | `notas.limpar()` |
| `.ordenar()` | `.sort()` | Ordena a lista no lugar | `notas.ordenar()` |
| `.inverter()` | `.reverse()` | Inverte a ordem da lista | `notas.inverter()` |
| `.copiar()` | `.copy()` | Retorna uma cópia da lista | `copia = notas.copiar()` |
| `.contar(x)` | `.count(x)` | Conta quantas vezes `x` aparece | `notas.contar(10)` |
| `.indice(x)` | `.index(x)` | Retorna a posição de `x` | `notas.indice(8.5)` |

**Exemplo completo:**

```
notas = [7.0, 8.5, 6.0, 9.0]
notas.adicionar(10.0)
notas.ordenar()
escreva("Notas ordenadas:", notas)
escreva("Maior nota:", maximo(notas))
escreva("Média:", soma(notas) / tamanho(notas))
```

---

### 6.8 Métodos de Dicionário

> Dicionários guardam pares de **chave: valor**, como uma agenda telefônica.

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.chaves()` | `.keys()` | Retorna todas as chaves | `agenda.chaves()` |
| `.valores()` | `.values()` | Retorna todos os valores | `agenda.valores()` |
| `.itens()` | `.items()` | Retorna pares (chave, valor) | `agenda.itens()` |
| `.obter(k, p)` | `.get(k, p)` | Retorna valor da chave, ou `p` se não existir | `agenda.obter("Ana", "?")` |
| `.atualizar(d)` | `.update(d)` | Adiciona/atualiza com outro dicionário | `agenda.atualizar(novos)` |
| `.excluir(k)` | `.pop(k)` | Remove e retorna o valor da chave `k` | `agenda.excluir("João")` |
| `.limpar()` | `.clear()` | Remove todos os itens | `agenda.limpar()` |
| `.copiar()` | `.copy()` | Retorna uma cópia do dicionário | `copia = agenda.copiar()` |
| `.definir_padrao(k, v)` | `.setdefault(k, v)` | Define valor padrão se chave não existir | `agenda.definir_padrao("x", 0)` |

**Exemplo completo:**

```
aluno = {"nome": "Ana", "nota": 9.5, "turma": "A"}

escreva("Nome:", aluno["nome"])
escreva("Chaves disponíveis:", aluno.chaves())

para chave, valor em aluno.itens():
    escreva(chave, "→", valor)
```

---

### 6.9 Métodos de Conjunto (set)

> Conjuntos não permitem itens repetidos e não têm ordem definida.

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.adicionar_item(x)` | `.add(x)` | Adiciona um item ao conjunto | `pares.adicionar_item(4)` |
| `.descartar(x)` | `.discard(x)` | Remove item (sem erro se não existir) | `pares.descartar(3)` |
| `.remover(x)` | `.remove(x)` | Remove item (com erro se não existir) | `pares.remover(2)` |
| `.limpar()` | `.clear()` | Remove todos os itens | `pares.limpar()` |
| `.copiar()` | `.copy()` | Retorna uma cópia | `copia = pares.copiar()` |
| `.uniao(outro)` | `.union(outro)` | União dos dois conjuntos | `pares.uniao(impares)` |
| `.intersecao(outro)` | `.intersection(outro)` | Elementos em comum | `a.intersecao(b)` |
| `.diferenca(outro)` | `.difference(outro)` | Elementos só no primeiro | `a.diferenca(b)` |

**Exemplo completo:**

```
frutas_a = conjunto(["maçã", "banana", "uva"])
frutas_b = conjunto(["banana", "laranja", "uva"])

em_comum = frutas_a.intersecao(frutas_b)
escreva("Frutas em comum:", em_comum)

todas = frutas_a.uniao(frutas_b)
escreva("Todas as frutas:", todas)
```

---

### 6.10 Métodos de Texto (str)

> Textos (strings) são cadeias de caracteres entre aspas.

#### Busca e Verificação

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.encontrar(s)` | `.find(s)` | Posição de `s` no texto (-1 se não achar) | `nome.encontrar("a")` |
| `.encontrar_direita(s)` | `.rfind(s)` | Busca da direita para esquerda | `nome.encontrar_direita("a")` |
| `.começa_com(s)` | `.startswith(s)` | Verifica se começa com `s` | `nome.começa_com("Jo")` |
| `.termina_com(s)` | `.endswith(s)` | Verifica se termina com `s` | `email.termina_com(".com")` |
| `.contar_texto(s)` | `.count(s)` | Quantas vezes `s` aparece | `frase.contar_texto("a")` |

#### Transformação de Caixa

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.maiusculo()` | `.upper()` | Converte para MAIÚSCULAS | `nome.maiusculo()` |
| `.minusculo()` | `.lower()` | Converte para minúsculas | `nome.minusculo()` |
| `.capitalizar()` | `.capitalize()` | Primeira letra maiúscula | `nome.capitalizar()` |
| `.titulo()` | `.title()` | Cada Palavra Com Maiúscula | `titulo.titulo()` |
| `.trocar_caixa()` | `.swapcase()` | Inverte maiúsculas/minúsculas | `texto.trocar_caixa()` |

#### Remoção de Espaços

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.retirar_espacos()` | `.strip()` | Remove espaços das duas pontas | `entrada.retirar_espacos()` |
| `.retirar_esq()` | `.lstrip()` | Remove espaços da esquerda | `entrada.retirar_esq()` |
| `.retirar_dir()` | `.rstrip()` | Remove espaços da direita | `entrada.retirar_dir()` |

#### Divisão e Junção

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.dividir()` | `.split()` | Divide em lista de palavras | `frase.dividir()` |
| `.dividir(" ")` | `.split(" ")` | Divide pelo separador | `dados.dividir(";")` |
| `.dividir_linhas()` | `.splitlines()` | Divide em linhas | `arquivo.dividir_linhas()` |
| `.juntar(lista)` | `.join(lista)` | Une lista em texto com separador | `", ".juntar(nomes)` |
| `.unir(lista)` | `.join(lista)` | Alias de juntar | `" - ".unir(itens)` |

#### Substituição e Formatação

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.substituir(a, b)` | `.replace(a, b)` | Substitui todas as ocorrências | `texto.substituir("a", "@")` |
| `.formatar(...)` | `.format(...)` | Formata com valores | `"Olá, {}!".formatar(nome)` |

#### Alinhamento e Preenchimento

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.centralizar(n)` | `.center(n)` | Centraliza em `n` caracteres | `titulo.centralizar(40)` |
| `.alinhar_esq(n)` | `.ljust(n)` | Alinha à esquerda em `n` caracteres | `nome.alinhar_esq(20)` |
| `.alinhar_dir(n)` | `.rjust(n)` | Alinha à direita em `n` caracteres | `valor.alinhar_dir(10)` |
| `.preencher_esq(n)` | `.zfill(n)` | Preenche com zeros à esquerda | `"42".preencher_esq(5)` |

#### Verificações de Conteúdo

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.eh_numero()` | `.isnumeric()` | É um número? | `entrada.eh_numero()` |
| `.eh_inteiro()` | `.isdigit()` | É formado só de dígitos? | `cpf.eh_inteiro()` |
| `.eh_letra()` | `.isalpha()` | É formado só de letras? | `nome.eh_letra()` |
| `.eh_alfanumerico()` | `.isalnum()` | É letras e/ou números? | `codigo.eh_alfanumerico()` |
| `.eh_maiusculo()` | `.isupper()` | Está em maiúsculas? | `sigla.eh_maiusculo()` |
| `.eh_minusculo()` | `.islower()` | Está em minúsculas? | `email.eh_minusculo()` |
| `.eh_espaco()` | `.isspace()` | É só espaços? | `entrada.eh_espaco()` |
| `.eh_titulo()` | `.istitle()` | Cada Palavra Com Maiúscula? | `titulo.eh_titulo()` |

**Exemplo completo:**

```
entrada = leia("Digite seu nome completo: ")
nome_limpo = entrada.retirar_espacos()
nome_formatado = nome_limpo.titulo()

escreva("Olá,", nome_formatado, "!")
escreva("Letras no nome:", tamanho(nome_limpo))

se nome_limpo.eh_letra():
    escreva("Nome válido!")
senao:
    escreva("O nome contém caracteres inválidos.")
```

---

### 6.11 Métodos de Arquivo

> Use `abrir()` para ler ou gravar arquivos de texto.

| Jybóia | Python | Descrição | Exemplo |
|:---|:---|:---|:---|
| `.ler_tudo()` | `.read()` | Lê o arquivo inteiro como texto | `arq.ler_tudo()` |
| `.ler_linha()` | `.readline()` | Lê uma linha por vez | `arq.ler_linha()` |
| `.ler_linhas()` | `.readlines()` | Lê todas as linhas como lista | `arq.ler_linhas()` |
| `.escrever(t)` | `.write(t)` | Grava texto no arquivo | `arq.escrever("Olá!\n")` |
| `.escrever_linhas(l)` | `.writelines(l)` | Grava lista de linhas | `arq.escrever_linhas(lista)` |
| `.fechar()` | `.close()` | Fecha o arquivo | `arq.fechar()` |
| `.posicao()` | `.tell()` | Posição atual no arquivo | `arq.posicao()` |
| `.mover_para(n)` | `.seek(n)` | Move para a posição `n` | `arq.mover_para(0)` |
| `.liberar()` | `.flush()` | Força gravação no disco | `arq.liberar()` |

**Exemplo de leitura:**

```
com abrir("dados.txt", "r") como arq:
    conteudo = arq.ler_tudo()
    escreva(conteudo)
```

**Exemplo de escrita:**

```
com abrir("resultado.txt", "w") como arq:
    arq.escrever("Resultado: aprovado\n")
    arq.escrever("Data: hoje\n")
```

---

## 7. Dicas e Boas Práticas

### ✅ Use nomes de variáveis em português

```
# Bom
nome_aluno = "Ana"
media_final = 8.5
lista_notas = [7, 8, 9]

# Evite misturar idiomas desnecessariamente
studentName = "Ana"   # menos claro para iniciantes
```

### ✅ Indentação com 4 espaços

O Jybóia (como o Python) usa a **indentação** para definir blocos de código. Use **4 espaços** por nível:

```
se nota >= 7:
    escreva("Aprovado!")    # ← 4 espaços de indentação
    se nota == 10:
        escreva("Nota máxima!")   # ← 8 espaços (2 níveis)
```

### ✅ Comentários com `#`

Use `#` para adicionar comentários explicativos:

```
# Este programa calcula a média de três notas
nota1 = 8.0   # primeira nota bimestral
nota2 = 7.5   # segunda nota bimestral
media = (nota1 + nota2) / 2
```

### ✅ Use `leia_inteiro` e `leia_real` para dados numéricos

```
# Correto: converte automaticamente para número
idade = leia_inteiro("Digite sua idade: ")
peso = leia_real("Digite seu peso: ")

# Evite: retorna texto, não número
idade = leia("Digite sua idade: ")   # precisa converter manualmente
```

---

## 8. Mensagens de Erro Comuns

| Mensagem | Causa provável | Como resolver |
|:---|:---|:---|
| `IndentationError` | Indentação incorreta | Verifique se usou 4 espaços dentro de blocos |
| `NameError: name '...' is not defined` | Variável usada antes de ser criada | Declare e atribua valor à variável antes de usá-la |
| `TypeError: can only concatenate str (not "int") to str` | Misturou texto com número | Converta com `texto(numero)`: `escreva("Idade: " + texto(idade))` |
| `ZeroDivisionError` | Divisão por zero | Verifique se o divisor pode ser zero antes de dividir |
| `SyntaxError` | Erro de sintaxe | Verifique a linha indicada: parênteses não fechados, dois pontos faltando no `se:`, `para:`, `enquanto:`, etc. |
| `IndexError: list index out of range` | Acesso a posição que não existe | Use `tamanho(lista)` para verificar o tamanho antes de acessar |
| `KeyError` | Chave não existe no dicionário | Use `.obter(chave, valor_padrao)` em vez de `dicionario[chave]` |

---

*Manual do Usuário — Jybóia IDE 2.0 | Programação em Português Estruturado*
