#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, timedelta

# lazy_days {{{
lazy_days = [
    date.fromisoformat("2025-04-18"),  # Paixão de Cristo
    date.fromisoformat("2025-04-21"),  # Tiradentes
    date.fromisoformat("2025-05-01"),  # dia mundial do trabalho
    date.fromisoformat("2025-05-24"),  # Padroeira de Goiânia
    date.fromisoformat("2025-06-19"),  # Corpus Christi
]  # }}}

discipline = {
    "IME0379": {  # Cálculo 1B {{{1
        "dname": "Cálculo 1B",
        "crono": [  # {{{2
            "Apresentação da disciplina",
            "Funções: definição e domínio",
            "Funções definidas por partes",
            "Funções polinomiais e racionais",
            "Funções trigonométricas: gráficos e propriedades",
            "Propriedades e composição de funções",
            "Funções exponencial e logarítmica: gráficos e propriedades",
            "Os problemas da tangente e da velocidade",
            "Definição de limite e limites laterais",
            "Limites infinitos",
            "Propriedades e cálculos de limites",
            "Limites no infinito",
            "Continuidade",
            "Derivada: definição, velocidade instantânea e reta tangente",
            "Derivada como função. Diferenciabilidade e continuidade",
            "Aula de exercícios",
            "Avaliação 1",
            "Derivada de funções polinomiais e exponenciais",
            "Regras do produto e do quociente",
            "Derivada de funções trigonométricas",
            "Regra da cadeia",
            "Derivada de funções logarítmicas",
            "Valores Máximo e mínimo",
            "Intervalos de crescimento e decrescimento",
            "Concavidade e pontos de inflexão",
            "Formas indeterminadas e regra de L’Hospital",
            "Esboço de curvas",
            "Esboço de curvas - Continuação",
            "Problemas de otimização",
            "Problemas de otimização - Continuação",
            "Antiderivada",
            "Aula de exercícios",
            "Avaliação 2",
        ],  # }}}
        "shift": {  # {{{2
            3: timedelta(days=2),
            5: timedelta(days=5),
        },  # }}}
    },  # }}}
    "IME0388": {  # Análise Real {{{1
        "dname": "Análise Real 1",
        "crono": [  # {{{2
            "Apresentação da disciplina",
            "Noções de Conjuntos",
            "Noções de Funções",
            "O conjunto dos números naturais e os axiomas de Peano",
            "Conjuntos finitos e suas propriedades",
            "Conjuntos finitos, infinitos e enumeráveis",
            "Conjuntos Infinitos e enumeráveis",
            "O conjunto dos números reais como corpo ordenado",
            "Supremos e ínfimos em um corpo ordenado",
            "A incompletude dos Racionais e o Postulado de Dedekind",
            "Densidade dos Racionais",
            "Não enumerabilidade do conjunto dos números reais",
            "Aula de exercícios",
            "Avaliação 1",
            "Sequência de números reais",
            "Sequencias monótonas e propriedades aritméticas de limites",
            "Sequencias especiais e o número de Euler",
            "O Teorema de Bolzano Weierstrass e lim sup e lim inf",
            "Sequencias de Cauchy e caracterização de convergência",
            "Limites infinitos",
            "Séries Numéricas",
            "Teste da comparação, serie p e Teorema de Leibniz para",
            "Séries alternadas",
            "Séries absolutamente convergentes e testes de convergência",
            "Pontos interiores e conjuntos abertos",
            "Conjuntos fechados e pontos de acumulação",
            "Conjuntos compactos",
            "O Conjunto de Cantor",
            "Aula de exercícios",
            "Avaliação 2",
            "Limites de funções",
            "Limites de funções",
            "Limites Laterais",
            "Propriedades de limites e limites da composta",
            "Limites Laterais",
            "Limites Laterais em funções monótonas e Limites Infinitos",
            "Limites no infinito",
            "Funções Contínuas",
            "Funções Contínuas",
            "Um pouco mais sobre descontinuidades",
            "Funções contínuas em intervalos",
            "Funções contínuas em compactos e o Teorema de Weiestrass",
            "Continuidade Uniforme",
            "Teorema da extensão contínua",
            "Aula de exercícios",
            "Avaliação 3",
            "Entrega de resultados",
        ],  # }}}
        "shift": {  # {{{2
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },  # }}}
    },  # }}}
    "IME0415": {  # Espaços Métricos {{{1
        "dname": "Espaços Métricos",
        "crono": [  # {{{2
            "Espaços métricos: Definição e exemplos",
            "Espaços métricos: Bolas e esferas",
            "Espaços métricos: Conjuntos limitados",
            "Espaços métricos: Distânica entre conjuntos",
            "Espaços métricos: Isometrias",
            "Funções Contínuas: Definição e exemplos",
            "Funções Contínuas: Propriedades elementares",
            "Funções Contínuas: Homeomorfismos",
            "Funções Contínuas: Métricas equivalentes",
            "Funções Contínuas: Transformações multilineares",
            "Topologia: Conjuntos abertos",
            "Topologia: Conjuntos abertos e continuidade",
            "Topologia: Espaços topológicos",
            "Topologia: Conjuntos fechados",
            "Avaliação 1",
            "Conjuntos conexos: Definição e exemplos",
            "Conjuntos conexos: Propriedades dos conjuntos conexos",
            "Conjuntos conexos: Conexidade por caminhos",
            "Conjuntos conexos: Componentes conexas",
            "Conjuntos conexos: A conexidade como invariante topológico",
            "Limites: Limites de sequências",
            "Limites: Sequências de números reais",
            "Limites: Séries",
            "Limites: Convergência e topologia",
            "Limites: Sequências de funções",
            "Limites: Produtos cartesianos infinitos",
            "Limites: Limites de funções",
            "Continuidade uniforme",
            "Avaliação 2",
            "Espaços completos: Sequências de Cauchy",
            "Espaços completos: Espaços métricos completos",
            "Espaços completos: Espaços de Banach e espaços de Hilbert",
            "Espaços completos: Extensão de aplicações contínuas",
            "Espaços completos: O Teorema de Baire",
            "Espaços completos: O método das aproximações sucessivas",
            "Espaços compactos: Compacidade na reta",
            "Espaços compactos: Espaços métricos compactos",
            "Espaços compactos: Produto Cartesiano por um fator Compacto",
            "Espaços compactos: Uma base para C(K,M)",
            "Espaços compactos: Caracterizações de espaços compactos",
            "Espaços compactos: Produtos cartesianos de espaços compactos",
            "Espaços compactos: Continuidade uniforme",
            "Espaços compactos: Espaços localmente compactos",
            "Espaços compactos: Espaços vetoriais normados de dimensão finita",
            "Espaços compactos: Equicontinuidade",
            "Espaços compactos: O Teorema de Stone-Weierstrass",
            "Avaliação 3",
        ],  # }}}
        "shift": {  # {{{2
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },  # }}}
    },  # }}}
    "IME0416": {  # Teoria de Galois {{{1
        "dname": "Teoria de Galois",
        "crono": [  # {{{2
            "Corpos e Corpo de decomposição de um polinômio",
            "Corpos e Corpo de decomposição de um polinômio",
            "Revisão de extensões de corpos",
            "Extensões normais e separáveis",
            "Extensões normais e separáveis",
            "Grupos de Galois e extensões galoisianas",
            "Grupos de Galois e extensões galoisianas",
            "Grupos de Galois e extensões galoisianas",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Teorema Fundamental da Teoria de Galois",
            "Revisão de grupos solúveis e solubilidade por radicais",
            "Revisão de grupos solúveis e solubilidade por radicais",
            "Revisão de grupos solúveis e solubilidade por radicais",
            "Corpos finitos",
            "Corpos finitos",
            "Corpos finitos",
            "Corpos finitos",
            "Extensões ciclotômicas",
            "Extensões ciclotômicas",
            "Extensões ciclotômicas",
            "Construções por régua e compasso",
            "Teorema Fundamental da Álgebra",
            "Norma e traço",
            "Apresentação de exercícios",
            "Apresentação de exercícios",
            "Avaliação",
            "Avaliação",
        ],  # }}}
        "shift": {  # {{{2
            2: timedelta(days=2),
            4: timedelta(days=5),
        },  # }}}
    },  # }}}
}


