#!/usr/bin/env python
import sys
import argparse


from functions import parse_bnf, remove_left_recursion, remove_left_factoring, predictionSet, isll1, pprint_table


def doIt(gramatica, _lambda='λ', _eof='$'):

    print()
    print("Original:")
    g = parse_bnf(gramatica, _lambda=_lambda, _eof=_eof)
    print(g)

    print("\nDespués de remover Recursión izquierda:")
    g = remove_left_recursion(g)
    print(g)

    #print("\nAfter removing left-factoring:")
    g = remove_left_factoring(g)
    # print(g)

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

    print()
    print("Lista de Primeros")
    print(firstsList)

    print()
    print("Lista de Siguientes")
    print(followsList)

    predictionTable = g.grammarwithoutRecursion()
    PredicSet = predictionSet(predictionTable, firstsList, followsList)
    print()
    print("El conjunto Prediccion: ")
    print(PredicSet)
    isll1(PredicSet)

    print()
    print('Tabla Impresión')
    impresionTable, ambiguous = g.parsing_table()
    if ambiguous:
        print(
            "El lenguaje de entrada no es LL(1) debido a que se encontraron ambigüedades.")

    pprint_table(g, impresionTable)

    print("Alejandro González Flórez")
    print("Marlon Stiven Aristizabal Herrera")
    print("Jeronimo Toro Calvo")
