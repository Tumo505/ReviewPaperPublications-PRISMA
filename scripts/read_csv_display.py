#!/usr/bin/env python3
"""
CSV Reader and Display Script
Reads the CSV file and displays it in a well-formatted table structure
"""

import pandas as pd
import sys
import os

def read_and_display_csv(file_path):
    """
    Read the CSV file and display it in a formatted way
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found!")
            return
        
        # Read the CSV file
        print("Reading CSV file...")
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # Display basic information about the dataset
        print(f"\n{'='*80}")
        print(f"CSV FILE ANALYSIS: {os.path.basename(file_path)}")
        print(f"{'='*80}")
        
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")
        
        print(f"\nColumn names:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i:2d}. {col}")
        
        # Display data types
        print(f"\nData types:")
        for col, dtype in df.dtypes.items():
            print(f"  {col}: {dtype}")
        
        # Check for missing values
        print(f"\nMissing values per column:")
        missing_counts = df.isnull().sum()
        for col, count in missing_counts.items():
            if count > 0:
                print(f"  {col}: {count} missing values")
            else:
                print(f"  {col}: No missing values")
        
        # Display first few rows with proper formatting
        print(f"\n{'='*80}")
        print("FIRST 5 ROWS OF DATA:")
        print(f"{'='*80}")
        
        # Set pandas display options for better formatting
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 50)  # Limit column width for readability
        
        print(df.head().to_string(index=True))
        
        # Display sample of data with specific columns for better readability
        print(f"\n{'='*80}")
        print("SAMPLE DATA WITH KEY COLUMNS:")
        print(f"{'='*80}")
        
        # Select key columns for display
        key_columns = ['Title', 'Authors', 'Year', 'Journal_Conference', 'Inclusion_Exclusion_decision']
        if all(col in df.columns for col in key_columns):
            sample_df = df[key_columns].head(10)
            print(sample_df.to_string(index=True))
        
        # Display some statistics
        print(f"\n{'='*80}")
        print("BASIC STATISTICS:")
        print(f"{'='*80}")
        
        # Year distribution if Year column exists
        if 'Year' in df.columns:
            print(f"\nYear distribution:")
            year_counts = df['Year'].value_counts().sort_index()
            print(year_counts.head(10))
        
        # Inclusion/Exclusion distribution
        if 'Inclusion_Exclusion_decision' in df.columns:
            print(f"\nInclusion/Exclusion decision distribution:")
            decision_counts = df['Inclusion_Exclusion_decision'].value_counts()
            print(decision_counts)
        
        # Journal distribution (top 10)
        if 'Journal_Conference' in df.columns:
            print(f"\nTop 10 journals/conferences:")
            journal_counts = df['Journal_Conference'].value_counts().head(10)
            print(journal_counts)
        
        print("DATA EXPORT OPTIONS:")
        print(f"{'-'*80}")
        print("You can export this data to different formats:")
        print("1. Excel: df.to_excel('output.xlsx', index=False)")
        print("2. JSON: df.to_json('output.json', indent=2)")
        print("3. HTML: df.to_html('output.html', index=False)")
        print("4. Tab-separated: df.to_csv('output.tsv', sep='\\t', index=False)")
        
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        print("Common issues:")
        print("- File encoding problems (try different encodings)")
        print("- Malformed CSV structure")
        print("- Special characters in the data")

def main():
    # Default file path
    csv_file = r"c:\Users\tumok\OneDrive\Documents\process_files_project\Complete_Filtered_462_Publications_PRISMA (1).csv"
    
    # Check if a different file path was provided as command line argument
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    
    print("CSV Reader and Display Tool")
    print(f"Target file: {csv_file}")
    
    read_and_display_csv(csv_file)

if __name__ == "__main__":
    main()