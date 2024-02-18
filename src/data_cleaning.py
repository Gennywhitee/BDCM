import matplotlib.pyplot as plt
import pandas as pd
import os
import re

PATH_SEPARATOR = os.sep


def dividiName(df):
    """
    Dalla fase di data_understing è sorto che la colonna 'Name' sembra contenere più informazioni insieme:
    cognome, titolo e nome.

    Inoltre le features 'Age' e 'Monetary' presentano dei valori mancanti. In particolare 'Age' in modo considerevole (153 e 10 per 'Monetary').

    Non meno importante è lo sbilanciamento della feature 'Class'!
    """

    # Sostituisco tutti i valori '2' con '0' nella colonna 'Class' per le persone che non hanno donato
    df['Class'] = df['Class'].replace(2, 0)

    # OPERAZIONE SULLE FEATURE
    # Divido la colonna Name in due: Surname e Title
    # Definisco una funzione lamba che applica la funzione split() su una stringa e ritorna il primo valore della separazione
    df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
    # Check
    # print(df['Surname'])

    # In questo caso la labda cerca un pattern, definito tramite espressione regolare, e se trova un match, restituisce il primo gruppo, ossia quello tra parentesi ()
    df['Title'] = df['Name'].apply(
        lambda x: re.search(r',\s*([^\.]+)\.', x).group(1) if re.search(r',\s*([^\.]+)\.', x) else None)

    # Elimino la vecchia colonna
    df.drop(['Name'], axis=1, inplace=True)

    return df


""" DA RIPORARTARE NEL MAIN
# Visualizzo i risultati ottenuti e quanti valori si ottengono per ciascun titolo
print(df['Title'].value_counts())
"""

"""Molti titoli sono ripetuti solo una o due volte, quindi potrebbero non essere molto utili.
Inoltre, alcune categorie possono essere unite, come Mme sinonimo di Mrs (fanno riferimento a donne sposate)
e Ms e Mlle sinonimi di Miss (fanno riferimento a donne non sposate)"""


def redistribuzioneCategorie(df):
    # Itero il dataset per redistribuire le diverse categorie
    for i, row in df.iterrows():
        title = row['Title']
        if title == 'Mme':
            df.loc[i, 'Title'] = 'Mrs'
        elif title == 'Ms' or title == 'Mlle':
            df.loc[i, 'Title'] = 'Miss'
        elif title != 'Mrs' and title != 'Miss' and title != 'Master' and title != 'Mr':
            df.loc[i, 'Title'] = 'Other'

    return df


""" DA RIPORTARE NEL MAIN
df = redistribuzioneCategorie(df)

print(df['Title'].value_counts())
"""


def gestioneValoriNullMonetary(df):
    # GESTIONE DEI DATI MANCANTI
    # I valori mancanti per la colonna 'Monetary' vengono sostituiti attraverso la mediana per ciascuna classe
    medianDonated = df.loc[df['Class'] == 1, 'Monetary'].median()
    medianNotDonated = df.loc[df['Class'] == 0, 'Monetary'].median()

    df.loc[(df['Class'] == 1) & (df['Monetary'].isnull()), 'Monetary'] = medianDonated
    df.loc[(df['Class'] == 0) & (df['Monetary'].isnull()), 'Monetary'] = medianNotDonated

    return df


def gestioneValoriNullAge(df):
    # I valori mancanti per la colonna 'Age' vengono sostituiti calcolando una mediana delle età delle persone aventi lo stesso titolo
    # medianAgeByTitle è una Serie

    medianAgeByTitle = df.groupby('Title')['Age'].median()

    for title, medianAge in medianAgeByTitle.items():
        df.loc[(df['Title'] == title) & pd.isnull(df['Age']), 'Age'] = medianAge

    return df


def showAgeDistribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=60, color='skyblue', edgecolor='black')
    plt.title('Distribuzione delle età')
    plt.xlabel('Età')
    plt.ylabel('Frequenza')
    plt.show()


""" DA RIPORTARE NEL MAIN
Il grafico rivela che la maggior parte dei donatori ha un'età compresa tra i 20 e 40 anni.
La feature 'Age' viene categorizzata in 4 intervalli diversi:
- 'giovane' con età < 25;
- 'giovane adulto' con 26 <= età <= 40;
- 'adulto medio' con 41 <= età <= 60
- 'adulto anziano' con età > 60
"""


def categorizzazioneAge(df):
    # Definisco gli estremi degli intervalli e le etichette per categorizzare l'età
    bins = [float('-inf'), 25, 41, 61, float('inf')]
    labels = ['giovane', 'giovane adulto', 'adulto medio', 'adulto anziano']

    """
    Dopo un'ulteriore analisi dei dati, il grafico mostra una forte concentrazione di punti tra i 20-40 anni di età e tra 
    0-20 per la frequenza delle donazioni. 
    In generale, questa fascia di età è la più propensa a donare, seguita dalla fascia di età 40-60.
    La frequenza delle donazioni diminuisce dopo circa i 65 anni, forse dovuto a patologie o altre informazioni cliniche della persona.
    """

    # Categorizzazione dell'età e creazione di una nuova colonna 'AgeGroup'
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    return df


def showIntersectionAgeAndFrequency(df):
    # Vediamo chi è più propenso a donare
    plt.figure(figsize=(10, 6))
    plt.scatter(df['AgeGroup'], df['Frequency'], alpha=0.5, color='blue')
    plt.title('Interazione tra Età e Frequenza delle Donazioni')
    plt.xlabel('Età')
    plt.ylabel('Frequenza delle Donazioni')
    plt.show()


# Elimino la vecchia colonna
"""df.drop(['Age'], axis=1, inplace=True)

df.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx", index=False,
            columns=['Surname', 'Title', 'Sex', 'AgeGroup', 'Frequency', 'Monetary', 'Recency', 'Time', 'Class'])"""


def dropColumn(dataset):
    label = ['Surname', 'Title']
    dataset.drop(label, axis=1, inplace=True)
    dataset.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPostDrop.xlsx", index=False,
                columns=['Sex', 'AgeGroup', 'Frequency', 'Monetary', 'Recency', 'Time', 'Class'])


def createOnlyTrue(dataset):
    newDataset = dataset[dataset['Class'] == 0]

    newDataset.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetFalse.xlsx", index=False)

