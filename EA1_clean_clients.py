import pandas as pd
fruits = {
    "Client": ["Apple Inc", "banana co", "Apple Inc"],
    "Invoices": [30, 21, 15]
}
df = pd.DataFrame(fruits)

# EA Magic: Clean + Summarize
df['Client'] = df['Client'].str.title().str.strip()  # Fixes "banana co" → "Banana Co"
summary = df.groupby('Client')['Invoices'].sum()     # Totals by client

print("Cleaned Data:")
print(df)
print("\nTotal Invoiced per Client:")
print(summary)
