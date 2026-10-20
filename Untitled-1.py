import pandas as pd
rtdf = pd.read_csv(
    r"D:\vijay\Data scientist\Projects\Messay data Sets\ecommerce_retail_transactions_raw.csv"
)
#print(rtdf)just to verify
#print(rtdf.shape)
#print(rtdf.isna)
#print(rtdf.isnull().sum()) #to see, which are the columns are faced nan values
#rtdf.dropna()
#print(rtdf.shape)verifying the after cleaning data
rtdf.drop(columns=["Customer_Rating"],inplace=True)
#print(rtdf.shape)
rtdf_cleaned=rtdf.dropna().copy()
#print(rtdf_cleaned.isnull().sum())
#comparision of orginal_data and cleaned_data
#print("Original dataset:", rtdf.shape)
#print("Cleaned dataset:", rtdf_cleaned.shape)
#print("Missing values:", rtdf_cleaned.isnull().sum().sum())
#print(rtdf_cleaned["Order_ID"].nunique())
#print(rtdf_cleaned.shape)

rtdf_cleaned["Order_Date"] = pd.to_datetime(
    rtdf_cleaned["Order_Date"], format="mixed", dayfirst=True, errors="coerce")

# ==============================
# EXPLORATORY DATA ANALYSIS (EDA)
# ==============================
#which product is more saled
#pris
#Which product category generates the highest revenue?
rtdf_cleaned["Revenue"] = (rtdf_cleaned["Quantity"]*rtdf_cleaned["Unit_Price_USD"])
#print(rtdf_cleaned[["Product_Category", "Quantity", "Unit_Price_USD", "Revenue"]].head())
#
category_revenue = rtdf_cleaned.groupby("Product_Category")["Revenue"].sum()
#print(category_revenue.sort_values(ascending=False))
rtdf_cleaned["net_revenue"]=rtdf_cleaned["Revenue"]*(1-rtdf_cleaned["Discount_Percent"]/100)
#print(rtdf_cleaned[["Product_Category", "Quantity", "Unit_Price_USD", "Discount_Percent","net_revenue"]].head())
category_net_revenue = rtdf_cleaned.groupby("Product_Category")["net_revenue"].sum()
#print(category_net_revenue.sort_values(ascending=False))

#Which product category has the highest number of orders?
category_revenue = rtdf_cleaned.groupby("Product_Category")["Order_ID"].count()
#print(category_revenue.sort_values(ascending=False))

#print(rtdf_cleaned["Order_ID"].nunique())
#print(rtdf_cleaned.shape[0])
#print(rtdf_cleaned["Customer_ID"].nunique())

#Which customers have placed the highest number of orders
category_revenue = rtdf_cleaned.groupby("Customer_ID")["Order_ID"].count().head()

#print(rtdf_cleaned["Order_Date"].dtype)
#print(rtdf_cleaned["Order_Date"].dt.month.head())
print(rtdf_cleaned["Order_Date"].dtype)

rtdf_cleaned["Order_Month"] = (
    rtdf_cleaned["Order_Date"].dt.to_period("M")
)

#print(rtdf_cleaned["Order_Month"].head())

#Calculate monthly net revenue
monthly_revenue = rtdf_cleaned.groupby("Order_Month")["net_revenue"].sum()

#print(monthly_revenue.sort_values(ascending=False))

rtdf_cleaned.to_csv(
    r"D:\vijay\Data scientist\Projects\Messay data Sets\ecommerce_retail_transactions_cleaned.csv",
    index=False
)