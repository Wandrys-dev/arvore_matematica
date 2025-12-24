"""
Árvore de Natal Matemática
Autor: Wandrys-dev
Data: Dezembro 2025

Um gerador de árvores de Natal usando conceitos matemáticos:
- Progressão geométrica para crescimento
- Funções trigonométricas para naturalidade
- Sequência de Fibonacci para decoração
- Mapeamento senoidal para cores
"""

import math
from typing import List, Tuple

class ArvoreMatematica:
    """Classe principal para geração da árvore de Natal matemática"""
    
    def __init__(self, altura: int = 20):
        """
        Inicializa o gerador de árvore
        
        Args:
            altura: Altura total da árvore em linhas
        """
        self.altura = altura
        self.configurar_parametros()
    
    def configurar_parametros(self):
        """Configura os parâmetros matemáticos da árvore"""
        # Constantes matemáticas ajustáveis
        self.TAXA_CRESCIMENTO = 1.25
        self.AMPLITUDE = 1.5
        self.FREQUENCIA = 0.8
        self.BASE_LARGURA = 2.2
        
        # Sequência de Fibonacci para enfeites
        self.fibonacci = self.gerar_fibonacci(8)
        
        # Paleta de cores ANSI
        self.cores = {
            'verde': '\033[92m',
            'vermelho': '\033[91m',
            'amarelo': '\033[93m',
            'azul': '\033[94m',
            'magenta': '\033[95m',
            'reset': '\033[0m'
        }
    
    @staticmethod
    def gerar_fibonacci(n: int) -> List[int]:
        """Gera os primeiros n números da sequência de Fibonacci"""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def calcular_largura(self, linha: int) -> int:
        """
        Calcula a largura da linha usando progressão geométrica + seno
        
        Fórmula: L(n) = 1 + B × (rⁿ - 1) + A × sin(ω × n)
        """
        # Termo de crescimento geométrico
        termo_geometrico = self.BASE_LARGURA * (
            math.pow(self.TAXA_CRESCIMENTO, linha) - 1
        )
        
        # Termo oscilatório (seno)
        termo_oscilatorio = self.AMPLITUDE * math.sin(self.FREQUENCIA * linha)
        
        # Largura total
        largura = 1 + int(termo_geometrico + termo_oscilatorio)
        
        # Garantir largura mínima e ímpar para simetria
        return max(3, largura if largura % 2 == 1 else largura + 1)
    
    def eh_posicao_enfeite(self, linha: int, coluna: int) -> bool:
        """Determina se uma posição deve ter enfeite baseado em Fibonacci"""
        if linha < 2 or linha > self.altura - 5:
            return False
        
        # Usar posição relativa na sequência de Fibonacci
        pos_relativa = (linha * 7 + coluna * 3) % 13
        return pos_relativa in [f % 13 for f in self.fibonacci if f > 0]
    
    def obter_cor_enfeite(self, linha: int, coluna: int) -> str:
        """Determina a cor do enfeite baseado em função senoidal"""
        # Função senoidal para variação suave de cores
        valor = math.sin(linha * 0.3 + coluna * 0.2) * 2 + math.cos(linha * 0.1)
        
        # Mapear para índice de cor
        idx = int((valor + 2) * 1.5) % 5
        
        cores_lista = [
            self.cores['vermelho'],
            self.cores['amarelo'],
            self.cores['azul'],
            self.cores['magenta'],
            self.cores['verde']
        ]
        
        return cores_lista[idx]
    
    def gerar_arvore(self) -> List[str]:
        """Gera a árvore completa como lista de strings"""
        arvore = []
        
        # Estrela no topo
        padding_estrela = (self.altura * 2 - 1) // 2
        arvore.append(f"{' ' * padding_estrela}{self.cores['amarelo']}★{self.cores['reset']}")
        
        # Galhos principais
        for linha in range(1, self.altura - 2):
            largura = self.calcular_largura(linha)
            padding = (self.altura * 2 - largura) // 2
            
            linha_str = []
            for col in range(self.altura * 2):
                if padding <= col < padding + largura:
                    if self.eh_posicao_enfeite(linha, col):
                        cor = self.obter_cor_enfeite(linha, col)
                        linha_str.append(f"{cor}o{self.cores['reset']}")
                    elif (linha + col) % 3 == 0:
                        linha_str.append(f"{self.cores['verde']}^{self.cores['reset']}")
                    else:
                        linha_str.append(f"{self.cores['verde']}*{self.cores['reset']}")
                else:
                    linha_str.append(" ")
            
            arvore.append("".join(linha_str))
        
        # Tronco
        padding_tronco = self.altura - 3
        for _ in range(3):
            arvore.append(f"{' ' * padding_tronco}{self.cores['verde']}███{self.cores['reset']}")
        
        return arvore
    
    def imprimir_arvore(self):
        """Imprime a árvore no terminal"""
        print("\n" + "=" * 60)
        print("🎄 ÁRVORE DE NATAL MATEMÁTICA 🎄".center(60))
        print("=" * 60 + "\n")
        
        for linha in self.gerar_arvore():
            print(linha)
        
        print("\n" + "=" * 60)
        print("Fórmulas aplicadas:".center(60))
        print(f"L(n) = 1 + {self.BASE_LARGURA} × ({self.TAXA_CRESCIMENTO}ⁿ - 1)".center(60))
        print(f"+ {self.AMPLITUDE} × sin({self.FREQUENCIA} × n)".center(60))
        print("=" * 60)

def main():
    """Função principal"""
    try:
        # Criar árvore com altura personalizável
        altura = 22  # Pode ser ajustado
        arvore = ArvoreMatematica(altura)
        arvore.imprimir_arvore()
        
        # Mensagem de Natal
        print("\n" + "🎅 FELIZ NATAL! 🎁".center(60))
        print("Que seu código sempre compile".center(60))
        print("e seus bugs sejam raros!".center(60))
        print("\n")
        
    except Exception as e:
        print(f"Erro ao gerar árvore: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())