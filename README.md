# PRODIGY_DS_04
# Twitter Sentiment Analysis

This project performs sentiment analysis on a Twitter dataset. It explores the distribution of sentiments across various tweets and also provides brand-specific sentiment analysis, such as for "Facebook."

## Project Overview

The project includes:
- **Data Loading and Preprocessing**: Loading the Twitter dataset, handling encoding issues, checking for missing values, and removing duplicates.
- **Sentiment Analysis**: Analyzing the sentiment distribution across all tweets and performing brand-specific sentiment analysis.
- **Visualizations**: Bar plots and pie charts for visualizing sentiment distributions.

## Dataset

The dataset used in this project is a Twitter dataset stored in `twitter_training.csv`. The dataset includes the following columns:
- `ID`: A unique identifier for each tweet.
- `Entity`: The entity (e.g., brand or person) mentioned in the tweet.
- `Sentiment`: The sentiment of the tweet (e.g., positive, negative, neutral, etc.).
- `Content`: The tweet content.

### Example Rows:

| ID  | Entity  | Sentiment | Content                                   |
| --- | ------- | --------- | ----------------------------------------- |
| 1   | Facebook| Positive  | I love using Facebook, it’s so user-friendly! |
| 2   | Google  | Negative  | Google’s new update is terrible.           |

## Requirements

Make sure you have the following Python libraries installed:

- `pandas`
- `matplotlib`

Install them using:

```bash
pip install pandas matplotlib
