import requests
from requests import api
import json
from termcolor import colored
import os
from config import api_key


if api_key:
    os.system('cls' if os.name == 'nt' else 'clear')

    keyword = input(colored("\nEnter a keyword: ", "green"))
    print("\nEnter 5 extensions, here are some examples:\ndocx\txlsx\tcsv\tpdf\njson\tdb\ttxt\tpng\njpg\tjpeg\tmp3\tmp4\npub\tid_rsa\tpem\tpriv")
    print("\nPremade Suggestions: \nid_rsa, pem, db, json, pub\ndocx, txt, xlsx, csv, json\n")
    extensions = input(colored("Extensions (comma separated): ", "green"))

    # Clean up input ready for insertion to URL.
    keyword = keyword.replace(" ", "%20").replace('"', '%22')
    extensions = extensions.replace(", ", ",").replace(" ", ",")

    ext_count = extensions.split(",")

    # Split to extnesion choices in to their own separate entities.
    ext_1 = extensions.split(",")[0]
    ext_2 = extensions.split(",")[1]
    ext_3 = extensions.split(",")[2]
    ext_4 = extensions.split(",")[3]
    ext_5 = extensions.split(",")[4]

    #print(f"\nExt1: {ext_1}\nExt2: {ext_2}\nExt3: {ext_3}\nExt4: {ext_4}\nExt5: {ext_5}")

    url = f"https://buckets.grayhatwarfare.com/api/v1/files/{keyword}/0/1000?extensions={extensions}&access_token={api_key}"

    print(f"\nSearching...")

    response = requests.get(url)
    data = json.loads(response.content)

    # Count the documents up
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0

    print("\n---------- RESULTS ----------\n")
    for links in data['files']:
        if links['url'].split(".")[-1] == ext_1:
            print(colored(f"{links['url']}", 'red'))
            a_count = a_count + 1
        elif links['url'].split(".")[-1] == ext_2:
            print(colored(f"{links['url']}", 'blue'))
            b_count = b_count + 1
        elif links['url'].split(".")[-1] == ext_3:
            print(colored(f"{links['url']}", 'green'))
            c_count = c_count + 1
        elif links['url'].split(".")[-1] == ext_4:
            print(colored(f"{links['url']}", 'white'))
            d_count = d_count + 1
        elif links['url'].split(".")[-1] == ext_5:
            print(colored(f"{links['url']}", 'magenta'))
            e_count = e_count + 1

    a_count = colored(str(a_count), "red")
    b_count = colored(str(b_count), "blue")
    c_count = colored(str(c_count), "green")
    d_count = colored(str(d_count), "white")
    e_count = colored(str(e_count), "magenta")

    # Output the results from GrayHatWarfare.
    print(f"\nResults Found: {data['results']} \n{ext_1}s: {a_count} \n{ext_2}s: {b_count} \n{ext_3}s: {c_count} \n{ext_4}s: {d_count} \n{ext_5}s: {e_count}")
else:
    print("\nPlease provide an API Key within config.py...\n")
