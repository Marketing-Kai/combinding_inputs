# combinding_inputs
I want to solve the problem of manualy combinding several CSV files from differen online marketing sources by creating a python script.
The problem is, that we do not know the column order and some files are missing some columns, witch we need to take care of.

We start by having a folder named combinding_inputs and filling it with two more folders, named "input" and "output". 
Extract all coulmn names you want, order them and put them into the list var called cols. For example: "Date,Media Source (pid),Campaign (c),Impressions,Clicks,Installs,"...

Later I want the user to do this in an file called "input.csv" in the combinding_inpiuts folder. This way we also could user other column names than the original input names, but we are not there yet.
For example self defined column names:
date,media_source,campaign,impressions,clicks,installs,...

After this, you fill the input folder with all files you want to combinde.
The program then looks into all files with the extension "csv" and combines all input files into one export file, in an ordered way. 
It will create a file in the output folder called "output.csv" overwirte any existing files called "output.csv"!


Coming:
Inputformat (SQL table to dataframe & Web calls)
Filters
GUIs
