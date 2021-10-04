import random
"""
asd = {'cap_let': ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
        'low_let': ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        'symbols': ['!','@','#','$','%','^','&','*','(',')','_','+',
            '-','=','/',',','.',':',';'],
        'numbers': ['1','2','3','4','5','6','7','8','9','0']
        }
"""
cap_let = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
low_let = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+',
            '-','=','/',',','.',':',';']
numbers = ['1','2','3','4','5','6','7','8','9','0']


def strong_pass():
    new_pass = []
    for c in range(2):
        rand_c = random.choice(cap_let)
        new_pass.append(rand_c)
    for l in range(5):
        rand_l = random.choice(low_let)
        new_pass.append(rand_l)
    for s in range(2): 
        rand_s = random.choice(symbols)
        new_pass.append(rand_s)
    for n in range(3):
        rand_n = random.choice(numbers)
        new_pass.append(rand_n)

    random.shuffle(new_pass)
    return ''.join(new_pass)
    
def weak_pass():
    new_pass = []
    for w in range(4):
        rand_l = random.choice(low_let)
        new_pass.append(rand_l)
    for s in range(1):
        rand_n = random.choice(numbers)
        new_pass.append(rand_n)

    random.shuffle(new_pass)
    return ''.join(new_pass)

pass_power = input("How strong password you want. strong/weak: ")


if pass_power == 'strong':
    print(f"Your strong password: {strong_pass()}")
elif pass_power == 'weak':
    print(f"Your weak password: {weak_pass()}")