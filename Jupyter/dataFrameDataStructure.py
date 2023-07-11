import pandas as pd

# I'm going to jump in with an example. Lets create three school records for students and their
# class grades. I'll create each as a series which has a student name, the class name, and the score.
record1 = pd.Series({'Name': 'Alice',
                        'Class': 'Physics',
                        'Score': 85})
record2 = pd.Series({'Name': 'Jack',
                        'Class': 'Chemistry',
                        'Score': 82})
record3 = pd.Series({'Name': 'Helen',
                        'Class': 'Biology',
                        'Score': 90})

df = pd.DataFrame([record1, record2, record3],
                  index=['school1', 'school2', 'school1'])

print(df.head())

# An alternative method is that you could use a list of dictionaries, where each dictionary
# represents a row of data.

students = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

# Then we pass this list of dictionaries into the DataFrame function
df = pd.DataFrame(students, index=['school1', 'school2', 'school1'])
# And lets print the head again
df.head()

print(df.loc['school2'])

print(df.loc['school1'])

print(df.T.loc['Score'])

print(df.loc['school1']['Name'])

print(df.loc[:,['Name', 'Score', 'Class']])