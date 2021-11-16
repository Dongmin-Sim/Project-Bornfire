import pandas as pd

def load_data(categroy):
    csv_dir = f'static/assets/data/result_{categroy}_patient.csv'
    

    df = pd.read_csv(csv_dir)
    label, data = df['date'].to_list(), df['total'].to_list()
    
    return label, data