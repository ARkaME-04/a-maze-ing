from numpy.core.defchararray import capitalize


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{capitalize(seed_type)} seeds:"
              f" {quantity} packets available")
    elif unit == "grams":
        print(f"{capitalize(seed_type)} seeds:"
              f" {quantity} grams total")
    elif unit == "area":
        print(f"{capitalize(seed_type)}"
              f" seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
