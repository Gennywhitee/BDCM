import pandas as pd
import os

PATH_SEPARATOR = os.sep

def printFrequency(df):  # CONTROLLO SUL BILANCIAMENTO DEI DATI

    # Numero di elementi per la classe 'Donating'
    print("Donating blood:", len(df[(df['Class'] == 1)]))

    # Numero di elementi per la classe 'Not Donating'
    print("Not donating blood:", len(df[(df['Class'] == 0)]))

    # Totale
    print("Total:", len(df))


# Abbiamo un numero maggiore per la classe positiva (PROBABILE BILANCIAMENTO?!)

def printNullValues(df):    # Verifico se e quanti valori nulli esistono attraverso
                            # la funzione isna() di pandas per trovarli e sum() per contarli

    nan_present = df.isna()
    nan_count = nan_present.sum()

    print(nan_count)

# Confermata la presenza di valori nulli nel dataset
