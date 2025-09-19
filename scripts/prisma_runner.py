#!/usr/bin/env python3
"""
PRISMA Study Selection Runner Script

This script demonstrates how to run the PRISMA study selection simulation
with custom parameters and configuration.
"""

import sys
import os
from datetime import datetime

# Add the scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from prisma_study_selection import PRISMAStudySelection
from prisma_study_methodology import PRISMAStudySelection as PRISMAMethodology
from prisma_config import STUDY_SELECTION_CONFIG, CUSTOM_CONFIG_EXAMPLE

def run_methodology_implementation():
    """Run the complete PRISMA study selection methodology."""
    
    print("Running PRISMA Study Selection Methodology - Complete Implementation")
    print("=" * 75)
    
    # Initialize with methodology implementation
    prisma = PRISMAMethodology(random_seed=42)
    
    # Generate results
    results = prisma.generate_prisma_flow()
    
    # Export results
    filename = "prisma_methodology"
    
    json_file, csv_file, exclusion_file = prisma.export_study_selection_data(results)
    
    # Generate flowchart
    flowchart = prisma.generate_detailed_flowchart(results)
    
    # Save flowchart
    flowchart_file = f"{filename}_flowchart.txt"
    with open(flowchart_file, 'w', encoding='utf-8') as f:
        f.write(flowchart)
    
    print(f"\nMethodology implementation completed!")
    print(f"Files generated:")
    print(f"  - {json_file}")
    print(f"  - {csv_file}")
    print(f"  - {exclusion_file}")
    print(f"  - {flowchart_file}")
    
    return results

def run_custom_simulation():
    """Run the simulation with custom configuration."""
    
    print("\nRunning PRISMA Study Selection Simulation - Custom Configuration")
    print("=" * 70)
    
    # Create custom PRISMA instance
    prisma = PRISMAStudySelection(random_seed=123)
    
    # Override with custom parameters
    prisma.initial_records = CUSTOM_CONFIG_EXAMPLE["target_numbers"]["initial_records"]
    prisma.title_abstract_excluded = CUSTOM_CONFIG_EXAMPLE["target_numbers"]["title_abstract_excluded"]
    prisma.full_text_excluded = CUSTOM_CONFIG_EXAMPLE["target_numbers"]["full_text_excluded"]
    prisma.final_included = CUSTOM_CONFIG_EXAMPLE["target_numbers"]["final_included"]
    
    # Update inclusion criteria
    prisma.inclusion_criteria.update(CUSTOM_CONFIG_EXAMPLE["inclusion_criteria"])
    
    # Regenerate synthetic studies with new parameters
    prisma.studies_df = prisma._generate_synthetic_studies()
    
    # Generate results
    results = prisma.generate_prisma_flow_data()
    
    # Export results
    filename = "prisma_custom"
    
    json_file, csv_file = prisma.export_results(results, filename)
    
    # Generate flowchart
    flowchart = prisma.generate_prisma_flowchart_text(results)
    
    # Save flowchart
    flowchart_file = f"{filename}_flowchart.txt"
    with open(flowchart_file, 'w', encoding='utf-8') as f:
        f.write(flowchart)
    
    print(f"\nCustom simulation completed!")
    print(f"Files generated:")
    print(f"  - {json_file}")
    print(f"  - {csv_file}")
    print(f"  - {flowchart_file}")
    
    return results

def compare_configurations():
    """Compare results from different configurations."""
    
    print("\nRunning Configuration Comparison")
    print("=" * 70)
    
    # Run both implementations
    methodology_results = run_methodology_implementation()
    custom_results = run_custom_simulation()
    
    # Compare key metrics
    print("\nConfiguration Comparison:")
    print("-" * 40)
    
    method_final = methodology_results["inclusion"]["final_synthesis"]
    custom_final = custom_results["inclusion"]["final_synthesis"]
    
    print(f"Methodology Implementation - Final Studies: {method_final}")
    print(f"Custom Config - Final Studies: {custom_final}")
    print(f"Difference: {abs(method_final - custom_final)}")
    
    # Compare exclusion rates
    method_excluded = (
        methodology_results["screening"]["title_abstract_phase"]["records_excluded"] +
        methodology_results["eligibility"]["full_text_assessment"]["articles_excluded"]
    )
    
    custom_excluded = (
        custom_results["screening"]["title_abstract_screening"]["excluded"] +
        custom_results["eligibility"]["full_text_assessment"]["excluded"]
    )
    
    print(f"\nTotal Exclusions:")
    print(f"Methodology Implementation: {method_excluded}")
    print(f"Custom Config: {custom_excluded}")
    
    return methodology_results, custom_results

