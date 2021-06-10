# Gelin Eguinosa Rosique
# C-511

import json
import time
from corpus import Corpus

if __name__ == '__main__':

    # Open JSON file.
    f = open('example1.json')
    # Get the JSON object as a dictionary.
    data = json.load(f)
    # Close file
    f.close()

    # Save Corpus
    start_time = time.time()
    corpus = Corpus(data)
    finish_time = time.time()

    print(f"Time to charge the corpus: {finish_time - start_time}")

    while True:
        print("\nPlease, enter your query (enter 'quit/q' to exit):")
        query = input()

        # Chequeando si el usuario quiere salir
        if query.lower() in {'q', 'quit'}:
            break

        # Realiza la busqueda de los documentos similares en el corpus
        docs_sim = corpus.query_process(query)

        # En caso que no se encuentren documentos relevantes
        if not docs_sim:
            print("\nNo relevant documents found. Try a different query.")
            continue

        # Imprime los resultados
        print("\nThis are the results of your query:")
        for document, similarity in docs_sim:
            print(f"\n  Document {document.id}")
            print(f"  Title: {document.title}")
            print(f"  Author: {document.author}")
            print(f"  Similarity: {similarity}")
