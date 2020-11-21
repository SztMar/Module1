import csv




with open('C:\\Kodilla_course\\Module9\\example_csv.csv',newline='') as csvfile_r:
    spamreader = csv.reader(csvfile_r, delimiter= ';')

    for row in spamreader:
        print(", ".join(row))

with open('example_csv3.csv','w', newline='') as csvfile_w:
    spamwriter = csv.writer(csvfile_w, delimiter= ';')

    spamwriter.writerow(['Spam'] *5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])





