import sqlite3
import csv 

def query(n):
    query = f"""
    SELECT cs.canonical_smiles, act.activity_id, act.assay_id, act.standard_relation,
        act.standard_value, act.standard_units, act.standard_type, act.molregno
    FROM Activities AS act
    JOIN compound_structures AS cs ON act.molregno = cs.molregno
    WHERE act.assay_id = {n}
    LIMIT 1;
    """
    # Made query and received assay id, execute query
    cursor.execute(query)
    results = cursor.fetchall()

    return results
def genCSV():
    output_file = "output.csv"
    # Generate and fill up CSV file with recently pulled data
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Canonical Smiles', 'Activity ID', 'Assay ID', 'Standard Relation',
                        'Standard Value', 'Standard Units', 'Standard Type', 'Molregno'])
        writer.writerows(results)
def printResults():
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
    input = input("Please enter the assay id:")
    if not input.isnumeric():
        print("Please enter an integer")
    else:
        results = query(input)
        genCSV()
        printResults()
    cursor.close()
    conn.close()