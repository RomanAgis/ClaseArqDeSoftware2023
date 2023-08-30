
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(filename1, filename2):
    x = read_csv_to_dict(filename1)
    y = read_csv_to_dict(filename2)

    

    for fila_x in x:
        articulo_existe = False  # Variable booleana 

   
        for fila_y in y:
            if fila_x['Name'] == fila_y['Name']:
                # El artículo ya existe en y, actualiza la cantidad
                articulo_existe = True
                fila_y['Quantity']= (int(fila_x['Quantity']))+int((fila_y['Quantity']))
               
                break  # No es necesario continuar buscando

    
        if not articulo_existe:
            x.append(fila_x)    

    write_list_of_dicts_to_csv("Nuevo.csv", x)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   
   main('sample_grocery.csv','grocery_batch_1.csv' )
  

 




