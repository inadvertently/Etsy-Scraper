Etsy-Description-Translater
==============

The Etsy Description translator is a small Python utility that uses BeautifulSoup to scrape a shop listing descriptions translate them, and export them as PDFs. I created this as adding descriptions to other Amazon platforms such as Amazon.mx and .br can be extremely unpleasant as translating hundreds of descriptions is not logical.

There is no rate-limiting protection built in. However, I have not encountered any rate limits. Read about  `Etsy Ratelimits`_. This program does not use the official Etsy API and is solely for educational purposes.

.. _Etsy Ratelimits: https://developer.etsy.com/documentation/essentials/rate-limits/

Features
--------
- Automated detection of paginated listings.
- No authentication is needed.
- Listing Titles Scraped and used as PDF filenames for easy navigation.
--------


* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

💻 Usage
==============
To run the program, run
::

    py main.py

📚 PDF Creator
================

- All PDFs are created in real-time and will be set to the dir ``Translations``.
- Filenames are set to match those of the listing title.
- Automatically centered, dependent on the character count and length of the translated description.

✏️ Scraper
================

Definitely could've done better in terms of organization and understanding here, though, this was mainly for personal use hence the carelessness of comprehension.

- Inspect Etsy's HTML to see if we're able to detect whether the shop has a paginated list of listings.
- Gather's description and title per listing.
- Removes special characters from Etsy listing titles as they may interfere with the PDF generation.


 Translation
================

Install dependencies:
::
    pip install easygoogletranslate
