# Quantium Starter Repo

Starter repo for the Quantium software engineering task. The goal is to take some raw sales data, pull out just the "Pink Morsel" sales, and then show it on a simple graph you can filter by region.

## What's in here

* `sift_data.py` — goes through `data/daily_sales_data.csv` and pulls out only the Pink Morsel rows, working out `sales = price * quantity` for each one. Writes the result to `final_sales_data.csv`.
* `dash_app.py` — takes `final_sales_data.csv` and plots it on a line chart using Dash/Plotly. There's a radio button to filter the chart by region (north, east, south, west, or all).
* `dash_test.py` — a few basic tests to check the app's components (header, chart, region picker) are actually there and working.
* `data/` — the raw sales CSVs.

## How to run it

1. Clone the repo and set up a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

2. Install the packages used in the project:
```
pip install pandas dash plotly pytest
```

3. Run the sifting script first to generate the filtered data:
```
python sift_data.py
```

4. Then start the app:
```
python dash_app.py
```
Open the link it gives you (usually `http://127.0.0.1:8050`) and you should see the Pink Morsel Visualizer with the region filter underneath the chart.

5. To run the tests:
```
pytest dash_test.py
```

## Notes

* `sift_data.py` only reads `daily_sales_data.csv`, not the split files (`_0`, `_1`, `_2`) — would need to combine those first if I want to use them instead.
* Chart colours are set near the top of `dash_app.py` if I want to change them later.

---

**Author**

Ameen Ahmed
