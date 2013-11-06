ADS-API-Scripts
============

A collection of python scripts that pull data using the ADS API.

In order to use any of these scripts, you will need your own API developer key from SAO/NASA ADS.
You can request an API key here: https://docs.google.com/spreadsheet/viewform?formkey=dFJZbHp1WERWU3hQVVJnZFJjbE05SGc6MQ#gid=0

CfA Bib Keywords:
Gets article keywords from papers in the CfA Bibliography collected in the SAO/NASA ADS, by month and frequency.

Article Info From Bibcode:
Given a list of bibcodes, this script will capture the author, affiliation, abstract, title, journal, and publication year for each paper in that list.  It ignores non-ascii characters by turning them into comparable ascii letters (I think...).
