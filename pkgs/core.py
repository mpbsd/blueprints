#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import date, timedelta


lazy_days = [  # {{{
    date.fromisoformat("2024-03-29"),  # paixao de cristo
    date.fromisoformat("2024-04-08"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-10"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-12"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-21"),  # tiradentes
    date.fromisoformat("2024-05-01"),  # dia do trabalhador
    date.fromisoformat("2024-05-24"),  # padroeira de goiania
    date.fromisoformat("2024-05-30"),  # corpus christi
    date.fromisoformat("2024-05-31"),  # ponto facultativo corpus christi
]  # }}}


discipline = {
    "IME0388": {
        "dname": "Análise Real 1",
        "crono": [  # {{{
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
            "Noções Topológicas da reta real - pontos interiores e conjuntos abertos",
            "Noções Topológicas da reta real - conjuntos fechados e pontos de acumulação",
            "Noções Topológicas da reta real - conjuntos compactos",
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
        "shift": {  # {{{
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },  # }}}
    },
    "IME0415": {
        "dname": "Espaços Métricos",
        "crono": [  # {{{
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
        "shift": {  # {{{
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },  # }}}
    },
}


def pprint(DATE, TOPIC, outfile):  # {{{
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


def pcrono(opening, discipline, outfile):  # {{{
    DATE = opening
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
    opening = date.fromisoformat("2024-03-18")
    with open("blueprint.tex", "w") as texfile:
        pcrono(opening, discipline["IME0388"], texfile)
        beancount(discipline["IME0388"])


if __name__ == "__main__":
    main()
