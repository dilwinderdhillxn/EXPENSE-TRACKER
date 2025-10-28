import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="💰 Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Enhanced CU Red & White Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #fff0f0 0%, #ffffff 50%, #fff5f5 100%);
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #DC143C 0%, #B91230 50%, #8B0000 100%);
        color: white;
        border-radius: 15px;
        height: 60px;
        font-size: 18px;
        font-weight: 700;
        border: none;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 6px 20px rgba(220, 20, 60, 0.35);
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #FF1744 0%, #DC143C 50%, #B91230 100%);
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 10px 30px rgba(220, 20, 60, 0.5);
    }
    
    .stButton>button:active {
        transform: translateY(-2px) scale(0.98);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #DC143C 0%, #B91230 50%, #8B0000 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(220, 20, 60, 0.35);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 40px rgba(220, 20, 60, 0.5);
    }
    
    .expense-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 5px 15px rgba(220, 20, 60, 0.2);
        border-left: 8px solid #DC143C;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .expense-card::after {
        content: '';
        position: absolute;
        right: -30px;
        top: -30px;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(220, 20, 60, 0.1), transparent);
        border-radius: 50%;
    }
    
    .expense-card:hover {
        transform: translateX(15px) scale(1.02);
        box-shadow: 0 8px 25px rgba(220, 20, 60, 0.3);
        border-left: 8px solid #FF1744;
    }
    
    .add-expense-section {
        background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(220, 20, 60, 0.25);
        border: 4px solid #DC143C;
        margin-bottom: 40px;
        position: relative;
        overflow: hidden;
    }
    
    .add-expense-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #DC143C, #FF1744, #DC143C);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -100% 0; }
        100% { background-position: 200% 0; }
    }
    
    h1 {
        color: #DC143C;
        text-align: center;
        font-size: 4em;
        margin-bottom: 10px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        font-weight: 700;
        letter-spacing: 2px;
        animation: fadeInDown 0.8s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    h2 {
        color: #DC143C;
        font-weight: 600;
    }
    
    h3 {
        color: #8B0000;
        font-weight: 600;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%);
        border: 3px solid #DC143C;
        color: #DC143C;
        border-radius: 15px;
        padding: 12px 25px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(220, 20, 60, 0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #ffe0e0 0%, #fff0f0 100%);
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(220, 20, 60, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #DC143C 0%, #B91230 50%, #8B0000 100%);
        color: white;
        border: 3px solid #8B0000;
        box-shadow: 0 6px 20px rgba(220, 20, 60, 0.4);
        transform: translateY(-3px);
    }
    
    /* Input fields text color - BLACK */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stDateInput>div>div>input {
        border: 3px solid #DC143C;
        border-radius: 12px;
        padding: 15px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%);
        color: #000000 !important;
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #888888 !important;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus, .stDateInput>div>div>input:focus {
        border: 3px solid #FF1744;
        box-shadow: 0 0 15px rgba(220, 20, 60, 0.3);
        transform: scale(1.02);
        color: #000000 !important;
    }
    
    /* Selectbox text color - BLACK */
    .stSelectbox>div>div>div {
        border: 3px solid #DC143C;
        border-radius: 12px;
        background: linear-gradient(135deg, #ffffff 0%, #fff8f8 100%);
        transition: all 0.3s ease;
        color: #000000 !important;
        font-weight: 600;
    }
    
    .stSelectbox>div>div>div:hover {
        border: 3px solid #FF1744;
        box-shadow: 0 0 15px rgba(220, 20, 60, 0.2);
    }
    
    /* Selectbox dropdown options - BLACK */
    .stSelectbox [data-baseweb="select"] > div {
        color: #000000 !important;
        font-weight: 600;
    }
    
    .stSelectbox option {
        color: #000000 !important;
        font-weight: 600;
    }
    
    /* Number input arrows */
    .stNumberInput input[type="number"] {
        color: #000000 !important;
        font-weight: 600;
    }
    
    /* Date input */
    .stDateInput input {
        color: #000000 !important;
        font-weight: 600;
    }
    
    .welcome-box {
        text-align: center;
        padding: 60px;
        background: linear-gradient(135deg, #ffffff 0%, #fff5f5 100%);
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(220, 20, 60, 0.15);
        border: 3px dashed #DC143C;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .footer-box {
        text-align: center;
        color: #DC143C;
        padding: 30px;
        background: linear-gradient(135deg, #ffffff 0%, #fff5f5 100%);
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(220, 20, 60, 0.15);
        border-top: 5px solid #DC143C;
    }
    
    .category-box {
        background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #DC143C;
        text-align: center;
        margin: 10px;
        box-shadow: 0 4px 15px rgba(220, 20, 60, 0.2);
        transition: all 0.3s ease;
    }
    
    .category-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(220, 20, 60, 0.3);
    }
    
    /* Delete button special styling */
    div[data-testid="column"]:has(button[kind="secondary"]) button {
        background: linear-gradient(135deg, #ff4444 0%, #cc0000 100%);
        height: 45px;
        font-size: 16px;
        border-radius: 10px;
    }
    
    div[data-testid="column"]:has(button[kind="secondary"]) button:hover {
        background: linear-gradient(135deg, #ff0000 0%, #990000 100%);
        transform: translateY(-3px);
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #fff5f5;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #DC143C 0%, #8B0000 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #FF1744 0%, #DC143C 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Animated Title
st.markdown("<h1>💰 Smart Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #DC143C; font-size: 1.4em; margin-top: -15px; font-weight: 600; letter-spacing: 1px;'>🎓 Chandigarh University Theme Edition 🎓</p>", unsafe_allow_html=True)
st.markdown("---")

# Add Expense Section on Main Page
st.markdown("<div class='add-expense-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #DC143C; margin-bottom: 30px; font-size: 2em;'>➕ Add New Expense</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

with col1:
    expense_name = st.text_input("📝 Expense Name", placeholder="e.g., Groceries, Fuel, Movie", key="expense_name", label_visibility="visible")

with col2:
    expense_amount = st.number_input("💵 Amount (₹)", min_value=0.0, step=10.0, format="%.2f", key="expense_amount")

with col3:
    expense_category = st.selectbox("🏷️ Category", 
        ["🍔 Food", "🚗 Transport", "🛍️ Shopping", "💊 Health", 
         "🎬 Entertainment", "📚 Education", "🏠 Bills", "💼 Other"], key="expense_category")

with col4:
    expense_date = st.date_input("📅 Date", datetime.now(), key="expense_date")

st.markdown("<br>", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([3, 2, 3])
with col_btn2:
    if st.button("✅ ADD EXPENSE", key="add_btn"):
        if expense_name and expense_amount > 0:
            st.session_state.expenses.append({
                "name": expense_name,
                "amount": expense_amount,
                "category": expense_category,
                "date": expense_date.strftime("%Y-%m-%d")
            })
            st.balloons()
            st.success(f"✅ Successfully Added: {expense_name} - ₹{expense_amount:.2f}")
            st.rerun()
        else:
            st.error("⚠️ Please enter valid expense details!")

st.markdown("</div>", unsafe_allow_html=True)

# Main content area
if not st.session_state.expenses:
    st.markdown("""
        <div class='welcome-box'>
            <h2 style='color: #DC143C; font-size: 2.5em; margin-bottom: 20px;'>👋 Welcome to Your Expense Tracker!</h2>
            <p style='font-size: 1.3em; color: #666; margin-bottom: 20px;'>Start managing your finances smartly by adding your first expense above.</p>
            <p style='font-size: 1.1em; color: #DC143C; font-weight: 600;'>✨ Track • Analyze • Save ✨</p>
        </div>
    """, unsafe_allow_html=True)
else:
    # Calculate total and statistics
    total_expenses = sum(exp['amount'] for exp in st.session_state.expenses)
    num_expenses = len(st.session_state.expenses)
    avg_expense = total_expenses / num_expenses if num_expenses > 0 else 0
    
    # Find highest expense
    max_expense = max(st.session_state.expenses, key=lambda x: x['amount'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display metrics with animation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; font-size: 1.3em; font-weight: 600; opacity: 0.9;">💰 Total Spent</h3>
                <h2 style="margin:20px 0; font-size: 3em; font-weight: 700;">₹{total_expenses:,.2f}</h2>
                <p style="margin:0; font-size: 0.9em; opacity: 0.8;">Keep tracking!</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #FF1744 0%, #DC143C 50%, #B91230 100%);">
                <h3 style="margin:0; font-size: 1.3em; font-weight: 600; opacity: 0.9;">📊 Total Expenses</h3>
                <h2 style="margin:20px 0; font-size: 3em; font-weight: 700;">{num_expenses}</h2>
                <p style="margin:0; font-size: 0.9em; opacity: 0.8;">Transactions</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #C41E3A 0%, #A01728 50%, #8B0000 100%);">
                <h3 style="margin:0; font-size: 1.3em; font-weight: 600; opacity: 0.9;">📈 Average</h3>
                <h2 style="margin:20px 0; font-size: 3em; font-weight: 700;">₹{avg_expense:,.2f}</h2>
                <p style="margin:0; font-size: 0.9em; opacity: 0.8;">Per expense</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["📋 All Expenses", "📊 Analytics", "🗑️ Manage"])
    
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📋 Your Expense History")
        
        # Create DataFrame
        df = pd.DataFrame(st.session_state.expenses)
        df_display = df.copy()
        df_display['amount'] = df_display['amount'].apply(lambda x: f"₹{x:,.2f}")
        df_display.index = range(1, len(df_display) + 1)
        
        # Display summary
        col1, col2 = st.columns([1, 1])
        with col1:
            st.metric("💸 Highest Expense", f"₹{max_expense['amount']:,.2f}", f"{max_expense['name']}")
        with col2:
            latest_expense = st.session_state.expenses[-1]
            st.metric("🕐 Latest Entry", f"₹{latest_expense['amount']:,.2f}", f"{latest_expense['name']}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display as styled table
        st.dataframe(
            df_display,
            use_container_width=True,
            height=450
        )
    
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📊 Detailed Expense Analytics")
        
        # Create DataFrame for charts
        df_chart = pd.DataFrame(st.session_state.expenses)
        
        # Category breakdown
        category_sum = df_chart.groupby('category')['amount'].sum().reset_index()
        category_sum = category_sum.sort_values('amount', ascending=False)
        
        st.markdown("### 🏆 Top Spending Categories")
        
        # Display category cards
        for idx, row in category_sum.iterrows():
            percentage = (row['amount'] / total_expenses) * 100
            st.markdown(f"""
                <div class="category-box">
                    <h3 style="color: #DC143C; margin: 0;">{row['category']}</h3>
                    <h2 style="color: #8B0000; margin: 10px 0;">₹{row['amount']:,.2f}</h2>
                    <p style="color: #666; font-size: 1.1em; margin: 0;">{percentage:.1f}% of total spending</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Bar chart using Streamlit
        st.markdown("### 📊 Category-wise Spending")
        st.bar_chart(category_sum.set_index('category')['amount'], use_container_width=True, color="#DC143C")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Timeline chart
        st.markdown("### 📈 Daily Spending Trend")
        df_timeline = df_chart.groupby('date')['amount'].sum().reset_index()
        df_timeline = df_timeline.sort_values('date')
        df_timeline['date'] = pd.to_datetime(df_timeline['date'])
        
        st.line_chart(df_timeline.set_index('date')['amount'], use_container_width=True, color="#DC143C")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Additional Statistics
        st.markdown("### 📈 Statistical Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Total Spent", f"₹{total_expenses:,.2f}")
        with col2:
            st.metric("📊 Total Entries", num_expenses)
        with col3:
            st.metric("📈 Average", f"₹{avg_expense:,.2f}")
        with col4:
            st.metric("🔝 Highest", f"₹{max_expense['amount']:,.2f}")
    
    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🗑️ Manage Your Expenses")
        
        if st.session_state.expenses:
            st.markdown(f"**Total Entries:** {len(st.session_state.expenses)}")
            st.markdown("<br>", unsafe_allow_html=True)
            
            for idx, exp in enumerate(st.session_state.expenses):
                col1, col2 = st.columns([6, 1])
                
                with col1:
                    st.markdown(f"""
                        <div class="expense-card">
                            <h3 style="margin:0; color:#DC143C; font-size: 1.4em;">{exp['category']} - {exp['name']}</h3>
                            <p style="margin:10px 0; color:#666; font-size: 1.15em;">
                                💰 <strong style="color:#DC143C; font-size: 1.2em;">₹{exp['amount']:,.2f}</strong> 
                                &nbsp;&nbsp;|&nbsp;&nbsp; 
                                📅 <strong>{exp['date']}</strong>
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("<br><br>", unsafe_allow_html=True)
                    if st.button("🗑️ Delete", key=f"delete_{idx}", type="secondary"):
                        deleted_expense = st.session_state.expenses.pop(idx)
                        st.success(f"✅ Deleted: {deleted_expense['name']}")
                        st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 1, 2])
            with col2:
                if st.button("🗑️ CLEAR ALL EXPENSES", key="clear_all", type="secondary"):
                    if st.session_state.expenses:
                        st.session_state.expenses = []
                        st.success("✅ All expenses cleared successfully!")
                        st.rerun()

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div class='footer-box'>
        <p style="font-size: 1.2em; margin-bottom: 15px;">💡 <strong>Pro Tip:</strong> Track your expenses daily to develop better financial habits!</p>
        <p style="font-size: 1.3em; margin-top: 15px;">Made with ❤️ by <strong style="color: #DC143C;">MAYANK & KAIF</strong></p>
        <p style="font-size: 1.1em; margin-top: 10px; color: #8B0000;">Stay Smart with Your Money 💰 | CU Pride 🎓</p>
    </div>
""", unsafe_allow_html=True)
