def convert_speed(kmh: float):
    """Converts speed from Km/h to Mi/h and prints the result.
    Args:
        kmh (float): The speed in Km/h.
    """

    mph = round(0.6212 * round(kmh, 1), 1)

    print(f"Speed: {kmh} Km/h | {mph} Mi/h")
