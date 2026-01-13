# 💬 SBSC WhatsApp Group Finder

A simple, single-page web app for **Shaheed Bhagat Singh College (Delhi University)** students to find and join their subject-wise WhatsApp groups instantly.

## 🎯 Problem Solved

Students struggle every semester to find the correct WhatsApp group links for their subjects. This app provides a centralized, filterable directory of all active groups.

## ✨ Features

- **Simple Filtering**: Select Course → Semester → Subject
- **One-Click Join**: Direct WhatsApp link opening
- **Mobile-Friendly**: Fully responsive design
- **No Login Required**: Instant access for all students
- **Active Groups Only**: Shows only currently active groups
- **Easy Updates**: Admin can update groups via CSV file

## 📋 Tech Stack

- **Framework**: Streamlit (Python)
- **Data Storage**: CSV file
- **Deployment**: Streamlit Cloud (free hosting)

## 🚀 Quick Start (Local Testing)

### 1. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🌐 Deployment to Streamlit Cloud (FREE)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click **"New Repository"**
3. Name it: `sbsc-whatsapp-groups`
4. Make it **Public**
5. Create repository

### Step 2: Upload Files to GitHub

Upload these files to your repository:
- `app.py`
- `data.csv`
- `requirements.txt`
- `.streamlit/config.toml`
- `README.md`

You can use GitHub's web interface or command line:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sbsc-whatsapp-groups.git
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository: `sbsc-whatsapp-groups`
5. Set main file: `app.py`
6. Click **"Deploy"**

🎉 **Your app will be live in 2-3 minutes!**

You'll get a URL like: `https://sbsc-whatsapp-groups.streamlit.app`

## 📊 Data Structure

The app uses `data.csv` with this structure:

```csv
Course,Semester,Subject,WhatsApp_Link,Status
B.Com,1,Financial Accounting,https://chat.whatsapp.com/xxxxx,Active
B.Com,1,Business Mathematics,https://chat.whatsapp.com/xxxxx,Active
B.A,1,English Literature,https://chat.whatsapp.com/xxxxx,Active
```

### Columns Explained:

- **Course**: B.Com, B.A, B.Sc, etc.
- **Semester**: 1, 2, 3, 4, 5, 6
- **Subject**: Full subject name
- **WhatsApp_Link**: Full WhatsApp group invite link
- **Status**: Active or Inactive (only Active groups are shown)

## 🔄 How to Update Groups

### Method 1: Edit on GitHub (Easiest)

1. Go to your GitHub repository
2. Click on `data.csv`
3. Click the pencil icon (✏️) to edit
4. Make your changes
5. Scroll down and click **"Commit changes"**
6. Streamlit Cloud will auto-deploy the update in 1-2 minutes

### Method 2: Download, Edit, Re-upload

1. Download `data.csv` from GitHub
2. Open in Excel/Google Sheets
3. Add/edit/delete rows
4. Save as CSV
5. Upload back to GitHub (replace old file)

### Method 3: Use Google Sheets (Advanced)

If you want real-time updates from Google Sheets:

1. Create a Google Sheet with the same structure
2. Make it publicly viewable
3. Get the CSV export link
4. Modify `app.py` line 57 to use the Google Sheet URL:

```python
df = pd.read_csv('YOUR_GOOGLE_SHEET_CSV_LINK')
```

## 🎨 Customization

### Change Colors

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor="#25D366"  # WhatsApp green
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
```

### Change Title

Edit `app.py` line 48:

```python
st.markdown('<h1 class="title">💬 Your Custom Title</h1>', unsafe_allow_html=True)
```

## 🐛 Troubleshooting

### App shows "Data file not found"
- Ensure `data.csv` is in the same directory as `app.py`
- Check file name is exactly `data.csv` (case-sensitive)

### Groups not showing up
- Check the `Status` column is set to `Active` (not `active` or `ACTIVE`)
- Ensure no extra spaces in CSV data

### WhatsApp link doesn't work
- Use full WhatsApp invite links: `https://chat.whatsapp.com/XXXXX`
- Test links manually before adding to CSV

### Deployment fails
- Verify `requirements.txt` is in the root directory
- Check GitHub repository is public
- Ensure all files are committed and pushed

## 📱 Mobile Experience

The app is fully mobile-responsive and works great on:
- ✅ Android phones
- ✅ iPhones
- ✅ Tablets
- ✅ Desktop browsers

## 🔐 Security & Privacy

- No login required = No user data collected
- No backend database = No data breaches
- WhatsApp links are public invite links
- Open-source code = Transparent and auditable

## 📞 Support

For issues or questions:
- Contact your College CR
- Create an issue on GitHub
- Email: [your-email@example.com]

## 📝 License

Free to use and modify for educational purposes.

## 🙏 Credits

Built for SBSC students by students.

---

**Last Updated**: January 2026
**Version**: 1.0
