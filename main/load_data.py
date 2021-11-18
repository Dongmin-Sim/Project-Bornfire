from flask.globals import _lookup_app_object
import pandas as pd

def load_patient_data(btnValue):
    csv_dir = f'static/assets/data/patient/result_{btnValue}_patient.csv'
    

    df = pd.read_csv(csv_dir)
    label, data = df['date'].to_list(), df['total'].to_list()
    
    return label, data


def load_sexAge_data(btnValue):
    male_csv_dir = f'static/assets/data/sexAge/counts_male.csv'
    female_csv_dir = f'static/assets/data/sexAge/counts_female.csv'
    pie_csv_div = f'static/assets/data/sexAge/total_cost.csv'

    # bar chart
    male_df = pd.read_csv(male_csv_dir)
    female_df = pd.read_csv(female_csv_dir)

    label = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80']
    
    male_data, female_data = male_df[btnValue].to_list(), female_df[btnValue].to_list()

    # pie chart
    cost_df = pd.read_csv(pie_csv_div)
    cost_result = cost_df[btnValue].to_list()
    
    print(type(female_data), type(cost_result))

    data = [male_data[1:], female_data[1:], cost_result]

    return label, data