import shlex
import csv

features, salaries=[], []
headers = {}

def read_data_from_excel(file_path='/Users/shawnwinston/Desktop/ece_143/Train_rev1_salaries.csv'):
    '''
    reads raw data from an execl file and stores it in a dxn list
    where n is the number of data examples and d is the number
    of categories

    input: file name of where to read data from

    output:nxd list of extracted raw data

    '''

    assert isinstance(file_path, str)

    print "Reading data..."

    with open(file_path) as data:
        data_csv = csv.reader(data)

        header = data.readline().split(',')
        #these are the categories
        # ['Id', 'Title', 'FullDescription', 'LocationRaw', 'LocationNormalized', 'ContractType', 'ContractTime', 'Company', 'Category', 'SalaryRaw', 'SalaryNormalized', 'SourceName\r\n']

        i=0
        for name in header:
            headers[name] = i
            i+=1

        lines = [x for x in data_csv]

        for l in lines:
            features.append(l[0:9]+[l[11]])
            salaries.append(float(l[10]))
    print "done"

    #Can access each feature by name instead of number using below syntax
    #print features[0][categories['Id']]


def visualize_salary_data(x_values, y_values, data):
    '''
    Makes a chart and visualizes the salary data that is passed to it


    :param x_values:
    :param y_values:
    :param data:
    :return:
    '''
    pass

def salary_per_category(category_name):
    '''
    Gets average salary data and max salary data for desired catergory_name

    input: the category name you wish to see salary data for ex: location, company, job title, etc.

    output: average_catergory_salary - dictonary that stores the average salary data per category values
            max_catergory_salary - dictonary that stores the max salary data per category values
    '''

    from collections import defaultdict

    assert isinstance(category_name, str)
    assert category_name in headers

    category_salaries = defaultdict(list)
    average_category_salaries = {}
    max_category_salary = {}

    #create dictonary of lists that stores all the salary values for each category value
    for i in range(len(salaries)):
        category_salaries[features[i][headers[category_name]]].append(salaries[i])

    #Calculate average and max salary for each category value
    for key in category_salaries.keys():
        average_category_salaries[key] = sum(category_salaries[key])/len(category_salaries[key])
        max_category_salary[key] = max(category_salaries[key])

    #print average_category_salaries
    #print max_category_salary

    #all categories in dataset
    #print category_salaries.keys()

    return average_category_salaries, max_category_salary

def job_titles():
    pass

#average salary of all jobs
def average_salary():
    pass


####### MAIN LOOP ########

read_data_from_excel()
salary_per_category('Category')

#maybe find job Titles with the top salaries
header_truncated = ['Title', 'LocationNormalized', 'Company', 'Category']
#for name in header_truncated:
#    avg_salary_dict, max_salary_dict = salary_per_category(name)
#    visualize_salary_data() #visual average salary data
#    visualize_salary_data() #visualize max salary data

