# 🚀 DEPLOYMENT GUIDE - Streamlit Cloud

## Complete Step-by-Step Instructions for Non-Technical Users

---

## ⏱️ Time Required: 10-15 minutes

---

## 📋 Prerequisites

1. A GitHub account (free) - [Sign up here](https://github.com/signup)
2. All app files ready (you already have them)
3. Internet connection

---

## STEP 1: Create GitHub Account (if you don't have one)

1. Go to https://github.com/signup
2. Enter your email
3. Create a password
4. Choose a username (e.g., `sbsc-student-2026`)
5. Verify your account via email
6. Complete the setup

✅ **Done? Move to Step 2**

---

## STEP 2: Create a New Repository

1. Log in to GitHub
2. Click the **"+"** icon (top right corner)
3. Click **"New repository"**

### Repository Settings:

- **Repository name**: `sbsc-whatsapp-groups`
- **Description**: "WhatsApp group finder for SBSC students"
- **Visibility**: ✅ **Public** (must be public for free hosting)
- **Initialize**: ❌ Do NOT check "Add a README file"
- Click **"Create repository"**

📝 **Save your repository URL**: `https://github.com/YOUR_USERNAME/sbsc-whatsapp-groups`

✅ **Done? Move to Step 3**

---

## STEP 3: Upload Files to GitHub

You'll see an empty repository page. Choose **Option A** (easiest):

### Option A: Upload via Web Interface (Recommended)

1. Click **"uploading an existing file"** link on the empty repo page
2. Click **"choose your files"** button
3. Select all these files from your computer:
   - `app.py`
   - `data.csv`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`

4. **Important**: For `.streamlit/config.toml`:
   - Click **"Create new file"**
   - Name it: `.streamlit/config.toml` (include the folder path)
   - Copy-paste the config content
   - Click **"Commit new file"**

5. Scroll down, enter commit message: "Initial commit"
6. Click **"Commit changes"**

### Option B: Using Git Command Line (Advanced Users)

```bash
# Navigate to your app folder
cd /path/to/sbsc-whatsapp-app

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/sbsc-whatsapp-groups.git

# Push to GitHub
git branch -M main
git push -u origin main
```

✅ **Done? Your files should now be visible on GitHub. Move to Step 4**

---

## STEP 4: Deploy on Streamlit Cloud

### 4.1: Go to Streamlit Cloud

1. Open https://share.streamlit.io
2. Click **"Sign up"** (top right)
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit Cloud to access your GitHub

### 4.2: Deploy Your App

1. Click **"New app"** button (big button in the center or top right)

2. Fill in the deployment form:
   - **Repository**: Select `YOUR_USERNAME/sbsc-whatsapp-groups`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Choose a custom name like `sbsc-groups` or leave default

3. Click **"Deploy!"** button

### 4.3: Wait for Deployment

- You'll see a spinner and logs
- This takes **2-5 minutes**
- The app will automatically start once ready

### 4.4: Your App is Live! 🎉

You'll get a URL like:
```
https://sbsc-groups.streamlit.app
```
or
```
https://YOUR_USERNAME-sbsc-whatsapp-groups.streamlit.app
```

**Share this URL with all SBSC students!**

✅ **Deployment Complete!**

---

## 📊 Testing Your App

### Test Checklist:

1. ✅ Open the app URL
2. ✅ Select a Course (e.g., B.Com)
3. ✅ Select a Semester (e.g., 1)
4. ✅ Select a Subject (e.g., Financial Accounting)
5. ✅ Click "Join WhatsApp Group" button
6. ✅ Check if WhatsApp opens

### Expected Behavior:

- Dropdowns should show available options
- Button should be green with white text
- Clicking button opens WhatsApp (web or app)
- Mobile-friendly on phones

---

## 🔄 How to Update WhatsApp Links (After Deployment)

### Method 1: Edit Directly on GitHub (Easiest)

1. Go to your GitHub repository
2. Click on **`data.csv`** file
3. Click the **pencil icon** (✏️ Edit this file) on the right
4. Make your changes:
   - Add new rows for new groups
   - Update WhatsApp links
   - Change Status to Inactive for old groups
5. Scroll down
6. Add commit message: "Updated WhatsApp links for Semester 2"
7. Click **"Commit changes"**

**The app will automatically redeploy in 1-2 minutes!**

### Method 2: Upload New CSV File

1. Download current `data.csv` from GitHub
2. Open in Excel or Google Sheets
3. Make changes (add/edit/delete rows)
4. Save as CSV (ensure UTF-8 encoding)
5. Go to GitHub repository
6. Click on `data.csv`
7. Click **trash icon** to delete
8. Upload your new `data.csv`
9. Commit changes

**The app will automatically update!**

---

## 🎨 Customization Guide

### Change App Title

1. Edit `app.py` on GitHub (pencil icon)
2. Find line 48: 
   ```python
   st.markdown('<h1 class="title">💬 SBSC Subject-wise WhatsApp Groups</h1>'
   ```
3. Change the text between `>` and `</h1>`
4. Commit changes

### Change Colors

1. Edit `.streamlit/config.toml`
2. Change color codes:
   ```toml
   primaryColor="#25D366"  # Button color (WhatsApp green)
   backgroundColor="#FFFFFF"  # Background (white)
   ```
3. Commit changes

### Add More Courses

1. Edit `data.csv`
2. Add rows with new course names
3. The app will automatically show the new course in dropdown

---

## 🐛 Common Issues & Solutions

### Issue 1: "Data file not found" error

**Solution**: 
- Check that `data.csv` is in the repository root (same level as `app.py`)
- File name must be exactly `data.csv` (lowercase)

### Issue 2: Groups not appearing in dropdown

**Solution**:
- Check CSV format: `Course,Semester,Subject,WhatsApp_Link,Status`
- Ensure Status is exactly `Active` (capital A)
- No extra spaces before/after commas

### Issue 3: WhatsApp link doesn't work

**Solution**:
- Use full link format: `https://chat.whatsapp.com/XXXXXXXXXXXXX`
- Test link manually in browser first
- Ensure no spaces in the link

### Issue 4: App is slow to load

**Solution**:
- This is normal for Streamlit Cloud free tier
- First load can take 10-30 seconds
- Subsequent loads are faster (cached)

### Issue 5: App shows old data after updating CSV

**Solution**:
- Wait 2-3 minutes for auto-redeploy
- Click "Refresh Data" in sidebar
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)

---

## 💡 Pro Tips

### Tip 1: Get a Custom Domain (Optional)

You can connect a custom domain like `groups.sbsc.edu.in`:
1. Go to Streamlit Cloud settings
2. Click "Custom domain"
3. Follow DNS setup instructions

### Tip 2: Monitor App Usage

Streamlit Cloud shows:
- Number of users
- App uptime
- Load times

Access via: Settings → Analytics

### Tip 3: Set Up Notifications

Get email alerts when app goes down:
1. Go to app settings
2. Enable "Email notifications"

### Tip 4: Add Admin Password (Advanced)

To restrict who can update data, add authentication:
```python
# In app.py
import streamlit as st

# Add at the top of your app
password = st.sidebar.text_input("Admin Password", type="password")
if password != "your_secret_password":
    st.error("Access Denied")
    st.stop()
```

### Tip 5: Use Google Sheets for Real-Time Updates

1. Create Google Sheet with same columns
2. File → Share → Anyone with link can view
3. Get CSV export link: File → Download → .csv
4. In `app.py`, replace:
   ```python
   df = pd.read_csv('data.csv')
   ```
   with:
   ```python
   df = pd.read_csv('YOUR_GOOGLE_SHEET_CSV_EXPORT_URL')
   ```

---

## 📞 Getting Help

### Streamlit Community

- Forum: https://discuss.streamlit.io
- Documentation: https://docs.streamlit.io
- Examples: https://streamlit.io/gallery

### GitHub Issues

Create an issue on your repository if you face problems

### Contact Support

- Streamlit Cloud support: support@streamlit.io
- Response time: 1-3 business days (free tier)

---

## 📈 Scaling Up (Future)

When you have 100+ groups:

1. **Add Search Bar**: Filter groups by keyword
2. **Add Admin Panel**: Web interface to update groups
3. **Use Database**: Move from CSV to PostgreSQL/MongoDB
4. **Add Analytics**: Track which groups are most popular
5. **Add User Feedback**: Let students report broken links

For these features, you'll need to upgrade from Streamlit to a full-stack solution.

---

## ✅ Launch Checklist

Before sharing with students:

- [ ] Test on mobile phone
- [ ] Test on desktop browser
- [ ] Test all WhatsApp links work
- [ ] Verify all courses/semesters show correctly
- [ ] Check for typos in subject names
- [ ] Test "No group found" scenario
- [ ] Share URL with 2-3 friends for feedback
- [ ] Create backup of `data.csv`
- [ ] Note down GitHub username and repo name
- [ ] Save Streamlit Cloud login credentials

---

## 🎉 You're All Set!

Your app is now:
- ✅ Live and accessible 24/7
- ✅ Mobile-friendly
- ✅ Easy to update
- ✅ Free to host
- ✅ Scalable

**Share the URL and help your fellow students! 🚀**

---

**Created**: January 2026  
**Version**: 1.0  
**Maintainer**: [Your Name/CR Name]
