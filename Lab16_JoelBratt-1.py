"""
Lab16_JoelBratt-1.py
Joel Bratt
Reads ohio unemployment data csv.
07/24/2026
"""
import matplotlib.pyplot as plot
import csv
from datetime import datetime

def main():
    """The main function does everything."""

    dates = []
    unemployment = []

    file_name = 'OHUR.csv'

    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            header_row = next(csv_reader)
            print("Reading header row:")
            for index, column_name in enumerate(header_row):
                print(f' Column {index}: {column_name}')

            for row in csv_reader:
                try:
                    date_string = row[0]
                    date_obj = datetime.strptime(date_string, "%Y-%m-%d")

                    rate = float(row[1])

                    dates.append(date_obj)
                    unemployment.append(rate)

                except ValueError as e:
                    print (f'Data convert erro on {row}: {e}. Skipping row')
                    continue
                except IndexError as e: 
                    print(f'Empty data on row {e}. Skipping row')
                    continue

    except FileNotFoundError:
        print(f'File of {file_name} Not found. Ensure that there is a file in the same folder as the script.')
        return
    except Exception as e:
        print(f'An unpredictable, unforseeable, or otherwise unknown error has occured while trying to read file {e}.')
        return

    if dates and unemployment:

        plot.figure(figsize=(12,10))

        plot.plot(dates, unemployment, color='cyan', linestyle='-')

        plot.title('Ohio Unemployment Rates and Dates')

        plot.xlabel("Date")
        plot.ylabel('Unemployment Rates')

        image = "ohio_unemployment.png"
        plot.savefig(image)
        print('Created an image check your folder.')

    else:
        print('\nNo data was found/Something went wrong.')

if __name__ == "__main__":
    main()
