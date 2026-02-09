# StackConverter

StackConverter is a small app to convert Stack Exchange data dumps from .xml format into .csv files for creation of local SQL databases (using DBeaver or similar).

## Installation

To install necessary packages, use

```bash
pip install -r requirements.txt
```

then run the app once to create the necessary directories.

## Usage

Download .xml files for the required Stack Exchange forum from [Internet Archive](https://archive.org/details/stackexchange) and unpack/copy files into StackConverter's 'xmls' folder.

Run the app from the command line, and the xml files will be converted into DBeaver-friendly csv files.

When loading csv files into DBeaver, use " as the quote character, and '\\' as the escape character.

Data types for each table can be found in

```bash
root_directory/data_types/QueryResults.csv
```

but may need tweaking depending on which DBMS is being used, e.g. NVARCHAR(-1) may become VARCHAR() or TEXT in Postgres.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.