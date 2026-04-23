import random
import bisect

lista = random.sample(range(1, 10001), 1000)
lista.sort()
print(lista)

algoritmo = int(input('Escolha o método: 1 para recursivo, 2 para iterativo, 3 para bisect: '))

#------------------------------------------------------------------------------------------------

if algoritmo == 1:
    def binary_search_1(arr, target, left=0, right=None):
        if right is None:
            right = len(arr) - 1
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_1(arr, target, mid +1, right)
        else:
            return binary_search_1(arr, target, left, mid - 1)

    numero_alvo = int(input('Escolha um numero da lista: '))
    print(f'o objeto esta na posição (index): {binary_search_1(lista, numero_alvo)}')

#------------------------------------------------------------------------------------------------

elif algoritmo == 2:
    def binary_search_2(arr_2, target_2):
        left_2 = 0
        right_2 = len(arr_2) - 1

        while left_2 <= right_2:
            mid = (left_2 + right_2) // 2
            if arr_2[mid] == target_2:
                return mid
            elif arr_2[mid] < target_2:
                left_2 = mid + 1
            else:
                right_2 = mid - 1
        return -1

    numero_alvo_2 = int(input('Escolha um numero da lista: '))
    print(f'o objeto esta na posição (index): {binary_search_2(lista, numero_alvo_2)}')

#------------------------------------------------------------------------------------------------

elif algoritmo == 3:
    numero_alvo_3 = int(input('Escolha um numero da lista: '))
    pos = bisect.bisect_left(lista, numero_alvo_3)
    if pos < len(lista) and lista[pos] == numero_alvo_3:
        print(f'O numero {numero_alvo_3} esta na posição {pos}')
    else:
        print('Numero nao encontrado')
else:
    pass
