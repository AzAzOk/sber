import re
import json
from datetime import datetime


def mask_card_number_from(text):
    match = re.search(r'\d{16,20}', text)
    if match:
        return text.replace(
            match.group(),
            ' '.join([match.group()[:4], match.group()[4:6] + '**', '*' * 4, match.group()[-4:]]))
    return text


def mask_card_number_to(text):
    match = re.search(r'\d{4}$', text)
    if match:
        return '**' + match.group()
    return text


with open('operations.json', 'r', encoding='utf-8') as fors:
    data = json.load(fors)


def key(datta):
    if datta.get("state") == "EXECUTED":
        return datta.get("date", "")
    else:
        return ""


sorted_data = sorted(data, key=key, reverse=True)

for entry in sorted_data[:5]:
    date = datetime.strptime(entry["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

    print(f"{date} {entry["description"]}")

    print(f""
          f"{mask_card_number_from(entry.get("from", "Неизвестно"))}"
          f" -> "
          f"{mask_card_number_to(entry.get("to", "Неизвестно"))}")

    print(f"{entry["operationAmount"]["amount"]} {entry["operationAmount"]["currency"]["name"]}\n")
