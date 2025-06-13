import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees['time_spent'] = employees['out_time'] - employees['in_time']

    df = employees.groupby(['event_day','emp_id'])['time_spent'].sum().reset_index().rename(columns = {'event_day':'day','time_spent':'total_time'})

    return df