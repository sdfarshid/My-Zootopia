import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_data(animals_datas: list[dict]) -> list[dict]:
    return [
        {
            "name": animal_data.get("name", False),
            "Diet": animal_data["characteristics"].get("diet", False),
            "Type": animal_data["characteristics"].get("type", False),
            "Location": animal_data["locations"][0] if animal_data["locations"] else False,
        }
        for animal_data in animals_datas
    ]


def main():
    animals_data = load_data('animals_data.json')
    print(fetch_data(animals_data))


if __name__ == "__main__":
    main()
