# 🧮 Citizen Participation Data Pipeline (2019)

This project is a complete data pipeline that processes and analyzes citizen participation statistics from a CSV file, stores them in a PostgreSQL database, and visualizes them in a Power BI dashboard.

## 📊 Project Overview

- 📥 Extract data from a CSV file (`recap_pai2019.csv`)
- 🔄 Clean and transform data using Python (Pandas & NumPy)
- 🧠 Calculate new metrics such as:
  - Percentage of men participation
  - Rank based on women's participation
  - Flag high youth participation (above 20%)
- 🛢️ Load the processed data into a **PostgreSQL** database
- 📈 Build interactive visualizations using **Power BI**

---

## 🛠️ Tech Stack

| Tool        | Purpose                            |
|-------------|------------------------------------|
| Python      | Data processing & transformation   |
| Pandas      | Data wrangling                     |
| SQLAlchemy  | Database connection                |
| PostgreSQL  | Data storage                       |
| Power BI    | Data visualization                 |

---

## 📁 Project Structure


datapipeline/ │ ├── script/ │ └── etl_participation.py # Python script for 
ETL ├── dashboard/ │ └── powerbi_dashboard.pbix # Power BI dashboard file ├── data/ │
 └── recap_pai2019.csv # Original data source ├── README.md # 
Project documentation └── requirements.txt # Python dependencies


---

## 🚀 How to Run It

### 1. Clone the repository
bash
git clone https://github.com/your-username/datapipeline.git
cd datapipeline

### 2. Set up a PostgreSQL database
Make sure PostgreSQL is running locally and a database called madw is created.

You can use this connection in the script (adjust as needed):
postgresql://postgres:trao@localhost/madw

### 3.install dependencies 
pip install -r requirements.txt

### 4. Run the Python script
python script/etl_participation.py
The script will:

Load the data

Clean and enrich it

Push it to the PostgreSQL table


📈 Power BI Dashboard
Open the .pbix file in the dashboard/ folder using Power BI Desktop.
Make sure your PostgreSQL is running so the visuals can refresh from the source.

🔍 Sample insights:
Top regions by % of women's participation

Areas with >20% youth involvement

Distribution of male participation

🧠 Future Improvements
Add data from multiple years (e.g., 2020, 2021)

Schedule ETL job with Airflow or cron

Deploy interactive dashboard using Power BI Service or Streamlit

📝 License
This project is licensed under the MIT License — see the LICENSE file for details.

