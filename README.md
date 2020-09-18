# combinding_inputs
I want to solve the problem of manualy combinding several CSV files from differen online marketing sources by creating a python script.

We start by having a folder named combinding_inputs and filling it with two more folder, named "input" and "output". 

Fill the input folder with a file callesd input.csv, where you can specify the colums you want and give them names you want.
This must be  done in CSV format with "," as colum separation.
You just need to write all wanted original colums in the first cell a1. For example: "Date,Media Source (pid),Campaign (c),Impressions,Clicks,Installs,"...
In cell a2, you gan give the colums own names, but you can not change the order (order must be the same, but can be set by you). For example like this:
date,media_source,campaign,impressions,clicks,installs,...

After this, you fill the input folder with all files you want to combilde.

The program then looks for all headers of all files with the extension "csv" and combines all input files into one export file, in a ordered way. 

It will create a file in the output folder called "export", but the folder muss be empty, because we cant overwirte yet!


Coming:
Inputformat (SQL table to dataframe & Web calls)
Filters
GUIs
