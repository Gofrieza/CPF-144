def WindChill(temperature, speed):
    """
    :param temperature: value of temperature should be less than 50 in absolute value
    :param speed:value of speed should be less than 120 or greater than 3
    """

    effective_temperature = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * (speed * 0.16)
    print("the effective temperature (the wind chill) to be:", effective_temperature)


temperature = float(input('Enter the value of temp in fahrenheit: '))
speed = float(input('Enter the value of speed in miles per hour: '))
WindChill(temperature, speed)
