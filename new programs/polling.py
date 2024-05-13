favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'perrin': 'c++',
    'luquet': 'java',
}
people_to_poll = ['jen', 'letembet', 'franck', 'sarah', 'luquet', 'perrin', 'reine']
for person in people_to_poll:
    if person in favorite_languages.keys():
        print("Thank you for taking the poll, " + person.title() + ".")
    else:
        print(person.title() + ", what is your favorite programming language?")