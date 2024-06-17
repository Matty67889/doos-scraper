# Dictionary of Obscure Sorrows Web Scraper

## About

The scripts in this project will allow one to gather data on the words from the [Dictionary of Obscure Sorrows website](https://www.thedictionaryofobscuresorrows.com/). Given a text file of words to gather data on, it returns a JSON with information on the words, such as the defintion, part of speech, and origin.

I was inspired to make this project because I needed a way to acquire a JSON of the words in the words in the dictionary of obscure sorrows for a word project I was working on for my personal website, and I couldn't find one online. The closest thing I found was [lazaryo's Dictionary of Obscure Sorrows API](https://github.com/lazaryo/obscure), which wasn't quite what I was looking for.

## Getting Set Up

### Text file of words to search for

A text file of words to search for is required. The file must be formatted in the following fashion:

1. Each word should occupy one line, and the next word should appear on the next line.
2. Words should be UTF encoded, so they cannot contain special characters like those with accents.
3. Words must not contain spaces. Hyphens should replace spaces.
4. Words must be the words used in the URLs of the webpages for the words. For example, the word Énouement has an é, but the url for this word, <https://www.thedictionaryofobscuresorrows.com/word/enouement> spells "enouement" with an e, not an é.

A list of words on the website from this project's last update is included for reference of valid words.

### Setting up a Python environment

Setting up a Python virtual environment is recommended so that the required libraries do not have to be downloaded on the main computer, but it is not necessary. If not setting up the virtual environment, skip the activate the virtual environment step below.

Setup a Python venv virtual environment as shown [in this Guide](https://docs.python.org/3/library/venv.html). A good place to put the environment is in the main project folder. When the environment is created, follow the following steps:

1. Activate the virtual environment.
2. Navigate to the folder containing `requirements.txt`. Download the python requirements with the command `pip install -r requirements.txt`.

## Usage

To run the script, run `python web-scrape.py` after all the setup is complete.

## Special Notes

1. The scraper may break if the website updates. Feel free to update the scraper accordingly on your own if need be!

2. Verify that the words in the text file provided are actually on the website, some words have accents, but the webpage link to them is the word without accents.
