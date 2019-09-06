import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def heap(lista, n, i):
  maior = i
  es = 2 * i + 1
  di = 2 * i + 2
  if es < n and lista[i] < lista[es]:
    maior = es
  if di < n and lista[maior] < lista[di]:
    maior = di
  if maior != i:
    lista[i], lista[maior] = lista[maior],lista[i]
    heap(lista, n, maior)

def HSort(lista):
  n = len(lista)
  for i in range(n, -1, -1):
    heap(lista, n, i)
  for i in range(n-1, 0, -1):
    lista[i], lista[0] = lista[0], lista[i]
    heap(lista, i, 0)


size = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = geraLista(s)
    time.append(timeit.timeit("HSort({})".format(lista),
                              setup="from __main__ import HSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "heapSort.png")