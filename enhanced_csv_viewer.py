#!/usr/bin/env python3
"""
Enhanced CSV Reader and Display Tool
Provides multiple viewing options for the PRISMA publications CSV file
"""

import pandas as pd
import sys
import os
from textwrap import fill

def display_table_formatted(df, max_rows=10, max_col_width=50):
    """Display dataframe in a nicely formatted table"""
    # Create a copy for formatting
    display_df = df.copy()
    
    # Truncate long text in columns for better display
    for col in display_df.columns:
        if display_df[col].dtype == 'object':
            display_df[col] = display_df[col].astype(str).apply(
                lambda x: x[:max_col_width] + '...' if len(str(x)) > max_col_width else str(x)
            )
    
    # Set pandas options for clean display
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', max_col_width)
    pd.set_option('display.expand_frame_repr', False)
    
    print(display_df.head(max_rows).to_string(index=True))

def display_publication_details(df, indices=None):
    """Display detailed view of specific publications"""
    if indices is None:
        indices = range(min(5, len(df)))
    
    for i, idx in enumerate(indices):
        if idx >= len(df):
            continue
            
        row = df.iloc[idx]
        print(f"\n{'='*80}")
        print(f"PUBLICATION #{idx + 1}")
        print(f"{'='*80}")
        
        print(f"Title: {fill(str(row['Title']), width=75, subsequent_indent='       ')}")
        print(f"Authors: {fill(str(row['Authors']), width=75, subsequent_indent='         ')}")
        print(f"Year: {row['Year']}")
        print(f"Journal: {fill(str(row['Journal_Conference']), width=75, subsequent_indent='         ')}")
        print(f"DOI/URL: {row['DOI_URL']}")
        print(f"Source: {row['Database_source']}")
        print(f"Decision: {row['Inclusion_Exclusion_decision']}")
        print(f"Reason: {fill(str(row['Reason_for_inclusion_exclusion']), width=75, subsequent_indent='        ')}")
        print(f"Abstract: {fill(str(row['Abstract']), width=75, subsequent_indent='          ')}")
        print(f"Source ID: {row['Internal_Source_ID']}")

def create_summary_report(df):
    """Create a comprehensive summary report"""
    print(f"\n{'='*80}")
    print("COMPREHENSIVE SUMMARY REPORT")
    print(f"{'='*80}")
    
    # Basic statistics
    print(f"\nDATASET OVERVIEW:")
    print(f"• Total publications: {len(df)}")
    print(f"• Included publications: {len(df[df['Inclusion_Exclusion_decision'] == 'Include'])}")
    print(f"• Excluded publications: {len(df[df['Inclusion_Exclusion_decision'] == 'Exclude'])}")
    print(f"• Inclusion rate: {len(df[df['Inclusion_Exclusion_decision'] == 'Include']) / len(df) * 100:.1f}%")
    
    # Year analysis
    print(f"\nTEMPORAL DISTRIBUTION:")
    year_stats = df['Year'].describe()
    print(f"• Year range: {int(year_stats['min'])} - {int(year_stats['max'])}")
    print(f"• Average year: {year_stats['mean']:.1f}")
    print(f"• Most recent 5 years: {len(df[df['Year'] >= 2020])} publications")
    
    # Source distribution
    print(f"\nDATABASE SOURCES:")
    source_counts = df['Database_source'].value_counts()
    for source, count in source_counts.items():
        print(f"• {source}: {count} publications")
    
    # Top journals
    print(f"\nTOP 10 PUBLICATION VENUES:")
    journal_counts = df['Journal_Conference'].value_counts().head(10)
    for i, (journal, count) in enumerate(journal_counts.items(), 1):
        print(f"{i:2d}. {journal}: {count} publications")
    
    # Inclusion reasons analysis
    print(f"\nINCLUSION REASONS (TOP 10):")
    included_df = df[df['Inclusion_Exclusion_decision'] == 'Include']
    reason_counts = included_df['Reason_for_inclusion_exclusion'].value_counts().head(10)
    for i, (reason, count) in enumerate(reason_counts.items(), 1):
        short_reason = reason[:60] + '...' if len(reason) > 60 else reason
        print(f"{i:2d}. {short_reason}: {count} publications")
    
    # Exclusion reasons analysis
    print(f"\nEXCLUSION REASONS:")
    excluded_df = df[df['Inclusion_Exclusion_decision'] == 'Exclude']
    if len(excluded_df) > 0:
        exclusion_reasons = excluded_df['Reason_for_inclusion_exclusion'].value_counts()
        for reason, count in exclusion_reasons.items():
            short_reason = reason[:60] + '...' if len(reason) > 60 else reason
            print(f"• {short_reason}: {count} publications")

