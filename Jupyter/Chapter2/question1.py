import pandas as pd







def proportion_of_education():
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)
    mel1 = len(df[df['EDUC1'] == 1])
    mel2 = len(df[df['EDUC1'] == 2])
    mel3 = len(df[df['EDUC1'] == 3])
    mel4 = len(df[df['EDUC1'] == 4])
    print(len(df))

    total = mel4 + mel3 + mel2 + mel1
    return {"less than high school": mel1/total,
            "high school": mel2/total,
            "more than high school but not college": mel3/total,
             "college": mel4/total}

print(proportion_of_education())