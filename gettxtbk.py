from libgen_api import LibgenSearch
from pypdf import PdfReader
import wget
import os
import json

s = LibgenSearch()
filters = {"Author": "Peter J. Eccles", "Extension": "pdf"}
results = s.search_title_filtered(
    "An Introduction to Mathematical Reasoning", filters, exact_match=False
)
txtbook = results[0]


def download_pdf(entry):
    download_links = s.resolve_download_links(entry)
    url = download_links["Cloudflare"]
    wget.download(url, "C:/Users/rishi/Documents/GitHub/txtbook-client/tmp_txtbooks")


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


files = list_files("./tmp_txtbooks", ".pdf")


def toc(bookmark_list):
    result = {}
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call
            result.update(toc(item))
        else:
            result[item.title] = reader.get_destination_page_number(item) + 1
    return result


reader = PdfReader(files[0])
with open("toc.json", "w") as write_file:
    json.dump(toc(reader.outline), write_file)
# download_pdf(txtbook)
