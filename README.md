You use Tiller Money and also use Apple Card, but Apple does not yet support OFX to automatically import your transaction into Tiller. Oh noes! This script helps you import your Apple transactions into Tiller.

Workflow: 

1. Download your Apple Card transactions in csv format (instructions [here](https://www.macrumors.com/how-to/export-apple-card-data-to-spreadsheet/)).
2. From the command line, navigate to the root of this repo
3. From the command line, issue the command:
    `python apple-card.py tillerize --input inputfilename.csv --output outputfilename.csv --last4 1234`

where:
* `inputfilename.csv` is the path to your exported Apple Card csv
* `outputfilename.csv` is where the ready-for-Tiller csv will be
* `1234` (optional) are the last 4 digits of your Apple Card if you care about having them right in the output csv

You can then open `outputfilename.csv`, copy your transactions, and paste them in the Transactions worksheet of your Tiller workbook as explained [here](https://help.tillerhq.com/en/articles/432708-how-to-manually-import-your-bank-data), sort all transactions by date, edit categories, etc.
