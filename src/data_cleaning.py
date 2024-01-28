import pandas as pd
import os
import re

PATH_SEPARATOR = os.sep
df=pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx")

"""Dalla fase di data_understing è sorto che le features 'Age' e 'Monetary'
presentano dei valori mancanti. In particolare 'Age' in modo considerevole.

Inoltre la colonna 'Name' sembra contenere più informazioni insieme:
cognome, titolo e nome.

Non meno importante è lo sbilanciamento delle classi!"""

#Divido la colonna Name in due: Surname e Title
#Definisco una funzione lamba che applica la funzione split() su una stringa e ritorna il primo valore della separazione
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
#Check
#print(df['Surname'])

#In questo caso la labda cerca un pattern definito tramite espressione regolare e se trova un match, restituisce il primo gruppo, ossia quello tra parentesi ()
df['Title'] = df['Name'].apply(lambda x: re.search(r',\s*([^\.]+)\.', x).group(1) if re.search(r',\s*([^\.]+)\.', x) else None)

df.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx", index=False)

#Visualizzo i risultati ottenuti e quanti valori si ottengono per ciascun titolo