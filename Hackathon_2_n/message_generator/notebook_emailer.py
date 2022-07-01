#Adam Surmiak, classroom management/emailer
import pandas as pd

Name = []
Sname = []
Curr_mark = []
Miss_task = []

def name_import():

    df = pd.read_excel('class.xlsx')
    t = df.columns.ravel()
    Name = df[t[0]].tolist()
    Name = Name[0:241]
    return Name

def sname_import():

    df = pd.read_excel('class.xlsx')
    t = df.columns.ravel()
    Sname = df[t[1]].tolist()
    Sname = Sname[0:241]
    return Sname

def curr_import():

    df = pd.read_excel('class.xlsx')
    t = df.columns.ravel()
    Curr_mark = df[t[2]].tolist()
    Curr_mark = Curr_mark[0:241]
    return Curr_mark

def email_replacement(Name, Sname, Curr_mark):

    for i in range(len(Name)):
        with open('email_text.txt', 'r') as file:
            filedata = file.read()
            filedata = filedata.replace('N1', Name[i])
            filedata = filedata.replace('S1', Sname[i])
            filedata = filedata.replace('CURRENT', str(Curr_mark[i]))
            filedata = filedata.replace('FUTURE', str(6 - Curr_mark[i]))
            filedata = filedata.replace('MISSING', str(6 - Curr_mark[i]))
            filedata = filedata.replace('DEADLINE', '27 06 2022')

        with open(f'file{i}.txt', 'a') as file:

            file.write(filedata)

    # for i in Name:
        with open('email_text.txt', 'r') as file:
            filedata = file.read()
    #     for k in Sname:
    #         temp = i
    #         stem = k
    #         filedata = filedata.replace('N1', temp)
    #         filedata = filedata.replace('S1', stem)


def main():
    Name = name_import()
    Sname = sname_import()
    Curr_mark = curr_import()
    #print(k)
    email_replacement(Name, Sname, Curr_mark)

    #print(k)



if __name__ == '__main__':
    main()
