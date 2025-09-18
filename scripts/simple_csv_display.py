#!/usr/bin/env python3
"""
Simple CSV Display Script - Non-interactive version
Displays the CSV data in a clean, organized format
"""

import pandas as pd
import os
from textwrap import fill

def main():
    csv_file = r"c:\Users\tumok\OneDrive\Documents\process_files_project\Complete_Filtered_462_Publications_PRISMA (1).csv"
    
    print("PRISMA Publications CSV Display")
    print("="*80)
    
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file, encoding='utf-8')
        
        # Set pandas display options
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 120)
        pd.set_option('display.max_colwidth', 40)
        pd.set_option('display.expand_frame_repr', False)
        
        print(f"\nDataset Summary:")
        print(f"- Total publications: {len(df)}")
        print(f"- Columns: {len(df.columns)}")
        print(f"- Date range: {df['Year'].min()} - {df['Year'].max()}")
        
        # Display first 10 rows in a clean table format
        print(f"\n{'='*120}")
        print("FIRST 10 PUBLICATIONS (Table View)")
        print(f"{'='*120}")
        
        # Create a simplified view for table display
        display_df = df[['Title', 'Authors', 'Year', 'Journal_Conference', 'Inclusion_Exclusion_decision']].head(10).copy()
        
        # Truncate long text for table display
        display_df['Title'] = display_df['Title'].apply(lambda x: x[:40] + '...' if len(str(x)) > 40 else str(x))
        display_df['Authors'] = display_df['Authors'].apply(lambda x: x[:30] + '...' if len(str(x)) > 30 else str(x))
        display_df['Journal_Conference'] = display_df['Journal_Conference'].apply(lambda x: x[:25] + '...' if len(str(x)) > 25 else str(x))
        
        print(display_df.to_string(index=True))
        
        # Display detailed view of first 3 publications
        print(f"\n{'='*120}")
        print("DETAILED VIEW - FIRST 3 PUBLICATIONS")
        print(f"{'='*120}")
        
        for i in range(min(3, len(df))):
            row = df.iloc[i]
            print(f"\n--- PUBLICATION #{i+1} ---")
            print(f"Title: {row['Title']}")
            print(f"Authors: {row['Authors']}")
            print(f"Year: {row['Year']}")
            print(f"Journal: {row['Journal_Conference']}")
            print(f"Decision: {row['Inclusion_Exclusion_decision']}")
            print(f"Reason: {row['Reason_for_inclusion_exclusion']}")
            print(f"Abstract: {row['Abstract'][:200]}..." if len(str(row['Abstract'])) > 200 else f"Abstract: {row['Abstract']}")
            print("-" * 80)
        
        # Statistics
        print(f"\n{'='*120}")
        print("STATISTICS")
        print(f"{'='*120}")
        
        print(f"\nYear Distribution:")
        year_counts = df['Year'].value_counts().sort_index()
        for year, count in year_counts.items():
            print(f"  {year}: {count} publications")
        
        print(f"\nInclusion/Exclusion Status:")
        decision_counts = df['Inclusion_Exclusion_decision'].value_counts()
        for decision, count in decision_counts.items():
            print(f"  {decision}: {count} publications")
        
        print(f"\nTop 10 Journals/Conferences:")
        journal_counts = df['Journal_Conference'].value_counts().head(10)
        for i, (journal, count) in enumerate(journal_counts.items(), 1):
            short_journal = journal[:50] + '...' if len(journal) > 50 else journal
            print(f"  {i:2d}. {short_journal}: {count}")
        
        # Export clean version
        output_file = 'cleaned_publications_display.csv'
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\n✓ Clean CSV exported to: {output_file}")
        
        print(f"\n{'='*120}")
        print("CSV DISPLAY COMPLETE")
        print(f"{'='*120}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()