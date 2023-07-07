x = 'This is a string'

print(x[0])
print(x[0:1])
print(x[5:6])

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}

for name in x:
    print(x[name])

for name, email in x.items():
    print(name)
    print(email)

sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'}

print(sales_record)