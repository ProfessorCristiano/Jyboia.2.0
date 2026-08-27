Corrigir:
1. Estrutura e Organização do Código
[] 1.1 Duplicação entre jyboia/ e jyboia/core/
Existem duas cópias praticamente idênticas dos mesmos módulos:

thonny/jyboia/transpiler.py ↔ thonny/jyboia/core/transpiler.py
thonny/jyboia/keywords.py ↔ thonny/jyboia/core/keywords.py
thonny/jyboia/sourcemap.py ↔ thonny/jyboia/core/sourcemap.py
thonny/jyboia/builtins_runtime.py ↔ thonny/jyboia/core/builtins_runtime.py
O core/ usa imports de jyboia.core.xxx (sem o prefixo thonny.), o que provavelmente não funciona quando executado dentro do Thonny. Essa duplicação gera manutenção dupla e risco de divergência.

Sugestão: Remover o diretório core/ e manter apenas thonny/jyboia/, ou refatorar core/ como a implementação canônica e fazer thonny/jyboia/ apenas re-exportar.

[] 1.2 Ausência de __init__.py com __version__
O pacote thonny/jyboia/ não expõe uma versão. Isso dificulta debugging e rastreamento.

2 Tabela de palavras Chave:
[] 2.1 Faltam as palavras chaves para funções de Listas/Tuplas/Dicionários. Implementar.

3. UX e Recursos
[] 3.1 Sem autocomplete para palavras-chave Jybóia
O Thonny tem autocomplete para Python. Não está claro se ele reconhece palavras-chave em português para auto-completar.

[] 3.2 Sem "modo didático" ou tour inicial
Para uma ferramenta educacional, falta um tutorial interativo ou tour que explique as palavras-chave disponíveis ao primeiro uso.

[] 3.3 Sem suporte para abrir e editar arquivos .py e derivados nativos do thonny. Não era para ter Suprimido era para ter mantido os dois formatos, tanto .jy, como .py.

[] 3.4 Sem exportação de código Python
O botão "Copiar Python" no preview existe, mas não há "Salvar como .py" independente para o aluno levar o código para outro ambiente.

[] 3.5 Sem suporte a temas escuros para keywords Jybóia
O realce de sintaxe usa as mesmas cores do Python. Palavras-chave em português poderiam ter cores diferenciadas para destacar a dualidade.

4. Infraestrutura e Manutenção
[] 4.1 Sem pyproject.toml ou setup.py
O projeto não tem configuração de empacotamento. Não é possível instalar via pip install.

Sugestão: Criar pyproject.toml para permitir instalação e distribuição. Incluíndo Script de instalação — ou um pip install -e ., ou um instalador que crie uma venv embutida

[] 4.2 Sem CI/CD
Não há pipeline de testes automáticos, linting ou type checking.

Sugestão: Adicionar GitHub Actions com pytest, mypy e ruff.

[] 4.3 Sem .gitignore adequado
Não há .gitignore visível na raiz. Arquivos __pycache__/ e .pyc podem ser commitados acidentalmente.

[] 4.4 PLANEJAMENTO_PROJETO.md desatualizado
O planejamento descreve uma arquitetura que parcialmente diverge da implementação atual (ex: o core/ existe mas não é descrito no planejamento).

[] 4.5 EMPACOTAMENTO DO PYTHON
Empacotamento do Python — para funcionar como o Thonny original (zero dependências para o usuário), seria necessário usar algo como PyInstaller, Nuitka, ou um instalador customizado que inclua o interpretador Python
