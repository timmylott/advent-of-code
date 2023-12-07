import re

file1 = open('day_06_input.txt', 'r')
file_lines = file1.readlines()

race_time = []
race_distance = []

for line in file_lines:
    re.findall('\d+',line)
    if 'Time:' in line:
        race_time = re.findall('\d+',line)
    if 'Distance:' in line:
        race_distance = re.findall('\d+', line)

print(race_time)
print(race_distance)
hold_time_distance = {}
beat_record = 0
race_beat_record = []
record_mult = 1

for t in race_time:
    d = race_distance[race_time.index(t)]
    for r in range(int(t)):
        dist = (r+1) * (int(t)-(r+1))
        hold_time_distance[str(r+1)] = dist
        if dist > int(d):
            beat_record = beat_record + 1
    race_beat_record.append(beat_record)
    beat_record = 0

for r in race_beat_record:
    record_mult = record_mult * int(r)
print(race_beat_record)
print(record_mult)

# part 2

file1 = open('day_06_input.txt', 'r')
file_lines = file1.readlines()

race_time = []
race_distance = []

for line in file_lines:
    re.findall('\d+',line)
    if 'Time:' in line:
        race_time = line.split(':')[1].replace(' ','').strip()
    if 'Distance:' in line:
        race_distance = line.split(':')[1].replace(' ','').strip()

beat_record = 0
d = race_distance
t = race_time

for r in range(int(t)):
    dist = (r+1) * (int(t)-(r+1))
    if dist > int(d):
        beat_record = beat_record + 1

print(beat_record)