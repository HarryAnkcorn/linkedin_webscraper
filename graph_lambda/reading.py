import csv
from datetime import date
import ast
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def make_list_from_csv(file_name):
    lst = []
    tmp_file = f'/tmp/{file_name}'
    with open(tmp_file, 'r') as csvfile: # make this /tmp/ in lambda
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            lst.append(row)
    return lst

def make_list_from_txt(file_name):
    lst = []
    tmp_file = f'/tmp/{file_name}'
    f = open(tmp_file, 'r', encoding="utf-8")
    for line in f:
        if line != '':
            if line.isupper(): 
                lst.append(line.strip())
    f.close()
    return lst

def tally_skills(data, skills):
    skill_results = defaultdict(list)
    amount_of_jobs = []
    dates = []
    for row in data:
        date_lst = row[0].split('-')
        dates.append(date(int(date_lst[0]),int(date_lst[1]),int(date_lst[2])))
        
        amount_of_jobs.append(int(row[1]))

        day_tally = row[3].strip('"Counter()')
        day_tally = ast.literal_eval(day_tally)
        for word in skills:
            if word not in day_tally:
                skill_results[word].append(0)
            else:
                skill_results[word].append(day_tally[word])
    return amount_of_jobs, dates, skill_results

def make_graph(dates, skill_results, graph_file_name):
    plt.figure(figsize=(9, 4))
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)
    plt.xlabel('Date')

    plt.ylabel('Results')
    for word in skill_results:
        plt.plot(dates, skill_results[word], label = word)       
    plt.legend(skill_results.keys(), loc='bottom left')

    plt.grid()
    plt.savefig(f'/tmp/{graph_file_name}', bbox_inches = 'tight')