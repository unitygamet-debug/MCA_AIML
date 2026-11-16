#write a program to accept time in hour , min , sec and covert the total in sec
hour = int(input("Enter hours: "))
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))

total_sec = (hour * 60 * 60) + (min * 60) + sec

print("Total time in seconds:", total_sec)