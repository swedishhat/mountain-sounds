# Mountain Sounds

This is a proof of concept Python program that uses the Google Maps APIs to make bautiful, screechy music from the elevations collected from the path between two points. You need to get an API key from Google to make this work and enable geocoding and elevation. 

# Process
The script collects a few basics from the user:
* Start address (geocoded to produce lat/lng)
* End address (geocoded to produce lat/lng)
* Total time of produced sound file
* "Sampling rate" (i.e. number of elevation data points per second)

The script then gathers all the necessary points, normalizes them from -1 to 1, packages it into a .WAV file and then saves the result. 

# TODO
* Rewrite in javascript -- still use google API, add things like graph.js
* API key entry
* Better error checking
* Graph points
* Make sounds
* GUI
* Refactor with functions and classes
