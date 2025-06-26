import pandas as pd
from sqlalchemy import create_engine
import pymysql

# --- Database Connection Details ---
# 🔁 Replace 'your_MySQL_password' with your actual MySQL password
db_connection_str = 'mysql+pymysql://root:your_MySQL_password@localhost:3306/retail_project'

try:
   
    db_connection = create_engine(db_connection_str)

   
    query = "SELECT * FROM superstore"
    df_superstore = pd.read_sql(query, db_connection)

    print("✅ Data loaded successfully!\n")

    
    print("🔍 First 5 rows:")
    print(df_superstore.head())

   
    print("\n📊 Correlation between Sales and Profit:")
    print(df_superstore[['Sales', 'Profit']].corr())

  
    df_superstore['Order_Date'] = pd.to_datetime(df_superstore['Order_Date'])
    df_superstore['Ship_Date'] = pd.to_datetime(df_superstore['Ship_Date'])

   
    df_superstore['Inventory_Days'] = (df_superstore['Ship_Date'] - df_superstore['Order_Date']).dt.days

 
    print("\n📦 Correlation between Inventory Days and Profit:")
    print(df_superstore[['Inventory_Days', 'Profit']].corr())

except Exception as e:
    print(f"❌ An error occurred: {e}")
finally:
    
    if 'db_connection' in locals() and db_connection:
        db_connection.dispose()
        print("\n🔒 Connection closed.")
