# Reports Directory

This directory contains analysis reports for the AirBnB data project.

## Files

- `airbnb_analysis_report.Rmd` - R Markdown report with embedded analysis code
- `airbnb_analysis_report.md` - Markdown summary report

## Generating Reports

### R Markdown Report

To generate the HTML report from the R Markdown file:

```r
# In R or RStudio
library(rmarkdown)
rmarkdown::render("reports/airbnb_analysis_report.Rmd")
```

This will create `airbnb_analysis_report.html` with all visualizations and analysis results.

### Requirements

For R Markdown reports:
- R packages: tidyverse, knitr, kableExtra, rmarkdown

For Python analysis:
- Python packages: pandas, numpy, matplotlib, seaborn, scipy

## Report Contents

The reports include:
1. Data loading and preparation
2. Exploratory data analysis
3. Visualizations
4. Statistical tests
5. Conclusions and recommendations
