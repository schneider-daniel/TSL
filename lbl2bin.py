"""
Script to convert labeled CSV files to binary label format based on project settings.

This script reads labeled CSV files according to project settings specified in 'project.json' 
file located in the project directory. It converts the labels from the CSV files to binary format 
and saves the resulting dataframes as new CSV files with '_lbl.csv' appended to the original file names.

Usage:
    Ensure 'project.json' file exists in the project directory containing the following keys:
        - 'files': List of CSV files to process
        - 'labels': List of label names
    
    Example 'project.json' content:
        {
            "files": ["file1.csv", "file2.csv"],
            "labels": ["label1", "label2"]
        }

Attributes:
    project_dir (str): Project directory path where 'project.json' is located.
    project_settings (dict): Dictionary containing project settings loaded from 'project.json'.
    df (DataFrame): DataFrame containing data read from CSV file.
    lbl_df (DataFrame): DataFrame containing binary label data.

Functions:
    None
"""


import os
import pandas as pd
import json

project_dir = r"../project_name"

with open(os.path.join(project_dir, 'project.json'), 'r') as file:
    project_settings = json.load(file)
file.close()


for file in project_settings['files']: 
    df = pd.read_csv(os.path.join(project_dir, file))

    lbl_df = pd.DataFrame(columns=project_settings['labels'])

    for lbl in project_settings['labels']:
        lbl_df[lbl] = df.filter(like=lbl).sum(axis=1).astype(int)

    # Save lbl-file
    lbl_df.to_csv(os.path.join(project_dir, file).replace('.csv', '_lbl.csv'), index=False)

print('>>> Done!')