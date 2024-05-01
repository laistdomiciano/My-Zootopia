import sys
print(sys.path)
import data_fetcher

def generate_animals_html(output):
    """ Reads original HTML file and then open a new one """
    with open('animals_template.html', 'r') as file:
        html_content = file.read()

    updated_html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w') as file:
        file.write(updated_html_content)

def serialize_animal(animals_data, animal_name):
    """ Loops through the animal info and creates outputs for the cards in the HTML page """
    output = ""
    if animals_data:
        for animal in animals_data:
            output += '<li class="cards__item">'
            output += f"<div class=\"card__title\">{animal['name']}</div>\n"
            output += '<p class="card__text">'
            output += f"<strong>Diet:</strong> {animal['characteristics'].get('diet')}<br/>\n"
            locations = animal['locations']
            output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
            if animal["characteristics"].get("type") is not None:
                output += f"<strong>Type:</strong> {animal['characteristics'].get('type')}<br/>\n\n"
            else:
                output += "<br/>\n"

            output += '</p>'
            output += '</li>'

        print("Website was successfully generated to the file animals.html")
    else:
        output += f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
        print(f"The animal \"{animal_name}\" doesn't exist.")
    generate_animals_html(output)
    return output

def main():
    animal_name = input('Enter a name of an animal: ')
    animals_data = data_fetcher.fetch_data(animal_name)
    output = serialize_animal(animals_data, animal_name)

if __name__ == "__main__":
    main()