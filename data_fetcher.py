import requests


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
  response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
  if response.status_code == requests.codes.ok:
    return response.json()
  else:
    print("Error:", response.status_code, response.text)