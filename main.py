# Gelin Eguinosa Rosique
# C-511

from dataset_search import dataset_search
from dataset_test import dataset_test

if __name__ == '__main__':

    # Ubicaciones de las colecciones de prueba
    cisi_docs_path = 'files/CISI.ALL.json'
    cisi_answers_path = 'files/CISI.REL.json'
    cisi_queries_path = 'files/CISI.QRY.json'
    cran_docs_path = 'files/CRAN.ALL.json'
    cran_answers_path = 'files/CRAN.REL.json'
    cran_queries_path = 'files/CRAN.QRY.json'

    # Tipo de MRI y autor
    print("\nInformation Retrieval Project - Vector Space Model")
    print("Gelin Eguinosa Rosique C-511\n")

    # Colecciones de Prueba disponibles
    print("Available Datasets:")
    print("  1. CISI - University of Glasgow")
    print("  2. Cranfield - Cranfield University\n")

    # Las acciones que se pueden realizar en la consola
    print("Options: ")
    print("  1. To load the CISI corpus (enter '1/cisi')")
    print("  2. To load the Cranfield corpus (enter '2/cranfield')")
    print("  3. To evaluate the Model with the CISI dataset (enter '3/cisi test')")
    print("  4. To evaluate the Model with the Cranfield dataset (enter '4/cranfield test')\n")

    # Pregunta cual coleccion de prueba se va a usar
    dataset = input("Please, enter the option you would like to do: ")
    dataset = dataset.lower()
    if dataset in {'1', 'cisi'}:
        print("\nLoading CISI dataset...")
        dataset_search(cisi_docs_path)
    elif dataset in {'2', 'cran', 'cranfield'}:
        print("\nLoading Cranfield dataset...")
        dataset_search(cran_docs_path)
    elif dataset in {'3', 'cisi test'}:
        print("\nEvaluating the Model using the CISI dataset.")
        dataset_test(cisi_docs_path, cisi_queries_path, cisi_answers_path)
    elif dataset in {'4', 'cran test', 'cranfield test'}:
        print("\nEvaluating the Model using the Cranfield dataset.")
        dataset_test(cran_docs_path, cran_queries_path, cran_answers_path)
    else:
        # No se especifico ninguna coleccion de prueba
        print("No supported action specified.\nClosing Program.")
