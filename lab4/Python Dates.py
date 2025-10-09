#1
print ("1 ex")
import datetime


x = datetime.datetime.now()
print("Current date and time:", x.date())


new_date = x - datetime.timedelta(days=5)
print("Date and time 5 days ago:", new_date.date())

#2
print ("2 ex")

x = datetime.datetime.now()
yesterday= x - datetime.timedelta(days=1)
tomorrow = x + datetime.timedelta(days=1)

print("yesterday:", yesterday.date())

print("today:", x.date())

print("tomorrow:", tomorrow.date())

#3

print ("3 ex")

x = datetime.datetime.now()
print("original datetime:", x)

new_x = x.replace(microsecond=0)
print("without microseconds:", new_x)

#4
print ("4 ex")
date1 = datetime.datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime.datetime(2025, 10, 5, 10, 40, 0)

difference = date1 - date2
seconds = difference.total_seconds()

print("Difference:", difference)
print("Difference in seconds:", seconds)
