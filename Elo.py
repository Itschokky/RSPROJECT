"""main"""
def main():
    """main"""
    vra = int(input())
    vrb = int(input())
    team = input()
    solea = 1/(1+10**((vrb-vra)/400))
    soleb = 1/(1+10**((vra-vrb)/400))
    if team == 'A':
        print('%.2f'%solea)
    else:
        print('%.2f'%soleb)
main()
