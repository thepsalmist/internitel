import requests

query = """query {
    characters {
    results {
      name
      status
      species
      type
      gender
    }
  }
}"""


def post_data():
    url = "https://api.sendgrid/graphql/"
    r = requests.post(url, json={"query": query})
    print(r.status_code)
    print(r.text)
