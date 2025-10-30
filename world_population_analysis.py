# 🌍 World Population Analysis (1970–2050)
# Author: Sushma J — Finance Analyst
# Tool: Python (Visual Studio Code / Jupyter Notebook)
# Description: Full population analytics and visualizations (1970–2050)

# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt

# --- Load Dataset ---
data = pd.read_csv("world_population.csv")

# --- Display Dataset Info ---
print("\n📘 Preview of Dataset:")
print(data.head())

print("\n🧾 Dataset Information:")
print(data.info())

# --- 1️⃣ Population by Continent (2022) ---
continent_pop = (
    data.groupby("Continent")["2022 Population"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
continent_pop.plot(kind="bar", color="teal")
plt.title("Population by Continent (2022)")
plt.xlabel("Continent")
plt.ylabel("Population")
plt.tight_layout()
plt.savefig("population_by_continent_2022.png")
plt.show()

# --- 2️⃣ Top 10 Most Populated Countries (2022) ---
top10 = data.nlargest(10, "2022 Population")[["Country", "2022 Population"]]

plt.figure(figsize=(10, 6))
plt.bar(top10["Country"], top10["2022 Population"], color="orange")
plt.title("Top 10 Most Populated Countries in 2022")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top10_populated_countries_2022.png")
plt.show()

# --- 3️⃣ Global Population Growth (1970–2022) ---
years = [
    "1970 Population",
    "1980 Population",
    "1990 Population",
    "2000 Population",
    "2010 Population",
    "2020 Population",
    "2022 Population",
]

# Calculate total world population per year
world_growth = data[years].sum()

plt.figure(figsize=(8, 5))
plt.plot(years, world_growth, marker="o", color="purple")
plt.title("Global Population Growth (1970–2022)")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.grid(True)
plt.tight_layout()
plt.savefig("global_population_growth.png")
plt.show()

# --- 4️⃣ Population Growth Rate by Continent (1970–2022) ---
data["Growth Rate (%)"] = ((data["2022 Population"] - data["1970 Population"]) / data["1970 Population"]) * 100
continent_growth = data.groupby("Continent")["Growth Rate (%)"].mean().sort_values(ascending=False)

plt.figure(figsize=(8,5))
continent_growth.plot(kind="bar", color="green")
plt.title("Average Population Growth Rate by Continent (1970–2022)")
plt.xlabel("Continent")
plt.ylabel("Growth Rate (%)")
plt.tight_layout()
plt.savefig("growth_rate_by_continent.png")
plt.show()

# --- 5️⃣ Top 5 Countries' Share of World Population (2022) ---
top5 = data.nlargest(5, "2022 Population")[["Country", "2022 Population"]]
plt.figure(figsize=(7,7))
plt.pie(top5["2022 Population"], labels=top5["Country"], autopct='%1.1f%%', startangle=140,
        colors=["gold","lightcoral","skyblue","lightgreen","violet"])
plt.title("Top 5 Countries' Share of Global Population (2022)")
plt.tight_layout()
plt.savefig("top5_country_share_pie.png")
plt.show()

# --- 6️⃣ Continent-wise Population Comparison (1970–2022) ---
continent_years = data.groupby("Continent")[years].sum().T
continent_years.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Population by Continent Over Years (1970–2022)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.tight_layout()
plt.savefig("continent_population_over_years.png")
plt.show()

# --- ✅ Summary Output ---
print("\n✅ Analysis Completed Successfully!")
print("All graphs have been generated and saved as PNG files:")
print("""
1️⃣ population_by_continent_2022.png
2️⃣ top10_populated_countries_2022.png
3️⃣ global_population_growth.png
4️⃣ growth_rate_by_continent.png
5️⃣ top5_country_share_pie.png
6️⃣ continent_population_over_years.png
""")