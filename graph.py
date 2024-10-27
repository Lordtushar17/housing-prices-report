# graph.py
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def create_graph():
    # Step 1: Load Data from the Database
    connection = mysql.connector.connect(
        host='localhost',        
        user='root',    
        password='win19Ftu7', 
        database='housing_db'
    )

    query = "SELECT city, AVG(price) AS average_price FROM housing_prices GROUP BY city"
    df = pd.read_sql(query, connection)
    
    average_prices_per_city = df.groupby('city')['average_price'].mean().reset_index()

    # Close the database connection
    connection.close()

    """# Step 2: Create a Bar Chart Using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(df['city'], df['average_price'], color='skyblue')
    plt.xlabel('City')
    plt.ylabel('Average Price ($)')
    plt.title('Average Housing Prices by City')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image file
    chart_file_path = "average_prices_by_city.png"
    plt.savefig(chart_file_path)
    plt.close()  # Close the plot"""
    
    # Create a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(average_prices_per_city['city'], average_prices_per_city['average_price'], marker='o', linestyle='-.', color='b')

    # Adding titles and labels
    plt.title('Average Housing Prices per City', fontsize=14)
    plt.xlabel('City', fontsize=12)
    plt.ylabel('Average Price ($)', fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid()

    # Save the plot as a PNG image
    plt.tight_layout()  # Adjust layout to fit labels
    plt.savefig('housing_prices_line_chart.png')  # Change this to your desired filename
    plt.close()
    
    return  "housing_prices_line_chart.png" # Return the file path of the saved image
