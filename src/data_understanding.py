import pandas as pd
import os

PATH_SEPARATOR = os.sep
df=pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx")

#Conversione in csv
df.to_csv(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}BloodDonations_Dataset.csv", index=False)

#CONTROLLO SUL BILANCIAMENTO DEI DATI
#Numero di elementi per la classe 'Donating'
print("Donating blood:", len(df[(df['Class'] == 1)]))
#Numero di elementi per la classe 'Not Donating'
print("Not donating blood:", len(df[(df['Class'] == 2)]))

#Totale
print("Total:", len(df))

#Abbiamo un numero maggiore per la classe positiva (PROBABILE BILANCIAMENTO?!)

#Verifico se e quanti valori nulli esistono attraverso la funzione isna() per trovarli e sum() per contarli
nan_present = df.isna()
nan_count = nan_present.sum()

print(nan_count)

#Confermato che non vi sono valori nulli all'interno del dataset

#ANALISI DELLE DISTRIBUZIONI DEI DATI
#print(df.describe())
#c'è molta variabilità nei dati

