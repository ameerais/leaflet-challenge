

# Import necessary libraries and modules
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import sqlite3
from data_loader import load_data, clean_data
from database_manager import save_to_database, fetch_data_from_db
import os

# Create directories for outputs if not existing
output_dir = 'static/plots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a static bar chart using Matplotlib
def generate_static_plot(df):
    """Generate static bar chart and save it as an image."""
    plt.figure(figsize=(12, 7))
    grouped_data = df.groupby('Condition')['Deaths'].sum().sort_values(ascending=False).head(10)
    grouped_data.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Top 10 Conditions Contributing to COVID-19 Deaths', fontsize=16)
    plt.ylabel('Number of Deaths', fontsize=12)
    plt.xlabel('Pre-existing Condition', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot as a PNG file
    output_path = os.path.join(output_dir, 'condition_deaths_bar.png')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    return output_path

# Function to generate an interactive plot using Plotly
def generate_interactive_plot(df):
    """Generate interactive bar chart using Plotly and display it."""
    fig = px.bar(
        df.groupby('Condition')['Deaths'].sum().sort_values(ascending=False).reset_index(),
        x='Condition', y='Deaths',
        title='Conditions Contributing to COVID-19 Deaths',
        labels={'Condition': 'Pre-existing Condition', 'Deaths': 'Number of Deaths'},
        color='Deaths', color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        title_font_size=20,
        yaxis_title="Number of Deaths",
        xaxis_title="Pre-existing Conditions"
    )
    fig.show()

# Main function for user interaction
def main():
    print("COVID-19 Data Visualization")
    # Load and clean the dataset
    dataset_path = 'https://path_to_your_csv_file'
    raw_data = load_data(dataset_path)
    cleaned_data = clean_data(raw_data)

    # Store cleaned data in the SQLite database
    db_name = 'covid_conditions.db'
    save_to_database(cleaned_data, db_name)

    # Fetch data from the database
    db_data = fetch_data_from_db(db_name)
    
    # Provide user options for visualization
    print("\nChoose a visualization option:")
    print("1. Static Bar Chart (Matplotlib)")
    print("2. Interactive Bar Chart (Plotly)")
    user_choice = input("\nEnter your choice (1 or 2): ")

    if user_choice == '1':
        print("Generating static plot...")
        plot_path = generate_static_plot(db_data)
        print(f"Static plot saved at: {plot_path}")
    elif user_choice == '2':
        print("Generating interactive plot...")
        generate_interactive_plot(db_data)
    else:
        print("Invalid option. Exiting.")

if __name__ == "__main__":
    main()
