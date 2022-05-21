#!/usr/bin/python3
# libraries
import datetime
import gc
import os
import shutil

gc.collect()

# person who is running this
editor = 'Maria E. Montes'

# global variables -------
# This is tho decide if dates should be 2000 or 1900
today_date = datetime.datetime.now()
today_year = str(today_date.year)
today_year = int(today_year[2:4])

# in file folder
in_dir = 'text_files/'
# out file folder
out_dir = 'csv_files/'
# reoprt file folder
rep_dir = 'report_files/'
# original files dir
original_dir = 'original_files/'

# input data -----
# read files in in the infile folder
files_in = os.listdir(in_dir)

# functions for each of the file types in Dairy Comp

def demo_function(file_name_in):
    file = file_name_in
    files_name_out = file.replace('txt','csv')

    ft_file = open((in_dir+ file))
    ft_file_lines = ft_file.readlines()
    ft_file.close()
    nrows = len(ft_file_lines)

    # create file out
    file_out = open((out_dir+ files_name_out), 'w')

    # spilt line 8 to find column widths 
    columns = ft_file_lines[7].split(' ')
    column_width = []
    for i in columns:
        width = len(i)
        column_width.append(width)

    # get column names from line 7 
    names = ft_file_lines[6]
    column_names = []
    start = 0
    for i in column_width:
        stop = start + i
        if(start == 0):
            col_name = names[:stop].strip()
        else: 
            col_name = names[start-1:stop].strip()
        column_names.append(col_name)
        start = stop + 1

    # number of columns 
    ncols = len(column_names)

    # identify columns that are dates
    dates = [idx for idx, col in enumerate(column_names) if 'DAT' in col]
    dates.append(ncols-1)

    # print header
    head = (',').join(column_names)
    file_out.write(head)
    file_out.write('\n')
    # edit and print rows
    for row in range(8, nrows):
        # extract data for every line
        line = ft_file_lines[row]
        line_data = [] # store data from each column
        start = 0 # string indices
        idx = 0  # index to find the columns that are dates
        for i in column_width:
            stop = start + i
            if(start == 0):
                data = line[:stop].strip()
            else:
                data = line[start-1:stop].strip()

            # delete extra , or "
            data = data.replace(',', '')
            data = data.replace('"', '')

            # date format 
            if idx in dates:
                day_list = data.split('/')
                if len(day_list)==3:
                    month = day_list[0].strip().zfill(2)
                    day = day_list[1].strip().zfill(2)
                    year = int(day_list[2])
                    if year > today_year:
                        year = str(year + 1900)
                    else: 
                        year = str(year + 2000)
                    new_date = year +'-'+ month +'-'+ day
                else: 
                    new_date = '-'   
                data = new_date

            line_data.append(data)
            idx = idx + 1
            start = stop +1
        if('Total' in line_data[0] or len(line_data[0]) == 0):
            report_out.write('removed:'+ line_data[0] + '\n')
        else:
            line_data_print = (',').join(line_data)
            file_out.write(line_data_print)
            file_out.write('\n')
    file_out.close()

def genom_function(file_name_in):
    file = file_name_in
    files_name_out = file.replace('txt','csv')

    ft_file = open((in_dir+ file))
    ft_file_lines = ft_file.readlines()
    ft_file.close()
    nrows = len(ft_file_lines)

    # create file out
    file_out = open((out_dir+ files_name_out), 'w')

    # spilt line 8 to find column widths 
    columns = ft_file_lines[7].split(' ')
    column_width = []
    for i in columns:
        width = len(i)
        column_width.append(width)

    # get column names from line 7 
    names = ft_file_lines[6]
    column_names = []
    start = 0
    for i in column_width:
        stop = start + i
        if(start == 0):
            col_name = names[:stop].strip()
        else: 
            col_name = names[start-1:stop].strip()
        column_names.append(col_name)
        start = stop + 1

    # number of columns 
    ncols = len(column_names)

    # identify columns that are dates
    dates = [] # in genomic only today is a date
    dates.append(ncols-1)

    # print header
    head = (',').join(column_names)
    file_out.write(head)
    file_out.write('\n')

    # edit and print rows
    for row in range(8, nrows):
        # extract data for every line
        line = ft_file_lines[row]
        line_data = [] # store data from each column
        start = 0 # string indices
        idx = 0  # index to find the columns that are dates
        for i in column_width:
            stop = start + i
            if(start == 0):
                data = line[:stop].strip()
            else:
                data = line[start-1:stop].strip()

            # date format 
            if idx in dates:
                day_list = data.split('/')
                if len(day_list)==3:
                    month = day_list[0].strip().zfill(2)
                    day = day_list[1].strip().zfill(2)
                    year = int(day_list[2])
                    if year > today_year:
                        year = str(year + 1900)
                    else: 
                        year = str(year + 2000)
                    new_date = year +'-'+ month +'-'+ day
                else: 
                    new_date = '-'   
                data = new_date

            line_data.append(data)
            idx = idx + 1
            start = stop +1
        if('Total' in line_data[0] or len(line_data[0]) == 0):
            report_out.write('removed:'+ line_data[0] + '\n')
        else:
            line_data_print = (',').join(line_data)
            file_out.write(line_data_print)
            file_out.write('\n')

    file_out.close()

