def ft_water_reminder() -> None:
    var = int(input("Days since last watering: "))
    if var > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
