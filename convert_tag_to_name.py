def convert_tag_to_name(sentence:str,target="#@이름#",name1_list=None,name2_list=None):
    
    flag=True
    position1=["아","이","은"] #받침 o
    position2=["야","가","는"] #받침 x
    
    
    
    while flag:
        
        start_index=sentence.find(target)
        end_index=start_index+5
        
        if start_index==-1:
            flag=False
            
        else:
            if sentence[end_index] in position1:
                
                name=random.choice(name1_list)
                last_name=random.choice([True,False])
                
                if not last_name:
                    name=name[1:]
                
                print(sentence[end_index])
                if start_index == 0:
                    name + sentence[end_index:]
                else:
                    sentence=sentence[:start_index] + name + sentence[end_index:]
                    
                    
            elif sentence[end_index] in position2:
                
                name=random.choice(name2_list)
                last_name=random.choice([True,False])
                
                if not last_name:
                    name=name[1:]
                
                print(sentence[end_index])
                if start_index == 0:
                    sentence=name + sentence[end_index:]
                else:
                    sentence=sentence[:start_index] + name + sentence[end_index:]
                    
            else:
                
                name=random.choice(name1_list+name2_list)

                last_name=random.choice([True,False])
                
                if not last_name:
                    name=name[1:]
                
                print(sentence[end_index])
                sentence=sentence[:start_index] + name + sentence[end_index:]
            
                
                
    return sentence
        
