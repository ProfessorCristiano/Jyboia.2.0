"""
Testes unitários para o SourceMap e tradução de erros no Jybóia IDE.
"""

import unittest
from thonny.jyboia.sourcemap import SourceMap, mapear_traceback


class TestJyboiaSourceMap(unittest.TestCase):

    def test_remapeamento_traceback(self):
        sm = SourceMap(
            jy_code='escreva(10 / 0)',
            py_code='print(10 / 0)',
            jy_filepath="calculo.jy",
            py_filepath="calculo.py",
        )
        fake_tb = '''Traceback (most recent call last):
  File "calculo.py", line 1, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero'''

        tb_remapeado = mapear_traceback(fake_tb, sm)
        self.assertIn('File "calculo.jy", line 1', tb_remapeado)
        self.assertIn('Dica Jybóia [Divisão por Zero]', tb_remapeado)


if __name__ == "__main__":
    unittest.main()
