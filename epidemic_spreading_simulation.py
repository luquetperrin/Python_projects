def simulate_epidemic(initial_infected, contamination_rate, recovery_rate, total_population):
    infected = [initial_infected]
    day = 0

    while sum(infected) < total_population:
        day += 1
        new_infected = infected[-1] * contamination_rate
        recovered = infected.pop(0) if len(infected) >= recovery_rate else 0
        infected.append(new_infected)

    return day

def main():
    print("Epidemic Spread II")
    print("------------------")
    initial_infected = int(input("Enter the initial number of infected people on day 1: "))
    contamination_rate = float(input("Enter the contamination rate per infected person per day: "))
    recovery_rate = int(input("Enter the recovery rate (number of days it takes for an infected person to recover): "))
    total_population = int(input("Enter the total population of the area: "))

    days_to_spread = simulate_epidemic(initial_infected, contamination_rate, recovery_rate, total_population)
    print(f"It will take {days_to_spread} days for the entire population to be infected.")

if __name__ == "__main__":
    main()