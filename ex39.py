#Create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonvile'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 20)
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is : ", states['Florida'])

#do it by using the state then cities dict
print('-' * 20)
print('Michigan has :', cities[states['Michigan']])
print('Florida has : ', cities[states['Florida']])

# print every states's abbreviation.
print('-' * 20)
for state, abbrev in list(states.items()) :
    print(f'{state} is abbreviated {abbrev}')

#print every city in the states
print('-' * 20)
for abbrev, city in list(cities.items()) :
    print(f'{abbrev} has the city {city}.')

#now do both in the same time
print('-' * 20)
for state, abbrev in list(states.items()) :
    print(f'{state} has the city {cities[abbrev]}.')

print('-' * 20)
#Safely get abbreviation by state that might not be there.
state = states.get('Texas')

if not state :
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('Tx', 'Does not exist')
print(f"The city for the state 'TX' is : {city}.")
