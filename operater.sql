import pandas as pd

# Sample data representing Ramesh's customer records
data = {
    'Customer_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'City': ['New York', 'Los Angeles', 'New York', 'New York', 'Chicago'],
    'Grade': [120, 95, 85, 200, 150]
}

df = pd.DataFrame(data)

# Filter: City is 'New York' AND Grade is greater than 100
filtered_df = df[(df['City'] == 'New York') & (df['Grade'] > 100)]

print("Customers in New York with a grade > 100:")
print(filtered_df)
