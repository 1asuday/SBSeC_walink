import streamlit as st
import pandas as pd
from urllib.parse import quote

# Page configuration
st.set_page_config(
    page_title="SBSC WhatsApp Groups",
    page_icon="💬",
    layout="centered"
)

# Custom CSS for better mobile experience and styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #25D366;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        border: none;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #128C7E;
    }
    .title {
        text-align: center;
        color: #075E54;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .no-result {
        background-color: #fff3cd;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        border-left: 5px solid #ffc107;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">💬 SBSC Subject-wise WhatsApp Groups</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Shaheed Bhagat Singh College (Delhi University)</p>', unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_data():
    """Load WhatsApp group data from CSV file"""
    try:
        df = pd.read_csv('data.csv')
        # Filter only active groups
        df = df[df['Status'].str.upper() == 'ACTIVE']
        return df
    except FileNotFoundError:
        st.error("❌ Data file not found. Please ensure 'data.csv' exists.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

# Load the data
df = load_data()

# Filters Section
st.markdown("### 🎯 Select Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    # Get unique courses
    courses = sorted(df['Course'].unique())
    selected_course = st.selectbox(
        "Course",
        options=courses,
        key="course"
    )

with col2:
    # Filter semesters based on selected course
    filtered_semesters = df[df['Course'] == selected_course]['Semester'].unique()
    semesters = sorted(filtered_semesters)
    selected_semester = st.selectbox(
        "Semester",
        options=semesters,
        key="semester"
    )

with col3:
    # Filter subjects based on selected course and semester
    filtered_subjects = df[
        (df['Course'] == selected_course) & 
        (df['Semester'] == selected_semester)
    ]['Subject'].unique()
    subjects = sorted(filtered_subjects)
    selected_subject = st.selectbox(
        "Subject",
        options=subjects,
        key="subject"
    )

# Result Section
st.markdown("---")

# Find the matching group
result = df[
    (df['Course'] == selected_course) & 
    (df['Semester'] == selected_semester) & 
    (df['Subject'] == selected_subject)
]

if not result.empty:
    # Get the WhatsApp link
    whatsapp_link = result.iloc[0]['WhatsApp_Link']
    
    # Display result
    st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f"### 📚 {selected_subject}")
    st.markdown(f"**Course:** {selected_course} | **Semester:** {selected_semester}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Join button
    if st.button("✅ Join WhatsApp Group", use_container_width=True):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={whatsapp_link}">', unsafe_allow_html=True)
        st.success("Opening WhatsApp... If it doesn't open automatically, click the link below:")
        st.markdown(f"[Open WhatsApp Group]({whatsapp_link})")
    
    # Direct link as fallback
    st.markdown(f"Or [click here to join directly]({whatsapp_link})")
    
else:
    # No match found
    st.markdown('<div class="no-result">', unsafe_allow_html=True)
    st.markdown("### ⚠️ Group Not Listed Yet")
    st.markdown("**This WhatsApp group is not available at the moment.**")
    st.markdown("Please contact your Class Representative (CR) for the link.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888; font-size: 14px;'>"
    "Made for SBSC Students | Update groups by editing data.csv"
    "</p>", 
    unsafe_allow_html=True
)

# Refresh data button (for admins)
if st.sidebar.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# Show data info in sidebar
with st.sidebar:
    st.markdown("### 📊 Data Info")
    st.markdown(f"**Total Active Groups:** {len(df)}")
    st.markdown(f"**Courses Available:** {len(df['Course'].unique())}")
    st.markdown(f"**Last Updated:** {pd.Timestamp.now().strftime('%d %b %Y')}")
