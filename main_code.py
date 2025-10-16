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




def total_profit_region_category(file):
    data = impt_my_csv_file(file)

    profit_dict = {}

    for row in data:
        region = row["Region"]
        category = row["Category"]
        profit = float(row["Profit"])

        if region not in profit_dict:
            profit_dict[region] = {}

        if category not in profit_dict[region]:
            profit_dict[region][category] = 0

        profit_dict[region][category] += profit

    return profit_dict



def col_names(file):

    col_header_lst = []
    my_data = impt_my_csv_file(file)
    headings = my_data[0].split(',')

    for header in headings:
        col_header_lst.append(header)

    
    return col_header_lst

def sample_data_row(file):
    my_data = impt_my_csv_file(file)
    row_data = my_data[1].strip()
    return row_data


def count_rows(file):
    my_data = impt_my_csv_file(file)
    count = -1 # trying to avoid counting header
    for line in my_data:
        count+=1

    return count



def write_results_to_txt(file):
    first_class_results = first_class_percentage_by_region(file)
    profit_results = total_profit_region_category(file)

    with open("results.txt", "w") as f:
        f.write("Project 1 Results\n\n")

        f.write("First Class Percentage by Region:\n")
        for region, percent in first_class_results.items():
            f.write(f"  {region}: {percent}%\n")
        f.write("\n")

        f.write("Total Profit by Region and Category:\n")
        for region, categories in profit_results.items():
            f.write(f"  {region}:\n")
            for category, profit in categories.items():
                f.write(f"    {category}: {round(profit, 2)}\n")

    print("Results written to 'results.txt'")







def main():
    file = f"{path}/SampleSuperstore.csv"
    write_results_to_txt(file)

tester_run = main()

print(tester_run)

import unittest
class TestAll(unittest.TestCase):
    def setUp(self):
        self.test_file = "sample.csv"
        
    def test_dict_regions(self):
        result = first_class_percentage_by_region(self.test_file)
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result) > 0)

    def test_values_in_range(self):
        result = first_class_percentage_by_region(self.test_file)
        for val in result.values():
            self.assertIsInstance(val, float)
            self.assertGreaterEqual(val, 0.0)
            self.assertLessEqual(val, 100.0)

    def test_firstclass(self):
        result = first_class_percentage_by_region(self.test_file)
        self.assertIn("South", result)
        self.assertIn("West", result)
        self.assertEqual(result["South"], 0.0)
        self.assertEqual(result["West"], 0.0)

    def test_firstclass_empty(self):
        empty_file = "empty_fc.csv"
        with open(empty_file, "w") as infile:
            infile.write("Ship Mode,Segment,Country,City,State,Postal Code,Region,Category,Sub-Category,Sales,Quantity,Discount,Profit\n")
        res = first_class_percentage_by_region(empty_file)
        os.remove(empty_file)
        self.assertEqual(res, {})

    def test_profit_returns_nested_dict(self):
        result = total_profit_region_category(self.test_file)
        self.assertIsInstance(result, dict)
        for region, inner in result.items():
            self.assertIsInstance(inner, dict)

    def test_profit_values_are_numeric(self):
        result = total_profit_region_category(self.test_file)
        for inner in result.values():
            for val in inner.values():
                self.assertIsInstance(val, (int, float))

    def test_profit_expected_totals_for_this_sample(self):
        result = total_profit_region_category(self.test_file)
        self.assertAlmostEqual(result["South"]["Furniture"], -121.5354)
        self.assertAlmostEqual(result["South"]["Office Supplies"], 2.5164)
        self.assertAlmostEqual(result["West"]["Office Supplies"], 8.8370)
        self.assertAlmostEqual(result["West"]["Furniture"], 14.1694)
        self.assertAlmostEqual(result["West"]["Technology"], 90.7152)

    def test_profit_empty_file_returns_empty_dict(self):
        empty_file = "empty_profit.csv"
        with open(empty_file, "w", newline="") as infile:
            infile.write("Ship Mode,Segment,Country,City,State,Postal Code,Region,Category,Sub-Category,Sales,Quantity,Discount,Profit\n")
        res = total_profit_region_category(empty_file)
        os.remove(empty_file)
        self.assertEqual(res, {})

if __name__ == "__main__":
    main()
    unittest.main()


