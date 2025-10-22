# STAT301 Project: AirBnB Data Analysis

A comprehensive statistical analysis of AirBnB listings data for STAT301 course project.

## Project Overview

This project performs exploratory data analysis on AirBnB listings to understand:
- Price distributions and patterns
- Room type characteristics
- Geographic trends across neighbourhoods
- Factors affecting listing popularity
- Statistical relationships between variables

## Project Structure

```
STAT301_Project/
├── data/                    # Data files
│   ├── sample_data.csv     # Sample AirBnB dataset
│   └── README.md           # Data documentation
├── scripts/                # Analysis scripts
│   ├── analyze_airbnb.R    # R analysis script
│   ├── analyze_airbnb.py   # Python analysis script
│   └── README.md           # Scripts documentation
├── figures/                # Generated visualizations
│   └── README.md           # Figures documentation
├── reports/                # Analysis reports
│   ├── airbnb_analysis_report.Rmd  # R Markdown report
│   └── README.md           # Reports documentation
└── README.md               # This file
```

## Getting Started

### Prerequisites

**For R analysis:**
```r
install.packages(c("tidyverse", "ggplot2", "knitr", "kableExtra", "rmarkdown"))
```

**For Python analysis:**
```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Running the Analysis

**Option 1: Using R**
```r
# Run the analysis script
source("scripts/analyze_airbnb.R")

# Or generate the full report
library(rmarkdown)
rmarkdown::render("reports/airbnb_analysis_report.Rmd")
```

**Option 2: Using Python**
```bash
# Run the analysis script
python scripts/analyze_airbnb.py
```

## Data

The project uses AirBnB listings data containing:
- Property details (location, type, size)
- Pricing information
- Availability and booking data
- Review scores and ratings
- Host information

Sample data is provided in `data/sample_data.csv`. For full datasets, visit [Inside AirBnB](http://insideairbnb.com/get-the-data.html).

## Analysis Components

### 1. Exploratory Data Analysis
- Summary statistics
- Data distribution analysis
- Missing value assessment

### 2. Visualizations
- Price distribution histograms
- Box plots by room type
- Geographic distribution maps
- Correlation scatter plots

### 3. Statistical Tests
- ANOVA for price differences by room type
- Correlation analysis between variables
- Hypothesis testing

### 4. Reporting
- Comprehensive R Markdown report
- Automated figure generation
- Statistical test results

## Results

Generated outputs include:
- **Figures**: Saved in `figures/` directory
  - `price_distribution.png`
  - `price_by_room_type.png`
  - `reviews_vs_price.png`
  - `neighbourhood_distribution.png`

- **Reports**: Generated in `reports/` directory
  - HTML report with full analysis
  - Embedded visualizations
  - Statistical test results

## Key Findings

(To be updated after running the analysis)

- Price patterns across different room types
- Most popular neighbourhoods
- Relationship between reviews and pricing
- Statistical significance of observed differences

## Contributors

STAT301 Project Team

## License

This project is for educational purposes as part of STAT301 coursework.

## Acknowledgments

- Data provided by Inside AirBnB
- Analysis conducted using R and Python
- Course: STAT301
