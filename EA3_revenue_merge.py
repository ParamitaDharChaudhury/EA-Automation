import pandas as pd
#EA Task: Merge 3 payment sources + clean + monthly report Pretend these are CSVs from Stripe, PayPal, Bank Export
stripe = {'Date': ['2026-09-01', '2026-09-01', '2026-09-05'], 
          'Client': [' apple inc', 'GOOGLE LLC', 'apple inc'], 
          'Amount': [500, 1200, 300]}
paypal = {'Date': ['2026-09-02'], 'Client': ['banana co '], 'Amount': [250]}
bank = {'Date': ['2026-09-05'], 'Client': ['Apple Inc'], 'Amount': [200]}

#Step 1: Combine all sources
df = pd.concat([pd.DataFrame(stripe), pd.DataFrame(paypal), pd.DataFrame(bank)])

#Step 2: Clean client names - the money line
df['Client'] = df['Client'].str.strip().str.title()

#Step 3: Remove duplicates + Convert date
df['Date'] = pd.to_datetime(df['Date'])
df = df.drop_duplicates()

#Step 4: Monthly summary for founder
df['Month'] = df['Date'].dt.to_period('M')
monthly_report = df.groupby(['Month', 'Client'])['Amount'].sum()

print("=== MONTHLY REVENUE REPORT FOR FOUNDER ===")
print(monthly_report)
print("\n=== TOTAL SEPTEMBER 2026 ===")
print(f"${df['Amount'].sum()}")
