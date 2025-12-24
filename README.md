# 🎄 Árvore de Natal Matemática

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

✨ Um gerador de árvores de Natal no terminal usando conceitos matemáticos avançados

## 🚀 Demonstração

![Demo da Árvore](assets/demo.gif)

## 📊 Fórmulas Matemáticas Implementadas

| Conceito | Fórmula | Aplicação |
|----------|---------|-----------|
| **Progressão Geométrica** | `L(n) = 1 + 2.2 × (1.25ⁿ - 1)` | Crescimento dos galhos |
| **Ondulação Senoidal** | `O(n) = 1.5 × sin(0.8n)` | Naturalidade da árvore |
| **Distribuição Fibonacci** | `P = Fₖ mod (2h)` | Posicionamento de enfeites |
| **Mapeamento de Cores** | `C(x,y) = palette[⌊(sin(x/2+y/3)+1)×2⌋ mod 6]` | Transição suave de cores |

## 🛠️ Instalação e Uso

### Pré-requisitos
```bash
python --version  # Python 3.8 ou superior


Execução Básica
bash
# Clone o repositório
git clone https://github.com/Wandrys-dev/arvore_matematica.git
cd arvore-matematica

# Execute o programa
python src/arvore_matematica.py
Personalização
python
# Exemplo: Árvore personalizada
from src.arvore_matematica import criar_arvore_personalizada

# Árvore com altura específica
criar_arvore_personalizada(altura=25, 
                           amplitude=3.0,
                           frequencia=0.6)
🧮 Conceitos Matemáticos Explorados
1. Crescimento Exponencial
python
# Modelo do crescimento dos galhos
def crescimento_galho(n):
    return base * (taxa ** n - 1) / (taxa - 1)
2. Padrões Fractais
Triângulo de Sierpinski para decoração

Auto-similaridade em diferentes escalas

3. Otimização Geométrica
Cálculo eficiente de padding central

Distribuição proporcional de elementos

🎨 Recursos
✅ Árvore gerada dinamicamente com parâmetros ajustáveis

✅ Sistema de cores ANSI para terminal

✅ Mensagem "FELIZ NATAL" com formatação matemática

✅ Explicação detalhada das fórmulas utilizadas

✅ Código modular e bem documentado

📈 Aplicações Práticas
Este projeto demonstra como conceitos matemáticos são aplicados em:

Computação Gráfica: Geração procedural de formas

Data Visualization: Representação visual de funções

Game Development: Criação de ambientes naturais

Educational Tools: Ensino de matemática através de código

🧪 Testes
bash
# Executar testes unitários
python -m pytest tests/
🤝 Contribuindo
Faça um Fork do projeto

Crie uma Branch (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add AmazingFeature')

Push para a Branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📝 Licença
Distribuído sob licença MIT. Veja LICENSE para mais informações.

📧 Contato
Wandrys - @wandrys_dev

Link do Projeto: https://github.com/Wandrys-dev/arvore_matematica

🙏 Agradecimentos
Inspirado pela beleza da matemática na natureza

Comunidade Python por ferramentas incríveis

Professores que mostram que matemática pode ser divertida

text

---

## **2. LICENSE (Licença MIT)**

```text
MIT License

Copyright (c) 2025 Wandrys-dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
