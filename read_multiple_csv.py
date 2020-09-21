import os
import glob
import pandas as pd
import numpy as np

# source: https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
# set working directory
os.chdir(r'''H:\SpaceApes\SpaceApes-Programing\Projects\bi_py\combinding_inputs\input''')
extension = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(extension))]
output_dir = r'''H:\SpaceApes\SpaceApes-Programing\Projects\bi_py\combinding_inputs\output\{}'''

# original column names found in the input files
cols = ["Date", "Media Source (pid)", "Campaign (c)", "Impressions", "Clicks", "Installs", "Sessions", "Total Cost", 
        "af_registration (Unique users)", "af_complete_registration (Unique users)", "af_purchase (Unique users)", "af_purchase_complete (Unique users)",
        "mm_registration (Unique users)", "mm_registration_complete (Unique users)", "mm_purchase_intent (Unique users)", "mm_purchase_complete (Unique users)",
        "filename"]

# bulild header of final df with all cols wanted
final_df = pd.DataFrame(columns=cols, index=[0])
final_df = final_df.drop(index=0)

file_counter = 0
row_counter = 0

# build df for file with all cols, but 0 when not in file
for file in all_files:
    file_df = pd.read_csv(file)

    # in file_df might be different cols in dif. order
    for col in cols:
        if col == cols[0]:
            temp_df = pd.DataFrame(file_df[col])
            row_counter += 1
        elif col in file_df.columns:
            temp_df = pd.concat([temp_df, file_df[col]], axis=1, ignore_index=True)
            row_counter += 1
        elif col == "filename":
            filename_df = pd.DataFrame(data=([file] * temp_df.shape[0]), columns=[col])
            temp_df = pd.concat([temp_df, filename_df], axis=1, ignore_index=True)
            row_counter += 1
        else:
            empty_df = pd.DataFrame(columns=[col])
            temp_df = pd.concat([temp_df, empty_df], axis=1, ignore_index=True)
            row_counter += 1

    # source: https://stackoverflow.com/questions/53927219/pandas-concat-two-data-frames-one-with-and-one-without-headers
    final_df = pd.DataFrame(np.concatenate([final_df.values, temp_df.values]), columns=final_df.columns)
    file_counter += 1

final_df = final_df.fillna(0)
final_df.to_csv(output_dir.format('output.csv'), index=False)
print("combined {} files with {} colums in total.".format(file_counter, row_counter))