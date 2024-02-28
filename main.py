import json
from datetime import datetime

with open('operations.json', 'r', encoding='utf-8') as fors:
    data = json.load(fors)


def key(F):
    if F.get("state") == "EXECUTED":
        return F.get("date", "")
    else:
        return ""


sorted_data = sorted(data, key=key, reverse=True)

for entry in sorted_data[:5]:
    from_account = entry.get("from", "Неизвестно")
    from_masked = ' '.join(
        [from_account[:4], '*' * 6, from_account[-4:]]) if from_account != "Неизвестно" else "Неизвестно"
    date_str = entry["date"]
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

    print(f"{date} {entry["description"]}")
    print(f"{from_masked} -> {entry["to"]}")
    print(f"{entry["operationAmount"]["amount"]} {entry["operationAmount"]["currency"]["name"]}\n")
