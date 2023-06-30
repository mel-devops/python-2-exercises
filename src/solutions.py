import inspect
from pprint import pprint
from WordCounter import WordCounter 
from Invoice import Invoice

def sort_people(listPeople, field, direction):
    pass #TODO:
    listPeople.sort(key=lambda p: p[field], reverse= (direction == 'desc'))

listPeople = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    
print(listPeople)

# # ----------------------------------------------------------------------------------->

def filter_males(males):
    pass #TODO:

listPeople = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

listPeopleNew = list(filter(lambda p: p['sex'] == 'male', listPeople))

print(listPeopleNew)

# ----------------------------------------------------------------------------------->


def calc_bmi(people_list):
    
    bmi_list = list(map(lambda person: {**person, 'bmi': round(person['weight_kg'] / person['height_meters'] ** 2, 1)}, people_list))
    return bmi_list

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)

ex3()

# ----------------------------------------------------------------------------------->

def ex4(get_people):
    
    listPeople = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}
    ]
    
    listPeopleNew = [p['name'] for p in listPeople if p['age'] >= 15]
    
    print(get_people(listPeopleNew))


def get_people(people):
    return people

ex4(get_people)

# ----------------------------------------------------------------------------------->


sentence = "Clear some space out so we can space out."
word_counter = WordCounter(sentence)

print(word_counter.get_word_count())    # Returns the number of all the words.
print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
print(word_counter.get_longest_word())  # Returns the length of the longest word.

#------------------------------------------------------------------------------------------>

data = [
    
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]

invoices = []

for item in data:
    invoice_id, user_id, amount, paid = item.split(", ")
    invoice = Invoice(invoice_id, user_id, amount, paid)
    invoices.append(invoice)
    
    print(invoices)
        

