import requests
import json
import math



schoolNumber = input("Please input your school ID: ")

page = requests.get(
                "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    schoolNumber)) 
 

professorBank = page.json()  # try to decode the response from JSON format
professorBank 

#schoolInfoInRMP = professorBank[u'professors'][0]
NumOfRating = professorBank[u'professors'][0][u'tNumRatings']
print("The number of rating for this university in RateMyProfessor.com " + str(NumOfRating))


schoolInfoInRMP = professorBank[u'professors'][0]
schoolInfoInRMP



professorBank = page.json()  # try to decode the response from JSON format
professorBank 
schoolName = professorBank[u'professors'][0]['institution_name']
overall_rating = professorBank[u'professors'][0]['overall_rating']
rating_class = professorBank[u'professors'][0]['rating_class']

print("The university name is "+ schoolName)
print("The overall rating is "+ overall_rating)
print("The rating for this class is " + str(rating_class))

if rating_class > 4:
    print("The rating is greater than 4, we recommend you take this class! ")
else:
    print("The rating is less than 4, we not recommend you take this class! ")


proFirstName = professorBank[u'professors'][0]['tFname']
proFirstName


