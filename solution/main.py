def main():

    avg_temp_by: dict = {}

    with open("measurements.txt", "r") as file:
        for line in file:
            city_name, city_temp = line.split(";")
            city_temp = float(city_temp)

            if city_name not in avg_temp_by:
                avg_temp_by[city_name] = {
                    "min": city_temp,
                    "max": city_temp,
                    "sum": city_temp,
                    "counter": 1,
                }
                continue

            if city_temp > avg_temp_by[city_name]["max"]:
                avg_temp_by[city_name]["max"] = city_temp

            if city_temp < avg_temp_by[city_name]["min"]:
                avg_temp_by[city_name]["min"] = city_temp

            avg_temp_by[city_name]["sum"] += city_temp
            avg_temp_by[city_name]["counter"] += 1

    for city_name in sorted(avg_temp_by.keys()):
        city = avg_temp_by[city_name]
        min = city["min"]
        max = city["max"]
        mean = city["sum"] / city["counter"]
        print(f"{city_name};{min};{mean:.1f};{max}")

main()
