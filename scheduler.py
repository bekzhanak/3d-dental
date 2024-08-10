import schedule
from db import extract_new_data
from utils import find_type_from_size, get_price_of_type, extract_date_time
from spreasheet import append_data_to_sheet


def get_insertion_data(data):
    photo_size = data[33]
    ray_type = find_type_from_size(photo_size)
    price = get_price_of_type(ray_type)
    date, time = extract_date_time(data[37])
    name = data[1] + " " + data[2]
    user = data[36]
    return [ray_type, price, name, date, time, user]


def job():
    new_data = extract_new_data()
    spreadsheet_rows = []
    for data in new_data:
        insertion_data = get_insertion_data(data)
        spreadsheet_rows.append(insertion_data)

    append_data_to_sheet(spreadsheet_rows)


if __name__ == "__main__":
    job()

# schedule.every().minute.do(job)
#
# while True:
#     schedule.run_pending()
