import pandas as pd
import os

import data_understanding as dc
import data_cleaning as dc
import data_modelling as dm

PATH_SEPARATOR = os.sep

#FASE DI DATA CLEANING

#PRIMO PROCESSING DEI DATI
df1 = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx")
dataset = (dc.categorizzazione_age(dc.gestione_valori_null_age
                                   (dc.gestioneValori_null_monetary(dc.redistribuzione_categorie(dc.dividi_name(df1))))))
dataset.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx", index=False,
                  columns=['Surname', 'Title',	'Sex', 'AgeGroup', 'Frequency', 'Monetary', 'Recency', 'Time',	'Class'])

#SECONDO PROCESSING DEI DATI
df = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx")

newDataset = dc.new_dataset(dc.change_cat(dc.change_age_group(dc.drop_column(df))))

#dc.show_intersection_age_and_frequency(datasetTrue)
#dc.show_intersection_age_and_frequency(datasetFalse)

#FASE DI DATA MODELLING
y_test, y_pred = dm.training_modello(newDataset)

accuracy, precision = dm.valutazione_modello(y_test, y_pred)

print(f"\n\nAccuracy del modello sul test set: {accuracy:.2f}")
print(f"Precison del modello sul test set: {precision:.2f}")

dataf = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx")

print("\n\nSituazione dopo aver bilanciato la classe:")
print("Donating blood:", len(dataf[(dataf['Class'] == 1)]))
#Numero di elementi per la classe 'Not Donating'
print("Not donating blood:", len(dataf[(dataf['Class'] == 0)]))