#https://python-twitter.readthedocs.io/en/latest/twitter.html#module-twitter.api
#https://pypi.org/project/pysub-parser/
import twitter
import configparser
#from os import path
import sys
from pysubparser import parser
import pathlib
import os
filepath = pathlib.Path(__file__).parent.absolute()

config = configparser.ConfigParser()
config.read(str(filepath) + '/config.ini')
filename = config['DEFAULT']['filename']

if len(sys.argv) < 2:
    quit()
indexToSend = int(sys.argv[1])
subtitles = parser.parse(str(filepath) + '/' + filename, 'srt')


api = twitter.Api(consumer_key=config['DEFAULT']['consumer_key'],
consumer_secret=config['DEFAULT']['consumer_secret'],
access_token_key=config['DEFAULT']['access_token_key'],
access_token_secret=config['DEFAULT']['access_token_secret'])

subtitleToSend = ''

for subtitle in subtitles:
    if subtitle.index == indexToSend:
        subtitleToSend = subtitle.text
        break

api.PostUpdates(status=subtitleToSend)