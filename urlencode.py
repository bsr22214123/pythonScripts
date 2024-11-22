#!/usr/bin/python3

import urllib.parse
import argparse

def url_encode(string, encode_all=False):
    if encode_all:
        # Encode all characters by setting safe characters to an empty string
        encodedString = urllib.parse.quote(string, safe='')
    else:
        # Default encoding
        encodedString = urllib.parse.quote(string)
    
    encodedString = encodedString.replace('.', '%2E')
    return encodedString

def url_decode(string):
    return urllib.parse.unquote(string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="URL encode a string.")
    parser.add_argument("string", help="The string to URL encode")
    parser.add_argument("-all", action="store_true", help="Encode all characters, including safe ones")
    parser.add_argument("-d", action="store_true", help="Decode the URL encoded string")

    args = parser.parse_args()

    if args.d:
        decoded_string = url_decode(args.string)
        print(f"{decoded_string}")
    else:
        encoded_string = url_encode(args.string, args.all)
        print(f"{encoded_string}")
