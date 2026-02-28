def inches_to_meter(inches):
    meter = inches * 0.0254
    return meter
inches = int(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_meter(inches)} meters.")