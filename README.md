# Twilight Zone Bot [@botRodSerling](https://twitter.com/botRodSerling)
This was a personal project to get familiar with Twitter's API and Markov chains.

#### Libraries used
* [Tweepy](https://github.com/tweepy/tweepy) to interact with Twitter API
* [Markovify](https://github.com/jsvine/markovify) to generate Markov chains


## rod.py

Reads `rod.txt` as input to create markov chains.

Tweets a randomly generated sentence based on input.

## scrapeMonologues.py

Scrapes Rod Serling's intro & outro monologues from [Wikiquote](https://en.wikiquote.org/wiki/The_Twilight_Zone_(1959_TV_series)) and outputs it to `rod.txt`.

I cleaned up a few monologues that got interrupted by other dialogue.

## rod.txt

This is the cleaned up and minimized text generated from `scrapeMonologues.py` that is read by `rod.py`.
