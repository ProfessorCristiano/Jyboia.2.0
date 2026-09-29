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
    "verdadeiro": "True",
    "Falso": "False",
    "falso": "False",
    "Nulo": "None",
    "nulo": "None",
    "Vazio": "None",
    "vazio": "None",
    
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
    "leia_inteiro": "int_input",
    "leia_real": "float_input",
    "leia_int": "int_input",
    "leia_float": "float_input",
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

METODOS_SEQUENCIAS: Dict[str, str] = {
    # ── Métodos de LISTA (list) ─────────────────────────────────────────────
    # Leitura / busca
    "contar":        "count",        # lista.contar(x)   → lista.count(x)
    "indice":        "index",        # lista.indice(x)   → lista.index(x)
    "índice":        "index",

    # Adição
    "adicionar":     "append",       # lista.adicionar(x)   → lista.append(x)
    "acrescentar":   "append",
    "inserir":       "insert",       # lista.inserir(i, x)  → lista.insert(i, x)
    "estender":      "extend",       # lista.estender(it)   → lista.extend(it)

    # Remoção
    "remover":       "remove",       # lista.remover(x)     → lista.remove(x)
    "retirar":       "pop",          # lista.retirar()      → lista.pop()
    "desempilhar":   "pop",
    "limpar":        "clear",        # lista.limpar()       → lista.clear()

    # Ordenação / inversão
    "ordenar":       "sort",         # lista.ordenar()      → lista.sort()
    "inverter":      "reverse",      # lista.inverter()     → lista.reverse()

    # Cópia
    "copiar":        "copy",         # lista.copiar()       → lista.copy()

    # ── Métodos de DICIONÁRIO (dict) ────────────────────────────────────────
    "chaves":        "keys",         # dicio.chaves()       → dicio.keys()
    "valores":       "values",       # dicio.valores()      → dicio.values()
    "itens":         "items",        # dicio.itens()        → dicio.items()
    "obter":         "get",          # dicio.obter(k, p)    → dicio.get(k, p)
    "atualizar":     "update",       # dicio.atualizar(d2)  → dicio.update(d2)
    "excluir":       "pop",          # dicio.excluir(k)     → dicio.pop(k)
    "definir_padrao":"setdefault",   # dicio.definir_padrao(k, v) → dicio.setdefault(k, v)
    "definir_padrão":"setdefault",
    "esta_em":       "keys",         # alias semântico ("k esta_em d" → "k in d.keys()")

    # ── Métodos de CONJUNTO (set) ────────────────────────────────────────────
    "adicionar_item":"add",          # conj.adicionar_item(x) → conj.add(x)
    "descartar":     "discard",      # conj.descartar(x)    → conj.discard(x)
    "uniao":         "union",        # conj.uniao(c2)        → conj.union(c2)
    "união":         "union",
    "intersecao":    "intersection", # conj.intersecao(c2)   → conj.intersection(c2)
    "intersecção":   "intersection",
    "diferenca":     "difference",   # conj.diferenca(c2)    → conj.difference(c2)
    "diferença":     "difference",

    # ── Métodos compartilhados (list + tuple + str) ──────────────────────────
    # (count e index já estão acima)
}

