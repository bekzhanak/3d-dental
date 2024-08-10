import pandas as pd

prices = {
    "3D снимок 2 челюсти": 13000,
    "3D снимок 1 челюсти": 10000,
    "3D снимок сегмента": 7000,
    "3D снимок 1 зуба": 6000,
    "3D снимок придаточных пазух носа": 13000,
    "3D снимок придаточных пазух носа (с захватом лобных)": 16000,
    "Панорамный снимок": 4000,
    "ТРГ (боковой/прямой проекции)": 10000,
    "ТРГ (боковой проекции)": 10000,
    "Кисть": 5000,
    "3D диагностический снимок 2 челюсти + ВНЧС": 18000,
    "3D диагностический снимок 2 челюсти +ТРГ": 20000,
    "3D диагностический снимок 2 челюсти + пазухи носа": 18000,
    "3D диагностический снимок 2 челюсти + пазухи носа + ВНЧС": 26000,
    "ТРГ + панорамный снимок": 12000
    }


def find_type_from_size(photo_size):
    ranges_data = pd.read_csv("ranges.csv")
    for _, row in ranges_data.iterrows():
        if row['min'] <= int(photo_size) <= row['max']:
            return row['type']
    return "Кисть"


def get_price_of_type(ray_type):
    return prices[ray_type]


def extract_date_time(datetime_str):
    # Extract the date part
    date_part = datetime_str[:8]
    # Extract the time part
    time_part = datetime_str[8:]

    # Format the date as YYYY-MM-DD
    formatted_date = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:]}"

    # Format the time as HH:MM:SS
    formatted_time = f"{time_part[:2]}:{time_part[2:4]}:{time_part[4:]}"

    return formatted_date, formatted_time
