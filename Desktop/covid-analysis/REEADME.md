COVID-19 Conditions Contributing to Deaths - Data Visualization Project

Overview
This project explores the correlation between pre-existing conditions and their contribution to COVID-19 fatalities. The goal is to identify which conditions had the greatest impact on the severity of COVID-19 outcomes, specifically in terms of death rates. Using Python for data analysis and visualization, this project provides static and interactive plots to illustrate these relationships. The project is powered by data stored in an SQLite database and allows user interaction to generate different types of visualizations.

Features
i. Data Loading and Cleaning: Load raw data from publicly available datasets, clean the data, and filter relevant information.
ii. Database Integration: Store the cleaned dataset in an SQLite database, enabling fast querying for visualizations.
iii. Static and Interactive Visualizations: Generate both static (Matplotlib) and interactive (Plotly) plots to visualize the top 10 conditions contributing to COVID-19 deaths.
iv. User Interaction: The user can select from various types of visualizations via a command-line interface (CLI).
v. Modular Design: The project is structured with modular Python scripts for easier management and extensibility.


Running the Project
To run the project and interact with the data visualizations:

python covid_analysis.py

This will load the dataset, clean it, store it in the SQLite database, and give you options to generate static or interactive plots based on the cleaned data.

Data Source
The dataset used in this project comes from a public repository on Kaggle. The dataset provides information about pre-existing health conditions contributing to COVID-19 deaths.

Source: Kaggle - COVID-19 Conditions Contributing to Deaths
Description: The dataset contains information about pre-existing health conditions and their contributions to COVID-19-related deaths across different demographics in the United States. The data includes details such as the condition name, the number of deaths attributed to the condition, and demographic information about the affected individuals.
Dataset Fields
Condition: The name of the pre-existing condition contributing to the death.
Deaths: The total number of deaths where this condition was a contributing factor.
The data was filtered and cleaned to focus on the most relevant conditions contributing to COVID-19 fatalities.

Usage Instructions
After running the project, users will be prompted to select from two visualization options:

Static Bar Chart (using Matplotlib): Generates and saves a bar chart showing the top 10 pre-existing conditions contributing to COVID-19 deaths.
Interactive Bar Chart (using Plotly): Opens an interactive bar chart in the browser, allowing users to explore the data dynamically.
Follow the on-screen prompts to choose your preferred visualization.

Ethical Considerations
This project considers ethical data usage and ensures that personal information is not included in the analysis. All data is anonymized, and only aggregated statistics about conditions and deaths are analyzed. Additionally, the project acknowledges that correlations between conditions and deaths do not imply causation, and care is taken in interpreting the results.

Contacts:
Name: Ameera Ismail
Email: ameeraismail040@gmail.com