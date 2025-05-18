import pandas as pd

import matplotlib.pyplot as plt

def visualize_data(data, model=None):
    """
    Visualizes the given data. If the data contains an 'age' column, it plots a histogram
    of the age distribution. If a model is provided, it can be used for additional visualizations.

    Parameters:
    - data: A dictionary or DataFrame containing the data to visualize.
    - model: (Optional) A trained model for additional visualizations.

    Returns:
    None
    """
    df = pd.DataFrame(data)
    
    # Visualize age distribution
    if 'age' in df.columns:
        plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
        plt.title("Age Distribution of Patients")
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.show()
    else:
        print("No 'age' column to visualize.")
    
    # Additional visualizations if a model is provided
    if model is not None:
        if 'feature_importances_' in dir(model):
            feature_importances = model.feature_importances_
            features = df.columns
            plt.bar(features, feature_importances, color='lightgreen', edgecolor='black')
            plt.title("Feature Importances")
            plt.xlabel("Features")
            plt.ylabel("Importance")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("The provided model does not have feature importances.")