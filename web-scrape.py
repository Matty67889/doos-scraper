# import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

### Constants ###
URL_PREFIX = "https://www.thedictionaryofobscuresorrows.com/word/"
PART_OF_SPEECH_MAP = {"n.": "noun", "v.": "verb", "adj.": "adjective"}

def get_word(soup):
  """
  Gets the word of the webpage mapped to the soup.
  """
  return soup.find_all("h1", class_="word-h1")[0].text

def get_def(soup):
  """
  Gets defintion of the word on the webpage mapped to the soup.
  """
  part_of_speech_symb = soup.find_all("div", class_="word-part")[0].text
  return PART_OF_SPEECH_MAP[part_of_speech_symb]

def get_part_of_speech(soup):
  """
  Gets the part of speech of the word on the webpage mapped to the soup.
  """
  return soup.find_all("div", class_="word-definition")[0].text

def main():
  """
  Returns a JSON of data for the word suerza.
  """
  # initialize soup for word
  url = URL_PREFIX + "suerza"

  source = urlopen(url)

  soup = bs(source, 'html.parser')
  print(soup.prettify())
  # print(soup.find_all("h1", class_="word-h1"))
  print({"word": get_word(soup), "part of speech": get_part_of_speech(soup), "definition": get_def(soup)})

if __name__ == '__main__':
  main()