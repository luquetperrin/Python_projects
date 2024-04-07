def calculate_infection_day(total_population):
    infected_count = 1  # Initial infected count
    day = 1  # Initial day
    
    while infected_count < total_population:
        # Each infected person contaminates two new people every day
        infected_count *= 2
        day += 1
    
    return day

# Read the total population from the user
total_population = int(input("Enter the total population of the area: "))

# Calculate the day at which the entire population will be infected
infection_day = calculate_infection_day(total_population)

print(f"The entire population will be infected on day {infection_day}.")
