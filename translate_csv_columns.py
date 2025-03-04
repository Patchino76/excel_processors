import pandas as pd
import os
from df_column_names import columns_dict, translate_column_names
from pathlib import Path

def main():
    """
    Demonstrates how to translate column names in an existing CSV file
    """
    # Find the CSV files in the directory
    parent_dir = Path(__file__).parent
    
    # Try to find processed CSV files
    files = list(parent_dir.glob("processed_dispatcher_data_*.csv"))
    
    if not files:
        print("No processed CSV files found!")
        return
    
    print(f"Found {len(files)} CSV files:")
    for file in files:
        print(f"  - {file.name}")
    
    # Process the first file found
    file_path = files[0]
    print(f"\nProcessing file: {file_path}")
    
    # Read the CSV file
    print("Reading the CSV file...")
    df = pd.read_csv(file_path)
    
    # Print original column names
    print("\nOriginal column names:")
    for col in df.columns:
        print(f"  - {col}")
    
    # Translate column names to English
    print("\nTranslating column names from Bulgarian to English...")
    df_en = translate_column_names(df, bg_to_en=True)
    
    # Print translated column names
    print("\nTranslated column names:")
    for col in df_en.columns:
        print(f"  - {col}")
    
    # Save the translated DataFrame to a new CSV file
    output_file = file_path.stem + "_en.csv"
    df_en.to_csv(output_file, index=False)
    print(f"\nSaved translated DataFrame to: {output_file}")
    
    # Example of how to translate back to Bulgarian
    print("\nTranslating column names back to Bulgarian...")
    df_bg = translate_column_names(df_en, bg_to_en=False)
    
    # Print Bulgarian column names
    print("\nBulgarian column names:")
    for col in df_bg.columns:
        print(f"  - {col}")

if __name__ == "__main__":
    main()
