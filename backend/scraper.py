import requests
from bs4 import BeautifulSoup
from config import GOOGLE_API_KEY, GOOGLE_CSE_ID

#
# searching Google using Custom Search JSON API
#
def google_search(query, api_key, cse_id, num_results=5):
  url = "https://www.googleapis.com/customsearch/v1"
  params = {
    "q": query,
    "key": api_key,
    "cx": cse_id,
    "num": num_results
  }
  # send the request to Google Custom Search API
  resp = requests.get(url, params=params)
  # parse the JSON response
  results = resp.json()
  urls = []
  # "items" is a key in a dictionary that contains the search results
  if "items" in results:
    for item in results["items"]:
      urls.append(item["link"])
  return urls

#
# scrape headlines from the URLs
#
def scrape(company: str, num_results=5):
  query = f"{company} rebranding news"

  urls = google_search(query, GOOGLE_API_KEY, GOOGLE_CSE_ID, num_results)
  print(urls)

  headlines = []

  for url in urls:
    try:
      # fetch the page content
      res = requests.get(url, timeout=5)
      # parse the HTML content
      soup = BeautifulSoup(res.text, 'html.parser')
      # extract the title of the page
      title = soup.title.string if soup.title else "No title"

      # appends to headlines
      headlines.append({"title": title, "url": url})
    except Exception as e:
      print(f"Failed to scrape {url}: {e}")
  return headlines