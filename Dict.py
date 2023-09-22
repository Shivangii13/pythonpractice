#create a dictionary
myDict = dict()
print(myDict)

englishScore = {'raman':'56', 'rani':'87','ridhi':'78','raj':'43'}
print(englishScore)

#update dictionary

info = {'name':'Abhi', 'age':'25'}
print(info)
info['age'] = 24
print(info)

#add in dictionary
info['address'] = 'aligarh'
print(info)

#traverse through dictionary
info = {'name':'Abhi', 'age':'25' ,'address':'aligarh'}
def traversedict(dict):
    for key in dict:
      print(key , dict[key])
traversedict(info)

#search in dictionary
info = {'name':'Abhi', 'age':26 ,'address':'aligarh'}
def searchDict(dict , value):
    for key in dict:
        if key == value:
          return key,value
    return("the value does not exist")
print(searchDict(info , 26))

#delete from dictionary
info = {'name':'Abhi', 'age':'25' ,'address':'aligarh','qaulification': 'btech'}
del info['age']
print(info)

removed_element = info.pop('name')
print(removed_element)
print(info)

