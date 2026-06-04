import pandas as pd

emails = {
    'From': ['billing@apple.com', 'ceo@google.com', 'support@banana.co', 'ceo@google.com', 'legal@tesla.com'],
    'Subject': ['Invoice Overdue', 'Urgent: Board Deck', 'Question', 'Re: Board Deck', 'Urgent: Contract'],
    'Date': ['2026-09-10', '2026-09-11', '2026-09-09', '2026-09-11', '2026-06-04']
}
df = pd.DataFrame(emails)

# Step 1: Extract client name
df['Client'] = df['From'].str.split('@').str[1].str.split('.').str[0].str.title()

# Step 2: Flag urgent with lambda
urgent_words = ['urgent', 'overdue', 'asap', 'board', 'contract']
df['Priority'] = df['Subject'].str.lower().apply(
    lambda x: 'HIGH' if any(word in x for word in urgent_words) else 'Normal'
)

# Step 3: THE FIX - Convert HIGH/Normal to 1/0 so sorting works
df['Priority_Score'] = df['Priority'].map({'HIGH': 1, 'Normal': 0})

# Step 4: Sort by score first, then date. Both descending = HIGH + newest on top
df = df.sort_values(by=['Priority_Score', 'Date'], ascending=[False, False])

# Step 5: Summary for founder
summary = df.groupby('Client')['Priority'].apply(lambda x: (x=='HIGH').sum())
summary.name = 'High Priority Emails'

print("=== INBOX TRIAGE REPORT ===")
print(df[['Date', 'Client', 'Subject', 'Priority']])  # Hide Priority_Score from founder
print("\n=== HIGH PRIORITY COUNT BY CLIENT ===")
print(summary[summary > 0])
