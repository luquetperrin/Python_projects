def build_profile(first, last, **user_info):
    """Build a profile about myself"""
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_info = build_profile('perrin',
                          'letembet',
                          age=29,
                          location='brazzaville',
                          favorite_language='C')
print(user_info)
