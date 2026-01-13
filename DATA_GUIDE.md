# 📊 DATA MANAGEMENT GUIDE

## How to Manage WhatsApp Group Data

---

## 📝 CSV File Structure

Your `data.csv` must have exactly these 5 columns in this order:

```
Course,Semester,Subject,WhatsApp_Link,Status
```

### Column Rules:

1. **Course**: 
   - Course name (e.g., B.Com, B.A, B.Sc, BBA, BCA)
   - Keep it short and consistent
   - Use exact same spelling every time

2. **Semester**: 
   - Numbers only: 1, 2, 3, 4, 5, 6
   - No text like "First" or "1st"

3. **Subject**: 
   - Full subject name
   - Be specific: "Financial Accounting" not "Accounting"
   - Use proper capitalization

4. **WhatsApp_Link**: 
   - Full WhatsApp group invite link
   - Format: `https://chat.whatsapp.com/XXXXXXXXXXXXX`
   - Must start with `https://`

5. **Status**: 
   - Only two values: `Active` or `Inactive`
   - Exactly as written (capital A or I)
   - Only Active groups show in app

---

## ✅ CORRECT Examples

```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Financial Accounting,https://chat.whatsapp.com/ABC123XYZ,Active
B.Com,1,Business Mathematics,https://chat.whatsapp.com/DEF456UVW,Active
B.Com,2,Cost Accounting,https://chat.whatsapp.com/GHI789RST,Active
B.A,1,English Literature,https://chat.whatsapp.com/JKL012MNO,Active
B.Sc,1,Physics,https://chat.whatsapp.com/PQR345STU,Inactive
```

---

## ❌ INCORRECT Examples (Don't Do This!)

### Wrong: Extra spaces
```csv
Course, Semester, Subject, WhatsApp_Link, Status
B.Com , 1 , Financial Accounting , https://... , Active
```
**Issue**: Spaces after commas cause errors

### Wrong: Incomplete link
```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Financial Accounting,chat.whatsapp.com/ABC123,Active
```
**Issue**: Missing `https://`

### Wrong: Wrong status capitalization
```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Financial Accounting,https://chat.whatsapp.com/ABC123,active
```
**Issue**: Should be `Active` not `active`

### Wrong: Text in semester
```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,First,Financial Accounting,https://chat.whatsapp.com/ABC123,Active
```
**Issue**: Should be `1` not `First`

---

## 🔄 Common Operations

### 1. Adding a New Group

Add a new row at the end:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
...existing groups...
B.Com,3,Marketing Management,https://chat.whatsapp.com/NEW123,Active
```

### 2. Deactivating an Old Group

Change Status from Active to Inactive:

**Before:**
```csv
B.Com,1,Old Subject,https://chat.whatsapp.com/OLD123,Active
```

**After:**
```csv
B.Com,1,Old Subject,https://chat.whatsapp.com/OLD123,Inactive
```

### 3. Updating a WhatsApp Link

Replace the old link with new one:

**Before:**
```csv
B.Com,1,Financial Accounting,https://chat.whatsapp.com/OLD456,Active
```

**After:**
```csv
B.Com,1,Financial Accounting,https://chat.whatsapp.com/NEW789,Active
```

### 4. Deleting a Group Permanently

Simply delete the entire row from CSV

### 5. Adding a New Course

Just add rows with the new course name:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
BBA,1,Principles of Management,https://chat.whatsapp.com/BBA001,Active
BBA,1,Business Communication,https://chat.whatsapp.com/BBA002,Active
```

The app will automatically show BBA in the Course dropdown!

---

## 📋 Template for New Semester

Copy-paste this template and fill in your data:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Subject Name 1,https://chat.whatsapp.com/LINK1,Active
B.Com,1,Subject Name 2,https://chat.whatsapp.com/LINK2,Active
B.Com,1,Subject Name 3,https://chat.whatsapp.com/LINK3,Active
B.Com,1,Subject Name 4,https://chat.whatsapp.com/LINK4,Active
B.Com,2,Subject Name 1,https://chat.whatsapp.com/LINK5,Active
B.Com,2,Subject Name 2,https://chat.whatsapp.com/LINK6,Active
```

---

## 🎯 Best Practices

### 1. Consistent Naming

✅ **Good**: Always use "B.Com" (don't mix with "BCom", "B Com", "Bcom")

❌ **Bad**: Using different variations for same course

### 2. Descriptive Subject Names

✅ **Good**: "Financial Accounting - Part I"

❌ **Bad**: "FA1" (too abbreviated)

### 3. Test Links Before Adding

1. Copy WhatsApp link
2. Paste in browser
3. Verify it opens correct group
4. Then add to CSV

### 4. Keep Backup

Always keep a backup copy of `data.csv` before making major changes.

### 5. Use Comments (Optional)

You can add comments for your reference:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
# Semester 1 Groups - Last Updated: Jan 2026
B.Com,1,Financial Accounting,https://chat.whatsapp.com/ABC,Active
```

**Note**: Comments start with `#` and are ignored by the app

