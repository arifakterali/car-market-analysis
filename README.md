# Car Market Trends Analysis

A data analysis and data cleaning project examining used car market trends, pricing patterns, vehicle depreciation, and usage characteristics using CarDekho sales data.

---

## Project Overview

Understanding the drivers of used car pricing is critical for buyers, sellers, and automotive dealerships. This project cleans and evaluates historical vehicle listings to uncover relationships between resale value (`Selling_Price`), original showroom price (`Present_Price`), vehicle age, odometer readings (`Kms_Driven`), fuel type, seller channels, and transmission systems.

### Key Objectives
- **Data Cleaning & Filtering**: Resolve duplicate records, eliminate high-mileage outliers, and segregate car listings from motorcycle/scooter entries.
- **Feature Engineering**: Derive analytical indicators including `Age` (relative to benchmark year 2019) and usage intensity (`Kms_per_year`).
- **Univariate Distribution Profiling**: Analyze the distribution of numeric and categorical attributes across the vehicle inventory.
- **Bivariate & Trend Analysis**: Evaluate depreciation curves, price correlation with original cost, and pricing variation across fuel types, transmission modes, and seller categories.

---

## Dataset Summary

The analysis starts with raw CarDekho listings (**301 rows**) and refines them into a targeted 4-wheeler dataset (**198 rows**):

| Attribute | Type | Description |
|---|---|---|
| `Car_Name` | String | Model / Make name of the vehicle |
| `Year` | Integer | Year of manufacture / initial registration (2003 – 2018) |
| `Selling_Price` | Float | Final listing / selling price (in ₹ Lakhs) |
| `Present_Price` | Float | Current showroom / ex-showroom price (in ₹ Lakhs) |
| `Kms_Driven` | Integer | Total distance covered by the vehicle (in kilometers) |
| `Fuel_Type` | Categorical | Fuel system (`Petrol`, `Diesel`, `CNG`) |
| `Seller_Type` | Categorical | Selling channel (`Dealer`, `Individual`) |
| `Transmission` | Categorical | Gearbox type (`Manual`, `Automatic`) |
| `Owner` | Integer | Number of previous owners (0, 1, 3) |
| `Age` *(Engineered)* | Integer | Vehicle age in years (`2019 - Year`) |
| `Kms_per_year` *(Engineered)* | Float | Annualized usage metric (`Kms_Driven / Age`) |

---

## Data Cleaning & Preprocessing Pipeline

Implemented in [`cleaning.py`]:

1. **Deduplication**: Removed duplicate listing entries.
2. **Extreme Outlier Filtering**: Trimmed vehicle entries with odometer readings exceeding 300,000 km.
3. **Vehicle Category Segregation**:
   - The original dataset merged both cars and two-wheelers (bikes/scooters like *Activa*, *Royal Enfield*, *Bajaj Pulsar*, etc.).
   - Used casing conventions (`str[0].islower()`) to isolate 4-wheelers from two-wheelers.
4. **Feature Engineering**:
   - `Age = 2019 - Year`
   - `Kms_per_year = Kms_Driven / Age`
5. **Output**: Stored cleaned records in [`cleaned_car_data.csv`] (198 clean car records).

---

## Visualizations & Key Findings

Generated via [`analysis.py`] and stored in the [`charts/`] directory:

| Visualization | Filename | Key Takeaway |
|---|---|---|
| **Selling Price Distribution** | `charts/01_selling_price_hist.png` | Right-skewed distribution; majority of used cars cluster between ₹2 – ₹8 Lakhs (Mean: ₹6.60 Lakhs). |
| **Present Price Distribution** | `charts/02_present_price_hist.png` | Long right tail representing luxury/SUV segments up to ₹92.6 Lakhs (Mean: ₹10.88 Lakhs). |
| **Kilometers Driven Distribution** | `charts/03_kms_driven_hist.png` | Concentrated between 20,000 and 60,000 km (Mean: ~41,400 km). |
| **Car Age Distribution** | `charts/04_car_age_hist.png` | Most cars are relatively recent, averaging ~5.4 years old (ranging from 1 to 16 years). |
| **Categorical Breakdowns** | `charts/05_fuel_type_bargraph.png`, `charts/06_seller_type_bargraph.png`, `charts/07_transmission_bargraph.png` | Petrol dominant (138), followed by Diesel (58) and CNG (2). Manual transmissions (168) vastly outnumber automatics (30); dealer listings represent the vast majority (193 vs 5 individual). |
| **Selling Price vs. Present Price** | `charts/08_price_vs_presentprice_scatter.png` | Strong positive linear correlation — higher initial showroom price commands higher absolute resale value. |
| **Selling Price vs. Age** | `charts/09_price_vs_age_scatter.png` | Clear downward sloping depreciation curve; steeper price drop in the initial 3–5 years. |
| **Selling Price vs. Odometer** | `charts/10_price_vs_kms_driven_scatter.png` | Moderate negative correlation with mileage; higher variance driven by underlying car segment. |
| **Price by Fuel Type** | `charts/11_price_by_fuel_type_boxplot.png` | Diesel vehicles maintain a higher median resale value compared to petrol cars. |
| **Price by Transmission** | `charts/13_price_by_transmission_boxplot.png` | Automatic vehicles exhibit higher median and upper-quartile resale prices than manual cars. |

---

## Getting Started

### Prerequisites

- Python 3.8+
- Required packages:
  ```bash
  pip install pandas numpy matplotlib seaborn
  ```

### Running the Workflow

1. **Clean Data and Engineer Features**:
   ```bash
   python cleaning.py
   ```
   *Generates `cleaned_car_data.csv`.*

2. **Generate Visualizations**:
   ```bash
   python analysis.py
   ```
   *Outputs all 13 plots into the `charts/` directory.*

---

## Tech Stack

- **Language**: Python
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
