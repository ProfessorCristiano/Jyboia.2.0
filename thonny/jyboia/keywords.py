"""
Tabela de palavras-chave, operadores e funções embutidas do Português Estruturado (Jybóia).
"""

from typing import Dict, Set

PALAVRAS_CHAVE: Dict[str, str] = {
    # Controle de Fluxo Condicional
    "se": "if",
    "senaose": "elif",
    "senãose": "elif",
    "senao_se": "elif",
    "senão_se": "elif",
    "senao": "else",
    "senão": "else",
    
    # Laços de Repetição
    "enquanto": "while",
    "para": "for",
    "em": "in",
    "retorne": "return",
    "retorna": "return",
    "pare": "break",
    "interrompa": "break",
    "continue": "continue",
    "proximo": "continue",
    "próximo": "continue",
    "passe": "pass",
    
    # Declarações e Definições
    "funcao": "def",
    "função": "def",
    "defina": "def",
    "metodo": "def",
    "método": "def",
    "classe": "class",
    "global": "global",
    "nao_local": "nonlocal",
    "não_local": "nonlocal",
    "anonima": "lambda",
    "anônima": "lambda",
    "lambda": "lambda",
    
    # Valores e Constantes
    "Verdadeiro": "True",
    "Falso": "False",
    "Nulo": "None",
    "Vazio": "None",
    
    # Operadores Lógicos e de Identidade
    "e": "and",
    "ou": "or",
    "nao": "not",
    "não": "not",
    "eh": "is",
    "é": "is",
    
    # Tratamento de Exceções
    "tente": "try",
    "exceto": "except",
    "trate": "except",
    "finalmente": "finally",
    "lance": "raise",
    "dispare": "raise",
    "afirme": "assert",
    "assegure": "assert",
    
    # Módulos e Contexto
    "importe": "import",
    "importar": "import",
    "de": "from",
    "como": "as",
    "com": "with",
    "produza": "yield",
    "gere": "yield",
    "assincrono": "async",
    "assíncrono": "async",
    "aguarde": "await",
}

PALAVRAS_COMPOSTAS: Dict[tuple, str] = {
    ("senao", "se"): "elif",
    ("senão", "se"): "elif",
    ("nao", "em"): "not in",
    ("não", "em"): "not in",
    ("eh", "nao"): "is not",
    ("é", "nao"): "is not",
    ("eh", "não"): "is not",
    ("é", "não"): "is not",
}

FUNCOES_EMBUTIDAS: Dict[str, str] = {
    "escreva": "print",
    "escrever": "print",
    "imprima": "print",
    "imprimir": "print",
    "mostrar": "print",
    "mostre": "print",
    "leia": "input",
    "ler": "input",
    "leia_texto": "input",
    "intervalo": "range",
    "tamanho": "len",
    "comprimento": "len",
    "inteiro": "int",
    "real": "float",
    "texto": "str",
    "booleano": "bool",
    "lista": "list",
    "dicionario": "dict",
    "dicionário": "dict",
    "conjunto": "set",
    "tupla": "tuple",
    "soma": "sum",
    "somatorio": "sum",
    "somatório": "sum",
    "minimo": "min",
    "mínimo": "min",
    "maximo": "max",
    "máximo": "max",
    "absoluto": "abs",
    "arredonde": "round",
    "tipo": "type",
    "ajuda": "help",
    "ordene": "sorted",
    "ordenado": "sorted",
    "invertido": "reversed",
    "enumerar": "enumerate",
    "enumere": "enumerate",
    "abrir": "open",
}

TODAS_PALAVRAS_RESERVADAS: Set[str] = (
    set(PALAVRAS_CHAVE.keys())
    | set(FUNCOES_EMBUTIDAS.keys())
    | {"senao se", "senão se", "não em", "nao em", "é não", "eh não", "leia_inteiro", "leia_real", "leia_int", "leia_float"}
)
