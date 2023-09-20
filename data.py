import csv

# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]



def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    data = read_csv_to_dict(r'C:\Users\r_man\OneDrive\Escritorio\Nueva carpeta\LayerApp\src\grocery\repository\sample_grocery.csv')
    for row in data:
        print(row)
    return data

#def load_sample_data():
#    return [
#        {
#            'SKU': 123,
#            'quantity': 15
#        },
#        {
#            'SKU': 456,
#            'quantity': 16
#        },
#        {
#            'SKU': 789,
#            'quantity': 17
#        },
#    ]
