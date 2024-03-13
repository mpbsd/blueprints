#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import date, timedelta


non_labor_days = [
    date.fromisoformat("2024-03-29"),  # paixao de cristo
    date.fromisoformat("2024-04-08"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-10"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-12"),  # vii coloquio do centro-oeste
    date.fromisoformat("2024-04-21"),  # tiradentes
    date.fromisoformat("2024-05-01"),  # dia do trabalhador
    date.fromisoformat("2024-05-24"),  # padroeira de goiania
    date.fromisoformat("2024-05-30"),  # corpus christi
    date.fromisoformat("2024-05-31"),  # ponto facultativo corpus christi
]


discipline = {
    "analise_real_1": {
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
        "shift": {
            1: timedelta(days=2),
            3: timedelta(days=2),
            5: timedelta(days=3),
        },
    },
}


def printcrono(discipline, opening):
    Date = opening
    for C in discipline["crono"]:
        if Date in non_labor_days:
            while Date in non_labor_days:
                Date += discipline["shift"][Date.isoweekday() % 7]
        print(Date, C)
        Date += discipline["shift"][Date.isoweekday() % 7]


def main():
    opening = date.fromisoformat("2024-03-18")
    printcrono(discipline["analise_real_1"], opening)


if __name__ == "__main__":
    main()
