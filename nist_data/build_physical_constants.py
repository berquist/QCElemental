"""
This file will generate a JSON blob usable by QCElemental for physical constants
"""

import json
import datetime
import requests
from yapf.yapflib.yapf_api import FormatCode

metadata_file = "srd121_nist-codata-fundamental-physical-constants-2014-metadata.json"
with open(metadata_file, "r") as handle:
    metadata = json.load(handle)

title = metadata["title"]
date_modified = metadata["modified"]
year = date_modified.split('-')[0]
doi = metadata['distribution'][-1]['accessURL'].strip('https://dx.doi.org/')
url = metadata['distribution'][0]['downloadURL']
access_date = str(datetime.datetime.utcnow())

constants = requests.get(url).json()

output = f'''
"""
This is a automatically generated file from the {year} NIST fundamental constants.
Title: {title}
Date: {date_modified}
DOI: {doi}
URL: {url}
Access Date: {access_date} UTC

File Authors: QCElemental Authors
"""


'''

constants_json = {
    "title": title,
    "date": date_modified,
    "doi": doi,
    "url": url,
    "access_data": access_date,
    "constants": {}
}

for pc in constants['constant']:
    value = pc['Value'].strip()
    uncertainty = pc['Uncertainty']
    if uncertainty == '(exact)':
        value = value.replace('...', '')

    constants_json["constants"][pc["Quantity "].lower()] = {
        "quantity": pc["Quantity "],
        "unit": pc["Unit"],
        "value": value.replace(" ", ""),
        'uncertainty': uncertainty
    }
output += f"nist_{year}_codata = {constants_json}"

output = FormatCode(output)

fn = f"nist_{year}_codata.py"
with open(fn, "w") as handle:
    handle.write(output[0])
