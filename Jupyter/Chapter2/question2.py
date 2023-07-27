import pandas as pd



def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)

    #To filter NaN values with P_NUMFLU field
    df = (df[df['P_NUMFLU'] >= 0])

    notBreastFedDf = df[df['CBF_01'] == 2]
    influenzaNotBreastFed = notBreastFedDf['P_NUMFLU'].sum()

    breastFedDf = df[df['CBF_01'] == 1]
    influenzaBreastFed = breastFedDf['P_NUMFLU'].sum()

    return ((influenzaBreastFed/len(breastFedDf) ), (influenzaNotBreastFed/len(notBreastFedDf)))


print((average_influenza_doses()))
