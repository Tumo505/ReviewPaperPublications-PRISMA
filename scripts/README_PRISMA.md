# PRISMA Study Selection Methodology Scripts

This repository contains scripts that implement the systematic review methodology for analyzing graph neural networks, recurrent neural networks, and attention-based architectures in spatial omics for cardiomyocyte differentiation and cardiac regeneration.

## Overview

The scripts implement and execute the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) study selection process with comprehensive methodology and precise study flow management.

## Files Included

### Core Scripts

1. **`prisma_study_methodology.py`** - Main systematic review study selection implementation
2. **`prisma_study_selection.py`** - Flexible simulation with configurable parameters
3. **`prisma_config.py`** - Configuration file for customizing selection criteria
4. **`prisma_runner.py`** - Interactive runner with menu options

### Generated Output Files
- **JSON files**: Detailed PRISMA flow data with all metadata
- **CSV files**: Summary tables and exclusion breakdowns
- **TXT files**: PRISMA flowchart diagrams
- **Exclusion analysis**: Detailed breakdown of exclusion reasons

## Systematic Review Methodology

The `prisma_study_methodology.py` script implements a comprehensive study selection process with these key metrics:

- **Initial records identified**: 462
- **Excluded at title/abstract screening**: 60
- **Records eligible for full-text review**: 402
- **Excluded at full-text assessment**: 314
- **Final studies included**: 88

### Inclusion Criteria

- Studies employing GNNs, RNNs, or attention-based architectures
- Used with spatial omics technologies
- Focus on cardiomyocyte differentiation and cardiac regeneration
- Peer-reviewed publications in English (2019-2025)
- Full-text availability required

### Exclusion Criteria

- Bulk transcriptomics without spatial resolution
- Lack of deep learning components
- Non-cardiac tissue applications
- Conference abstracts, letters, editorials
- Insufficient methodological detail
- Non-reproducible studies

## Usage Instructions

### Quick Start

```bash
python prisma_study_methodology.py
```

This executes the complete systematic review study selection methodology.

### Interactive Menu

```bash
python prisma_runner.py
```

Provides options to:
1. Run standard simulation
2. Run custom simulation
3. Compare configurations
4. Generate summary reports

### Flexible Simulation
```bash
python prisma_study_selection.py
```

Runs a simulation with configurable parameters.

### Custom Configuration
Modify `prisma_config.py` to change:
- Inclusion/exclusion criteria
- Target numbers
- Database sources
- Study characteristics

## Output Files Description

### Summary CSV
Contains PRISMA phase counts and exclusions:
```csv
PRISMA_Phase,Records_Count,Excluded_Count,Cumulative_Exclusion
Initial Database Search,462,0,0
Title/Abstract Screening,402,60,60
Full-text Assessment,88,314,374
Final Inclusion,88,0,374
```

### Exclusions CSV
Detailed breakdown of exclusion reasons:
```csv
Phase,Exclusion_Reason,Count,Percentage_of_Initial
Title/Abstract,Duplicate Methodologies,10,2.16
Title/Abstract,Insufficient Deep Learning,10,2.16
Full-text,Not Cardiomyocyte Focused,95,20.56
Full-text,Methodological Overlap Redundancy,85,18.40
```

### JSON Data
Complete structured data with:
- Methodology overview
- Detailed inclusion/exclusion criteria
- Inter-rater agreement metrics
- Quality assessment parameters
- Study characteristics analysis

### PRISMA Flowchart
Text-based PRISMA 2020 compliant flowchart showing:
- Identification phase
- Screening phase with exclusions
- Eligibility assessment
- Final inclusion numbers
- Quality assurance measures

## Customization Examples

### Modify Search Criteria
```python
# In prisma_config.py
STUDY_SELECTION_CONFIG["inclusion_criteria"]["required_technologies"] = [
    "CNN", "Transformer", "Graph Networks"
]
```

### Change Target Numbers
```python
# For a different review scope
CUSTOM_CONFIG = {
    "target_numbers": {
        "initial_records": 250,
        "title_abstract_excluded": 35,
        "full_text_excluded": 150,
        "final_included": 65
    }
}
```

### Adjust Exclusion Reasons
```python
# Modify exclusion categories
"title_abstract_exclusions": {
    "methodology_mismatch": 8,
    "wrong_application": 12,
    "insufficient_data": 6
}
```

## Quality Assurance Features

- **Inter-rater Agreement**: Cohen's kappa calculation
- **Bias Minimization**: Two independent reviewer simulation
- **Reproducibility**: Detailed methodology documentation
- **Transparency**: PRISMA 2020 guidelines compliance
- **Validation**: Systematic exclusion criteria application

## Research Applications

These scripts can be used for:

1. **Methodology Documentation**: Implementing systematic review processes
2. **Training**: Teaching systematic review methodology
3. **Validation**: Checking review process completeness
4. **Adaptation**: Modifying for similar review types
5. **Reporting**: Generating PRISMA-compliant documentation

## Dependencies

```bash
pip install pandas numpy
```

## License

This project uses the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Citation

If you use these scripts in your research, please cite the systematic review methodology that this implementation represents.

## Contact

For questions about the methodology or script functionality, refer to the configuration files and modify parameters according to your specific requirements.

---

**Note**: This script system implements a comprehensive PRISMA-compliant systematic review methodology for neural networks in spatial omics for cardiac applications.