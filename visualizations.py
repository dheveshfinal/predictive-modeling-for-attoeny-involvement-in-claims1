import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def create_distribution_plot(df, attribute):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df[attribute], kde=True, bins=20, ax=ax, color='#4A90E2')
    ax.set_title(f"Distribution of {attribute}")
    return fig

def create_boxplot(df, attribute):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df[attribute], ax=ax, color='#50C878')
    ax.set_title(f"Boxplot of {attribute}")
    return fig

def create_countplot(df, attribute):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(y=df[attribute], 
                 order=df[attribute].value_counts().index, 
                 ax=ax, 
                 palette='viridis')
    ax.set_title(f"Countplot of {attribute}")
    return fig

def create_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if numeric_df.empty:
        return None
    
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, cmap='coolwarm', annot=True, ax=ax)
    ax.set_title("Correlation Matrix Heatmap")
    return fig

def create_pairplot(df, cols):
    fig = sns.pairplot(df[cols], diag_kind='kde', corner=True)
    return fig

def create_barplot_with_hue(df, x_attr, hue_attr):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=x_attr, hue=hue_attr, data=df, ax=ax, palette='Set2')
    ax.set_title(f"{x_attr} Count by {hue_attr}")
    return fig

def render_visualizations(df):
    st.title("Data Visualizations Dashboard")
    st.markdown("Explore patterns and relationships in the insurance claims dataset.")

    # Single Attribute Analysis
    st.header("Single Attribute Analysis")
    attribute = st.selectbox("Select Attribute", df.columns)
    
    if df[attribute].dtype in ['int64', 'float64']:
        st.pyplot(create_distribution_plot(df, attribute))
        st.pyplot(create_boxplot(df, attribute))
    else:
        st.pyplot(create_countplot(df, attribute))

    # Relationship Analysis
    st.header("Relationship Analysis")
    col1, col2 = st.columns(2)
    with col1:
        attr_x = st.selectbox("X-axis Attribute", df.columns, key='x_axis')
    with col2:
        attr_y = st.selectbox("Y-axis Attribute", df.columns, key='y_axis')

    if attr_x and attr_y:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x=attr_x, y=attr_y, ax=ax, color='#9B59B6')
        ax.set_title(f"{attr_x} vs {attr_y}")
        st.pyplot(fig)

    # Advanced Visualizations
    st.header("Advanced Analytics")

    # Financial Metrics
    st.subheader("Financial Metrics Overview")
    financial_cols = ['CASENUM', 'LOSS', 'Claim_Amount_Requested', 'Settlement_Amount']
    if all(col in df.columns for col in financial_cols):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=df[financial_cols])
        ax.set_title("Financial Metrics Comparison")
        st.pyplot(fig)

    # Driving Record Distribution
    st.subheader("Driving Record Distribution")
    if 'Driving_Record' in df.columns:
        fig, ax = plt.subplots(figsize=(8, 8))
        df['Driving_Record'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_title("Driving Record Distribution")
        st.pyplot(fig)

    # Correlation Analysis
    st.subheader("Correlation Analysis")
    correlation_fig = create_correlation_heatmap(df)
    if correlation_fig:
        st.pyplot(correlation_fig)
    else:
        st.warning("No numeric columns available for correlation analysis.")

    # Pairplot for Selected Columns
    st.subheader("Pairplot of Selected Attributes")
    pairplot_cols = st.multiselect("Select Columns for Pairplot", df.select_dtypes(include=['float64', 'int64']).columns)
    if pairplot_cols:
        pairplot_fig = create_pairplot(df, pairplot_cols)
        st.pyplot(pairplot_fig)

    # Barplot with Hue
    st.subheader("Categorical Attribute Analysis")
    if 'ATTORNEY' in df.columns and 'CLMSEX' in df.columns:
        st.pyplot(create_barplot_with_hue(df, 'ATTORNEY', 'CLMSEX'))

    if 'SEATBELT' in df.columns and 'Claim_Approval_Status' in df.columns:
        st.pyplot(create_barplot_with_hue(df, 'SEATBELT', 'Claim_Approval_Status'))