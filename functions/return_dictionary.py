def build_person(first_name, last_name, middle_name ='', age='',occupation=''):
  """Return a dictionary of information about a person."""
  person = {
    'first': first_name,
    'last': last_name
  }
  if middle_name:
    person['middle_name'] = middle_name
  if age:
    person['age'] = age
  if occupation:
    person['occupation'] = occupation

  return person


engineer = build_person('perrin', 'letembet', middle_name='luquet', age = 27)
print(engineer)