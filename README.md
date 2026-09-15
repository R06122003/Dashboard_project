# Superstore Sales Analytics Dashboard

The project is live at: https://dashboardproject-srijit.streamlit.app/

This project is a multi-page interactive dashboard built with Streamlit, Pandas, and Plotly. It uses a Superstore-style sales dataset to practice core Data Analytics concepts such as data loading, filtering, aggregation, KPI creation, trend analysis, profit analysis, and dashboard storytelling.

The project is best described as a Data Analytics / Business Intelligence project. It focuses on exploring and presenting business data rather than building machine learning models.

## Project Objective

The goal of this project is to understand how raw business data can be converted into useful insights through an interactive dashboard.

The dashboard helps answer questions such as:

- How much total sales and profit were generated?
- Which categories and sub-categories perform best?
- How do sales change over time?
- Which regions are more or less profitable?
- How are orders distributed by shipping mode, segment, and category?

## Concepts Practiced

- Loading CSV data with Pandas
- Cleaning column names and parsing date columns
- Creating reusable data loading utilities
- Using Streamlit caching for faster dashboard refreshes
- Building interactive filters with Streamlit sidebar controls
- Grouping and aggregating data with Pandas
- Creating business KPIs such as sales, profit, orders, and margin
- Building bar charts, line charts, scatter plots, and pie charts with Plotly
- Organizing a Streamlit app into multiple pages
- Separating chart logic, utility logic, and page layout code
- Preparing a project for GitHub with documentation and dependency files

## Dashboard Pages

### Home

The landing page introduces the dashboard and provides navigation links to the main sections.

### Sales

The Sales page focuses on overall sales performance. It includes KPIs, category-level sales, monthly sales trends, and filtered raw data.

### Profit

The Profit page analyzes profitability by region, category, and segment. It also includes a sales vs. profit scatter plot to compare revenue and profitability.

### Orders

The Orders page focuses on order volume, shipping mode, sub-category performance, and detailed order-level records.

## Project Structure

```text
.
|-- app.py
|-- pages/
|   |-- 1_Sales.py
|   |-- 2_Profit.py
|   `-- 3_Orders.py
|-- data/
|   `-- superstore.csv
|-- charts/
|   |-- __init__.py
|   |-- bar.py
|   |-- line.py
|   |-- kpi.py
|   `-- theme.py
|-- utils/
|   |-- loader.py
|   `-- sidebar.py
|-- assets/
|   `-- style.css
|-- requirements.txt
|-- run.bat
|-- .gitignore
`-- README.md
```

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## Dataset

The app expects the dataset to be available at:

```text
data/superstore.csv
```

The dashboard uses columns such as:

- `Order ID`
- `Order Date`
- `Ship Date`
- `Ship Mode`
- `Segment`
- `Region`
- `Category`
- `Sub-Category`
- `Sales`
- `Profit`
- `Quantity`
- `Discount`

If you use another dataset, make sure it has the same column names or update the code accordingly.

## How to Run the Project

### Option 1: Quick Run on Windows

After downloading or cloning the project, open PowerShell or Command Prompt in the project folder and run:

```powershell
.\run.bat
```

This script will:

- Install the required Python packages from `requirements.txt`
- Start the Streamlit dashboard

After the app starts, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

### Option 2: Manual Setup

Use these steps if you want to set up the project manually or use a virtual environment.

#### 1. Clone the Repository

```powershell
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub details.

#### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

#### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

#### 4. Add the Dataset

Place the CSV file here:

```text
data/superstore.csv
```

#### 5. Run the App

```powershell
python -m streamlit run app.py
```

Streamlit will start a local server and show a URL similar to:

```text
http://localhost:8501
```

Open that URL in your browser.

## Useful Commands

Quick run on Windows:

```powershell
.\run.bat
```

Run the app manually:

```powershell
python -m streamlit run app.py
```

Stop the app:

```text
Ctrl + C
```

Check installed packages:

```powershell
pip list
```

Save updated dependencies:

```powershell
pip freeze > requirements.txt
```

## Learning Outcome

By completing this project, you get hands-on practice with a typical data analyst workflow:

1. Load business data
2. Clean and prepare fields
3. Create reusable analysis components
4. Build metrics and charts
5. Add filters for interactive exploration
6. Present insights through a dashboard
7. Document and publish the project on GitHub

## Notes

If the `streamlit` command is not recognized, use:

```powershell
python -m streamlit run app.py
```

Generated folders such as `__pycache__`, virtual environments, and temporary files should not be committed to GitHub. They are ignored through `.gitignore`.
