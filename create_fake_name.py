# 이름 자동 생성기 


import pickle
from faker import Faker
fake = Faker('ko-KR')
fake.name()


def has_coda(word):
    return (ord(word[-1])-44032)%28==0
  
 if __name__=="__main__":


    name_list_1=[] #받침 o
    name_list_2=[] #받침 x
    for _ in range(1500000):
        
        name=fake.name()
        
        if has_coda(name):
            name_list_2.append(name)
        else:
            name_list_1.append(name)
        
        
    #with open("name_list_coda.list","wb") as f:
    #    pickle.dump(name_list_1,f)
        

    #with open("name_list_nocoda.list","wb") as f:
    #    pickle.dump(name_list_2,f)
