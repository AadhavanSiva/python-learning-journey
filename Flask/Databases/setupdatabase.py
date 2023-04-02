from adoption import db,Puppy
#creates all table
db.create_all()

sam = Puppy('Oscar',2, "lab")
frank = Puppy('Frankie',4, "lab")

# None
# None
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)