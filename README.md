# txtbook-client

A CLI client to securely search and download textbooks to a specified folder from LibGen.
To use the client download `gettxtbook.py` and ensure that you have Python3 and `pip` installed.

### Installing Dependencies

```bash
pip install .
```

### Running the CLI

```bash
python3 gettxtbook.py
```

Once you've run the client you'll be provided an input where you can search for your textbook title or author. Once you've entered your search a list of search results will be displayed that you can select from. The textbook edition, author, title, and published date will be displayed the same way it is on LibGen.

### Changing Mirrors

If you would like to select a different mirror to download from please change the index of `download_links` to `IPFS` or your mirror of choice. The default mirror is Cloudflare.

### EPUB

If you would like to exclusively download `.epub` files please replace

```python
filters = {"Extension": "pdf"}
# replace this section with
filters = {"Extension" : "epub"}
```

### Future Improvements

In the next version I will upgrade the CLI to a a React and Electron GUI that will traverse your folder and allow you to categorize and view your textbooks with the relevant table of contents.
