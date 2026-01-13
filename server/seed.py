#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    fake = Faker()

    # 1. Clear the database first
    print("Deleting existing pets...")
    Pet.query.delete()

    # 2. Define possible species
    species_list = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = []

    # 3. Generate 10 random pets
    print("Generating 10 new pets...")
    for n in range(10):
        # Using fake.first_name() for a random name
        # Using rc() to pick a random species from our list
        new_pet = Pet(name=fake.first_name(), species=rc(species_list))
        pets.append(new_pet)

    # 4. Save everything to the database
    db.session.add_all(pets)
    db.session.commit()
    print("Seeding complete!")