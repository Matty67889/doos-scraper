import json
import argparse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.error import HTTPError

### Constants ###

URL_PREFIX = "https://www.thedictionaryofobscuresorrows.com/word/"
PART_OF_SPEECH_MAP = {"n.": "noun", "v.": "verb", "adj.": "adjective", "v. intr.": "intransitive verb"}

def get_word(soup):
  """
  Gets the word of the webpage mapped to the soup.
  """
  return soup.find_all("h1", class_="word-h1")[0].text.lower()

def get_part_of_speech(soup):
  """
  Gets the part of speech of the word on the webpage mapped to the soup.
  """
  part_of_speech_symb = soup.find_all("div", class_="word-part")[0].text
  return PART_OF_SPEECH_MAP[part_of_speech_symb]

def get_def(soup):
  """
  Gets the defintion of the word on the webpage mapped to the soup.
  """
  return soup.find_all("div", class_="word-definition")[0].text

def get_etymology(soup):
  """
  Gets the etymology of the word on the webpage mapped to the soup.
  """
  return soup.find_all("div", class_="word-etymology")[0].find("p").text

def scrape_word_info(word):
  url = URL_PREFIX + word
  source = urlopen(url)
  soup = bs(source, 'html.parser')

  word_dict = {"word": get_word(soup),
              "definition": get_def(soup),
              "partOfSpeech": get_part_of_speech(soup),
              "etymology": get_etymology(soup)
              }
  
  return word_dict

def main():
  """
  Returns a JSON of data for the word suerza.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("--words-list-path",type=str,help="input the file path of the words to scrape for")
  parser.add_argument("--output-file-path",type=str,help="input the file path of the destination for JSON list")
  args = parser.parse_args()

  input_file_path = args.words_list_path
  output_file_path = args.output_file_path
  
  words_to_scrape = []
  word_jsons = []

  try:
    file_reader = open(input_file_path, "r")
    # only add non empty entries to be scraped
    words_to_scrape = [line.strip() for line in file_reader if line.strip()]
    file_reader.close()
  except Exception as err:
    print("The program has encountered an error reading the input file, shown below. Try again with a proper input file path.")
    print(err)
    exit(0)
  
  try:
    for word in words_to_scrape:
      word_jsons.append(scrape_word_info(word.lower()))
    json.dump(word_jsons, open(output_file_path, 'w'))
  except HTTPError as err:
    # no crashing for HTTPErrors
    print(err)
    exit(0)
  except Exception as err:
    print("The program has encountered an error with the output file, shown below. Try again with a proper output file path.")
    print(err)
    exit(0)

if __name__ == '__main__':
  main()