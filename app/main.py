import logging
from pathlib import Path
logger = logging.getLogger(__name__)

from config.settings import CSV_DIR, XML_DIR
from create_csv import create_csv

def ensure_directories() -> None:
    XML_DIR.mkdir(parents=True, exist_ok=True)
    CSV_DIR.mkdir(parents=True, exist_ok=True)

def xml_files_exist() -> list[str]:
    return [
        p for p in XML_DIR.iterdir()
        if p.is_file() and p.suffix.lower() == '.xml'
    ]

def main():

    ensure_directories()

    xml_files = xml_files_exist()
    
    if not xml_files:
        logger.info(f'No xml files found. Please add xmls to {XML_DIR.resolve()} and rerun this script')
        return
    
    logger.info(f'Found {len(xml_files)} XML files. Starting CSV conversion')
    create_csv()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()