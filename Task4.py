import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with specified encoding and column names
data_path = "D:/PSG_Academics/TASK/twitter_training.csv"
col_names = ['ID', 'Entity', 'Sentiment', 'Content']

try:
    df = pd.read_csv(data_path, encoding='utf-8', names=col_names)
except UnicodeDecodeError:
    df = pd.read_csv(data_path, encoding='latin1', names=col_names)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Check for and drop duplicates
print("Number of duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("After dropping duplicates, number of duplicate rows:", df.duplicated().sum())

# Sentiment Analysis
sentiment_counts = df['Sentiment'].value_counts()

# Plot Sentiment Distribution
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon', 'gold'])  # Customizing bar chart colors
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=0)
plt.show()

# Example: Sentiment Distribution for a specific brand like 'Facebook'
brand_name = 'Facebook'
brand_df = df[df['Entity'].str.contains(brand_name, case=False, na=False)]
brand_sentiment_counts = brand_df['Sentiment'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(brand_sentiment_counts, labels=brand_sentiment_counts.index, autopct='%1.1f%%',
        colors=['lightcoral', 'lightskyblue', 'lightgreen', 'gold'])  # Customizing pie chart colors
plt.title(f'Sentiment Distribution for {brand_name}')
plt.show()
