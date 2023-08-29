hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))



minutes = (mins + dura) % 60
hours = int(hour + (dura + mins)/60)% 24

print(hours, ":", minutes)
