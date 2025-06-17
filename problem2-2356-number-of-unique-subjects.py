import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    df = teacher[['teacher_id','subject_id']].drop_duplicates()
    df = df.groupby('teacher_id')['subject_id'].count().reset_index().rename(columns={'subject_id':'cnt'})
    return df