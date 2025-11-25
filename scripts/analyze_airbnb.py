#!/usr/bin/env python3
"""
AirBnB Data Analysis Script
STAT301 Project

This script performs exploratory data analysis on AirBnB listings data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Set style for plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def load_data(filepath):
    """Load AirBnB data from CSV file"""
    print(f"Loading AirBnB data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Data loaded successfully! Shape: {df.shape}")
    return df

def basic_info(df):
    """Display basic information about the dataset"""
    print("\n=== Dataset Overview ===")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"\nColumn names:\n{df.columns.tolist()}")
    
    print("\n=== Data Types ===")
    print(df.dtypes)
    
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    
    print("\n=== Summary Statistics ===")
    print(df.describe())

def analyze_prices(df):
    """Analyze price distribution"""
    print("\n=== Price Analysis ===")
    print(f"Average price: ${df['price'].mean():.2f}")
    print(f"Median price: ${df['price'].median():.2f}")
    print(f"Price range: ${df['price'].min():.2f} - ${df['price'].max():.2f}")
    print(f"Standard deviation: ${df['price'].std():.2f}")

def analyze_room_types(df):
    """Analyze room type distribution"""
    print("\n=== Room Type Distribution ===")
    print(df['room_type'].value_counts())
    print("\n=== Average Price by Room Type ===")
    print(df.groupby('room_type')['price'].mean().sort_values(ascending=False))

def analyze_neighbourhoods(df):
    """Analyze neighbourhood distribution"""
    print("\n=== Top 10 Neighbourhoods by Number of Listings ===")
    print(df['neighbourhood'].value_counts().head(10))
    print("\n=== Average Price by Top 5 Neighbourhoods ===")
    top_neighbourhoods = df['neighbourhood'].value_counts().head(5).index
    print(df[df['neighbourhood'].isin(top_neighbourhoods)].groupby('neighbourhood')['price'].mean().sort_values(ascending=False))

def create_visualizations(df, output_dir='figures'):
    """Create and save visualizations"""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Price distribution
    print("\nGenerating price distribution plot...")
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=30, color='steelblue', alpha=0.7, edgecolor='black')
    plt.xlabel('Price ($)', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Distribution of AirBnB Listing Prices', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/price_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Price by room type
    print("Generating price by room type plot...")
    plt.figure(figsize=(10, 6))
    df.boxplot(column='price', by='room_type', patch_artist=True)
    plt.xlabel('Room Type', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.title('Price Distribution by Room Type', fontsize=14, fontweight='bold')
    plt.suptitle('')  # Remove default title
    plt.tight_layout()
    plt.savefig(f'{output_dir}/price_by_room_type.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Reviews vs Price
    print("Generating reviews vs price scatter plot...")
    plt.figure(figsize=(10, 6))
    plt.scatter(df['number_of_reviews'], df['price'], alpha=0.6, color='steelblue')
    
    # Add regression line
    z = np.polyfit(df['number_of_reviews'], df['price'], 1)
    p = np.poly1d(z)
    plt.plot(df['number_of_reviews'].sort_values(), 
             p(df['number_of_reviews'].sort_values()), 
             "r--", alpha=0.8, linewidth=2)
    
    plt.xlabel('Number of Reviews', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.title('Relationship between Number of Reviews and Price', fontsize=14, fontweight='bold')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/reviews_vs_price.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Neighbourhood distribution
    print("Generating neighbourhood distribution plot...")
    plt.figure(figsize=(10, 8))
    top_neighbourhoods = df['neighbourhood'].value_counts().head(10)
    plt.barh(range(len(top_neighbourhoods)), top_neighbourhoods.values, color='steelblue')
    plt.yticks(range(len(top_neighbourhoods)), top_neighbourhoods.index)
    plt.xlabel('Number of Listings', fontsize=12)
    plt.ylabel('Neighbourhood', fontsize=12)
    plt.title('Top 10 Neighbourhoods by Number of Listings', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/neighbourhood_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nAll figures saved to: {output_dir}/")

def statistical_tests(df):
    """Perform statistical tests"""
    print("\n=== Statistical Tests ===")
    
    # ANOVA test: Price differences by room type
    print("\n1. ANOVA Test: Price Differences by Room Type")
    room_types = df['room_type'].unique()
    groups = [df[df['room_type'] == rt]['price'].values for rt in room_types]
    f_stat, p_value = stats.f_oneway(*groups)
    print(f"F-statistic: {f_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Result: Significant difference in prices between room types (p < 0.05)")
    else:
        print("Result: No significant difference in prices between room types (p >= 0.05)")
    
    # Correlation test: Price vs Number of Reviews
    print("\n2. Correlation Test: Price vs Number of Reviews")
    corr_coef, p_value = stats.pearsonr(df['price'], df['number_of_reviews'])
    print(f"Correlation coefficient: {corr_coef:.4f}")
    print(f"P-value: {p_value:.4f}")
    if abs(corr_coef) < 0.3:
        strength = "weak"
    elif abs(corr_coef) < 0.7:
        strength = "moderate"
    else:
        strength = "strong"
    direction = "positive" if corr_coef > 0 else "negative"
    print(f"Result: {strength.capitalize()} {direction} correlation")

def main():
    """Main analysis function"""
    # Load data
    df = load_data('data/sample_data.csv')
    
    # Perform analyses
    basic_info(df)
    analyze_prices(df)
    analyze_room_types(df)
    analyze_neighbourhoods(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Statistical tests
    statistical_tests(df)
    
    print("\n=== Analysis Complete ===")
    print("Figures saved to: figures/")
    print("Check the report in: reports/")

if __name__ == "__main__":
    main()
