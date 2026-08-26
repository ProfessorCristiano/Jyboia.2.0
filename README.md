#Jybóia IDE 2.0 (Fork do Thonny IDE)
![Jybóia Logo](./logo.png) 
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

## 🚀 Como Iniciar

### Opção 1: Pelo arquivo executável (.bat)
Dê um duplo clique no arquivo:
```cmd
iniciar_jyboia.bat
```

### Opção 2: Pelo Terminal / Prompt de Comando
```cmd
python iniciar_jyboia.py
```

---

## 📂 Estrutura do Projeto

```
Jybóia 2.0/
├── iniciar_jyboia.bat             # Launcher rápido para Windows
├── iniciar_jyboia.py              # Ponto de entrada Python
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


![Jybóia Mascote](./logo-mascote.png)