def generate_summary_report():
    """Generate a comprehensive summary report."""
    
    print("\nGenerating Summary Report")
    print("=" * 70)
    
    # Get configuration details
    config = STUDY_SELECTION_CONFIG
    
    # Create summary
    summary = f"""
PRISMA STUDY SELECTION SIMULATION SUMMARY REPORT
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

CONFIGURATION OVERVIEW:
-----------------------
Study Focus: Graph Neural Networks, RNNs, and Attention in Spatial Omics
Application: Cardiomyocyte Differentiation and Cardiac Regeneration
Date Range: {config['inclusion_criteria']['date_range']['start_year']}-{config['inclusion_criteria']['date_range']['end_year']}

TARGET NUMBERS:
--------------
Initial Records: {config['target_numbers']['initial_records']}
Title/Abstract Excluded: {config['target_numbers']['title_abstract_excluded']}
Full-text Excluded: {config['target_numbers']['full_text_excluded']}
Final Included: {config['target_numbers']['final_included']}

INCLUSION CRITERIA:
------------------
Technologies: {', '.join(config['inclusion_criteria']['required_technologies'])}
Omics Types: {', '.join(config['inclusion_criteria']['omics_types'])}
Applications: {', '.join(config['inclusion_criteria']['application_focus'])}
Language: {config['inclusion_criteria']['language']}
Publication Type: {config['inclusion_criteria']['publication_type']}

SEARCH DATABASES:
----------------
{chr(10).join([f"- {db}" for db in config['search_databases']])}

QUALITY ASSESSMENT:
------------------
Methodological Rigor: Required
Data Quality: Assessed
Reporting Standards: Evaluated
Inter-rater Agreement: Cohen's kappa calculated

OUTPUT FILES:
------------
The simulation generates the following files:
- JSON file with detailed PRISMA flow data
- CSV file with summary statistics
- Text file with PRISMA flowchart
- Configuration log for reproducibility

USAGE INSTRUCTIONS:
------------------
1. Run 'python prisma_runner.py' for interactive menu
2. Modify 'prisma_config.py' to customize parameters
3. Use 'prisma_study_selection.py' directly for programmatic access

For questions or modifications, refer to the configuration file
and adjust parameters according to your specific review requirements.
"""
    
    # Save summary report
    report_file = "prisma_summary_report.txt"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(summary)
    print(f"\nSummary report saved to: {report_file}")
    
    return report_file

def main():
    """Main function with interactive menu."""
    
    print("PRISMA Study Selection Simulation Tool")
    print("======================================")
    print()
    print("This tool reproduces the study selection methodology described in your paper:")
    print("- Systematic database searches")
    print("- Title/abstract screening with specific exclusion criteria") 
    print("- Full-text assessment and final inclusion")
    print("- Inter-rater agreement calculation")
    print("- PRISMA flow diagram generation")
    print()
    
    while True:
        print("\nSelect an option:")
        print("1. Run complete methodology implementation")
        print("2. Run custom simulation (modify parameters)")
        print("3. Compare configurations")
        print("4. Generate summary report")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            run_methodology_implementation()
        elif choice == "2":
            run_custom_simulation()
        elif choice == "3":
            compare_configurations()
        elif choice == "4":
            generate_summary_report()
        elif choice == "5":
            print("\nThank you for using the PRISMA simulation tool!")
            break
        else:
            print("\nInvalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()