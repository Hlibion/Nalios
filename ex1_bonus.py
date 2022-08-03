def fizz_buzz(rules : dict):
    for i in range(1,101):
        answer = ''
        for k,v in rules.items():
            if i%int(k) == 0:
                answer += v
        if answer !='' : 
            print(answer)
        else : print (i)