def filter_and_display(df):
    """Interactive filtering options"""
    print(f"\n{'='*80}")
    print("FILTERING OPTIONS")
    print(f"{'='*80}")
    
    # Filter by inclusion status
    included = df[df['Inclusion_Exclusion_decision'] == 'Include']
    excluded = df[df['Inclusion_Exclusion_decision'] == 'Exclude']
    
    print(f"\nINCLUDED PUBLICATIONS ({len(included)}):")
    display_table_formatted(included[['Title', 'Authors', 'Year', 'Journal_Conference']], max_rows=10)
    
    print(f"\n\nEXCLUDED PUBLICATIONS ({len(excluded)}):")
    display_table_formatted(excluded[['Title', 'Authors', 'Year', 'Reason_for_inclusion_exclusion']], max_rows=10)
    
    # Filter by recent years
    recent = df[df['Year'] >= 2020]
    print(f"\n\nRECENT PUBLICATIONS (2020-2025) - {len(recent)} publications:")
    display_table_formatted(recent[['Title', 'Authors', 'Year', 'Journal_Conference']], max_rows=8)

def export_clean_csv(df, output_file='cleaned_publications.csv'):
    """Export a cleaned version of the CSV"""
    try:
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\n✓ Cleaned CSV exported to: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Error exporting CSV: {e}")
        return False

def main():
    csv_file = r"c:\Users\tumok\OneDrive\Documents\process_files_project\Complete_Filtered_462_Publications_PRISMA (1).csv"
    
    print("Enhanced CSV Reader and Display Tool")
    print("PRISMA Publications Analysis")
    print(f"{'='*80}")
    
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file, encoding='utf-8')
        
        # Display menu options
        while True:
            print(f"\n{'='*50}")
            print("SELECT VIEWING OPTION:")
            print(f"{'='*50}")
            print("1. Quick Overview (default)")
            print("2. Detailed Publication View")
            print("3. Comprehensive Summary Report")
            print("4. Filtered Views")
            print("5. Export Clean CSV")
            print("6. Custom Table View")
            print("0. Exit")
            
            choice = input("\nEnter your choice (1-6, 0 to exit): ").strip()
            
            if choice == '' or choice == '1':
                print(f"\n{'='*80}")
                print("QUICK OVERVIEW")
                print(f"{'='*80}")
                display_table_formatted(df, max_rows=15)
                
            elif choice == '2':
                print(f"\n{'='*80}")
                print("DETAILED PUBLICATION VIEW")
                print(f"{'='*80}")
                try:
                    num_pubs = int(input("How many publications to display in detail (default 3)? ") or "3")
                    display_publication_details(df, range(num_pubs))
                except ValueError:
                    display_publication_details(df, range(3))
                    
            elif choice == '3':
                create_summary_report(df)
                
            elif choice == '4':
                filter_and_display(df)
                
            elif choice == '5':
                output_name = input("Enter output filename (default: cleaned_publications.csv): ").strip()
                if not output_name:
                    output_name = 'cleaned_publications.csv'
                export_clean_csv(df, output_name)
                
            elif choice == '6':
                print("\nAvailable columns:")
                for i, col in enumerate(df.columns, 1):
                    print(f"{i}. {col}")
                
                col_input = input("\nEnter column numbers to display (comma-separated, e.g., 1,2,3): ").strip()
                try:
                    col_indices = [int(x.strip()) - 1 for x in col_input.split(',')]
                    selected_cols = [df.columns[i] for i in col_indices if 0 <= i < len(df.columns)]
                    if selected_cols:
                        print(f"\nCustom view with columns: {', '.join(selected_cols)}")
                        display_table_formatted(df[selected_cols], max_rows=20)
                    else:
                        print("Invalid column selection.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter valid column numbers.")
                    
            elif choice == '0':
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please select 1-6 or 0.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()