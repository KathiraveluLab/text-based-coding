import csv
# Open the file in write mode
with open("output.csv", "w") as csv_file:
    # Create a writer object
    csv_writer = csv.writer(csv_file)
    # Write the data to the file
    csv_writer.writerow(["Name", "Age", "Country"])
    csv_writer.writerow(["John Doe", 30, "United States"])
    csv_writer.writerow(["Jane Doe", 28, "Canada"])