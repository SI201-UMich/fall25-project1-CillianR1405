# Cillian Reynolds
# UMID: 2405 4188
#

# had to slightly adjust original calculations to ensure that they included 3 columns


import kagglehub, os

path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")


def impt_my_csv_file(file):

    my_data = []
    with open(file, 'r') as my_file:
        data = my_file.readlines()
        headers = data[0].strip().split(",")


        for line in data[1:]:
            my_values = line.strip().split(",")    
            row_dict = {}                       
            for i in range(len(headers)):
                header = headers[i]
                value = my_values[i]
                row_dict[header] = value

            my_data.append(row_dict)          
    return my_data
