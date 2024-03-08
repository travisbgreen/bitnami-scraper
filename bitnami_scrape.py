#!/usr/bin/env python

import re
import requests
import logging

# jupyter does weird stuff with logging
# https://stackoverflow.com/questions/18786912/get-output-from-the-logging-module-in-ipython-notebook
logger = logging.getLogger()
logger.setLevel(logging.INFO)

base_url = 'https://bitnami.com'
stacks_url = f'{base_url}/stacks/virtual-machine'

regex_pattern = r'(?<=href=\x22)/stack/[^\x22]+virtual-machine(?=\x22)'
ova_regex = r'(?<=\shref=\")[^\x22]+\.ova(?=\x22)'

ova_list = []

response = requests.get(stacks_url)
if response.status_code == 200:
    content = response.text
    matches = re.findall(regex_pattern, content)
    if matches:
        for match in matches:
            logging.debug(f"Found match: {match}")
            stack_url = f'{base_url}{match}'
            stack_response = requests.get(stack_url)
            if stack_response.status_code == 200:
                stack_content = stack_response.text
                ova_matches = re.findall(ova_regex, stack_content)
                if ova_matches:
                    for ova in ova_matches:
                        logging.debug(f"Found match: {ova}")
                        logging.debug(f"Download URL: {base_url}{ova}")
                        ova_list.append(f"{base_url}{ova}")
                else:
                    logging.error("No matches found.")
    else:
        logging.error("No matches found.")
else:
    logging.error(f"Failed to fetch URL. Status code: {response.status_code}")


# %%
ova_list = list(set(ova_list))
print(f"Found {len(ova_list)} matches.")

# %%
with open('tmpfile', 'w') as f:
    for ova in ova_list:
        logging.debug(f'ova file link: {ova}')
        f.write(ova + '\r\n')
    f.close

print('list complete, now run the following command:')
print('wget -nc --continue -i tmpfile')
