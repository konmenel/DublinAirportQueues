#!/usr/bin/env python3
"""Python script to scrape the terminal queues for dublin airport and save the data to a csv file."""
import os
import re
import datetime
import argparse
from typing import Dict

import requests
from bs4 import BeautifulSoup


URL = "https://www.dublinairport.com/flight-information/live-departures"

def save_to_csv(data: Dict[str, int]) -> None:
    """Function to save the data to a csv file. If it exist it will append the data to the file.

    Parameters
    ----------
    data : dict
        Dictionary of terminal number as key and queue times as value.
        ex: {'T1': 10, 'T2': 20}
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not os.path.isdir('data'):
        os.mkdir('data')
    
    for terminal in data.keys():
        filename = f'data/{terminal}_queues.csv'
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as file:
                file.write('Timestamp[%Y-%m-%d %H:%M],Queue[mins]\n')
    
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'{timestamp},{data[terminal]}\n')


def main() -> int:
    """Scrape the data from the website and save it to a csv file.

    Returns
    -------
    int
        Exit status of the program. 0 for success, 1 for failure. 
    """

    # Parsing the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--plot', action='store_true', help='Plot the data')
    parser.add_argument('-n', '--no-scrape', action='store_true', help='Do not scrape data')

    args = parser.parse_args()

    if args.no_scrape and not args.plot:
        print('No actions specified.')
        return 1

    if not args.no_scrape:
        print('Scraping the data...', end='', flush=True)
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")

        queues = soup.find("div", class_="sec-times")

        queues_re = re.compile(r'<span><span>Terminal</span> (T[12]) <strong> = ([0-9]+) min</strong></span>')

        queues_times = {match[0]: int(match[1]) for match in queues_re.findall(str(queues))}

        save_to_csv(queues_times)
        print('Done')
    
    if args.plot:
        # Importing plot only if needed (matplotlib is a heavy dependency)
        import plot
        plot.main()
    
    return 0



if __name__ == '__main__':
    raise SystemExit(main())
