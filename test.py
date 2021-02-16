school_class = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class2': '4б', 'scores': [2,4,5,3,2]},
{'school_class3': '4в', 'scores': [4,4,4,3,5]}
]
a = 0
b = 0 # класс  
 
for result in school_class:
    b=sum(result['scores'])/len(result['scores'])
    print(b)
    a+= sum(result['scores'])/len(result['scores'])
print(a/len(school_class))