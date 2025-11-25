# AirBnB Data Analysis Summary

**STAT301 Project**  
**Date:** October 2025

---

## Executive Summary

This report presents an exploratory data analysis of AirBnB listings data. The analysis examines pricing patterns, room type distributions, geographic trends, and factors affecting listing popularity.

### Key Findings

- Average listing price: **$104.25** (Median: $87.00)
- Most common room type: **Private rooms** (65% of listings)
- Price range: **$40 - $225**
- Significant price differences exist between room types (p < 0.05)
- Weak negative correlation between reviews and price (r = -0.19)

---

## 1. Introduction

### Background

AirBnB is a popular platform for short-term rental accommodations. Understanding the factors that influence listing prices and popularity is important for both hosts and guests.

### Research Questions

1. What is the distribution of listing prices?
2. How do prices vary by room type?
3. Which neighbourhoods have the most listings?
4. Is there a relationship between number of reviews and price?
5. Are there significant price differences between room types?

### Dataset

The dataset contains **20 AirBnB listings** with the following key variables:
- Property details (location, type, size)
- Pricing information
- Availability and booking data
- Review scores and ratings

---

## 2. Data Overview

### Dataset Characteristics

- **Total Listings:** 20
- **Variables:** 15
- **Missing Values:** Minimal (last_review and reviews_per_month have 1 missing value each)

### Variables Included

| Variable | Type | Description |
|----------|------|-------------|
| id | Integer | Unique listing identifier |
| name | Text | Listing name |
| neighbourhood | Text | Location neighbourhood |
| room_type | Categorical | Type of accommodation |
| price | Integer | Nightly price ($) |
| number_of_reviews | Integer | Total reviews |
| availability_365 | Integer | Days available per year |

---

## 3. Exploratory Data Analysis

### 3.1 Price Analysis

**Summary Statistics:**

| Statistic | Value |
|-----------|-------|
| Mean | $104.25 |
| Median | $87.00 |
| Minimum | $40.00 |
| Maximum | $225.00 |
| Std Dev | $49.66 |
| 25th Percentile | $67.50 |
| 75th Percentile | $136.25 |

**Key Insights:**
- The median price ($87) is lower than the mean ($104.25), suggesting a right-skewed distribution
- Price variability is moderate with a standard deviation of ~$50
- 50% of listings are priced between $67.50 and $136.25

See visualization: `figures/price_distribution.png`

### 3.2 Room Type Analysis

**Distribution:**

| Room Type | Count | Percentage | Avg Price |
|-----------|-------|------------|-----------|
| Private room | 13 | 65% | $83.15 |
| Entire home/apt | 7 | 35% | $143.43 |

**Key Insights:**
- Private rooms are the most common listing type
- Entire homes/apartments command significantly higher prices (~72% more expensive)
- Clear market segmentation between room types

See visualization: `figures/price_by_room_type.png`

### 3.3 Geographic Analysis

**Top 5 Neighbourhoods:**

| Neighbourhood | Listings | Avg Price |
|---------------|----------|-----------|
| Williamsburg | 4 | $78.75 |
| East Harlem | 2 | $82.50 |
| Upper West Side | 2 | $107.00 |
| Harlem | 2 | $119.50 |
| Midtown | 1 | $225.00 |

**Key Insights:**
- Williamsburg has the highest concentration of listings
- Midtown has the highest average price
- Manhattan neighbourhoods generally command higher prices

See visualization: `figures/neighbourhood_distribution.png`

### 3.4 Reviews Analysis

**Correlation: Reviews vs. Price**
- Correlation coefficient: **-0.19**
- Interpretation: Weak negative correlation
- Statistical significance: Not significant (p = 0.42)

**Key Insights:**
- Number of reviews has minimal relationship with price
- Higher-priced listings don't necessarily receive more reviews
- Other factors likely influence review frequency

See visualization: `figures/reviews_vs_price.png`

---

## 4. Statistical Analysis

### 4.1 ANOVA: Price Differences by Room Type

**Hypotheses:**
- H₀: Mean prices are equal across all room types
- H₁: At least one room type has a different mean price

**Results:**
- F-statistic: **9.81**
- P-value: **0.0058**

**Conclusion:** 
✓ Reject the null hypothesis (p < 0.05)  
✓ There are **significant differences** in prices between room types  
✓ The data provides strong evidence that room type affects pricing

### 4.2 Correlation Analysis

**Price vs. Number of Reviews:**
- Pearson correlation: **-0.19**
- P-value: **0.42**

**Conclusion:**
✗ No significant correlation (p > 0.05)  
✗ Number of reviews does not predict price in this dataset  
✗ The weak negative trend may be due to chance

---

## 5. Conclusions

### Summary of Findings

1. **Pricing Structure:**
   - Average nightly rate is $104.25
   - Prices range from $40 to $225
   - Right-skewed distribution indicates some high-priced outliers

2. **Room Types:**
   - Private rooms dominate the market (65%)
   - Entire homes/apartments cost 72% more on average
   - Room type significantly affects pricing (ANOVA, p < 0.01)

3. **Geographic Trends:**
   - Williamsburg has the most listings
   - Manhattan areas command premium prices
   - Neighbourhood diversity in listing concentration

4. **Review Patterns:**
   - No significant relationship between reviews and price
   - Review count varies independently of pricing
   - Popularity may be driven by factors other than price

### Limitations

- **Sample Size:** Only 20 listings analyzed
- **Time Period:** Single snapshot in time, no temporal trends
- **Missing Variables:** Amenities, host characteristics, and guest ratings not included
- **Geographic Scope:** Limited to specific neighbourhoods

### Recommendations

**For Hosts:**
- Price according to room type and neighbourhood benchmarks
- Focus on factors beyond pricing to drive reviews
- Consider offering entire homes/apartments for higher revenue potential

**For Future Analysis:**
- Expand dataset size for more robust conclusions
- Include seasonal pricing variations
- Analyze impact of amenities on pricing
- Investigate host characteristics and success metrics

---

## 6. Visualizations

All visualizations are saved in the `figures/` directory:

1. **price_distribution.png** - Histogram of listing prices
2. **price_by_room_type.png** - Box plots comparing prices by room type
3. **reviews_vs_price.png** - Scatter plot with regression line
4. **neighbourhood_distribution.png** - Bar chart of top neighbourhoods

---

## 7. Methodology

### Tools Used
- **Python 3.x** with pandas, numpy, matplotlib, seaborn, scipy
- **R** with tidyverse, ggplot2
- **Statistical Tests:** ANOVA, Pearson correlation

### Data Processing
1. Data loading and validation
2. Missing value assessment
3. Summary statistics computation
4. Visualization generation
5. Statistical hypothesis testing

### Reproducibility

All analysis code is available in the `scripts/` directory:
- `analyze_airbnb.py` - Python implementation
- `analyze_airbnb.R` - R implementation

To reproduce the analysis:
```bash
# Python
pip install -r requirements.txt
python scripts/analyze_airbnb.py

# R
Rscript scripts/analyze_airbnb.R
```

---

## References

- **Data Source:** Inside AirBnB (http://insideairbnb.com/)
- **Course:** STAT301 - Statistical Methods
- **Tools:** Python, R, pandas, tidyverse

---

*Report generated for STAT301 Project - AirBnB Data Analysis*
