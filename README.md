#Jybóia IDE 2.0 (Fork do Thonny IDE)
---
![Jybóia Logo](./logo.png) 
---

**Jybóia IDE** é um Ambiente de Desenvolvimento Integrado focado no ensino de programação para falantes da língua portuguesa. É construído como um **Fork direto do Thonny IDE**, integrando um transpilador nativo que converte código em **Português Estruturado (`.jy`)** para **Python padrão (`.py`)** e o executa no interpretador Python do sistema.

---

## ✨ Recursos Principais

- **Transpilador Integrado**: Escreva comandos com palavras-chave em Português (`se`, `senao`, `enquanto`, `para`, `funcao`, `escreva`, `leia`, etc.) mantendo a mesma sintaxe e indentação do Python.
- **Visualizador Python em Tempo Real**: Painel acoplado que mostra a tradução automática do seu código para Python padrão enquanto você digita.
- **Realce de Sintaxe (Syntax Highlighting)**: Termos em português, nomes de funções, classes, variáveis, números e textos recebem coloração diferenciada no editor.
- **Suporte Duplo a Arquivos (`.jy` e `.py`)**: Ao salvar um arquivo `.jy`, a IDE gera e mantém sincronizada a versão `.py` correspondente.
- **Monitor de Variáveis (Variables View)**: Tabela lateral que exibe em tempo real o nome, tipo e valor de cada variável na memória durante e após a execução do programa.
- **Remapeamento de Erros**: Quando ocorre um erro no código Python gerado, a IDE remapeia a linha de erro de volta para o arquivo `.jy` original e apresenta dicas explicativas em português.

---

## 📖 Tabela de Palavras-Chave do Jybóia

| Português Estruturado (`.jy`) | Python (`.py`) | Descrição |
| :--- | :--- | :--- |
| `se` | `if` | Condicional se |
| `senaose` / `senão se` | `elif` | Condicional senão se |
| `senao` / `senão` | `else` | Condicional senão |
| `enquanto` | `while` | Laço de repetição enquanto |
| `para` | `for` | Laço de repetição para |
| `em` | `in` | Pertencimento / iteração |
| `intervalo(...)` | `range(...)` | Gerador de sequência numérica |
| `funcao` / `função` / `defina` | `def` | Declaração de função |
| `classe` | `class` | Declaração de classe |
| `retorne` | `return` | Retorno de função |
| `pare` | `break` | Interrupção de laço |
| `continue` | `continue` | Próxima iteração de laço |
| `Verdadeiro` / `Falso` | `True` / `False` | Valores booleanos |
| `Nulo` / `Vazio` | `None` | Valor nulo |
| `e` / `ou` / `nao` / `eh` | `and` / `or` / `not` / `is` | Operadores lógicos |
| `escreva(...)` / `imprima(...)` | `print(...)` | Exibição na tela |
| `leia(...)` | `input(...)` | Leitura de texto do teclado |
| `leia_inteiro(...)` | Leitura de número inteiro com validação |
| `leia_real(...)` | Leitura de número decimal com validação |
| `tamanho(...)` | `len(...)` | Tamanho de textos ou listas |

---

## 🚀 Como Instalar e Executar

Existem **três modos de distribuição**, escolha o que melhor se adapta ao seu ambiente:

---

### 🟢 Modo A — Versão Portable Autônoma (Recomendado para alunos no Windows)

> Não precisa instalar Python. Funciona em qualquer Windows (10 ou 11) de forma 100% autônoma e isolada.

