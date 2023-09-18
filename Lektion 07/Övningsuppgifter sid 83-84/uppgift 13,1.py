import requests


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


try:
    num = int(input("Ange ett positivt heltal: "))
    if num <= 0:
        print("Du måste ange ett positivt heltal.")
    else:
        if is_prime(num):
            print(f"{num} är ett primtal.")
        else:
            print(f"{num} är inte ett primtal.")

        factors = get_factors(num)
        print(f"Numrets faktorer är: {', '.join(map(str, factors))}.")

        # Gör ett API-anrop för att hämta information om talet.
        url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={num}"
        response = requests.get(url)


except ValueError:
    print("Du måste ange ett giltigt heltal.")
