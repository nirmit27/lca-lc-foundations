"""
Driver script - PoC
"""

import requests

from pprint import pprint


API_URL = r"http://localhost:8000"


def main():
    print("\nPoC - Validation\n")

    try:
        response = requests.post(f"{API_URL}/sum")
        pprint(response.json())
    except Exception as e:
        print(f"ERROR : {e}")


if __name__ == "__main__":
    main()