---

## 🔍 How to Get WhatsApp Group Links

### Method 1: From Group Admin

1. Ask CR or group admin
2. They go to group settings
3. Click "Invite via link"
4. Copy the link

### Method 2: If You're in the Group

1. Open WhatsApp group
2. Tap group name (top)
3. Scroll to "Invite via link"
4. Tap and copy link

### Format Check:
Valid link looks like:
```
https://chat.whatsapp.com/ABCdef123456789XYZ
```

---

## 📊 Sample Data for Testing

Use this sample data to test your app:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Financial Accounting,https://chat.whatsapp.com/test1,Active
B.Com,1,Business Organization,https://chat.whatsapp.com/test2,Active
B.Com,1,Business Mathematics,https://chat.whatsapp.com/test3,Active
B.Com,1,Microeconomics,https://chat.whatsapp.com/test4,Active
B.Com,2,Corporate Accounting,https://chat.whatsapp.com/test5,Active
B.Com,2,Business Statistics,https://chat.whatsapp.com/test6,Active
B.Com,2,Macroeconomics,https://chat.whatsapp.com/test7,Active
B.Com,3,Cost Accounting,https://chat.whatsapp.com/test8,Active
B.Com,3,Company Law,https://chat.whatsapp.com/test9,Active
B.A,1,English Literature,https://chat.whatsapp.com/test10,Active
B.A,1,Political Science,https://chat.whatsapp.com/test11,Active
B.A,1,History,https://chat.whatsapp.com/test12,Active
B.A,2,Sociology,https://chat.whatsapp.com/test13,Active
B.Sc,1,Mathematics,https://chat.whatsapp.com/test14,Active
B.Sc,1,Physics,https://chat.whatsapp.com/test15,Active
B.Sc,1,Chemistry,https://chat.whatsapp.com/test16,Active
```

**Note**: These are test links. Replace with real WhatsApp group links before going live!

---

## 🛠️ Editing Tools

### Option 1: Excel (Windows/Mac)

1. Open `data.csv` in Excel
2. Edit as needed
3. File → Save As → CSV (Comma delimited) (*.csv)
4. **Important**: Choose UTF-8 encoding if available

### Option 2: Google Sheets (Recommended)

1. Open Google Sheets
2. File → Import → Upload `data.csv`
3. Edit the data
4. File → Download → Comma Separated Values (.csv)

### Option 3: Text Editor (Advanced)

Use Notepad++, VS Code, or any text editor:
- Ensure UTF-8 encoding
- Watch out for extra spaces
- Use "Find and Replace" for bulk updates

### Option 4: GitHub Web Interface (Easiest for updates)

1. Click on `data.csv` in GitHub
2. Click pencil icon (✏️)
3. Edit directly
4. Commit changes
5. App auto-updates!

---

## 🔐 Data Privacy

### Safe to Include:

✅ Course names  
✅ Semester numbers  
✅ Subject names  
✅ WhatsApp invite links (public by nature)  

### Don't Include:

❌ Student names  
❌ Phone numbers  
❌ Email addresses  
❌ Private/personal information  

---

## 📈 Scaling Your Data

### Small College (< 20 groups)

- Use CSV file directly
- Manual updates via GitHub

### Medium College (20-100 groups)

- Consider Google Sheets integration
- Set up multiple editors

### Large College (100+ groups)

- Consider upgrading to database (PostgreSQL)
- Add admin panel for easier management
- Implement search functionality

---

## 🚨 Emergency Procedures

### If You Accidentally Break the CSV:

1. Go to GitHub repository
2. Click on `data.csv`
3. Click "History"
4. Find the last working version
5. Click "..." → "View file"
6. Copy the content
7. Edit current `data.csv` and paste the old content

### If App Stops Working:

1. Check Streamlit Cloud dashboard for errors
2. Verify CSV format (use CSV validator online)
3. Test locally: `streamlit run app.py`
4. Check GitHub Actions/Deployments tab

---

## ✅ Monthly Maintenance Checklist

**Beginning of Semester:**
- [ ] Review and update all WhatsApp links
- [ ] Mark old semester groups as Inactive
- [ ] Add new semester groups
- [ ] Test all links
- [ ] Announce to students

**Mid-Semester:**
- [ ] Check for broken/expired links
- [ ] Add any new groups created
- [ ] Remove duplicate entries

**End of Semester:**
- [ ] Archive old groups (set to Inactive)
- [ ] Backup the CSV file
- [ ] Prepare for next semester

---

## 📞 Need Help?

Common questions:

**Q: Can I have multiple groups for same subject?**  
A: Yes! Just add different rows. Students will see the first match.

**Q: Can I add groups for multiple colleges?**  
A: Yes! Add a "College" column and modify the app.

**Q: Can I password-protect editing?**  
A: Use GitHub branch protection or add authentication to app.

**Q: How do I add images/documents?**  
A: CSV only supports text. For documents, share Google Drive links in subject name.

---

**Last Updated**: January 2026  
**Version**: 1.0
