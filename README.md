# EA Automation Scripts — Python for C-Suite Operations
Built by Paramita Dhar Chaudhury | Remote Systems EA | $22/hr EST
### 1. Revenue Merge — `EA3_revenue_merge.py`
**Problem:** Founder gets paid via Stripe, PayPal, Bank. Monthly totals take 45 mins in Excel. 
**Solution:** Merges 3 CSVs, groups by client, sums revenue. 10 seconds.
**Output:** `TOTAL SEPTEMBER 2026: $2450`

### 2. Inbox Triage — `EA4Final_inbox_sort.py` 
**Problem:** 100+ emails. Urgent client requests buried.
**Solution:** Lambda scans subjects for `urgent|overdue|board|contract`. Maps HIGH=1 for correct sorting.
**Output:** HIGH priority + newest emails first.

### 3. Calendar Conflict Detector — `EA5_calendar_conflicts.py`
**Problem:** Founder double-books investors. Looks unprofessional.
**Solution:** Converts times to datetime, uses `.shift()` to flag overlaps.
**Output:** `WARNING: 14:00 Investor Call overlaps 14:30 Client Demo`

### 4. Client Billing Dedupe — `EA1_clean_clients.py`
**Problem:** `Apple Inc` vs `apple inc` vs `Apple` = 3 invoices. Accounting mess.
**Solution:** Standardizes names, groups, sums. Prevents duplicate billing.

## Run Any Script
```bash
