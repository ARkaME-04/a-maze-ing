def recursion(var: int, current: int) -> None:
    if current > var:
        return
    print("Day", current)
    recursion(var, current + 1)


def ft_count_harvest_recursive() -> None:
    var = int(input("Days until harvest: "))
    recursion(var, 1)
    print("Harvest time!")
