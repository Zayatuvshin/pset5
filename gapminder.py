import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Gapminder data
@st.cache_data
def load_data():
    data = pd.read_csv('gapminder.csv')
    return data
    
data = load_data()



st.sidebar.title("World Data Explorer")
st.sidebar.markdown("Explore country-specific development metrics over time.")
country = st.sidebar.selectbox("Choose a country", data['country'].unique())
metric = st.sidebar.selectbox("Choose a metric", ['lifeExp', 'gdpPercap', 'pop'])
st.title("Gapminder Data Visualization")
st.markdown(f"### {metric} Over Time for {country}")

country_data = data[data['country'] == country]
plt.style.use("ggplot")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(country_data['year'], country_data[metric], marker='o', color='green', linewidth=2)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel(metric, fontsize=12)
ax.set_title(f"{metric} in {country} Over Time", fontsize=16, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(plt)


avg_value = country_data[metric].mean()
latest_value = country_data[metric].iloc[-1]
st.markdown("### Key Statistics")
st.write(f"**Average {metric}**: {avg_value:.2f}")
st.write(f"**Latest {metric} (most recent year)**: {latest_value:.2f}")

st.sidebar.info("Use the dropdowns to select a country and metric.")