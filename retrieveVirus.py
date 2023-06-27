import sqlite3
import csv 

def query(n):
    query = f"""SELECT td.organism, td.pref_name, td.target_type FROM target_dictionary td WHERE td.organism like '%{n}%' ORDER by td.organism"""
    # Made query and received assay id, execute query
    cursor.execute(query)
    r = cursor.fetchall()

    return r
def genCSV(results):
    output_file = "output.csv"
    # Generate and fill up CSV file with recently pulled data
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Canonical Smiles', 'Activity ID', 'Assay ID', 'Standard Relation',
                        'Standard Value', 'Standard Units', 'Standard Type', 'Molregno'])
        writer.writerows(results)
def printResults(results):
    # Print the results in command prompt
    for row in results:
        canonical_smiles, activity_id, assay_id, standard_relation, \
        standard_value, standard_units, standard_type, molregno = row
        
        print("Canonical Smiles:", canonical_smiles)
        print("Activity ID:", activity_id)
        print("Assay ID:", assay_id)
        print("Standard Relation:", standard_relation)
        print("Standard Value:", standard_value)
        print("Standard Units:", standard_units)
        print("Standard Type:", standard_type)
        print("Molregno:", molregno)

if __name__ == '__main__':
    conn = sqlite3.connect("chembl_33.db")
    cursor = conn.cursor()
    input = input("Please enter the virus name: ")
    if input.isnumeric():
        print("Please enter a string")
    else:
        res = query(input)
        print(res)
        #genCSV(res)
        #printResults(res)
    cursor.close()
    conn.close()