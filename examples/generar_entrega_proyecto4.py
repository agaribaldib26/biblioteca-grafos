import csv
import math
import random
from pathlib import Path

from src.grafos.generadores import (
    grafoMalla,
    grafoErdosRenyi,
    grafoGilbert,
    grafoGeografico,
    grafoBarabasiAlbert,
    grafoDorogovtsevMendes,
)

random.seed(42)

BASE = Path('output/proyecto4')
CARPETAS = {
    'generados': BASE / 'gv' / 'generados',
    'kruskal_d': BASE / 'gv' / 'kruskal_d',
    'kruskal_i': BASE / 'gv' / 'kruskal_i',
    'prim': BASE / 'gv' / 'prim',
}
for carpeta in CARPETAS.values():
    carpeta.mkdir(parents=True, exist_ok=True)
for categoria in CARPETAS:
    (BASE / 'imagenes' / categoria).mkdir(parents=True, exist_ok=True)
(BASE / 'capturas').mkdir(parents=True, exist_ok=True)

MODELOS = [
    'malla',
    'erdos_renyi',
    'gilbert',
    'geografico',
    'barabasi_albert',
    'dorogovtsev_mendes',
]
TAMANOS = [30, 500]

def generar_grafo(modelo, n):
    if modelo == 'malla':
        return grafoMalla(5, 6) if n == 30 else grafoMalla(20, 25)
    if modelo == 'erdos_renyi':
        return grafoErdosRenyi(n, 4 * n)
    if modelo == 'gilbert':
        return grafoGilbert(n, min(0.30, 8 / (n - 1)))
    if modelo == 'geografico':
        radio = math.sqrt(12 / (math.pi * (n - 1)))
        return grafoGeografico(n, radio)
    if modelo == 'barabasi_albert':
        return grafoBarabasiAlbert(n, 3)
    if modelo == 'dorogovtsev_mendes':
        return grafoDorogovtsevMendes(n)
    raise ValueError(f'Modelo desconocido: {modelo}')

def es_conexo(grafo):
    if not grafo.nodos:
        return False
    adyacencias = {nodo_id: [] for nodo_id in grafo.nodos}
    for arista in grafo.aristas:
        u, v = arista.origen.id, arista.destino.id
        adyacencias[u].append(v)
        adyacencias[v].append(u)
    inicio = next(iter(grafo.nodos))
    visitados = {inicio}
    pila = [inicio]
    while pila:
        actual = pila.pop()
        for vecino in adyacencias[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                pila.append(vecino)
    return len(visitados) == len(grafo.nodos)

def asignar_pesos(grafo):
    for arista in grafo.aristas:
        arista.peso = round(random.uniform(1, 100), 2)


def peso_total(grafo):
    return sum(arista.peso for arista in grafo.aristas)

def procesar(modelo, n):
    for _ in range(20):
        grafo = generar_grafo(modelo, n)
        if es_conexo(grafo):
            break
    else:
        raise ValueError(f'No se obtuvo un grafo conexo: {modelo}_{n}')

    asignar_pesos(grafo)
    resultados = {
        'kruskal_d': grafo.KruskalD(),
        'kruskal_i': grafo.KruskalI(),
        'prim': grafo.Prim(),
    }
    pesos = {metodo: peso_total(mst) for metodo, mst in resultados.items()}
    referencia = pesos['kruskal_d']

    for metodo, mst in resultados.items():
        if (len(mst.nodos) != n
                or len(mst.aristas) != n - 1
                or not es_conexo(mst)):
            raise AssertionError(f'Arbol invalido: {modelo}_{n}, {metodo}')
        if not math.isclose(pesos[metodo], referencia,
                            rel_tol=0.0, abs_tol=1e-6):
            raise AssertionError(f'Pesos distintos: {modelo}_{n}, {metodo}')

    nombre = f'{modelo}_{n}'
    grafo.guardar_gv(
        str(CARPETAS['generados'] / f'{nombre}.gv'),
        mostrar_pesos=True,
    )
    for metodo, mst in resultados.items():
        mst.guardar_gv(
            str(CARPETAS[metodo] / f'{nombre}_{metodo}.gv'),
            mostrar_pesos=True,
        )

    linea = (
        f'{nombre}: '
        f"KruskalD={pesos['kruskal_d']:.2f} | "
        f"KruskalI={pesos['kruskal_i']:.2f} | "
        f"Prim={pesos['prim']:.2f} | OK"
    )
    return {
        'modelo': modelo,
        'nodos': n,
        'aristas_original': len(grafo.aristas),
        'peso_kruskal_d': f"{pesos['kruskal_d']:.2f}",
        'peso_kruskal_i': f"{pesos['kruskal_i']:.2f}",
        'peso_prim': f"{pesos['prim']:.2f}",
    }, linea

def main():
    filas = []
    lineas = ['RESULTADOS DEL PROYECTO 4 - PESOS DEL MST', '']
    for modelo in MODELOS:
        for n in TAMANOS:
            fila, linea = procesar(modelo, n)
            filas.append(fila)
            lineas.append(linea)
            print(linea)

    csv_path = BASE / 'resultados_mst.csv'
    with csv_path.open('w', encoding='utf-8-sig', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=filas[0].keys())
        writer.writeheader()
        writer.writerows(filas)

    txt_path = BASE / 'pesos_mst.txt'
    txt_path.write_text('\n'.join(lineas) + '\n', encoding='utf-8')
    total = sum(len(list(carpeta.glob('*.gv')))
                for carpeta in CARPETAS.values())
    print(f'\nArchivos .gv del proyecto 4: {total}')
    print(f'Resumen de pesos: {txt_path}')
    print(f'Tabla de resultados: {csv_path}')


if __name__ == '__main__':
    main()

