import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Financial Forecast Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS dengan Bootstrap Icons
st.markdown("""
<style>
    /* Import Bootstrap Icons */
    @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Main container */
    .main-container {
        padding: 20px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Header */
    .dashboard-header {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
    }
    
    .title {
        font-size: 42px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }
    
    .title i {
        margin-right: 15px;
        color: #ffd700;
    }
    
    .subtitle {
        color: rgba(255,255,255,0.7);
        font-size: 16px;
    }
    
    /* Stat Cards */
    .stat-card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 25px 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .stat-icon {
        font-size: 40px;
        margin-bottom: 10px;
        display: inline-block;
    }
    
    .stat-value {
        font-size: 28px;
        font-weight: 700;
        color: #2c3e50;
        margin: 10px 0;
    }
    
    .stat-label {
        font-size: 13px;
        color: #7f8c8d;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    .stat-change {
        font-size: 12px;
        margin-top: 8px;
        padding: 4px 8px;
        border-radius: 20px;
        display: inline-block;
    }
    
    .change-positive {
        background: #d4edda;
        color: #155724;
    }
    
    .change-negative {
        background: #f8d7da;
        color: #721c24;
    }
    
    /* Chart Card */
    .chart-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .chart-title {
        font-size: 18px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #e9ecef;
    }
    
    .chart-title i {
        margin-right: 10px;
        color: #667eea;
    }
    
    /* Prediction Cards */
    .pred-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: white;
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 10px 0;
    }
    
    .pred-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .pred-month {
        font-size: 14px;
        opacity: 0.9;
        margin-bottom: 10px;
    }
    
    .pred-amount {
        font-size: 24px;
        font-weight: 700;
        margin: 15px 0;
    }
    
    .pred-badge {
        background: rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 5px 10px;
        font-size: 11px;
        display: inline-block;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin: 15px 0;
    }
    
    .info-box h4 {
        margin-bottom: 15px;
    }
    
    .info-box p {
        margin: 10px 0;
    }
    
    /* Custom Tabs */
    .custom-tabs {
        display: flex;
        gap: 15px;
        margin-bottom: 30px;
        padding: 10px;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .tab-button {
        flex: 1;
        padding: 12px 24px;
        background: rgba(255,255,255,0.9);
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
        color: #333;
    }
    
    .tab-button i {
        margin-right: 8px;
    }
    
    .tab-button.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .tab-button:hover:not(.active) {
        background: rgba(255,255,255,1);
        transform: translateY(-2px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: rgba(255,255,255,0.6);
        margin-top: 40px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .title {
            font-size: 28px;
        }
        .stat-value {
            font-size: 20px;
        }
        .pred-amount {
            font-size: 18px;
        }
    }
    
    /* Slider styling */
    .stSlider {
        padding: 10px 0;
    }
    
    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Row spacing */
    .row {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header Dashboard
st.markdown("""
<div class="dashboard-header animate">
    <div class="title">
        <i class="bi bi-graph-up-arrow"></i> Financial Forecast Dashboard
    </div>
    <div class="subtitle">
        <i class="bi bi-robot"></i> AI-Powered Expense Prediction | 
        <i class="bi bi-calendar-check"></i> Real-time Analytics |
        <i class="bi bi-shield-check"></i> Accurate Forecast
    </div>
</div>
""", unsafe_allow_html=True)

# Control Panel
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### <i class='bi bi-sliders2'></i> Prediction Settings", unsafe_allow_html=True)
    prediction_months = st.slider("Forecast Horizon (Months)", 1, 12, 6, key="months_slider")
    confidence_level = st.select_slider("Confidence Level", options=["Low (70%)", "Medium (85%)", "High (95%)"], value="Medium (85%)")

# Sample data
total_expense = 142_500_000
avg_expense = 11_875_000
max_expense = 15_800_000
min_expense = 8_200_000
growth = 18.5

# Prediction data
predictions = [12_500_000, 13_200_000, 13_900_000, 14_700_000, 15_500_000, 16_400_000, 
               17_200_000, 18_000_000, 18_800_000, 19_500_000, 20_200_000, 21_000_000]
pred_months = ['Jan 2025', 'Feb 2025', 'Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025',
               'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025']

# Historical data
dates = pd.date_range(start='2024-01-01', end='2024-12-01', freq='MS')
expenses = [8_200_000, 8_900_000, 9_500_000, 10_100_000, 10_800_000, 11_500_000,
            12_200_000, 12_900_000, 13_500_000, 14_100_000, 14_800_000, 15_800_000]

# Create tabs with proper HTML
st.markdown("""
<style>
    /* Fix for streamlit tabs */
    button[data-baseweb="tab"] {
        font-size: 16px !important;
        padding: 10px 24px !important;
    }
    button[data-baseweb="tab"] i {
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Use st.tabs with proper format
tab1, tab2, tab3 = st.tabs(["📊 Main Dashboard", "📈 Deep Analysis", "💡 Insights & Reports"])

# TAB 1: MAIN DASHBOARD
with tab1:
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card animate">
            <div class="stat-icon"><i class="bi bi-wallet2"></i></div>
            <div class="stat-value">Rp {total_expense:,.0f}</div>
            <div class="stat-label">Total Expenses</div>
            <div class="stat-change change-positive"><i class="bi bi-arrow-up"></i> +12.5%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card animate">
            <div class="stat-icon"><i class="bi bi-calculator"></i></div>
            <div class="stat-value">Rp {avg_expense:,.0f}</div>
            <div class="stat-label">Monthly Average</div>
            <div class="stat-change change-positive"><i class="bi bi-arrow-up"></i> +8.3%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card animate">
            <div class="stat-icon"><i class="bi bi-graph-up"></i></div>
            <div class="stat-value">Rp {max_expense:,.0f}</div>
            <div class="stat-label">Highest Expense</div>
            <div class="stat-change change-positive"><i class="bi bi-calendar"></i> December</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-card animate">
            <div class="stat-icon"><i class="bi bi-piggy-bank"></i></div>
            <div class="stat-value">Rp {min_expense:,.0f}</div>
            <div class="stat-label">Lowest Expense</div>
            <div class="stat-change change-negative"><i class="bi bi-calendar"></i> January</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts Row
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="chart-card animate">
            <div class="chart-title">
                <i class="bi bi-graph-up"></i> Expense Trend (2024)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=expenses,
            mode='lines+markers',
            name='Actual Expenses',
            line=dict(color='#667eea', width=3),
            marker=dict(size=10, color='#764ba2', symbol='circle'),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ))
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis_title="Month",
            yaxis_title="Amount (Rp)",
            hovermode='x unified',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(family="Inter", size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="chart-card animate">
            <div class="chart-title">
                <i class="bi bi-pie-chart"></i> Expense Distribution
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        categories = ['Living', 'Transport', 'Food', 'Entertainment', 'Healthcare', 'Others']
        values = [35, 20, 25, 10, 5, 5]
        
        fig2 = go.Figure(data=[go.Pie(
            labels=categories,
            values=values,
            hole=0.6,
            marker_colors=['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe'],
            textinfo='label+percent',
            textposition='outside'
        )])
        
        fig2.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Prediction Section
    st.markdown("---")
    st.markdown(f"#### <i class='bi bi-crystal-ball'></i> {prediction_months}-Month Forecast", unsafe_allow_html=True)
    
    # Show predictions in rows of 4
    pred_cols = st.columns(4)
    for i in range(min(prediction_months, 4)):
        with pred_cols[i]:
            trend_icon = "bi-arrow-up" if i > 0 and predictions[i] > predictions[i-1] else "bi-arrow-down"
            trend_color = "#28a745" if i > 0 and predictions[i] > predictions[i-1] else "#dc3545"
            st.markdown(f"""
            <div class="pred-card animate">
                <div class="pred-month">
                    <i class="bi bi-calendar-month"></i> {pred_months[i]}
                </div>
                <div class="pred-amount">
                    Rp {predictions[i]:,.0f}
                </div>
                <div class="pred-badge">
                    <i class="{trend_icon}" style="color: {trend_color}"></i>
                    {f'+{((predictions[i]-predictions[i-1])/predictions[i-1]*100):.1f}%' if i > 0 else 'Starting'}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    if prediction_months > 4:
        pred_cols2 = st.columns(4)
        for i in range(4, min(prediction_months, 8)):
            with pred_cols2[i-4]:
                trend_icon = "bi-arrow-up" if predictions[i] > predictions[i-1] else "bi-arrow-down"
                st.markdown(f"""
                <div class="pred-card animate">
                    <div class="pred-month">
                        <i class="bi bi-calendar-month"></i> {pred_months[i]}
                    </div>
                    <div class="pred-amount">
                        Rp {predictions[i]:,.0f}
                    </div>
                    <div class="pred-badge">
                        <i class="{trend_icon}"></i>
                        +{((predictions[i]-predictions[i-1])/predictions[i-1]*100):.1f}%
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    if prediction_months > 8:
        st.info(f"<i class='bi bi-info-circle'></i> Showing 8 of {prediction_months} months forecast", unsafe_allow_html=True)

# TAB 2: DEEP ANALYSIS
with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="chart-card animate">
            <div class="chart-title">
                <i class="bi bi-activity"></i> Monthly Growth Rate
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        growth_rates = [8.5, 6.7, 6.3, 6.9, 7.4, 8.1, 5.7, 4.6, 4.4, 5.0, 6.8]
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=dates[:11],
            y=growth_rates,
            marker_color='#667eea',
            text=[f"{x:.1f}%" for x in growth_rates],
            textposition='outside'
        ))
        
        fig3.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis_title="Month",
            yaxis_title="Growth Rate (%)",
            height=400,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="chart-card animate">
            <div class="chart-title">
                <i class="bi bi-calendar-week"></i> Seasonal Pattern
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        seasons = ['Q1', 'Q2', 'Q3', 'Q4']
        season_values = [26_600_000, 32_400_000, 38_600_000, 44_900_000]
        
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=seasons,
            y=season_values,
            mode='lines+markers',
            line=dict(color='#f5576c', width=3),
            marker=dict(size=12, color='#f5576c'),
            fill='tozeroy',
            fillcolor='rgba(245, 87, 108, 0.2)'
        ))
        
        fig4.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis_title="Quarter",
            yaxis_title="Total Expense (Rp)",
            height=400,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig4, use_container_width=True)
    
    # Correlation matrix
    st.markdown("""
    <div class="chart-card animate">
        <div class="chart-title">
            <i class="bi bi-diagram-3"></i> Expense Correlation Matrix
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    corr_data = pd.DataFrame(
        np.array([[1.00, 0.85, 0.72, 0.68],
                  [0.85, 1.00, 0.78, 0.65],
                  [0.72, 0.78, 1.00, 0.82],
                  [0.68, 0.65, 0.82, 1.00]]),
        columns=['Income', 'Expense', 'Savings', 'Investment'],
        index=['Income', 'Expense', 'Savings', 'Investment']
    )
    
    fig5 = px.imshow(corr_data, text_auto=True, aspect="auto", color_continuous_scale='Viridis')
    fig5.update_layout(height=450, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig5, use_container_width=True)

# TAB 3: INSIGHTS & REPORTS
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box animate">
            <h4><i class="bi bi-exclamation-triangle"></i> Key Findings</h4>
            <p><i class="bi bi-check-circle"></i> Expense increased by <strong>18.5%</strong> in 2024</p>
            <p><i class="bi bi-check-circle"></i> Q4 shows <strong>+16.3%</strong> higher spending</p>
            <p><i class="bi bi-check-circle"></i> December peak: <strong>Rp 15.8M</strong></p>
            <p><i class="bi bi-check-circle"></i> Forecast suggests <strong>+23%</strong> growth in 2025</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box animate" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <h4><i class="bi bi-graph-up"></i> Recommendations</h4>
            <p><i class="bi bi-arrow-right"></i> Set budget limits for Q1 2025</p>
            <p><i class="bi bi-arrow-right"></i> Reduce non-essential spending</p>
            <p><i class="bi bi-arrow-right"></i> Create emergency fund (3-6 months)</p>
            <p><i class="bi bi-arrow-right"></i> Review subscription services</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="chart-card animate">
            <div class="chart-title">
                <i class="bi bi-file-text"></i> Monthly Report - December 2024
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        report_data = pd.DataFrame({
            'Category': ['Housing', 'Transportation', 'Food', 'Utilities', 'Entertainment', 'Healthcare', 'Others'],
            'Amount': [4_200_000, 2_500_000, 3_100_000, 1_800_000, 2_200_000, 1_200_000, 800_000],
            'Budget': [4_000_000, 2_000_000, 2_500_000, 1_500_000, 1_500_000, 1_000_000, 1_000_000]
        })
        
        fig6 = go.Figure()
        fig6.add_trace(go.Bar(name='Actual', x=report_data['Category'], y=report_data['Amount'], marker_color='#667eea'))
        fig6.add_trace(go.Bar(name='Budget', x=report_data['Category'], y=report_data['Budget'], marker_color='#f5576c'))
        
        fig6.update_layout(
            barmode='group',
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig6, use_container_width=True)
    
    # Savings projection
    st.markdown("""
    <div class="chart-card animate">
        <div class="chart-title">
            <i class="bi bi-piggy-bank"></i> Savings Projection (2025)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    savings_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    savings_current = [1_200_000, 1_500_000, 1_800_000, 2_000_000, 2_300_000, 2_500_000, 
                       2_800_000, 3_000_000, 3_200_000, 3_500_000, 3_800_000, 4_000_000]
    savings_target = [2_000_000] * 12
    
    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(name='Projected Savings', x=savings_months, y=savings_current, 
                              mode='lines+markers', line=dict(color='#28a745', width=3), marker=dict(size=8)))
    fig7.add_trace(go.Bar(name='Target', x=savings_months, y=savings_target, marker_color='rgba(102, 126, 234, 0.3)'))
    
    fig7.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis_title="Month",
        yaxis_title="Savings Amount (Rp)",
        height=400,
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig7, use_container_width=True)
    
    # Download button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("<i class='bi bi-file-pdf'></i> Download Full Report", use_container_width=True):
            st.success("Report generation started! Download will begin shortly.")

# Footer
st.markdown("""
<div class="footer">
    <i class="bi bi-robot"></i> Financial Forecast Dashboard v2.0 | 
    <i class="bi bi-shield-check"></i> Data encrypted & secure | 
    <i class="bi bi-clock-history"></i> Last updated: Today
    <br>
    <small><i class="bi bi-c-circle"></i> 2025 All rights reserved</small>
</div>
""", unsafe_allow_html=True)