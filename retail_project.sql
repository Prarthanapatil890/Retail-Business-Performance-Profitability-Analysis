CREATE DATABASE retail_project;
USE retail_project;
CREATE TABLE superstore (
    Row_ID INT,
    Order_ID VARCHAR(255),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(255),
    Customer_ID VARCHAR(255),
    Customer_Name VARCHAR(255),
    Segment VARCHAR(255),
    Country VARCHAR(255),
    City VARCHAR(255),
    State VARCHAR(255),
    Postal_Code VARCHAR(20), 
    Region VARCHAR(255),
    Product_ID VARCHAR(255),
    Category VARCHAR(255),
    Sub_Category VARCHAR(255),
    Product_Name TEXT,
    Sales DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(3, 2),
    Profit DECIMAL(10, 2)
);