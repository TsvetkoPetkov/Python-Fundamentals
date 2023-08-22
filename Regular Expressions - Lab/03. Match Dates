import re

dates = input()

pattern = r"(?P<Day>\b\d{2})([/\.-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4}\b)"

valid_dates = re.findall(pattern, dates)

for date in valid_dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
