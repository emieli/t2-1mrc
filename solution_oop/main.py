from temp import Temp

type City = str


def main():
    temps_by_city: dict[City, Temp] = {}

    with open("measurements.txt", "r", encoding="utf8") as file:
        for line in file:
            city, temp = line.split(";")
            temp = float(temp)
            if city not in temps_by_city:
                temps_by_city[city] = Temp(city, temp)
                continue

            temps_by_city[city].add_measurement(temp)

    for city, temp in temps_by_city.items():
        print(temp)


if __name__ == "__main__":
    main()
