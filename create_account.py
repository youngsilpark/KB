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
    
    
if __name__=="__main__":
    
    account_list=[]


    for _ in range(2500):
        dash=random.choice([True,False])
        bank_first=random.choice([True,False])
        short=random.choice([True,False])
        
        account_list.append(create_account(dash,bank_first,short))
        
    print(account_list[:10])
     
            
            
                        
    

    
