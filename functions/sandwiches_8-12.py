def make_sandwich(*items):
    """Summarize the ingredients in a sandwich
    
    Args:
        *items(str): A variable number of sandwich ingredients.
    """
    print("\nI'm making a sandwich with:")
    if not items:
       print("Huh, youd didn't ask for anything on your sandwich.")
    else:
        for item in items:
            print(f"- {item}")

# Call the function three times
make_sandwich('bread', 'turkey', 'cheese', 'mayo')
make_sandwich('roast beef', 'mustard')
make_sandwich('peanut butter', 'jelly')