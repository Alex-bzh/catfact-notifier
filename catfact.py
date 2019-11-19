#!/usr/bin/env python3
# coding: utf8

#
#   Modules imported
#
import urllib.request, json

#
#   Specific functions
#
def main(url, key):
    """
        Reads the content of a simple JSON object from HTTP
        @param {String} url: the URL to call
        @param {String} key: the key of the value to query
    """

    # Makes a request
    response = urllib.request.urlopen(url)

    # Gets the data
    data = response.read()

    # Reads it as a JSON object
    content = json.loads(data.decode("utf-8"))[key]

    # Finally, prints it
    print(content)


#
#   Main
#
if __name__ == "__main__":

    url = 'https://catfact.ninja/fact'
    key = 'fact'

    # Triggers the main() function
    main(url, key)
