# Gelin Eguinosa Rosique
# C-511

import json
import time
import sys
from corpus import Corpus

if __name__ == '__main__':

    # Tipo de MRI y autor
    print("Information Retrieval Project - Vector Space Model")
    print("Gelin Eguinosa Rosique C-511\n")

    # Colecciones de Prueba disponibles
    print("Available Datasets:")
    print("  1. Cranfield - Cranfield University (enter '1/Cranfield' to load)")
    print("  2. CISI - University of Glasgow (enter '2/CISI' to load)\n")

    # Pregunta cual coleccion de prueba se va a usar
    dataset = input("Please, enter the dataset you would like to use: ")
    dataset = dataset.lower()
    if dataset in {'1', 'cran', 'cranfield'}:
        path_dataset = 'files/CRAN.ALL.json'
        print("\nLoading Cranfield dataset...")
    elif dataset in {'2', 'cisi'}:
        path_dataset = 'files/CISI.ALL.json'
        print("\nLoading CISI dataset...")
    else:
        # No se especifico ninguna coleccion de prueba
        print("No dataset specified.\nClosing Program.")
        sys.exit()

    # Open JSON file.
    f = open(path_dataset)
    # Get the JSON object as a dictionary.
    data = json.load(f)
    # Close file
    f.close()

    # Save Corpus
    start_time = time.time()
    corpus = Corpus(data)
    finish_time = time.time()
    interval = finish_time - start_time

    print(f"{corpus.doc_count} documents loaded ({interval} seconds)")

    while True:
        print("\nPlease, enter your query (enter 'quit/q' to exit):")
        query = input()

        # Chequeando si el usuario quiere salir
        if query.lower() in {'q', 'quit'}:
            break

        # Realiza la busqueda de los documentos similares en el corpus
        start_time = time.time()
        docs_sim = corpus.query_process(query)
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
