import os
import copy
import arrow
import datetime
from bioblog.settings import STATICFILES_DIRS

class idEditor():
    def __init__(self):
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/idlist.txt'), 'r', encoding="utf-8") as f:
            content = f.readlines()
        self.id_list = {}
        for line in content:
            line = line.strip('\n').split('<&>')
            self.id_list[line[0]] = {
                "paper_id": line[0],
                "title": line[1],
                "author": line[2],
                "stamp": line[3],
                "date": line[4],
                "abstract": line[5],
                "image": line[6],
                "good": line[7],
            }
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/self.txt'), 'r', encoding="utf-8") as f:
            information = f.read().split("|")
        self.im_list = {
            "author":information[0],
            "password":information[1],
            "detail":information[2],
            "paper":information[3],
            "good":information[4],
            "like":information[5].split('&')
        }

    def search(self, artical_id):
        if artical_id in self.id_list:
            return self.id_list[artical_id]
        else:
            return 'Could not find articals like this'
    
    def get_idList(self):
        return self.id_list
    
    def get_imList(self):
        return self.im_list
    
    def write(self, title, author, stamp, date, abstract, image, content):
        paper_id = str(int(max(self.id_list)) + 1)
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/uploads/'+paper_id+'.md'), 'w', encoding="utf-8") as f:
            f.write(content)
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/idlist.txt'), 'a', encoding="utf-8") as f:
            f.write("<&>".join([paper_id, title, author, stamp, date, abstract, image, '0'])+'\n')
    
    def edit(self, paper_id, good):
        new_idList = self.id_list
        new_idList[paper_id]["good"] = str(int(new_idList[paper_id]["good"]) + int(good))
        content = []
        for key in new_idList:
            line = new_idList[key]
            line = line["paper_id"] + "<&>" + line["title"] + "<&>" + line["author"] + "<&>" + line["stamp"] + "<&>" + line["date"] + "<&>" + line["abstract"] + "<&>" + line["image"] + "<&>" + line["good"] + "\n"
            content.append(line)
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/idlist.txt'), 'w', encoding="utf-8") as f:
            f.write("".join(content))

    def delete(self, paper_id):
        new_idList = self.id_list
        good = new_idList[paper_id]["good"]
        del new_idList[paper_id]
        content = []
        for key in new_idList:
            line = new_idList[key]
            line = line["paper_id"] + "<&>" + line["title"] + "<&>" + line["author"] + "<&>" + line["stamp"] + "<&>" + line["date"] + "<&>" + line["abstract"] + "<&>" + line["image"] + "<&>" + line["good"] + "\n"
            content.append(line)
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/idlist.txt'), 'w', encoding="utf-8") as f:
            f.write("".join(content))
        return good

    def im_write(self, author=None, detail=None, paper=None, good=None, like=None):
        new_information = self.im_list
        if author != None:
            new_information["author"] = author
        if detail != None:
            new_information["detail"] = detail
        if paper != None:
            new_information["paper"] =  str(int(new_information["paper"]) + paper)
        if good != None:
            new_information["good"] = str(int(new_information["good"]) + good)
        if like != None:
            new_information["like"] = like
        else:
            new_information["like"] = "&".join(new_information["like"])
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/self/self.txt'), 'w', encoding="utf-8") as f:
            f.write("|".join([new_information["author"], new_information["password"], new_information["detail"], new_information["paper"], new_information["good"], new_information["like"]]))

def home_loading():
    id_list = idEditor().get_idList()
    content = {"id_list":[], "id_data":[]}
    for i in range(int(max(id_list)), 0, -1):
        if len(content["id_list"]) <=10 and str(i) in id_list:
            paper_id = str(i)
            title = id_list[paper_id]["title"]
            author = id_list[paper_id]["author"]
            stamp = id_list[paper_id]["stamp"]
            date = id_list[paper_id]["date"]
            abstract = id_list[paper_id]["abstract"]
            image = id_list[paper_id]["image"]
            content["id_list"].append(paper_id)
            content["id_data"].append(
                {"title":title, "author":author, "abstract":abstract, "stamp":stamp, "date":date, "image":image}
            )
        else:
            pass
    return content

def manage_loading():
    id_list = idEditor().get_idList()
    content = {"id_list":[], "id_data":[]}
    for i in range(int(max(id_list)), 0, -1):
        if str(i) in id_list:
            paper_id = str(i)
            title = id_list[paper_id]["title"]
            author = id_list[paper_id]["author"]
            stamp = id_list[paper_id]["stamp"]
            date = id_list[paper_id]["date"]
            abstract = id_list[paper_id]["abstract"]
            image = id_list[paper_id]["image"]
            good = id_list[paper_id]["good"]
            content["id_list"].append(paper_id)
            content["id_data"].append(
                {"title":title, "author":author, "abstract":abstract, "stamp":stamp, "date":date, "image":image, "good":good}
            )
        else:
            pass
    return content

def self_information():
    content = idEditor().get_imList()
    for i in range(len(content["like"])):
        paper_id = content["like"][i]
        paper_data = idEditor().search(paper_id)
        content["like"][i] = {
            "paper_id":paper_id,
            "title":paper_data['title'],
            "image":paper_data['image'],
            "good":paper_data['good']
        }
    return content

def search_paper(key):
    keys = key.split(' ')
    result_id = []
    id_list = idEditor().get_idList()
    for key in id_list:
        test = 0
        for word in keys:
            if word in id_list[key]["title"]:
                test += 1
        if test == len(keys):
            result_id.append(key)
    content = {"id_list":[], "id_data":[]}
    for paper_id in result_id:
        title = id_list[paper_id]["title"]
        author = id_list[paper_id]["author"]
        stamp = id_list[paper_id]["stamp"]
        date = id_list[paper_id]["date"]
        abstract = id_list[paper_id]["abstract"]
        image = id_list[paper_id]["image"]
        content["id_list"].append(paper_id)
        content["id_data"].append(
            {"title":title, "author":author, "abstract":abstract, "stamp":stamp, "date":date, "image":image}
        )
    return content

def isLeapYear(years):
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):
        days_sum = 366
        return days_sum
    else:
        days_sum = 365
        return days_sum
 
 
def getAllDayPerYear(years):
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    return all_date_list

def getYearList():
    now_year = getAllDayPerYear(str(datetime.datetime.now().year))
    past_year = getAllDayPerYear(str(int(str(datetime.datetime.now().year))-1))
    year_list = past_year + now_year
    id_list = idEditor().get_idList()
    now_day = datetime.datetime.now().strftime('%Y-%m-%d')
    date_list = year_list[year_list.index(now_day)-359:year_list.index(now_day)+1]
    result_list = copy.deepcopy(date_list)
    color_list = ['#ebedf0','#ff9789','#ff5842','#e31a00','#6c0d00']
    my_date = []
    for key in id_list:
        my_date.append(id_list[key]["date"].replace('.','-'))
    for i in range(len(result_list)):
        number = my_date.count(result_list[i])
        if number >= 5:
            result_list[i] = color_list[-1]
        else:
            result_list[i] = color_list[number]
    return date_list, result_list