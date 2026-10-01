for i in range(1, 4):
    print(f"\nIteration {i}")

    # Observe
    temperature = float(input("Enter the temperature: "))
    print(f"Observe: Temperature = {temperature}°C")

    # Decide
    if temperature > 30:
        decision = "Turn ON the fan"
    else:
        decision = "Keep the fan OFF"

    print(f"Decide: {decision}")

    # Act
    if temperature > 30:
        print("Act: Fan turned ON")
    else:
        print("Act: Fan remains OFF")

print("\nODA loop completed 3 iterations.")
