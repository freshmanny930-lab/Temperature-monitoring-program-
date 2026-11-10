# Temperature Monitor and Alarm Checker
# CTE123 Python Mini Project - ND1 Mechatronics Engineering, YabaTech
# Author: [Emmanuel Moses]

def get_valid_temperature(reading_number):
    """
    Ask the user for a temperature reading and keep asking
    until a valid number is entered.
    Returns the temperature as a float.
    """
    while True:
        user_input = input(f"Enter temperature reading #{reading_number} (°C): ")
        try:
            # Convert the input to float (handles both int and decimal)
            temperature = float(user_input)
            return temperature
        except ValueError:
            # If the user typed letters or symbols instead of a number
            print("Invalid input! Please enter a number only (e.g. 45.5 or 60).")


def show_ascii_bar(temperatures, safe_limit):
    """
    Draw a simple ASCII bar chart of the 5 temperature readings.
    Each * represents roughly 5 degrees Celsius.
    """
    print("\nTemperature Bar Chart (each * ≈ 5°C):")
    print("-" * 40)
    for i, temp in enumerate(temperatures, 1):
        # Calculate how many stars to show (minimum 1 if temperature > 0)
        bars = max(1, int(temp / 5)) if temp > 0 else 0
        # Mark readings that are above the safe limit with a warning
        warning = " ⚠ OVER LIMIT" if temp > safe_limit else ""
        print(f"Reading {i}: {'*' * bars} {temp:.1f}°C{warning}")
    print("-" * 40)


def main():
    print("=" * 50)
    print("   TEMPERATURE MONITOR AND ALARM CHECKER")
    print("=" * 50)
    print("This program records 5 temperature readings from a machine,")
    print("calculates highest, lowest and average, and warns if any")
    print("reading is above the safe limit.\n")

    # Ask user for the safe temperature limit
    while True:
        try:
            safe_limit = float(input("Enter the safe temperature limit (°C): "))
            if safe_limit <= 0:
                print("Safe limit must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Collect exactly 5 temperature readings into a list
    temperatures = []
    print("\nPlease enter 5 temperature readings:")
    for i in range(1, 6):
        temp = get_valid_temperature(i)
        temperatures.append(temp)

    # Calculate basic statistics
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    # ---- MY OWN TWIST ----
    # Count how many readings are above the safe limit
    # and how many are in the "warning zone" (80% to 100% of the limit)
    over_limit_count = 0
    warning_zone_count = 0
    warning_threshold = safe_limit * 0.8   # 80% of safe limit

    for temp in temperatures:
        if temp > safe_limit:
            over_limit_count += 1
        elif temp >= warning_threshold:
            warning_zone_count += 1

    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Temperatures recorded : {temperatures}")
    print(f"Highest temperature   : {highest:.1f}°C")
    print(f"Lowest temperature    : {lowest:.1f}°C")
    print(f"Average temperature   : {average:.1f}°C")
    print(f"Safe limit set to     : {safe_limit:.1f}°C")
    print("-" * 50)

    # Alarm / warning messages
    if over_limit_count > 0:
        print(f"⚠ ALARM: {over_limit_count} reading(s) exceeded the safe limit!")
    else:
        print("✓ All readings are within the safe limit.")

    if warning_zone_count > 0:
        print(f"⚠ WARNING ZONE: {warning_zone_count} reading(s) are between "
              f"{warning_threshold:.1f}°C and {safe_limit:.1f}°C "
              f"(80%–100% of safe limit).")
    else:
        print("✓ No readings in the warning zone.")

    # Show the ASCII bar chart (part of the twist)
    show_ascii_bar(temperatures, safe_limit)

    print("\nThank you for using the Temperature Monitor!")
    print("=" * 50)


# Program starts here
if __name__ == "__main__":
    main()
