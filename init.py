import pandas as pd


class Event:
    def __init__(self):
        self.value = Event.get_file_name()
        Event.main(self.value)

    def main(csv_file):
        try:
            df = pd.read_csv(f'csv_files\{csv_file}.csv', delimiter=';', encoding='ISO-8859-1', )
        except (FileNotFoundError):
            print('File not found')
            exit()

        yn = input("Have header? (y/n): ")
        
        while True:
            if yn == 'y' or yn == 'Y':
                df.to_excel(f'xlsx_files\{csv_file}.xlsx', index=None, header=True)
            elif yn == 'n' or yn == 'N':
                df.to_excel(f'xlsx_files\{csv_file}.xlsx', index=None, header=False)
            else:
                break

    def get_file_name():
        while True:
            value = input('Enter file name: ')
            if value == '':
                print('File name is empty')
            else:
                break
        return value

if __name__ == '__main__':
    Event()