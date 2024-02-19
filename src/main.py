import pandas as pd
import os

import data_understanding as du
import data_cleaning as dc
import data_modelling as dm

PATH_SEPARATOR = os.sep

#FASE DI DATA CLEANING
df = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx")

dataset = dc.newDataset(dc.changeCat(dc.changeAgeGroup(dc.dropColumn(df))))

#dc.showIntersectionAgeAndFrequency(datasetTrue)
#dc.showIntersectionAgeAndFrequency(datasetFalse)

#FASE DI DATA MODELLING
y_test, y_pred = dm.trainingModello(dataset)

accuracy, precision = dm.valutazioneModello(y_test, y_pred)

print(f"\n\nAccuracy del modello sul test set: {accuracy:.2f}")
print(f"Precison del modello sul test set: {precision:.2f}")

dataf = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx")

print("\n\nSituazione dopo aver bilanciato la classe:")
print("Donating blood:", len(dataf[(dataf['Class'] == 1)]))
#Numero di elementi per la classe 'Not Donating'
print("Not donating blood:", len(dataf[(dataf['Class'] == 0)]))