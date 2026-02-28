import pandas as pd
import matplotlib.pyplot as plt

# 1. Use Pandas to create/load data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [2500, 3200, 2800, 4100, 3900]
}
df = pd.DataFrame(data)

# 2. Use Pandas to perform a quick calculation
average_sales = df['Sales'].mean()
print(f"Average Sales: {average_sales}")

# 3. Use Matplotlib to visualize the Pandas DataFrame
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='skyblue', linewidth=2)

# Adding details with Matplotlib
plt.title('Monthly Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.7)

# Show the final result
plt.show()
