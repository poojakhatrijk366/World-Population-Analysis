# 🌍 World Population Analysis (1970–2050)
# Author: Sushma J — Finance Analyst

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
file_path = "world_population.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError("Dataset not found. Please make sure 'world_population.csv' is in the same folder.")

data = pd.read_csv(file_path)

# Display first few rows
print("Preview of dataset:")
print(data.head())

# Basic information
print("\nDataset Info:")
print(data.info())

# --- Population Trends by Continent ---
continent_pop = data.groupby("Continent")["2022 Population"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
continent_pop.plot(kind="bar", color="teal")
plt.title("Population by Continent (2022)")
plt.xlabel("Continent")
plt.ylabel("Population")
plt.tight_layout()
plt.savefig("population_by_continent.png")
plt.show()

# --- Top 10 Most Populated Countries in 2022 ---
top10 = data.nlargest(10, "2022 Population")[["Country/Territory", "2022 Population"]]
plt.figure(figsize=(10,6))
plt.barh(top10["Country/Territory"], top10["2022 Population"], color="orange")
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Population")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top10_countries_2022.png")
plt.show()

# --- Growth Analysis: 1970–2022 ---
data["Growth (1970–2022)"] = ((data["2022 Population"] - data["1970 Population"]) / data["1970 Population"]) * 100
top_growth = data.nlargest(10, "Growth (1970–2022)")[["Country/Territory", "Growth (1970–2022)"]]

plt.figure(figsize=(10,6))
plt.barh(top_growth["Country/Territory"], top_growth["Growth (1970–2022)"], color="purple")
plt.title("Top 10 Countries by Population Growth (1970–2022)")
plt.xlabel("Growth (%)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top10_growth_1970_2022.png")
plt.show()

print("\nAnalysis complete ✅. Charts saved as PNG files in your repository.")