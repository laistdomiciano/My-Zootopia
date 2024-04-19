import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

#print (load_data("animals_data.json"))

for animal in animals_data:
  name = animal["name"]
  diet = animal["characteristics"].get("diet")
  locations = animal["locations"]
  first_location = locations[0]
  animal_type = animal["characteristics"].get("type")


  print("Name:", name)
  print("Diet:", diet)
  print("Location:", first_location)
  if animal_type is not None:
    print("Type:", animal_type)
  print()
