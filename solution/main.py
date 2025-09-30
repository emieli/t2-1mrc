# This is the main function where the program starts
def main():
    # Create an empty dictionary to store temperature data for each city
    temp_by: dict[str,dict[str,float]] = {}

    # Open the file named "measurements.txt" in read mode
    with open("measurements.txt", "r", encoding="utf8") as file:
        # Go through each line in the file
        for line in file:
            city, temp = line.split(";") # Each line contains a city and a temperature, separated by a semicolon
            temp = float(temp) # Convert the temperature from text to a number (float)

            # If this city is not already in our dictionary, add it
            if city not in temp_by:
                temp_by[city] = {
                    "min": temp,       # Minimum temperature so far
                    "max": temp,       # Maximum temperature so far
                    "sum": temp,       # Sum of all temperatures (for average)
                    "counter": 1,      # Number of temperature readings
                }
                continue  # Skip the rest of the loop and go to the next line

            # If the new temperature is higher than the current max, update it
            if temp > temp_by[city]["max"]:
                temp_by[city]["max"] = temp
            # If the new temperature is lower than the current min, update it
            if temp < temp_by[city]["min"]:
                temp_by[city]["min"] = temp

            # Add the new temperature to the sum
            temp_by[city]["sum"] += temp
            # Increase the counter by 1
            temp_by[city]["counter"] += 1

    # Now go through each city and calculate the average temperature
    for city, temp in temp_by.items():
        min = temp["min"]  # Minimum temperature
        max = temp["max"]  # Maximum temperature
        avg = temp["sum"] / temp["counter"]  # Average temperature
        # Print the result in the format: city=min/avg/max
        # .1f tells python to only print the first decimal
        print(f"{city}={min}/{avg:.1f}/{max}")

# Call the main function to run the program
main()
