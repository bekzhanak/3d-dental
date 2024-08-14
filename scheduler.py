import schedule
from db import extract_new_data
from utils import find_type_from_size, get_price_of_type, extract_date_time, get_ray_type_from_comment
from spreasheet import append_data_to_sheet


def get_insertion_data(data):
    photo_size = data[33]
    ray_type = find_type_from_size(photo_size)
    ray_types = []
    if ray_type is None:
        comment = str(data[46]).lower()
        for ray in comment.split():
            ray_types.append(get_ray_type_from_comment(ray))
    else:
        ray_types = [ray_type]
    prices = []
    for ray_type in ray_types:
        price = get_price_of_type(ray_type)
        prices.append(price)
    date, time = extract_date_time(data[37])
    name = data[1] + " " + data[2]
    dentist = data[23]
    discount = data[41]
    return ray_types, prices, [discount, name, date, time, dentist]


def job():
    new_data = extract_new_data()
    spreadsheet_rows = []
    for data in new_data:
        insertion_data = get_insertion_data(data)
        for i in range(len(insertion_data[1])):
            spreadsheet_rows.append([insertion_data[0][i], insertion_data[1][i], *insertion_data[2]])

    append_data_to_sheet(spreadsheet_rows)


if __name__ == "__main__":
    job()
    schedule.every(30).minutes.do(job)

    while True:
        schedule.run_pending()
