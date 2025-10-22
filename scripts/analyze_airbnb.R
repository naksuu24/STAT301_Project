# AirBnB Data Analysis Script
# STAT301 Project
# 
# This script performs exploratory data analysis on AirBnB listings data

# Load required libraries
library(tidyverse)
library(ggplot2)

# Set working directory to project root
setwd(dirname(dirname(rstudioapi::getActiveDocumentContext()$path)))

# Load data
cat("Loading AirBnB data...\n")
airbnb_data <- read_csv("data/sample_data.csv")

# Display basic information
cat("\n=== Dataset Overview ===\n")
cat("Number of rows:", nrow(airbnb_data), "\n")
cat("Number of columns:", ncol(airbnb_data), "\n")
cat("\nColumn names:\n")
print(colnames(airbnb_data))

cat("\n=== Data Structure ===\n")
str(airbnb_data)

cat("\n=== Summary Statistics ===\n")
summary(airbnb_data)

# Price Analysis
cat("\n=== Price Analysis ===\n")
cat("Average price: $", mean(airbnb_data$price, na.rm = TRUE), "\n")
cat("Median price: $", median(airbnb_data$price, na.rm = TRUE), "\n")
cat("Price range: $", min(airbnb_data$price, na.rm = TRUE), " - $", 
    max(airbnb_data$price, na.rm = TRUE), "\n")

# Room type distribution
cat("\n=== Room Type Distribution ===\n")
room_type_counts <- table(airbnb_data$room_type)
print(room_type_counts)

# Neighbourhood analysis
cat("\n=== Top 5 Neighbourhoods by Number of Listings ===\n")
neighbourhood_counts <- sort(table(airbnb_data$neighbourhood), decreasing = TRUE)
print(head(neighbourhood_counts, 5))

# Create visualizations

# 1. Price distribution
cat("\nGenerating price distribution plot...\n")
p1 <- ggplot(airbnb_data, aes(x = price)) +
  geom_histogram(bins = 30, fill = "steelblue", color = "black", alpha = 0.7) +
  labs(title = "Distribution of AirBnB Listing Prices",
       x = "Price ($)",
       y = "Count") +
  theme_minimal()

ggsave("figures/price_distribution.png", p1, width = 8, height = 6, dpi = 300)

# 2. Price by room type
cat("Generating price by room type plot...\n")
p2 <- ggplot(airbnb_data, aes(x = room_type, y = price, fill = room_type)) +
  geom_boxplot() +
  labs(title = "Price Distribution by Room Type",
       x = "Room Type",
       y = "Price ($)") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("figures/price_by_room_type.png", p2, width = 8, height = 6, dpi = 300)

# 3. Reviews vs Price
cat("Generating reviews vs price scatter plot...\n")
p3 <- ggplot(airbnb_data, aes(x = number_of_reviews, y = price)) +
  geom_point(alpha = 0.6, color = "steelblue") +
  geom_smooth(method = "lm", color = "red", se = TRUE) +
  labs(title = "Relationship between Number of Reviews and Price",
       x = "Number of Reviews",
       y = "Price ($)") +
  theme_minimal()

ggsave("figures/reviews_vs_price.png", p3, width = 8, height = 6, dpi = 300)

# 4. Neighbourhood distribution
cat("Generating neighbourhood distribution plot...\n")
p4 <- airbnb_data %>%
  count(neighbourhood) %>%
  top_n(10, n) %>%
  ggplot(aes(x = reorder(neighbourhood, n), y = n)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "Top 10 Neighbourhoods by Number of Listings",
       x = "Neighbourhood",
       y = "Number of Listings") +
  theme_minimal()

ggsave("figures/neighbourhood_distribution.png", p4, width = 8, height = 6, dpi = 300)

# Statistical tests

# Test: Is there a significant difference in prices between room types?
cat("\n=== Statistical Test: Price Differences by Room Type ===\n")
cat("ANOVA test for price differences by room type:\n")
anova_result <- aov(price ~ room_type, data = airbnb_data)
print(summary(anova_result))

# Correlation analysis
cat("\n=== Correlation Analysis ===\n")
cat("Correlation between price and number of reviews:\n")
cor_test <- cor.test(airbnb_data$price, airbnb_data$number_of_reviews)
print(cor_test)

cat("\n=== Analysis Complete ===\n")
cat("Figures saved to: figures/\n")
cat("Check the report in: reports/\n")
