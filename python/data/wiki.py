# Install
# pip install wikipedia

import wikipedia

search = """
SEARCH FOR:

Trailer
Video
Movie
"""
print(search)

while True:
    command = input("Search: ")
    if command == "Trailer":
        print(wikipedia.page("Trailer").content)

    if command == "Video":
        print(wikipedia.page("Video").content)

    if command == "Movie":
        print(wikipedia.page("Movie").content)
