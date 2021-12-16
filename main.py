# import Framework.initialisation as init
# import Data.config
# from Packages.DataPreperation import CleanData
import Packages.selectData as selectData

# Open window to select data.
data = selectData.ChooseDataset().OpenWindow()
print(data)

# # Initialise the project by consuming the chosen 
# # dataset and cleaning the data.
# path = ""
# Initialisation = init.Initialise(path)
# getDF = Initialisation.GetDF()
# cleanDF = Initialisation.CleanData(getDF)
