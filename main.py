import feedparser
import re


# Define URLs to fetch film list.
URLS = [
    'http://www.thepiratefilmes.com/feed'
    ]

# Parse feed
feed = feedparser.parse(URLS[0])

# Build list of items in the feed
movie_list = [item.content[0].value for item in feed.entries]


# Defines the details to be parsed
details = [
    'TITULO ORIGINAL',
    'LAN.AMENTO',
    'G.NERO',
    'IMDB'
]

# Function to parse the movie details
def parse_details(labels, description):

    # Iterate through the details list and retrieve each value
    for label in labels:

        # Regex to find the label and description
        regex = r'<strong>({}):.*>(.*)<'.format(label)

        # Actual regex matching
        match = re.search(regex, description)

        # Print label and description
        print('{}: {}'.format(match.group(1), match.group(2)))

    # Print the magnet URI
    print((re.search(r'(magnet:\?xt=urn:btih:[A-F\d]+)', description)).group(1))  # prints magnet link

    # Print a separator
    print('\n')

# Iterates through the movie list and parses the details
for movie in movie_list:
    parse_details(details, movie)
