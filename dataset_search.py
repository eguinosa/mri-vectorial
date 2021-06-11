# Gelin Eguinosa Rosique
# C-511

import time
import json
from corpus import Corpus


def dataset_search(docs_path, max_docs=10, min_sim=0.05):
    """
    Funcion encargada de interactuar con el usuario y realizar las consultas
    que este indique en la consola.
    :param docs_path: La ubicacion del .JSON con los documentos del corpus
    :param max_docs: Cantidad maxima de documentos relevantes que se pueden
    devolver por cada consulta
    :param min_sim: El valor minimo similaridad que debe tener un documento con
    una consulta para ser considerado relevante.
    """

    # Comenzar a calcular el tiempo de carga de los documentos
    start_time = time.time()

    # Cargar la informacion del .JSON en un diccionario
    f = open(docs_path)
    docs_data = json.load(f)
    f.close()

    # Save Corpus
    corpus = Corpus(docs_data)

    # Determinar el tiempo total de carga de los documentos
    interval = time.time() - start_time

    print(f"{corpus.doc_count} documents loaded ({interval} seconds)")
    print(f"{max_docs} maximum number of documents per query.")
    print(f"{min_sim} minimum similarity.")

    while True:
        print("\nPlease, enter your query (enter 'quit/q' to exit):")
        query = input()

        # Chequeando si el usuario quiere salir
        if query.lower() in {'q', 'quit'}:
            break

        # Realiza la busqueda de los documentos similares en el corpus
        start_time = time.time()
        docs_sim = corpus.query_process(query, max_docs, min_sim)
        finish_time = time.time()
        interval = finish_time - start_time

        # En caso que no se encuentren documentos relevantes
        if not docs_sim:
            print("\nNo relevant documents found. Try a different query.")
            continue

        # Imprime los resultados
        print("\nThis are the results of your query:")
        print(f"{len(docs_sim)} results ({interval} seconds)")
        for document, similarity in docs_sim:
            print(f"\n  Document {document.id}")
            print(f"  Title: {document.title}")
            print(f"  Author: {document.author}")
            print(f"  Similarity: {similarity}")
