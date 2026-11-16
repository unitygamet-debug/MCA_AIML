import csv


#wap to import student.csv files and display all the values in terminal using dictReaderformat.
n_marks = 0
with open("students.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        mark = int(row["marks"])
        if mark< 80:
            n_marks = mark + (mark/2)
            if n_marks > 100:
                n_marks = 100
                print(row["name"], n_marks)
            else:
                print(row["name"], n_marks)











