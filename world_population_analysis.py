# 🌍 WORLD POPULATION ANALYSIS (1970–2050)
# ------------------------------------------------
# Author: Sushma J
# Role: Finance Analyst
# Tool: Python (Jupyter / VS Code)
# Dataset: world_population.csv
# ------------------------------------------------

# === IMPORT LIBRARIES ===
import pandas as pd
import matplotlib.pyplot as plt
import os

# === LOAD DATA ===
try:
    current_dir = os.getcwd()
    csv_path = os.path.join(current_dir, "world_population.csv")
    data = pd.read_csv(csv_path)
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: CSV file not found. Make sure it's in the same folder as this script.")
    data = None
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
    data = None

# === RUN ONLY IF DATA LOADED ===
if data is not None:
    print("\n📊 --- BASIC DATA INFO ---")
    print(data.head())
    print("\n🔢 Columns available:", list(data.columns))

    # === SUMMARY STATISTICS ===
    print("\n📈 --- STATISTICAL SUMMARY ---")
    print(data.describe())

    # === POPULATION GROWTH BY CONTINENT ===
    plt.figure(figsize=(8, 5))
    continent_growth = data.groupby("Continent")["2022 Population"].sum().sort_values(ascending=False)
    continent_growth.plot(kind="bar", color="#4CAF50")
    plt.title("🌎 Total Population by Continent (2022)")
    plt.xlabel("Continent")
    plt.ylabel("Population (in billions)")
    plt.tight_layout()
    plt.savefig("continent_population_2022.png")
    plt.show()

    # === TOP 10 COUNTRIES BY POPULATION (2022) ===
    plt.figure(figsize=(10, 6))
    top_countries = data.nlargest(10, "2022 Population")
    plt.bar(top_countries["Country"], top_countries["2022 Population"], color="#2196F3")
    plt.title("🏆 Top 10 Most Populous Countries (2022)")
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("top10_countries_2022.png")
    plt.show()

    # === POPULATION CHANGE OVER TIME ===
    plt.figure(figsize=(10, 6))
    plt.plot(data["Country"], data["1970 Population"], label="1970", color="orange")
    plt.plot(data["Country"], data["2022 Population"], label="2022", color="green")
    plt.title("📉 Population Change (1970 vs 2022)")
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig("population_change_1970_2022.png")
    plt.show()

    # === DENSITY ANALYSIS (Optional Column if present) ===
    if "Density (per km²)" in data.columns:
        plt.figure(figsize=(8, 5))
        plt.scatter(data["2022 Population"], data["Density (per km²)"], color="#9C27B0")
        plt.title("🌐 Density vs Population (2022)")
        plt.xlabel("Population")
        plt.ylabel("Density (per km²)")
        plt.tight_layout()
        plt.savefig("density_vs_population.png")
        plt.show()

    print("\n✅ Analysis completed successfully!")
else:
    print("\n⚠️ Analysis skipped due to missing data.")