# def pprint {{{
def pprint(DATE, TOPIC, outfile):
    M = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez",
    }
    W = ["Do", "Se", "Te", "Qa", "Qi", "Sx", "Sa"]
    y = DATE.year
    m = M[DATE.month]
    d = "%02d" % DATE.day
    w = W[DATE.isoweekday() % 7]
    R = f"\\item[({w}) {d}/{m}/{y}] {TOPIC}"
    print(R, file=outfile)


# }}}


# def pcrono {{{
def pcrono(opening, discipline, outfile):
    DATE = opening
    if (DATE.isoweekday() % 7) not in discipline["shift"].keys():
        while (DATE.isoweekday() % 7) not in discipline["shift"].keys():
            DATE += timedelta(days=1)
    for TOPIC in discipline["crono"]:
        if DATE in lazy_days:
            while DATE in lazy_days:
                DATE += discipline["shift"][DATE.isoweekday() % 7]
        pprint(DATE, TOPIC, outfile)
        DATE += discipline["shift"][DATE.isoweekday() % 7]


# }}}


def beancount(discipline):  # {{{
    print(2 * len(discipline["crono"]))


# }}}


def main():
    opening = date.fromisoformat("2025-03-06")

    for dkey in ["IME0379", "IME0416"]:
        dscpln = discipline[dkey]
        with open(f"{dkey}.tex", "w") as texfile:
            pcrono(opening, dscpln, texfile)
            beancount(dscpln)


if __name__ == "__main__":
    main()
