# Netflix Data Cleaning Project 🎬

This project focuses on cleaning and preprocessing the **Netflix Movies and TV Shows** dataset. Real-world data is often "messy"containing missing values, incorrect data types, and inconsistent formatting. The goal of this project is to transform raw data into a clean, structured format suitable for analysis. This project is from readmap.sh
https://roadmap.sh/projects/cleaning-netflix-dataset

## 📌 Project Overview
The dataset used in this project is sourced from Kaggle and contains a listing of all the movies and TV shows available on Netflix as of 2021. 

### Key Challenges Addressed:
* **Missing Values:** Strategically handling nulls in `director`, `cast`, `country`, and `rating`.
* **Data Misalignment:** Identifying and fixing rows where duration data (e.g., "74 min") was accidentally stored in the `rating` column.
* **Type Casting:** Converting strings into proper `datetime` objects for time-series analysis.
* **Feature Engineering:** Splitting mixed-type columns (like `duration`) into separate numeric values and units (Minutes/Seasons).

---

## 🛠️ Technologies Used
* **Pandas:** For high-performance data manipulation and cleaning.
* **VS Code:** Development environment.

---

## 📁 Dataset Dictionary
| Column | Description |
| :--- | :--- |
| `show_id` | Unique ID for every movie/show |
| `type` | Identifier - Movie or TV Show |
| `title` | Title of the content |
| `director` | Director of the movie/show |
| `cast` | Actors involved in the movie/show |
| `country` | Country of production |
| `date_added` | Date added to Netflix |
| `release_year` | Original release year |
| `rating` | TV Rating (PG, TV-MA, etc.) |
| `duration` | Total duration (in minutes or seasons) |
| `listed_in` | Genre/Category |

---

## Cleaning Methodology
1.  **Preservation over Deletion:** Instead of dropping rows with missing directors or cast members, we filled them with **"Unknown"** to maintain the integrity of other data points.
2.  **Automated Column Correction:** Developed a mask-based approach to detect duration values mistakenly entered into the rating column and moved them back to their correct position.
3.  **Standardization:**
    * Stripped whitespaces from string columns.
    * Parsed `date_added` into `YYYY-MM-DD` format.
    * Converted `duration` into a numeric format for potential statistical analysis.

## ✅ Results
The project generates a cleaned file: `netflix_titles_cleaned.csv`. This file is now ready for Exploratory Data Analysis (EDA) or for building recommendation systems without the risk of errors from null values or incorrect data types.
