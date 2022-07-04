from operator import itemgetter
times = {
    'Palmeiras': 18,
    'Flamengo': 12,
    'Coritiba': 22
}
print(times)
timesnovos = sorted(times.items(), key=itemgetter(1), reverse=True)
print(timesnovos)

for i, time in timesnovos:
    # print(f'{i+1} - {time[0]} - {time[1]}')
    print(i)
print(enumerate(timesnovos))