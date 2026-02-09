from pathlib import Path
import csv
import logging

logger = logging.getLogger(__name__)

from parse_xml import xmlparse

def create_csv() -> None:

    """
    Converts all .xml files in xmls folder
    into CSV format and writes to .csv files
    """
    
    for f in Path("xmls").iterdir():
        file_path = Path("csvs") / f"{f.stem}.csv"

        if not file_path.exists():

            with file_path.open('w', newline='', encoding='utf-8') as file:

                cols, rows = xmlparse(f)

                writer = csv.writer(
                    file, 
                    quotechar='"', 
                    quoting=csv.QUOTE_ALL, 
                    escapechar='\\',
                    lineterminator="\n"
                    )
                
                writer.writerow(cols)
                
                for r in rows:
                    writer.writerow(r.values())

            logger.info(f"File '{file_path.name}' created.")

        else:
            logger.info(f"The file '{file_path.name}' already exists.")