# Reading and writing Comma Separate Values files with Python
import csv


# TODO: list the dialects that are available to use
print(csv.list_dialects())

# TODO: Open a CSV file and read each row of data
def readerSample():
    with open('StockQuotes.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


# TODO: Use the CSV module Sniffer to see what dialect of CSV this is
def useSniffer():
    with open('StockQuotes.csv') as csvfile:
        dialects = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        hasHeader = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        print('Header found:', hasHeader)
        print(dialects.delimiter)
        print(dialects.escapechar)
        print(dialects.quotechar)


# TODO: Write data to a CSV file
def writerSample():
    with open('SampleData.csv',mode='w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'Department', 'Location'])
        csvwriter.writerow(['John Doe', 'Accounting', 'San Francisco'])
        csvwriter.writerow(['Jane Dae', 'Engineering', 'Seatle'])
        csvwriter.writerow(['Jim Due', 'Human Resources', 'New York'])
        


# Exercise the samples
# readerSample()
writerSample()
# useSniffer()
