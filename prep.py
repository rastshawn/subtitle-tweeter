# Load in file
import configparser
from pysubparser import parser
import datetime 
import os 
import pathlib
filepath = pathlib.Path(__file__).parent.absolute()

def getSeconds(timeObj):
    return float((timeObj.hour * 60 + timeObj.minute) * 60 + timeObj.second)

def callSystem(time, index):
    command = 'echo "python3 ' + str(filepath) + '/post.py ' + str(index) + '"'
    at = ' | at -M ' + str(time.strftime('%H:%M %Y-%m-%d') )
    print(command + at)

config = configparser.ConfigParser()
config.read(str(filepath) + '/config.ini')

filename = config['DEFAULT']['filename']
subtitlesGen = parser.parse('./' + filename)
subtitles = []
# convert Generator into a list because
# I'm not sure how else to accomplish thi
for subtitle in subtitlesGen:
    subtitles.append(subtitle)

startTime = datetime.datetime.strptime('00:00:00.000000', "%H:%M:%S.%f").time()
endTime = subtitles[len(subtitles) - 1].end

TOTAL_SECONDS_IN_ONE_YEAR = float(60 * 60 * 24 * 365)
secondsInMovie = getSeconds(endTime)

movieSecondMultiplier = TOTAL_SECONDS_IN_ONE_YEAR / secondsInMovie

#pseudoNow is sixty seconds in the future, to allow time for the script to run
pseudoNow = datetime.datetime.now() + datetime.timedelta(0, 60)
for i, subtitle in enumerate(subtitles):
    numSeconds = getSeconds(subtitle.start)
    secondsWithMultiplier = numSeconds * movieSecondMultiplier
    nowWithDelay = pseudoNow + datetime.timedelta(0, secondsWithMultiplier)
    callSystem(nowWithDelay, i)