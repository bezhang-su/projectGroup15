import requests
import json
import math



class RateMyProfScraper:
    
## University ID
        def __init__(self,):
        ## University ID
            self.UniversityId = schoolid
            self.professorlist = self.createprofessorlist()
            self.indexnumber = False

        def createprofessorlist(self):
# List object that include basic information on all Professors from the IDed University
            professorlistTemp = []
            professor_number = self.GetNumOfProfessors(self.UniversityId)
            num_of_pages = math.ceil(professor_number / 20)
            i = 1
            while (i <= num_of_pages):
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    self.UniversityId))
                temp_jsonpage = json.loads(page.content)
                temp_list = temp_jsonpage['professors']
                professorlistTemp.extend(temp_list)
                i += 1
            return professorlistTemp

        def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page
            temp_jsonpage = json.loads(page.content)
            professor_number = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            return professor_number

        def SearchProfessor(self, ProfessorName):
            self.indexnumber = self.GetProfessorIndex(ProfessorName)
            self.PrintProfessorInfo()
            return self.indexnumber

        def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def PrintProfessorInfo(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
            else:
                print(self.professorlist[self.indexnumber])

        def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
                return "error"
            else:
                print(self.professorlist[self.indexnumber][key])
                return self.professorlist[self.indexnumber][key]


