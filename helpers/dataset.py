import csv


class DatasetHandler:
    def __init__(self):
        self.file_path = 'helpers/data/coral_data.csv'
        self.data = []
        self.read_csv()

    def read_csv(self):
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)

    def get_raw_data(self):
        return self.data

    def get_data(self, years=None):
        if not years:
            years_list = list(set([int(row['Year']) for row in self.data]))
        elif isinstance(years, int):
            years_list = [years]
        else:
            years_list = years

        all_year_data = []
        for year in years_list:
            year_data = []
            for coral in ['Great Barrier Reef', 'Maldives', 'Beliza and West Caribbean']:
                for row in self.data:
                    if int(row['Year']) == int(year):
                        year_data.append(int(float(row[coral])))
                        break
            all_year_data.append(year_data)

        if len(years_list) == 1:
            return all_year_data[0]
        else:
            return all_year_data


if __name__ == "__main__":
    dataset_handler = DatasetHandler()

    # get data for single year
    yr_data = dataset_handler.get_data(2020)
    print(yr_data)

    # get data for multiple years
    yr_data = dataset_handler.get_data([2020, 2021])
    print(yr_data)

    # get data for all years
    yr_data = dataset_handler.get_data()
    print(yr_data)
