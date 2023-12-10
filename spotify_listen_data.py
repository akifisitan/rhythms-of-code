import json
from pprint import pprint
from datetime import datetime


def read_data(filename: str):
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


# Between 19/08/2023 and 26/10/2023
def get_listened_between_dates():
    data1 = read_data('spotify_data/2022-2023.json')
    data2 = read_data('spotify_data/2023_2.json')
    data3 = read_data('spotify_data/2023_3.json')
    all_listened = data1 + data2 + data3
    listened_by_date = {}
    for data in all_listened:
        datetime_string = data.get('ts')
        datetime_object = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%SZ')
        if datetime(2023, 8, 19) <= datetime_object < datetime(2023, 10, 27):
            # Check if song was listened to for more than 30 seconds
            ms = data.get('ms_played')
            if ms < 30 * 1000:
                continue
            date = str(datetime_object.date())
            time = str(datetime_object.time())
            minutes, remainder = divmod(ms // 1000, 60)
            seconds, milliseconds = divmod(remainder, 1)
            played = f"{minutes:02d}:{int(seconds):02d}.{int(milliseconds * 1000):02d}"
            track_name = f"{data.get('master_metadata_album_artist_name')} - {data.get('master_metadata_track_name')}"
            if date in listened_by_date:
                listened_by_date[date].append({
                    'played': played,
                    'time': time,
                    'name': track_name
                })
            else:
                listened_by_date[date] = [{
                    'played': played,
                    'time': time,
                    'name': track_name,
                }]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(listened_by_date, f, indent=4)


get_listened_between_dates()
