# 6-2-6
# (국민 계조번호),(국민은행,계좌번호),(계좌번호, 국민),(계좌번호,국민은행)


def create_account(dash=True,bank_first=True,short=True):
      
    ''''
    dash : 계좌에 "-" 추가
    bank_first : 은행명이 제일 앞에, False시 제일 뒤에
    short: True시 "꾹민" False 시 "국민은행"
    '''
    account = ""
    
    
    if dash:
        while len(account)<14:
            account+=str(random.randint(0,9))
            
        account=account[:6]+"-"+account[6:8]+"-"+account[8:]
        
    else:
        while len(account)<14:
            account+=str(random.randint(0,9))
            
    
    if short:
        if bank_first:
            account = "국민 " + account
        else:
            account = account + " 국민"
            
    else:
        if bank_first:
            account ="국민은행 "  +account
            
        else:
            account = account + " 국민은행"
      
      
    return account      


def convert_tag_to_name(sentence:str,target="#@이름#",name1_list=None,name2_list=None):
    
    ## 이름 자동생성기 찾아야 함
    
    
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


if __name__=="__main__":
    
    account_list=[]


    for _ in range(2500):
        dash=random.choice([True,False])
        bank_first=random.choice([True,False])
        short=random.choice([True,False])
        
        account_list.append(create_account(dash,bank_first,short))
        
    print(account_list[:10])
    
    
    
    with open("name_list_coda.list","rb") as f:
        name1_list=pickle.load(f)
        
        
    with open("name_list_nocoda.list","rb") as f:
        name2_list=pickle.load(f)
        
        
    sen='안녕하세요 만나서 반갑습니다. #@이름#은 얼른 퇴근하자 #@이름#가'
    print(convert_tag_to_name(sen,name1_list=name1_list,name2_list=name2_list))
     
        
