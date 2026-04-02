import pandas as pd

def clean_netflix_data(file_path):
    # 1. Load the dataset
    df = pd.read_csv(file_path)
    
    print("Initial Data Shape:", df.shape)

    # 2. Inspecting Missing Values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # 3. Handling 'director', 'cast', and 'country'
    # Decision: Replacing with 'Unknown' rather than dropping rows to preserve metadata.
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')

    # 4. Fixing 'rating' and 'duration'
    # Observation: Some 'duration' values are accidentally stored in the 'rating' column.
    # We move them to 'duration' and set rating to 'NR' (Not Rated).
    mask = df['duration'].isnull()
    df.loc[mask, 'duration'] = df.loc[mask, 'rating']
    df.loc[mask, 'rating'] = 'NR'
    
    # Fill remaining missing ratings with 'NR'
    df['rating'] = df['rating'].fillna('NR')

    # 5. Handling 'date_added'
    # Decision: Only 10 rows are missing dates. Since it's a small number, we drop them 
    # to ensure our datetime conversion is accurate.
    df.dropna(subset=['date_added'], inplace=True)

    # 6. Parse date columns into proper datetime objects
    # We strip whitespace and convert to datetime
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

    # 7. Fix mixed-type columns (duration)
    # Goal: Create a numeric column for analysis (e.g., 'duration_minutes')
    # We extract the number and leave the unit for Movies.
    df['duration_value'] = df['duration'].apply(lambda x: int(x.split(' ')[0]) if pd.notnull(x) else 0)
    df['duration_unit'] = df['duration'].apply(lambda x: x.split(' ')[1] if pd.notnull(x) else '')

    # 8. Final Inspection
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    
    # 9. Export the cleaned DataFrame
    output_file = 'netflix_titles_cleaned.csv'
    df.to_csv(output_file, index=False)
    print(f"\nCleaned dataset saved as: {output_file}")
    
    return df

# Execute the cleaning process
if __name__ == "__main__":
    cleaned_df = clean_netflix_data('netflix_titles.csv')
    print("\nCleaned Data Preview:")
    print(cleaned_df.head())