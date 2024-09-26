
# 1. Import necessary functionality
import json


# 2. Load the rates from a JSON file
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


# 3. Create the function
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    # 4. Make sure the user input is lowered
    base = base.lower()
    to = to.lower()

    # 5. Get the dictionaries
    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    # 6. Return the rates
    if base == 'eur':
        return amount * to_rates['rate']  # type: ignore
    else:
        return amount * (to_rates['rate'] / from_rates['rate'])  # type: ignore


# 7. Create a main entry point
def main() -> None:
    # 8. Load the rates
    rates: dict[str, dict] = load_rates('rates.json')

    # 9. Get the result
    result: float = convert(amount=75, base='eur', to='usd', rates=rates)
    print(result)


# 10. Run the script
if __name__ == '__main__':
    main()


