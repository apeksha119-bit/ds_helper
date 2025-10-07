import pandas as pd
from ds_helper import column_type_detector, visualize, TextCleaner

# Create a sample DataFrame
data = {
    'Age': [25, 30, 45, 22, 27],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male'],
    'Review': ['Good product', 'Excellent and fast', 'Not good', 'Very useful', 'Good value']
}
df = pd.DataFrame(data)

print("Sample DataFrame:")
print(df)

# Test column detector
print("\nColumn Types:")
types = column_type_detector(df)
print(types)

# Test text cleaner
print("\nText Cleaning:")
cleaner = TextCleaner()
sample_text = "Um, I think this product is, like, really good!!! But you know, it’s a bit pricey."
print("Original:", sample_text)
print("Cleaned:", cleaner.clean_text(sample_text))

# Test visualizer (this will show plots, but in script, it might not display)
print("\nVisualizing data...")
visualize(df)
print("Visualization complete.")
