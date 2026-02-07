import xmltodict
from pathlib import Path

def xmlparse(file: Path):
    with file.open('r', encoding="utf-8") as f:
        data_dict = xmltodict.parse(f.read())

        unique_keys = {}

        for i in data_dict[file.stem.lower()]['row']:
            for key in i.keys():
                if key not in unique_keys.keys():
                    unique_keys[key] = key[1:]


        vals = []
        for i in range(len(data_dict[file.stem.lower()]['row'])):
            current = data_dict[file.stem.lower()]['row'][i]
            tdict = {}
            for key, value in unique_keys.items():
                tdict[value] = current.get(key, 'NULL')
            vals.append(tdict)

        return [i for i in unique_keys.values()], vals