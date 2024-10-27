# main.py
import mysql.connector
import pandas as pd
from fpdf import FPDF
from graph import create_graph  # Import the create_graph function

def generate_pdf_report():
    # Generate the graph and get the image path
    chart_file_path = create_graph()

    # Load average prices from the database
    connection = mysql.connector.connect(
        host='localhost',        
        user='root',    
        password='win19Ftu7', 
        database='housing_db'
    )

    query = "SELECT city, AVG(price) AS average_price FROM housing_prices GROUP BY city"
    df = pd.read_sql(query, connection)

    # Close the database connection
    connection.close()

    # Step 3: Generate a PDF Report and Insert the Chart
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Housing Prices Report", ln=True, align='C')
    
    # Average Price
    average_price = df['average_price'].mean()
    
    # Calculate Average Price per City
    average_prices_per_city = df[['city', 'average_price']].sort_values(by='average_price', ascending=False)
    
    # Find the Most Popular City
    most_popular_city = average_prices_per_city.loc[average_prices_per_city['average_price'].idxmax()]
    
    # Insert Average Price of Housing
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Average Price of Housing: ${average_price:.2f}", ln=True)
    
    # Insert Average Price per City
    pdf.cell(200, 10, txt="Average Price per City:", ln=True)
    pdf.set_font("Courier", size=10)  # Change font for better readability
    for index, row in average_prices_per_city.iterrows():
        pdf.cell(200, 10, txt=f"{row['city']}: ${row['average_price']:.2f}", ln=True)
    
    # Insert Most Popular City
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Most Popular City: {most_popular_city['city']} (${most_popular_city['average_price']:.2f})", ln=True)
    
    # Add some space before the chart
    pdf.ln(10)  # Adjust the number as needed for spacing
    
    # Insert the chart image
    pdf.image(chart_file_path, x=10, y=None, w=190)  # 'y=None' places it after the last cell
    
    # Save the PDF file
    pdf_file_path = "housing_prices_report.pdf"
    pdf.output(pdf_file_path)
    
    print(f"Report generated: {pdf_file_path}")


# Run the report generation
if __name__ == "__main__":
    generate_pdf_report()
