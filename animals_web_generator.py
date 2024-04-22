import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

#print (load_data("animals_data.json"))

def generate_animals_html(output):
  """ Reads original HTML file and then open a new one """
  with open('animals_template.html', 'r') as file:
    html_content = file.read()

  updated_html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

  with open('animals.html', 'w') as file:
    file.write(updated_html_content)

def serialize_animal(animal_obj):
  """ Loops through the animal info and creates outputs for the cards in the HTML page """
  output = ""
  for animal in animals_data:  # loop for getting the animals data in a list of dictionaries
    # append information to each string
    output += '<li class="cards__item">'
    output += f"<div class=\"card__title\">{animal['name']}</div>\n"
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal['characteristics'].get('diet')}<br/>\n"
    locations = animal['locations']
    output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
    if animal["characteristics"].get("type") is not None: #just gets types that have valid information
      output += f"<strong>Type:</strong> {animal['characteristics'].get('type')}<br/>\n\n"
    else:
      output += "<br/>\n"
    output += '</p>'
    output += '</li>'

  generate_animals_html(output)
  return output

  generate_animals_html(output)
  return output

def main ():
  animals_data = load_data('animals_data.json')
  output = serialize_animal(animals_data)
  print(output)


if __name__ == "__main__":
  main()


# for animal in animals_data: #loop for getting the animals data in a list of dictionaries
#   name = animal["name"]
#   diet = animal["characteristics"].get("diet")
#   locations = animal["locations"]
#   first_location = locations[0]
#   animal_type = animal["characteristics"].get("type")

# print(f"Name: {name}")
# print(f"Diet: {diet}")
# print(f"Location:{first_location}")
# if animal_type is not None:
#   print(f"Type:{animal_type}")
# print()