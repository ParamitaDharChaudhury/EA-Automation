import pandas as pd

# EA Task: Find double-booked meetings before founder embarrasses themselves
meetings = {
    'Date': ['2026-09-15', '2026-09-15', '2026-09-15', '2026-09-16'],
    'Start': ['14:00', '14:30', '16:00', '10:00'],
    'End': ['15:00', '15:30', '17:00', '11:00'],
    'Title': ['Investor Call', 'Client Demo', 'Team Standup', 'Board Prep'],
    'Attendees': ['Sequoia', 'Apple Inc', 'Internal', 'Board']
}
df = pd.DataFrame(meetings)

# Step 1: Combine date + time for sorting
df['Start_DT'] = pd.to_datetime(df['Date'] + ' ' + df['Start'])
df['End_DT'] = pd.to_datetime(df['Date'] + ' ' + df['End'])

# Step 2: Sort by start time
df = df.sort_values('Start_DT')

# Step 3: Find overlaps - the money line
df['Conflict'] = df['Start_DT'] < df['End_DT'].shift(1)

# Step 4: Flag only real conflicts
conflicts = df[df['Conflict'] == True]

print("=== CALENDAR CONFLICT REPORT ===")
if conflicts.empty:
    print("No conflicts. Founder calendar is clean.")
else:
    print("WARNING: Double-booked meetings found:")
    print(conflicts[['Date', 'Start', 'End', 'Title', 'Attendees']])
    
print("\n=== FULL SCHEDULE ===")
print(df[['Date', 'Start', 'End', 'Title']])
