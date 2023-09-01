#!/usr/bin/python3
"""A script that sends a POST request with an email parameter to a URL
   and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception if request fails
        print(response.text)  # Print the body of the response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
