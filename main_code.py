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


def first_class_percentage_by_region(file):
    data = impt_my_csv_file(file)

    total_region = {}
    total_first_region = {}



    for row in data:
        region = row["Region"]
        ship_mode = row["Ship Mode"]

        if region not in total_region:
            total_region[region] = 0
        
        total_region[region] += 1

        if ship_mode == "First Class":
            if region not in total_first_region:
                total_first_region[region] = 0
            
            total_first_region[region] +=1

    first_calculation = {}
    for region in total_region:
        total = total_region[region]
        first_class = total_first_region.get(region, 0)
        percentage = (first_class / total) * 100
        first_calculation[region] = round(percentage, 2)

    
    return first_calculation
