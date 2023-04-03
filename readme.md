# Project allows to scrape selected data from the website:
- Product title
- Product id (partnumber)
- Short description
- Extended description
- Manufacturer
- Product link
- Product image

## How to use
1. Install requirements
```
pip3 install -r requirements.txt
```
2. Run the script
```
python3 run.py
```

## Roadmap
1. [+] Scrape number of pages in catalogue
2. Loop through all catalogue pages
3. [+] Scrape product links on each page to the database
4. Loop through all product links
5. Scrape product data from each product page to the DB
    a. check if partnumber is already in DB
    b. evaluate item type id by algorythm from TS
    c. evaluate manufacturer id by algorythm from TS
    d. save extended description with HTML tags in table "ditemtypes"
6. Download product images to the FTP
7. Save images names and path to the DB
8. Setup script as an exe file