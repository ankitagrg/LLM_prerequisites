import pandas as pd

df = pd.DataFrame({
    "Product": ["A", "B", "A", "C", "B", "A"],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Sales": [100, 150, 200, 250, 300, 350]
})

pivot = df.pivot_table(
    index="Product",
    columns="Month",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)

print("Pivot Table:\n", pivot)
