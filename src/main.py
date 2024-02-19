import pandas as pd
import os
import data_understanding as du
import data_cleaning as dc

PATH_SEPARATOR = os.sep


dataset = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetAgeChange.xlsx")



# dc.dropColumn(dataset)
#dc.createOnlyTrue(dataset)
#dc.showIntersectionAgeAndFrequency(datasetTrue)
#dc.showIntersectionAgeAndFrequency(datasetFalse)

dc.changeCat(dataset)

#dc.changeAgeGroup(dataset)
