def get_formatted_name(first_name, last_name, middle_name="", age=None, occupation=""):
  """Return a full name, neatly formatted, with optional middle name, age, and occupation."""
  full_name = f"{first_name.title()} {middle_name.title() if middle_name else ''} {last_name.title()}"
  if age:
      full_name += f", {age}"
  if occupation:
      full_name += f" ({occupation})"
  return full_name

while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
      break

  l_name = input("Last name: ")
  if l_name == 'q':
      break

  m_name = input("Middle name (optional): ")
  age = input("Age (optional): ")
  occupation = input("Occupation (optional): ")

  formatted_name = get_formatted_name(f_name, l_name, m_name, age, occupation)
  print("\nHello, " + formatted_name + "!")
