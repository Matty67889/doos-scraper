import json
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

### Constants ###

INPUT_FILE_PATH = "data/doos-words.txt"
OUTPUT_FILE_PATH = "output/output.json"

URL_PREFIX = "https://www.thedictionaryofobscuresorrows.com/word/"
PART_OF_SPEECH_MAP = {"n.": "noun", "v.": "verb", "adj.": "adjective", "v. intr.": "intransitive verb"}

def get_word(soup):
  """
  Gets the word of the webpage mapped to the soup.
  """
  return soup.find_all("h1", class_="word-h1")[0].text.lower()

def get_part_of_speech(soup):
  """
  Gets defintion of the word on the webpage mapped to the soup.
  """
  part_of_speech_symb = soup.find_all("div", class_="word-part")[0].text
  return PART_OF_SPEECH_MAP[part_of_speech_symb]

def get_def(soup):
  """
  Gets the part of speech of the word on the webpage mapped to the soup.
  """
  return soup.find_all("div", class_="word-definition")[0].text

def scrape_word(word):
  url = URL_PREFIX + word
  source = urlopen(url)
  soup = bs(source, 'html.parser')

  try:
    word_dict = {"word": get_word(soup),
               "definition": get_def(soup),
               "part of speech": get_part_of_speech(soup),
               }
  except:
    print("Crashed on " + url)
  return word_dict

def main():
  """
  Returns a JSON of data for the word suerza.
  """
  words_to_scrape = []
  word_jsons = []
  file_reader = open(INPUT_FILE_PATH)

  try:
    for line in file_reader:
      words_to_scrape.append(line)
  finally:
    file_reader.close()
  
  for word in words_to_scrape:
    word_jsons.append(scrape_word(word.lower()))
  json.dump(word_jsons, open(OUTPUT_FILE_PATH, 'w'))

if __name__ == '__main__':
  main()