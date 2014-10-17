Using rawWordDict_to_WordCloud.py
============

This script takes a rawWordDict list from an ADS 2.0 (http://labs.adsabs.harvard.edu/adsabs/) word cloud, and returns terms and weights in a timestamped .txt file for creating a wordle.net word cloud.

ADS: Query the ADS (http://labs.adsabs.harvard.edu/adsabs/) 

Developer's Toolkit: Open the browser's developer tools > network

ADS: View the ADS records as a Word Cloud 

Developer's Toolkit: Click on the word_cloud link on the left, click on the response tab at the top
Scroll down until you see a long string beginning with:

    //initialize final word list
    var wordCloud = {
        //load new data
        rawWordDict : {"AAS": {"idf": 0.00046360686138154843, "total_occurences": 9},

Highlight the entire rawWordDict line by multiple clicking

Copy and paste to a text editor - make no alterations!

Save as rawWordDict.txt in the same location as rawWordDict_to_WordCloud.py

Run rawWordDict_to_WordCloud.py (which produces a .txt file called cloudseedertimestamp.txt)

This text can now be copied and pasted into the create box at www.wordle.net