def testday_funtion(file_name_in):
    file = file_name_in
    files_name_out = file.replace('CSV','csv')

    ft_file = open((in_dir+ file))
    ft_file_lines = ft_file.readlines()
    ft_file.close()
    nrows = len(ft_file_lines)
        
    header_col1 = ft_file_lines[0].split(',')[0]
    if('ID' in header_col1):
        # if the file has headers then just move the file
        # move file
        file = file_name_in
        file_new_name = file.replace('CSV','csv')
        shutil.copy(in_dir + file, out_dir + file)
        os.rename((out_dir + file), (out_dir + file_new_name))
        note = 'not edited \n'
    else:
        # if the file doesnt have headers then add headers
        # create file out
        file_out = open((out_dir+ files_name_out), 'w')

        column_headers_td = ['ID','Test_Date','Milk', 'Fat', 'Protein', '305ME','SCC','Milk_estimate', 'Pen', 'Unknown']
        column_headers = (',').join(column_headers_td)

        file_out.write(column_headers)
        file_out.write('\n')
    
        for line in ft_file_lines:
            file_out.write(line)
        
        file_out.close()
        note = 'column headders addded \n'
    
    return note

def events_function(file_name_in):
    file = file_name_in
    file_new_name = file.replace('CSV','csv')
    shutil.copy(in_dir + file, out_dir + file)
    os.rename((out_dir + file), (out_dir + file_new_name))

# open report file
rep_file_name = 'dairy_comp_fileedit_report_' + today_date.strftime("%Y_%m_%d") + '.txt'
report_out = open((rep_dir+ rep_file_name), 'w')

report_out.write('\n Dairy Comp File edit \n script by: Maria E. Montes')
report_out.write('\n\n Script last edit: May 20, 2022 \n edited by: Maria E. Montes')
report_out.write('\n\n Run date-time edit: ' + today_date.strftime("%Y_%m_%d %H:%M:%S") + ' by: ' + editor)
report_out.write('\n -----------------------\n')

# print number of files in the report

# run functions on each file
for file_in in files_in:
    if 'Demographic' in file_in:
        report_out.write('\nDemographic file:'+ file_in +'\n')
        report_out.write('edited for extra "" and extra , + date formated to yyyy-mm-dd \n')
        demo_function(file_in)
        shutil.move((in_dir + file_in),(original_dir + file_in))
    elif 'Genomic' in file_in:
        report_out.write('\nGenomic file:'+ file_in +'\n')
        report_out.write('date formated to yyyy-mm-dd \n')
        genom_function(file_in)
        shutil.move((in_dir + file_in),(original_dir + file_in))
    elif 'Test' in file_in:
        report_out.write('\nTest Day file:'+ file_in +'\n')
        note = testday_funtion(file_in)
        report_out.write(note)
        shutil.move((in_dir + file_in),(original_dir + file_in))
    elif 'Events' in file_in:
        report_out.write('\nEvents file:'+ file_in +'\n')
        report_out.write('not edited \n')
        events_function(file_in)
        shutil.move((in_dir + file_in),(original_dir + file_in))

report_out.close()