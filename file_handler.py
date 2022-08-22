import csv


class FileHandler:
    def read_rows(self, file_path: str):
        with open(file_path, encoding='utf-8') as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]

    def write_rows(self, file_path, header, rows):
        with open(file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # writer.writerow(header)
            writer.writerows(rows)
