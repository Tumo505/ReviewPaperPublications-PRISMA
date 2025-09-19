"""
Configuration file for PRISMA Study Selection Simulation

This file contains all the configurable parameters for the systematic review
study selection process. Modify these values to match your specific review criteria.
"""

# Study Selection Criteria Configuration
STUDY_SELECTION_CONFIG = {
    
    # Inclusion Criteria
    "inclusion_criteria": {
        # Required technologies/methodologies
        "required_technologies": ["GNN", "RNN", "Attention", "Transformer"],
        
        # Required omics data types
        "omics_types": [
            "spatial_transcriptomics", 
            "spatial_epigenomics", 
            "spatial_multi_omics",
            "spatial_proteomics"
        ],
        
        # Application focus areas
        "application_focus": [
            "cardiomyocyte_differentiation", 
            "cardiac_regeneration",
            "cardiac_development",
            "heart_disease_modeling"
        ],
        
        # Publication requirements
        "publication_type": "peer_reviewed",
        "language": "English",
        "date_range": {
            "start_year": 2019,
            "end_year": 2025
        },
        "full_text_required": True,
        
        # Minimum sample size
        "min_sample_size": 10,
        
        # Required study components
        "spatial_resolution_required": True,
        "empirical_data_required": True,
        "methodology_detail_required": True
    },
    
    # Exclusion Criteria
    "exclusion_criteria": {
        "bulk_omics_only": True,
        "no_deep_learning_components": True,
        "non_cardiac_applications": True,
        "conference_abstracts": True,
        "letters_editorials": True,
        "insufficient_methodology": True,
        "theoretical_only": True,
        "duplicate_studies": True,
        "non_reproducible": True
    },
    
    # Target Numbers (based on your methodology)
    "target_numbers": {
        "initial_records": 462,
        "title_abstract_excluded": 60,
        "full_text_excluded": 314,
        "final_included": 88
    },
    
    # Title/Abstract Screening Exclusion Breakdown
    "title_abstract_exclusions": {
        "duplicate_methodologies": 10,
        "insufficient_deep_learning": 10,
        "preliminary_results": 8,
        "no_spatial_resolution": 7,
        "non_cardiac_focus": 6,
        "insufficient_methodology": 6,
        "small_sample_sizes": 4,
        "theoretical_only": 4,
        "language_barriers": 3,
        "publication_type_mismatch": 3
    },
    
    # Full-text Screening Exclusion Categories
    "full_text_exclusions": {
        "not_cardiomyocyte_focused": 85,
        "methodological_overlap": 75,
        "insufficient_reproducibility": 60,
        "bulk_transcriptomics_only": 45,
        "no_spatial_integration": 35,
        "inadequate_deep_learning": 14
    },
    
    # Database Sources
    "search_databases": [
        "PubMed",
        "Web of Science", 
        "Embase",
        "IEEE Xplore",
        "ACM Digital Library",
        "Scopus",
        "arXiv",
        "bioRxiv",
        "medRxiv"
    ],
    
    # Journal Categories (for simulation)
    "journal_categories": {
        "high_impact": [
            "Nature", "Science", "Cell", "Nature Biotechnology",
            "Nature Methods", "Nature Medicine"
        ],
        "bioinformatics": [
            "Bioinformatics", "Genome Biology", "BMC Bioinformatics",
            "Nature Computational Science", "PLOS Computational Biology"
        ],
        "cardiology": [
            "Circulation", "Circulation Research", "JACC",
            "European Heart Journal", "Cardiovascular Research"
        ],
        "ai_ml": [
            "Nature Machine Intelligence", "Machine Learning",
            "Journal of Machine Learning Research", "IEEE TPAMI"
        ],
        "general": [
            "PLOS ONE", "Nature Communications", "Scientific Reports",
            "Frontiers in Genetics", "BMC Genomics"
        ]
    },
    
    # Study Characteristics Distribution (for realistic simulation)
    "study_characteristics": {
        "technology_distribution": {
            "GNN": 0.35,
            "RNN": 0.25, 
            "Attention": 0.40,
            "Combined": 0.15
        },
        
        "omics_distribution": {
            "spatial_transcriptomics": 0.60,
            "spatial_multi_omics": 0.25,
            "spatial_epigenomics": 0.15
        },
        
        "application_distribution": {
            "cardiomyocyte_differentiation": 0.55,
            "cardiac_regeneration": 0.35,
            "both": 0.10
        },
        
        "sample_size_ranges": {
            "small": (10, 50),
            "medium": (51, 200),
            "large": (201, 1000)
        },
        
        "year_distribution": {
            2019: 0.08,
            2020: 0.12,
            2021: 0.15,
            2022: 0.20,
            2023: 0.22,
            2024: 0.18,
            2025: 0.05
        }
    },
    
    # Quality Assessment Criteria
    "quality_criteria": {
        "methodological_rigor": [
            "clear_methodology_description",
            "reproducible_code_availability", 
            "adequate_validation",
            "appropriate_controls"
        ],
        
        "data_quality": [
            "sufficient_sample_size",
            "appropriate_data_preprocessing",
            "quality_control_measures",
            "statistical_significance"
        ],
        
        "reporting_standards": [
            "follows_reporting_guidelines",
            "transparent_limitations",
            "ethical_considerations",
            "data_availability"
        ]
    },
    
    # Inter-rater Agreement Parameters
    "inter_rater_agreement": {
        "kappa_range": {
            "min": 0.75,
            "max": 0.95
        },
        "interpretation_thresholds": {
            "poor": 0.20,
            "fair": 0.40,
            "moderate": 0.60,
            "substantial": 0.80,
            "perfect": 1.00
        }
    },
    
    # Output Configuration
    "output_settings": {
        "export_formats": ["json", "csv", "excel"],
        "include_flowchart": True,
        "include_summary_stats": True,
        "timestamp_files": True,
        "detailed_logging": True
    }
}

# Validation Rules
VALIDATION_RULES = {
    "required_fields": [
        "inclusion_criteria",
        "exclusion_criteria", 
        "target_numbers",
        "search_databases"
    ],
    
    "numeric_constraints": {
        "min_initial_records": 100,
        "max_initial_records": 10000,
        "min_final_included": 10,
        "max_exclusion_ratio": 0.95
    },
    
    "date_constraints": {
        "earliest_year": 2000,
        "latest_year": 2030
    }
}

# Example Custom Configuration
CUSTOM_CONFIG_EXAMPLE = {
    "study_focus": "Neural Networks in Spatial Genomics for Cancer Research",
    
    "inclusion_criteria": {
        "required_technologies": ["CNN", "RNN", "Transformer", "Graph Networks"],
        "omics_types": ["spatial_transcriptomics", "spatial_proteomics"],
        "application_focus": ["cancer_diagnosis", "tumor_heterogeneity", "metastasis"],
        "date_range": {"start_year": 2020, "end_year": 2024}
    },
    
    "target_numbers": {
        "initial_records": 325,
        "title_abstract_excluded": 45,
        "full_text_excluded": 195,
        "final_included": 85
    }
}