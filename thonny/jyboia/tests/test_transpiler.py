"""
Testes unitários para o transpilador thonny.jyboia.
"""

import ast
import unittest
from thonny.jyboia.transpiler import transpilar


class TestJyboiaTranspiler(unittest.TestCase):

    def test_ola_mundo(self):
        codigo_jy = 'escreva("Olá, Jybóia IDE!")'
        codigo_py, _ = transpilar(codigo_jy)
        self.assertEqual(codigo_py.strip(), 'print("Olá, Jybóia IDE!")')
        ast.parse(codigo_py)

    def test_estruturas_condicionais(self):
        codigo_jy = """se nota >= 7:
    escreva("Aprovado")
senaose nota >= 5:
    escreva("Recuperação")
senao:
    escreva("Reprovado")
"""
        codigo_py, _ = transpilar(codigo_jy)
        esperado = """if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
"""
        self.assertEqual(codigo_py, esperado)
        ast.parse(codigo_py)

    def test_lacos_e_funcoes(self):
        codigo_jy = """funcao calcular_fatorial(n):
    se n <= 1:
        retorne 1
    total = 1
    para i em intervalo(2, n + 1):
        total = total * i
    retorne total

res = calcular_fatorial(5)
escreva("Fatorial de 5:", res)
"""
        codigo_py, _ = transpilar(codigo_jy)
        esperado = """def calcular_fatorial(n):
    if n <= 1:
        return 1
    total = 1
    for i in range(2, n + 1):
        total = total * i
    return total

res = calcular_fatorial(5)
print("Fatorial de 5:", res)
"""
        self.assertEqual(codigo_py, esperado)
        ast.parse(codigo_py)

    def test_preservacao_strings(self):
        codigo_jy = 'frase = "se voce quiser esta funcao nao quebra"'
        codigo_py, _ = transpilar(codigo_jy)
        self.assertEqual(codigo_py, 'frase = "se voce quiser esta funcao nao quebra"')


if __name__ == "__main__":
    unittest.main()
