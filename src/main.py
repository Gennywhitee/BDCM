import eel
import numpy as np
import pandas as pd
import os
import data_understanding as du
import data_cleaning as dc
import data_modelling as dm

PATH_SEPARATOR = os.sep

datasetTest = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTest.xlsx")
datasetTrain = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx")
datasetFinale = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetFinale.xlsx")

"""FASE DI DATA CLEANING
#PRIMO PROCESSING DEI DATI
df1 = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}Dataset.xlsx")
dataset = (dc.categorizzazione_age(dc.gestione_valori_null_age
                                   (dc.gestioneValori_null_monetary(dc.redistribuzione_categorie(dc.dividi_name(df1))))))
dataset.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx", index=False,
                 columns=['Surname', 'Title',	'Sex', 'AgeGroup', 'Frequency', 'Monetary', 'Recency', 'Time',	'Class'])

#SECONDO PROCESSING DEI DATI
df = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetPulito.xlsx")

#Creo il DatasetFinale
newDataset = dc.new_dataset(dc.change_cat(dc.change_age_group(dc.drop_column(df))))"""


# dataset = dc.new_dataset(dc.change_cat(dc.change_age_group(dc.drop_column(df))))

# dc.dropColumn(dataset)
# dc.create_only_true(dataset)
# dc.showIntersectionAgeAndFrequency(datasetTrue)
# dc.showIntersectionAgeAndFrequency(datasetFalse)
#dc.show_age_distribution(datasetFinale)

# -------------------FASE DI DATA MODELLING---------------------------------
"""y_test, y_pred = dm.training_modello(dataset)

accuracy, precision = dm.valutazione_modello(y_test, y_pred)

print(f"\n\nAccuracy del modello sul test set: {accuracy:.2f}")
print(f"Precison del modello sul test set: {precision:.2f}")

dataf = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx")

print("\n\nSituazione dopo aver bilanciato la classe:")
print("Donating blood:", len(dataf[(dataf['Class'] == 1)]))
#Numero di elementi per la classe 'Not Donating'
print("Not donating blood:", len(dataf[(dataf['Class'] == 0)]))"""

# dc.show_intersection_age_and_frequency(dataset)
# dc.show_intersection_age_and_frequency(datasetFinale)

# du.printFrequency(datasetFinale)
# dm.merge_datasets(dataset, datasetFinale)
# dm.average(dataset)
# dm.oversampling_data(datasetFinale,200)

#dm.data_partitioning(datasetFinale)
#dm.oversampling_data(datasetTrain,180)
#dm.undersampling(datasetTrain)
#du.printFrequency(datasetTest)
#du.printFrequency(datasetTrain)

dm.train_multinomial_naive_bayes(datasetTrain, datasetTest)

"""model = dm.get_model("naive_bayes_MN_classifier.pkl")
data = {"Sex": 0, "AgeGroup": 4, "Frequency": 15, "Monetary": 17500, "Recency": 14, "Time": 30}
input_df = pd.DataFrame([data], index=[0])
dm.get_prediction(input_df, model)"""

"""eel.init('web')

@eel.expose
def invia_dati_al_modello(dati):
    # Carica il modello
    model = dm.get_model("naive_bayes_MN_classifier.pkl")

    # Converte la lista di stringhe in un array numpy di float
    array_dati = np.array(dati).astype(float)

    # Reshape in un array 2D
    array_dati_2D = array_dati.reshape(1, -1)

    # Effettua la previsione
    prediction = dm.get_prediction(array_dati_2D, model)
    print(prediction)

    return prediction


eel.start('index.html', size=(800, 600))"""
