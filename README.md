
# Investor Finder

**Investor Finder** is a lightweight Python and Streamlit application that helps early-stage biotech startups identify aligned life science investors based on key strategic criteria such as investment stage, therapeutic focus, modality, and location.

This project demonstrates how structured data and simple web tools can support decision-making and improve efficiency in the investor sourcing process.

## What the App Does

Given a startup’s profile, the application:
- Loads a structured dataset of biotech-focused investors
- Filters and scores investors based on alignment with the input profile
- Displays top-matching investors in an interactive, sortable table

## Data Used

The dataset includes 100 simulated biotech investors and the following fields:
- Investor name  
- Stage focus (e.g., Seed, Series A)  
- Therapeutic focus (e.g., Oncology, Neurology)  
- Modality focus (e.g., RNA, Cell Therapy)  
- Geographic location  
- Notable investments  
- Estimated fund size

> Note: This dataset is simulated and intended for demonstration purposes only.

## Technologies Used

- Python 3  
- Pandas (for data manipulation)  
- Streamlit (for interactive user interface)

## How to Run the App

1. Clone the repository  
2. Install required packages:
   ```bash
   pip install pandas streamlit
   ```
3. Run the application:
   ```bash
   streamlit run investor_match_app.py
   ```

Make sure the CSV file (`biotech_investors_100.csv`) is in the same directory.
## Data Enrichment Script

This project includes a scripted pipeline to detect and fill missing fields in the investor dataset.

### How It Works

- Detects missing values in columns like `Fund Size (M USD)` and `Modality Focus`
- Fills them using simulated enrichment logic (e.g., placeholder values)
- Saves both the original and enriched files for comparison

### Run It

```bash
python scripts/enrich_investors.py

## Future Improvements

- Integrate with real investor databases and APIs (e.g., Crunchbase, PitchBook)  
- Add user input forms for more flexible search criteria  
- Implement weighted scoring algorithms  
- Enable CSV export of filtered results  
- Include investor profile pages with links and fund summaries

## 🔁 Periodic Update Script

The `scripts/update_from_api.py` script simulates fetching new investor data from an external source (e.g., OpenVC API or a firm’s public CSV).

### How It Works

- Fetches updates from a dummy local file (you can replace with a real API call)
- Merges new or updated investor rows into the master dataset
- Saves a timestamped backup of the original
- Outputs an updated dataset (`investor_data_updated.csv`)

### To Run It

```bash
python scripts/update_from_api.py
