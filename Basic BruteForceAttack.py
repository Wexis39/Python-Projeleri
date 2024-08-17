numbers = '0123456789'
password = '13288'

def bruteForce():
    flag = True
    for x0 in numbers:
        for x1 in numbers:
            for x2 in numbers:
                for x3 in numbers:
                    for x4 in numbers:
                        psw = (x0+x1+x2+x3+x4)
                        print(psw)
                        if psw == password:
                            print('Correct password: {}'.format(psw))
                            print('BruteForce Attack Completed')
                            flag = False
                            break
                    if flag == False:
                        break
                if flag == False:
                    break
            if flag == False:
                break
        if flag == False:
            break
bruteForce()