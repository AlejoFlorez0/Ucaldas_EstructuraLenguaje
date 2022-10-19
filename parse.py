#!/usr/bin/env python
import sys
import argparse

from functions import parse_bnf, remove_left_recursion, remove_left_factoring


def doIt(gramatica, _lambda='λ', _eof='$'):

    print()
    print("Original:")
    g = parse_bnf(gramatica, _lambda=_lambda, _eof=_eof)
    print(g)

    print("\nDespués de remover Recursión izquierda:")
    g = remove_left_recursion(g)
    print(g)

    #vprint("\nAfter removing left-factoring:")
    g = remove_left_factoring(g)
    # vprint(g)

    firstsList = []
    followsList = []

    print()
    for nt in g.nonterminals:
        print('Primero({}) = {}'.format(nt, g.first(nt)))

        firstsList.append(
            {"name": '{}'.format(nt, g.first(nt)),
             "firsts": '{1}'.format(nt, g.first(nt))}
        )

    # print(firstsList)
    follow = [(nt, g.follow(nt)) for nt in g.nonterminals]

    print()
    for nt, f in follow:
        print('Siguiente({}) = {}'.format(nt, f))
        followsList.append(
            {"name": '{}'.format(nt, g.first(nt)),
             "follows": '{1}'.format(nt, g.first(nt))}
        )

    print("Lista de Primeros")
    print(firstsList)

    print("Lista de Siguientes")
    print(followsList)

    print()
    print('Tabla Predicción')
