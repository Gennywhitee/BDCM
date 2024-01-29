import pandas as pd
import os
import re

PATH_SEPARATOR = os.sep
df=pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx")

"""Dalla fase di data_understing è sorto che la colonna 'Name' sembra contenere più informazioni insieme:
cognome, titolo e nome.

Inoltre le features 'Age' e 'Monetary' presentano dei valori mancanti. In particolare 'Age' in modo considerevole (153 e 10 per 'Monetary').

Non meno importante è lo sbilanciamento delle classi!"""

# Sostituisco tutti i valori '2' con '0' nella colonna 'Class' per le persone che non hanno donato
df['Class'] = df['Class'].replace(2, 0)

# OPERAZIONE SULLE FEATURE
# Divido la colonna Name in due: Surname e Title
# Definisco una funzione lamba che applica la funzione split() su una stringa e ritorna il primo valore della separazione
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
# Check
# print(df['Surname'])

# In questo caso la labda cerca un pattern, definito tramite espressione regolare, e se trova un match, restituisce il primo gruppo, ossia quello tra parentesi ()
df['Title'] = df['Name'].apply(lambda x: re.search(r',\s*([^\.]+)\.', x).group(1) if re.search(r',\s*([^\.]+)\.', x) else None)

# Elimino la vecchia colonna
df.drop(['Name'], axis=1, inplace=True)

# Visualizzo i risultati ottenuti e quanti valori si ottengono per ciascun titolo
print(df['Title'].value_counts())

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

df = redistribuzioneCategorie(df)

print(df['Title'].value_counts())

#df.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx", index=False)

# GESTIONE DEI DATI MANCANTI
# I valori mancanti per la colonna 'Monetary' vengono sostituiti attraverso la mediana per ciascuna classe
medianDonated = df.loc[df['Class'] == 1, 'Monetary'].median()
medianNotDonated = df.loc[df['Class'] == 0, 'Monetary'].median()

df.loc[(df['Class'] == 1) & (df['Monetary'].isnull()), 'Monetary'] = medianDonated
df.loc[(df['Class'] == 0) & (df['Monetary'].isnull()), 'Monetary'] = medianNotDonated

# I valori mancanti per la colonna 'Age' vengono sostituiti calcolando una mediana delle età delle persone aventi lo stesso titolo
# medianAgeByTitle è una Serie
medianAgeByTitle = df.groupby('Title')['Age'].median()

for title, medianAge in medianAgeByTitle.items():
    df.loc[(df['Title'] == title) & pd.isnull(df['Age']), 'Age'] = medianAge

df.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx", index=False)
