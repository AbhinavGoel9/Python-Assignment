import csv

# Function to filter products by price range and category
def filter_products(input_file, output_file, min_price, max_price, category_filter):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write header to output file
        writer.writeheader()

        for row in reader:
            price = float(row['price'])
            category = row['category']

            # Check if product matches the criteria
            if min_price <= price <= max_price and category == category_filter:
                writer.writerow(row)

# Example usage
filter_products(
    input_file='sample_input.csv',
    output_file='filtered_output.csv',
    min_price=10.0,
    max_price=50.0,
    category_filter='Electronics'
)
