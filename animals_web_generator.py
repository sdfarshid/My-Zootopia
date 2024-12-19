import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html_file(file_path: str) -> str:
    """ Loads a Html file """
    file = open(file_path, "r")
    content = file.read()
    file.close()
    return content


def write_html_file(file_path: str, content: str) -> None:
    """ Loads a Html file """
    file = open(file_path, "w")
    content = file.write(content)
    file.close()


def fetch_data(animals_datas: list[dict]) -> list[dict]:
    return [
        {
            "Name": animal_data.get("name", False),
            "Diet": animal_data["characteristics"].get("diet", False),
            "Type": animal_data["characteristics"].get("type", False),
            "Location": animal_data["locations"][0] if animal_data["locations"] else False,
        }
        for animal_data in animals_datas
    ]


def generate_string_output(animals_datas: list[dict]) -> str:
    output = ""
    for animal_data in animals_datas:
        name = animal_data.get("Name", False)
        diet = animal_data.get("Diet", False)
        type_ = animal_data.get("Type", False)
        location = animal_data.get("Location", False)

        if name:
            output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if type_:
            output += f"Type: {type_}\n"
        if location:
            output += f"Location: {location}\n"
        output += "\n"

    return output


def set_dynamic_data(static_file: str, dynamic_data: str) -> str:
    return static_file.replace("__REPLACE_ANIMALS_INFO__", dynamic_data)


def main():
    animals_data = load_data('animals_data.json')
    dynamic_data = generate_string_output(fetch_data(animals_data))
    static_file = read_html_file("animals_template.html")
    new_html_content = set_dynamic_data(static_file, dynamic_data)
    write_html_file("animals_template.html",new_html_content)

    print()


if __name__ == "__main__":
    main()