1. Acesse a página de **[Releases no Portable](https://github.com/ProfessorCristiano/Jyboia.2.0/releases/tag/Portable)**
2. Baixe o arquivo **`Jyboia-Portable-Windows.zip`**
3. Extraia o `.zip` em qualquer pasta (Desktop, pen drive, etc.)
4. Abra a pasta extraída `dist/Jyboia` (formato Onedirectory oficial com `_internal/` e `samples/`) e dê duplo clique em **`Jyboia.exe`** 🎉

> 💡 A pasta pode ser copiada para um pen drive e usada em qualquer computador Windows sem instalação.
> 💡 Ao executar um novo código sem salvar, o Jybóia solicita o salvamento como `.jy` ou cria automaticamente `unsaved.jy`, garantindo que comandos como `escreva()` e `leia()` funcionem perfeitamente.

---

### 🟡 Modo B — Versão Leve Universal / Multiplataforma (Windows e Linux)

> Para quem **já possui Python (>= 3.9) instalado**. Não requer compilação pesada e inclui identificação inteligente do Python.

1. Baixe o arquivo **`Jyboia-Universal.zip`**[Releases no Padrão](https://github.com/ProfessorCristiano/Jyboia.2.0/releases/tag/Jyboia-Padrao)
2. Extraia o `.zip` no seu computador
3. **No Windows:**
   - Dê duplo clique em **`iniciar_jyboia.bat`**. O launcher detecta automaticamente a instalação correta do Python no Windows (via `py -3`, PATH, AppData, Program Files ou Registro) e valida o suporte a Tkinter.
4. **No Linux ou macOS:**
   - Abra o terminal na pasta e execute:
     ```bash
     chmod +x iniciar_jyboia.sh
     ./iniciar_jyboia.sh
     ```
   - O script localiza o interpretador `python3` e valida se o pacote `python3-tk` está presente, exibindo dicas de instalação se necessário.

---

### 🔵 Modo C — Instalação via `pip` (Para desenvolvedores Python)

> Compatível com Windows, Linux e macOS. Requer Python 3.9 ou superior.

```bash
# 1. Clone ou baixe o projeto
git clone https://github.com/ProfessorCristiano/Jyboia.2.0.git
cd Jyboia.2.0

# 2. (Recomendado) Crie um ambiente virtual
python -m venv .venv

# Ativar no Windows:
.venv\Scripts\activate

# Ativar no Linux/macOS:
source .venv/bin/activate

# 3. Instale o projeto
pip install .

# 4. Execute
jyboia
```

Após a instalação, o comando `jyboia` fica disponível diretamente no terminal.

---

### 🛠️ Modo D — Execução direta pelo código-fonte

```cmd
python iniciar_jyboia.py
```

Ou pelo arquivo `.bat` no Windows:

```cmd
iniciar_jyboia.bat
```

---

## 📂 Estrutura do Projeto

```
Jybóia 2.0/
├── iniciar_jyboia.bat             # Launcher inteligente Windows com detecção automática do Python
├── iniciar_jyboia.sh              # Launcher Linux/macOS com checagem de Tkinter
├── iniciar_jyboia.py              # Ponto de entrada Python multiplataforma
├── build_portable.py / .bat       # Gerador da versão Portable Onedir com Python embutido
├── build_universal.py / .bat      # Gerador da versão Universal leve para Windows e Linux
├── pyproject.toml                 # Config para "pip install ." (Modo C)
├── requirements.txt               # Dependências opcionais do projeto
├── jyboia.spec                    # Config do PyInstaller para o Portable Onedirectory
├── logo.ico                       # Ícone do executável Windows
├── logo.png                       # Logotipo PNG
├── logo-mascote.png               # Mascote da Jybóia
├── PLANEJAMENTO_PROJETO.md        # Documentação arquitetural completa
├── samples/                       # Exemplos práticos em .jy e .py
│   ├── ola_mundo.jy / .py
│   ├── calculo_media.jy / .py
│   ├── tabuada.jy / .py
│   └── monitor_variaveis_demo.jy / .py
└── thonny/                        # Código-fonte do Jybóia IDE (Fork do Thonny)
    ├── jyboia/                    # Núcleo do Transpilador
    │   ├── keywords.py            # Dicionários de palavras-chave
    │   ├── transpiler.py          # Motor de conversão via tokenize
    │   ├── sourcemap.py           # Mapeamento de linhas e tracebacks
    │   └── builtins_runtime.py    # Funções didáticas auxiliares
    ├── plugins/
    │   ├── coloring.py            # Realce de sintaxe com termos Jybóia
    │   ├── variables.py           # Monitor de Variáveis
    │   └── jyboia_python_view.py  # Visualizador do código Python traduzido
    ├── editors.py                 # Gestão de arquivos e extensão .jy
    ├── running.py                 # Interceptação de .jy e execução no Python
    └── workbench.py               # Janela principal do Jybóia IDE
```

