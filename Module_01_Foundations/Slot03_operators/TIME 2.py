#write a program to accept time in sec and convert time into total hour, min , sec
sec = int(input("Enter time in seconds: "))

hour = sec // 3600
sec = sec % 3600

min = sec // 60
sec = sec % 60

print("Hour:", hour)
print("Minutes:", min)
print("Seconds:", sec)