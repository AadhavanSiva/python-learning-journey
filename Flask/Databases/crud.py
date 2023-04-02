from basicprojects.basic import db,Puppy

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

my_puppy = Puppy('Oscar', 2)
db.session.add(my_puppy)
db.session.commit()

#READ
all_puppies = Puppy.query.all()
print(all_puppies)

# select by id
puppy_by_name = Puppy.query.filter_by(name='Rufus').first()
print("************  For Rufus    **************")
print(puppy_by_name)

#filters
puppy_by_age = Puppy.query.filter_by(age=3).first()
if( puppy_by_age is None):
    print("not found for age = 3")

puppy_by_age = Puppy.query.filter_by(age=2).first()
print("************  For age = 2   **************")
print(puppy_by_age.name)

print(puppy_by_age.age)

puppy_by_age.age = 3
db.session.commit()


uppy_by_age = Puppy.query.filter_by(age=3).first()
print("************  For age = 3   **************")
print(puppy_by_age.name)

print(puppy_by_age.age)
# for puppy in puppies:
#     db.session.delete(puppy)
#     db.session.commit()
# print("************  For Frankie   **************")
#print(puppy_frankie)
db.session.delete(puppy_by_age)
db.session.commit()

db.session.delete(puppy_by_name)
db.session.commit()
#print(puppy_frankie.all())

####update

#first_puppy = db.session.get(1, Puppy)
# first_puppy = Puppy.query.filter_by(id=1).first()
# first_puppy.age = 10
# db.session.add(first_puppy)
# db.session.commit()

####DELETE
#
# second_pup=db.session.get(2, Puppy)
# db.session.delete(second_pup)
# db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)