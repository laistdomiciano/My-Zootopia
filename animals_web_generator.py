import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

#print (load_data("animals_data.json"))

def generate_animals_html(output):
  with open('animals_template.html', 'r') as file:
    html_content = file.read()

  updated_html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

  with open('animals.html', 'w') as file:
    file.write(updated_html_content)

def main ():
  animals_data = load_data('animals_data.json')

  output = ''  # define an empty string

  for animal in animals_data:  # loop for getting the animals data in a list of dictionaries
    # append information to each string
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics'].get('diet')}\n"
    locations = animal['locations']
    output += f"Location: {locations[0]}\n"
    if animal["characteristics"].get("type") is not None:
      output += f"Type: {animal['characteristics'].get('type')}\n\n"
    else:
      output += "\n"

  generate_animals_html(output)
  print (output)

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