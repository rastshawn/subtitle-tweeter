Idea: To post subtitles for a given movie, spread over the course of a year, to a twitter account, using the 'at' command. 

Components: 

prep.py: Script to read subtitle .srt file and add a series of numbered 'at' jobs to the system based on when the subtitle appears onscreen. 

post.py: Script to read a given index, post to twitter. 

Installation:
Make sure you have python3 and pip3 installed. 

Install requirements:
pip3 install python-twitter pusub-parser

Modify config file to use your twitter API credentials.

place an SRT subtitle file in the same directory, and modify config file to link to that srt file. 
