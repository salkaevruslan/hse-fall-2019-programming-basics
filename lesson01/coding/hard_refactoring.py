#!/usr/bin/env python3
import collections
import sys
from datetime import date

Person = collections.namedtuple('Person', ['first_name', 'last_name', 'birth_date', 'area'])
people = [
    Person(first_name='Albert', last_name='Einstein', birth_date=date(year=1879, month=3, day=14), area='physics'),
    Person(first_name='Alan', last_name='Turing', birth_date=date(year=1912, month=6, day=23), area='cs'),
    Person(first_name='Edsger', last_name='Dijkstra', birth_date=date(year=1930, month=5, day=11), area='cs'),
    Person(first_name='Niels', last_name='Bohr', birth_date=date(year=1885, month=10, day=7), area='physics'),
    Person(first_name='Leslie', last_name='Lamport', birth_date=date(year=1941, month=2, day=7), area='cs'),
]

# Student's code starts.

print('--- Physics ---')
def build_people_dict(people):
    people_dict = {}
    for p in people:
        people_dict[p.area] = people_dict.get(p.area, [])
        people_dict[p.area].append(p)
    return people_dict

def format_person(person):
    return "{}. {}, born on {}".format(person.first_name[:1], person.last_name, person.birth_date)

def print_people_by_area(title, people):
    print(f'--- {title} ---')
    for person in people:
        print('* ' + format_person(person))

def get_oldest_person(people):
    return min(people, key=lambda x: x.birth_date)

def print_people_by_areas(people_dict, areas_mapping):
    for key in people_dict:
        print_people_by_area(areas_mapping[key], people_dict[key])
        print('Total: {}\n'.format(len(people_dict[key])))

areas_mapping = {
    "cs" : "Computer Science",
    "physics" : "Physics"
}

people_dict = build_people_dict(people)
print_people_by_areas(people_dict, areas_mapping)

oldest_person = get_oldest_person(people)
print('Oldest person: ' + format_person(oldest_person))
