import pandas as pd
from ics import Calendar, Event
import datetime

file_path = "calendario.xlsx"

# dataframe
df = pd.read_excel(file_path)

#check for my lessons
matches = df.isin(["Paolo"])

lessons = []

for row_idx, col_idx in zip(*matches.to_numpy().nonzero()):
    # print(f'Found Paolo at row {row_idx} and column {col_idx}')
    hours = df.iloc[row_idx, 0]
    subject = df.iloc[row_idx, col_idx - 1]  
    day = df.iloc[row_idx + 7 - int(hours.split(".")[0]), col_idx - 1]

    lessons.append({"hours": hours, "subject": subject, "day": day})

df_lessons = pd.DataFrame(lessons)
groupedlessons = df_lessons.groupby("day")
#print(groupedlessons.describe())

# for key, item in groupedlessons:
#     print(item)
calendar = Calendar()

for key, item in groupedlessons:
    data = item.to_dict("records")
    print(data)

    for el in data:
        #print("Ore: ", el["hours"])
        event = Event()
        event.name = el["subject"] + " - DAITA25"
        date_begin = date_begin = datetime.datetime.strptime(f"{key.date()} { el['hours'].split('-')[0]}", "%Y-%m-%d %H.%M")
        event.begin = date_begin
        event.duration = {"hours" : 1}
        calendar.events.add(event)

with open("lessons.ics", "w") as file:
    file.writelines(calendar)