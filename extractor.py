from tabula import read_pdf
import pandas as pd

# Define the file path for the PDF
pdf_file = "Tennessee_Motorcycle_Crash_Statistics.pdf"

# Define pages containing tables of interest
pages_of_interest = {
    "speeding": 18,  # Replace with the actual page number for speeding
    "alcohol": 19    # Replace with the actual page number for alcohol use
}

# Dictionary to store extracted and cleaned tables
cleaned_tables = {}

# Function to clean data
def clean_data(df):
    # Drop unnecessary columns (e.g., "Unnamed" columns)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Drop rows with all NaN values
    df = df.dropna(how='all')

    # Rename columns (adjust based on table content)
    df.columns = ["Year", "Day of Week", "Sunday", "Monday", "Tuesday", 
                  "Wednesday", "Thursday", "Friday", "Saturday"]

    # Keep rows where "Year" has data
    df = df[df["Year"].notna()]

    return df

# Extract and clean tables for each topic
for topic, page in pages_of_interest.items():
    try:
        print(f"Extracting data for {topic} from page {page}...")
        tables = read_pdf(pdf_file, pages=page, multiple_tables=True, lattice=True)

        # Combine tables if needed
        combined_table = pd.concat(tables, ignore_index=True) if len(tables) > 1 else tables[0]
        
        # Preview the extracted table
        print(f"Raw data for {topic} (preview):")
        print(combined_table.head(), "\n")

        # Clean the extracted table
        cleaned_table = clean_data(combined_table)
        print(f"Cleaned data for {topic} (preview):")
        print(cleaned_table.head(), "\n")

        # Save the cleaned table to a CSV file
        csv_file = f"{topic}_cleaned.csv"
        cleaned_table.to_csv(csv_file, index=False)
        cleaned_tables[topic] = csv_file
        print(f"Cleaned {topic} data saved to {csv_file}\n")
    except Exception as e:
        print(f"Failed to process data for {topic}: {e}\n")

# Summary of saved files
print("Data extraction and cleaning completed. Cleaned files:")
for topic, file in cleaned_tables.items():
    print(f"{topic}: {file}")
