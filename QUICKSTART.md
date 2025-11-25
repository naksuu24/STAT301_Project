# Quick Start Guide

Get started with the AirBnB data analysis in just a few steps!

## Prerequisites

Choose your preferred analysis environment:

### Option A: Python
```bash
pip install -r requirements.txt
```

### Option B: R
```r
install.packages(c("tidyverse", "ggplot2", "knitr", "kableExtra", "rmarkdown"))
```

---

## Running the Analysis

### Python (Recommended for Quick Results)

```bash
# Navigate to project directory
cd /path/to/STAT301_Project

# Run the analysis
python scripts/analyze_airbnb.py
```

**Output:**
- Console output with statistics and test results
- 4 PNG visualizations in `figures/` directory

### R

```r
# Set working directory
setwd("/path/to/STAT301_Project")

# Run the analysis
source("scripts/analyze_airbnb.R")
```

**Output:**
- Console output with statistics and test results
- 4 PNG visualizations in `figures/` directory

---

## Generating the Full Report

### R Markdown Report (Most Comprehensive)

```r
library(rmarkdown)
rmarkdown::render("reports/airbnb_analysis_report.Rmd")
```

This creates an HTML report with:
- Embedded code
- Interactive tables
- All visualizations
- Statistical test results
- Professional formatting

The report will be saved as `reports/airbnb_analysis_report.html`

### Markdown Summary (Quick Reference)

Simply open `reports/airbnb_analysis_summary.md` in any text editor or markdown viewer for a comprehensive summary of findings.

---

## What You'll Get

### Visualizations (in `figures/`)

1. **price_distribution.png**
   - Histogram showing price distribution
   - Helps identify pricing patterns and outliers

2. **price_by_room_type.png**
   - Box plots comparing prices by room type
   - Shows median, quartiles, and outliers

3. **reviews_vs_price.png**
   - Scatter plot with regression line
   - Examines relationship between reviews and pricing

4. **neighbourhood_distribution.png**
   - Bar chart of top neighbourhoods
   - Identifies most popular areas

### Statistical Results

- **Descriptive Statistics:** Mean, median, std dev, quartiles
- **ANOVA Test:** Price differences by room type
- **Correlation Analysis:** Reviews vs. price relationship
- **Distribution Analysis:** Price and review patterns

---

## Customizing the Analysis

### Using Your Own Data

1. **Format your data** to match the sample CSV structure:
   - Required columns: id, price, room_type, neighbourhood, number_of_reviews
   - Optional columns: all others

2. **Save your data** as `data/your_data.csv`

3. **Update the script** to use your data:
   
   **Python:**
   ```python
   df = load_data('data/your_data.csv')
   ```
   
   **R:**
   ```r
   airbnb_data <- read_csv("data/your_data.csv")
   ```

### Modifying Visualizations

Edit the scripts to customize:
- Colors and themes
- Figure dimensions
- Statistical tests
- Additional analyses

---

## Troubleshooting

### Python Issues

**Problem:** ModuleNotFoundError
```bash
# Solution: Install missing packages
pip install pandas numpy matplotlib seaborn scipy
```

**Problem:** File not found
```bash
# Solution: Ensure you're in the project directory
cd /path/to/STAT301_Project
python scripts/analyze_airbnb.py
```

### R Issues

**Problem:** Package not found
```r
# Solution: Install missing packages
install.packages("tidyverse")
```

**Problem:** Working directory error
```r
# Solution: Set working directory
setwd("/path/to/STAT301_Project")
```

---

## Example Output

When you run the Python script, you should see:

```
Loading AirBnB data from data/sample_data.csv...
Data loaded successfully! Shape: (20, 15)

=== Dataset Overview ===
Number of rows: 20
Number of columns: 15

=== Price Analysis ===
Average price: $104.25
Median price: $87.00
...

=== Statistical Tests ===
ANOVA Test: Price Differences by Room Type
F-statistic: 9.8092
P-value: 0.0058
Result: Significant difference in prices between room types

=== Analysis Complete ===
Figures saved to: figures/
```

---

## Next Steps

1. **Review the figures** in the `figures/` directory
2. **Read the summary report** at `reports/airbnb_analysis_summary.md`
3. **Generate the full HTML report** using R Markdown
4. **Customize the analysis** with your own data
5. **Extend the analysis** with additional statistical tests

---

## Getting Help

- Check the main README.md for detailed documentation
- Review comments in the analysis scripts
- Consult the reports README for report generation details
- Refer to the data README for dataset information

---

## Typical Workflow

```bash
# 1. Clone/download the project
git clone <repository-url>
cd STAT301_Project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python scripts/analyze_airbnb.py

# 4. View the results
ls figures/          # Check generated plots
cat reports/airbnb_analysis_summary.md  # Read the summary

# 5. (Optional) Generate full report
# Open R or RStudio
# rmarkdown::render("reports/airbnb_analysis_report.Rmd")
```

That's it! You're now ready to analyze AirBnB data! 🎉
