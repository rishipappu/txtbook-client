from libgen_api import LibgenSearch
from pypdf import PdfReader
from prettytable import PrettyTable
import wget
import os
import json

s = LibgenSearch()


def download_pdf(entry):
    download_links = s.resolve_download_links(entry)
    url = download_links["Cloudflare"]
    wget.download(url, "C:/Users/rishi/Documents/GitHub/txtbook-client/tmp_txtbooks")


def search():
    print("Please enter a title (leave blank if only searching by author): \n")
    title = input()
    print(
        "Please enter the name of the author (leave blank if only searching by title): \n"
    )
    author = input()
    filters = {"Extension": "pdf"}
    results = ""
    if title == "" and author == "":
        print("You have not entered any search terms please search again!\n")
        search()
    elif title != "" and author == "":
        results = s.search_title_filtered(title, filters, exact_match=False)
    elif title == "" and author != "":
        results = s.search_author_filtered(author, filters, exact_match=False)
    else:
        filters.update({"Author": author})
        results = s.search_title_filtered(title, filters, exact_match=False)

    print_search(results)
    return results


def print_search(titles):
    search_results = PrettyTable(["Index", "Title", "Author", "Publisher", "Pages"])
    index = 1
    for doc in titles:
        search_results.add_row(
            [index, doc["Title"], doc["Author"], doc["Publisher"], doc["Pages"]]
        )
        index += 1
    print(search_results)


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


# files = list_files("./tmp_txtbooks", ".pdf")


def toc(bookmark_list):
    result = {}
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call
            result.update(toc(item))
        else:
            result[item.title] = reader.get_destination_page_number(item) + 1
    return result


# reader = PdfReader(files[0])
# with open("toc.json", "w") as write_file:
#     json.dump(toc(reader.outline), write_file)
# download_pdf(txtbook)
current_search = search()
