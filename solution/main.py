def main():

    temp_by: dict = {}

    with open("measurements.txt", "r") as file:
        for line in file:
            city, temp = line.split(";")
            temp = float(temp)

            if city not in temp_by:
                temp_by[city] = {
                    "min": temp,
                    "max": temp,
                    "sum": temp,
                    "counter": 1,
                }
                continue

            if temp > temp_by[city]["max"]:
                temp_by[city]["max"] = temp

            if temp < temp_by[city]["min"]:
                temp_by[city]["min"] = temp

            temp_by[city]["sum"] += temp
            temp_by[city]["counter"] += 1

    for city, temp in temp_by.items():
        min = temp["min"]
        max = temp["max"]
        avg = temp["sum"] / temp["counter"]
        print(f"{city};{min};{avg:.1f};{max}")

main()