METODOS_TEXTO: Dict[str, str] = {
    # ── Busca e verificação ──────────────────────────────────────────────────
    "encontrar":        "find",          # texto.encontrar("a")      → texto.find("a")
    "encontrar_direita":"rfind",         # texto.encontrar_direita() → texto.rfind()
    "indice_texto":     "index",         # texto.indice_texto("a")   → texto.index("a")
    "começa_com":       "startswith",    # texto.começa_com("Oi")    → texto.startswith("Oi")
    "comeca_com":       "startswith",
    "termina_com":      "endswith",      # texto.termina_com("!")    → texto.endswith("!")
    "contem":           "find",          # alias: texto.contem(s)    → texto.find(s) != -1
    "contém":           "find",

    # ── Transformação de caixa ───────────────────────────────────────────────
    "maiusculo":        "upper",         # texto.maiusculo()         → texto.upper()
    "maiúsculo":        "upper",
    "minusculo":        "lower",         # texto.minusculo()         → texto.lower()
    "minúsculo":        "lower",
    "capitalizar":      "capitalize",    # texto.capitalizar()       → texto.capitalize()
    "titulo":           "title",         # texto.titulo()            → texto.title()
    "título":           "title",
    "trocar_caixa":     "swapcase",      # texto.trocar_caixa()      → texto.swapcase()

    # ── Remoção de espaços e caracteres ─────────────────────────────────────
    "retirar_espacos":  "strip",         # texto.retirar_espacos()   → texto.strip()
    "retirar_espaços":  "strip",
    "retirar_esq":      "lstrip",        # texto.retirar_esq()       → texto.lstrip()
    "retirar_dir":      "rstrip",        # texto.retirar_dir()       → texto.rstrip()

    # ── Divisão e junção ────────────────────────────────────────────────────
    "dividir":          "split",         # texto.dividir()           → texto.split()
    "dividir_linhas":   "splitlines",    # texto.dividir_linhas()    → texto.splitlines()
    "juntar":           "join",          # sep.juntar(lista)         → sep.join(lista)
    "unir":             "join",

    # ── Substituição ────────────────────────────────────────────────────────
    "substituir":       "replace",       # texto.substituir("a","b") → texto.replace("a","b")
    "formatar":         "format",        # texto.formatar(x, y)      → texto.format(x, y)

    # ── Preenchimento e alinhamento ──────────────────────────────────────────
    "preencher_esq":    "zfill",         # numero.preencher_esq(5)   → numero.zfill(5)
    "alinhar_esq":      "ljust",         # texto.alinhar_esq(10)     → texto.ljust(10)
    "alinhar_dir":      "rjust",         # texto.alinhar_dir(10)     → texto.rjust(10)
    "centralizar":      "center",        # texto.centralizar(10)     → texto.center(10)

    # ── Verificações de conteúdo ─────────────────────────────────────────────
    "eh_numero":        "isnumeric",     # texto.eh_numero()         → texto.isnumeric()
    "é_numero":         "isnumeric",
    "eh_inteiro":       "isdigit",       # texto.eh_inteiro()        → texto.isdigit()
    "é_inteiro":        "isdigit",
    "eh_letra":         "isalpha",       # texto.eh_letra()          → texto.isalpha()
    "é_letra":          "isalpha",
    "eh_alfanumerico":  "isalnum",       # texto.eh_alfanumerico()   → texto.isalnum()
    "é_alfanumerico":   "isalnum",
    "eh_maiusculo":     "isupper",       # texto.eh_maiusculo()      → texto.isupper()
    "é_maiúsculo":      "isupper",
    "eh_minusculo":     "islower",       # texto.eh_minusculo()      → texto.islower()
    "é_minúsculo":      "islower",
    "eh_espaco":        "isspace",       # texto.eh_espaco()         → texto.isspace()
    "é_espaco":         "isspace",
    "eh_titulo":        "istitle",       # texto.eh_titulo()         → texto.istitle()
    "é_título":         "istitle",

    # ── Codificação ──────────────────────────────────────────────────────────
    "codificar":        "encode",        # texto.codificar("utf-8")  → texto.encode("utf-8")
    "decodificar":      "decode",        # bytes.decodificar()       → bytes.decode()
    "contar_texto":     "count",         # texto.contar_texto("a")   → texto.count("a")
}

METODOS_ARQUIVO: Dict[str, str] = {
    # ── Leitura ──────────────────────────────────────────────────────────────
    "ler_tudo":         "read",          # arq.ler_tudo()            → arq.read()
    "ler_linha":        "readline",      # arq.ler_linha()           → arq.readline()
    "ler_linhas":       "readlines",     # arq.ler_linhas()          → arq.readlines()

    # ── Escrita ──────────────────────────────────────────────────────────────
    "escrever":         "write",         # arq.escrever("texto")     → arq.write("texto")
    "escrever_linhas":  "writelines",    # arq.escrever_linhas(l)    → arq.writelines(l)

    # ── Controle ─────────────────────────────────────────────────────────────
    "fechar":           "close",         # arq.fechar()              → arq.close()
    "posicao":          "tell",          # arq.posicao()             → arq.tell()
    "posição":          "tell",
    "mover_para":       "seek",          # arq.mover_para(0)         → arq.seek(0)
    "liberar":          "flush",         # arq.liberar()             → arq.flush()
}

# Mapa unificado de todos os métodos para uso pelo transpilador
TODOS_METODOS: Dict[str, str] = {
    **METODOS_SEQUENCIAS,
    **METODOS_TEXTO,
    **METODOS_ARQUIVO,
}

TODAS_PALAVRAS_RESERVADAS: Set[str] = (
    set(PALAVRAS_CHAVE.keys())
    | set(FUNCOES_EMBUTIDAS.keys())
    | set(TODOS_METODOS.keys())
    | {
        "senao se", "senão se",
        "não em", "nao em",
        "é não", "eh não",
        "leia_inteiro", "leia_real", "leia_int", "leia_float",
    }
)

