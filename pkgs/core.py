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
            "Noções Sobre Conjuntos e Funções",
            "Noções Sobre Conjuntos e Funções",
            "Conjuntos finitos: propriedades",
            "Conjuntos finitos: caracterização",
            "Conjuntos Infinitos enumeráveis",
            "Conjuntos Infinitos enumeráveis",
            "Conjuntos Infinitos enumeráveis",
            "O conjunto dos números reais como corpo ordenado",
            "Cotas superiores",
            "Supremo",
            "Postulado de Dedekind",
            "Não-enumerabilidade do conjunto dos números reais",
            "Aula de exercícios",
            "Avaliação 1",
            "Sequência de números reais: definição e convergência",
            "Sequencias monótonas e propriedades aritméticas de limites",
            "Sequencias de Cauchy e caracterização de convergência",
            "Sequencias de Cauchy e caracterização de convergência",
            "Séries Numéricas",
            "Séries absolutamente convergentes e testes de convergência",
            "Séries absolutamente convergentes e testes de convergência",
            "Pontos interiores e conjuntos abertos",
            "Conjuntos fechados, pontos de acumulação",
            "Conjuntos compactos",
            "Conjunto de Cantor",
            "Aula de exercícios",
            "Avaliação 2",
            "Limites de funções",
            "Propriedades de limites e limites da composta",
            "Propriedades de limites e limites da composta",
            "Limites Laterais",
            "Limites Laterais",
            "Limites Infinitos",
            "Limites no infinito",
            "Funções Contínuas",
            "Funções Contínuas",
            "Funções descontínuas",
            "Funções descontínuas",
            "Funções contínuas em intervalos",
            "Funções contínuas em intervalos",
            "Funções contínuas em compactos e o Teorema de Weiestrass",
            "Continuidade Uniforme",
            "Teorema da extensão contínua",
            "Aula de exercícios",
            "Avaliação 3",
            "Conclusão da disciplina",
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
            "Espaços métricos: Pseudo-métricas",
            "Funções Contínuas: Definição e exemplos",
            "Funções Contínuas: Propriedades elementares",
            "Funções Contínuas: Homeomorfismos",
            "Funções Contínuas: Métricas equivalentes",
            "Funções Contínuas: Transformações multilineares",
            "Topologia: Conjuntos abertos",
            "Topologia: Conjuntos abertos e continuidade",
            "Topologia: Espaços topológicos",
            "Topologia: Conjuntos fechados",
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
            "Continuidade uniforme: Observações e exemplos",
            "Espaços completos: Sequências de Cauchy",
            "Espaços completos: Espaços métricos completos",
            "Espaços completos: Espaços de Banach e espaços de Hilbert",
            "Espaços completos: Extensão de aplicações contínuas",
            "Espaços completos: Completamento de um espaço métrico",
            "Espaços completos: Espaços métricos topologicamente completos",
            "Espaços completos: O Teorema de Baire",
            "Espaços completos: O método das aproximações sucessivas",
            "Espaços compactos: Compacidade na reta",
            "Espaços compactos: Espaços métricos compactos",
            "Espaços compactos: Produtos de dois fatores, um dos quais é compacto",
            "Espaços compactos: Uma base para C(K,M)",
            "Espaços compactos: Caracterizações de espaços compactos",
            "Espaços compactos: Produtos cartesianos de espaços compactos",
            "Espaços compactos: Continuidade uniforme",
            "Espaços compactos: Espaços localmente compactos",
            "Espaços compactos: Espaços vetoriais normados de dimensão finita",
            "Espaços compactos: Equicontinuidade",
            "Espaços compactos: O Teorema de Stone-Weierstrass",
        ],  # }}}
        "shift": {  # {{{
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },  # }}}
        "fmean": {  # {{{
            1: date.fromisoformat("2024-04-21"),
            2: date.fromisoformat("2024-06-21"),
            3: date.fromisoformat("2024-07-15"),
        },  # }}}
    },
}


def pprint(DATE, TOPIC, outfile):  # {{{
    M = [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
    ]
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
        pcrono(opening, discipline["IME0415"], texfile)
        beancount(discipline["IME0415"])


if __name__ == "__main__":
    main()
