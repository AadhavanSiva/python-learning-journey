import pandas as pd


def chickenpox_by_sex():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)

    dfKids = df[df['SEX'] == 1]
    dfVacKids = dfKids[dfKids['P_NUMVRC'] >= 1.0]
    ctAffKids = len(dfVacKids[dfVacKids['HAD_CPOX'] == 1])
    ctUnAffKids = len(dfVacKids[dfVacKids['HAD_CPOX'] == 2])
    boysRatio = (ctAffKids / ctUnAffKids)

    dfKids = df[df['SEX'] == 2]
    dfVacKids = dfKids[dfKids['P_NUMVRC'] >= 1.0]
    ctAffKids = len(dfVacKids[dfVacKids['HAD_CPOX'] == 1])
    ctUnAffKids = len(dfVacKids[dfVacKids['HAD_CPOX'] == 2])
    girlsRatio = (ctAffKids / ctUnAffKids)

    return {"male":boysRatio,
            "female":girlsRatio}

df = pd.read_csv('assets/NISPUF17.csv', index_col=0)


print(chickenpox_by_sex())

assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."

