#!/usr/bin/env python3
"""
CSV Formatting Fix Script
Creates properly formatted CSV files with explicit column separation
"""

import pandas as pd
import csv
import os

def create_properly_formatted_csv():
    """Create a properly formatted CSV with explicit settings"""
    
    # Read the original CSV
    original_file = r"c:\Users\tumok\OneDrive\Documents\process_files_project\Complete_Filtered_462_Publications_PRISMA (1).csv"
    
    print("Reading original CSV file...")
    df = pd.read_csv(original_file, encoding='utf-8')
    
    print(f"Data shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Create multiple export formats to ensure compatibility
    
    # 1. Standard CSV with explicit settings
    output_file_1 = "properly_formatted_publications.csv"
    print(f"\nCreating {output_file_1}...")
    df.to_csv(
        output_file_1, 
        index=False, 
        encoding='utf-8-sig',  # UTF-8 with BOM for Excel compatibility
        sep=',',
        quoting=csv.QUOTE_MINIMAL,
        escapechar=None,
        lineterminator='\n'
    )
    
    # 2. Tab-separated file for better column separation
    output_file_2 = "properly_formatted_publications.tsv"
    print(f"Creating {output_file_2}...")
    df.to_csv(
        output_file_2, 
        index=False, 
        encoding='utf-8-sig',
        sep='\t',
        quoting=csv.QUOTE_MINIMAL,
        lineterminator='\n'
    )
    
    # 3. Excel file for guaranteed proper columns
    output_file_3 = "properly_formatted_publications.xlsx"
    print(f"Creating {output_file_3}...")
    try:
        # Install openpyxl if needed
        df.to_excel(output_file_3, index=False, engine='openpyxl')
        print(f"✓ Excel file created successfully")
    except ImportError:
        print("⚠ Excel export requires openpyxl. Installing...")
        import subprocess
        subprocess.check_call([
            "C:/Users/tumok/OneDrive/Documents/process_files_project/.venv/Scripts/python.exe", 
            "-m", "pip", "install", "openpyxl"
        ])
        df.to_excel(output_file_3, index=False, engine='openpyxl')
        print(f"✓ Excel file created successfully")
    
    # 4. Pipe-separated file (alternative separator)
    output_file_4 = "properly_formatted_publications_pipe.csv"
    print(f"Creating {output_file_4}...")
    df.to_csv(
        output_file_4, 
        index=False, 
        encoding='utf-8-sig',
        sep='|',
        quoting=csv.QUOTE_MINIMAL,
        lineterminator='\n'
    )
    
    # 5. Manual CSV creation with explicit quoting
    output_file_5 = "manually_formatted_publications.csv"
    print(f"Creating {output_file_5}...")
    
    with open(output_file_5, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Write header
        writer.writerow(df.columns.tolist())
        
        # Write data rows
        for index, row in df.iterrows():
            writer.writerow(row.tolist())
    
    # Display sample of each file to verify formatting
    print("\n" + "="*80)
    print("VERIFICATION - First 3 rows of each file:")
    print("="*80)
    
    files_to_check = [output_file_1, output_file_2, output_file_4, output_file_5]
    
    for file_name in files_to_check:
        print(f"\n--- {file_name} ---")
        try:
            if file_name.endswith('.tsv'):
                test_df = pd.read_csv(file_name, sep='\t', encoding='utf-8-sig')
            elif 'pipe' in file_name:
                test_df = pd.read_csv(file_name, sep='|', encoding='utf-8-sig')
            else:
                test_df = pd.read_csv(file_name, encoding='utf-8-sig')
            
            print(f"Shape: {test_df.shape}")
            print(f"Columns: {len(test_df.columns)}")
            print("Sample data:")
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_colwidth', 30)
            print(test_df[['Title', 'Authors', 'Year']].head(2).to_string(index=False))
            
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
    
    # Create a summary report
    print("\n" + "="*80)
    print("EXPORT SUMMARY")
    print("="*80)
    print(f"Original file: {original_file}")
    print(f"Exported {len(df)} rows and {len(df.columns)} columns to:")
    print(f"  1. {output_file_1} (Standard CSV)")
    print(f"  2. {output_file_2} (Tab-separated)")
    print(f"  3. {output_file_3} (Excel format)")
    print(f"  4. {output_file_4} (Pipe-separated)")
    print(f"  5. {output_file_5} (Manually formatted CSV)")
    
    print("\nRecommended file to use:")
    print(f"  - For Excel: {output_file_3}")
    print(f"  - For text editors: {output_file_2} (tab-separated)")
    print(f"  - For general use: {output_file_1} (standard CSV)")
    
    return output_file_1

def display_csv_structure(filename):
    """Display the structure of a CSV file to verify formatting"""
    print(f"\n" + "="*80)
    print(f"DETAILED STRUCTURE ANALYSIS: {filename}")
    print("="*80)
    
    try:
        # Read with different methods to check consistency
        df = pd.read_csv(filename, encoding='utf-8-sig')
        
        print(f"File: {filename}")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")
        print(f"Column names: {list(df.columns)}")
        
        # Check for any data issues
        print(f"\nData quality check:")
        print(f"  - Missing values per column:")
        for col in df.columns:
            missing = df[col].isnull().sum()
            print(f"    {col}: {missing}")
        
        # Display first row in detail
        print(f"\nFirst row data:")
        first_row = df.iloc[0]
        for col in df.columns:
            value = str(first_row[col])
            if len(value) > 50:
                value = value[:50] + "..."
            print(f"  {col}: {value}")
        
        # Show raw CSV content (first few lines)
        print(f"\nRaw file content (first 3 lines):")
        with open(filename, 'r', encoding='utf-8-sig') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    break
                print(f"  Line {i+1}: {line.strip()[:100]}...")
        
    except Exception as e:
        print(f"Error analyzing {filename}: {e}")

def main():
    print("CSV Formatting Fix Tool")
    print("="*80)
    
    # Create properly formatted files
    main_output = create_properly_formatted_csv()
    
    # Analyze the main output file
    display_csv_structure(main_output)
    
    print(f"\n" + "="*80)
    print("FORMATTING FIX COMPLETE")
    print("="*80)
    print("\nIf you're still seeing issues with the CSV:")
    print("1. Try opening the .xlsx file instead")
    print("2. Use the tab-separated .tsv file")
    print("3. Check your CSV viewer settings (delimiter, encoding)")
    print("4. Try the pipe-separated version if commas in data cause issues")

if __name__ == "__main__":
    main()