def corr_chickenpox_old():
    import scipy.stats as stats
    import pandas as pd

    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)


    cleanDF = df[(df['P_NUMVRC'] >= 0) & (df['HAD_CPOX'] <= 2)]

    hadCpox = cleanDF['HAD_CPOX']

    numVaccination = cleanDF['P_NUMVRC']

    df = pd.DataFrame({"had_chickenpox_column": hadCpox,
                       "num_chickenpox_vaccine_column": numVaccination})

    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])

    return corr



def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    mb = pd.read_csv("assets/NISPUF17.csv")

    v1 = mb[(mb['P_NUMVRC'] >=0) & (mb['HAD_CPOX'] <= 2)]

    no_yes = v1['HAD_CPOX']

    est_vaccine = v1['P_NUMVRC']

    # this is just an example dataframe
    df=pd.DataFrame({"had_chickenpox_column":no_yes,
                   "num_chickenpox_vaccine_column":est_vaccine})

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])

    # just return the correlation
    return corr

assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."
print(corr_chickenpox())

print(corr_chickenpox_old())