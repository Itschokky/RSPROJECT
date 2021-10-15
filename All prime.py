"""prime chcek"""
def main():
    """prime chcek"""
    num = int(input())
    num_of_prime = []
    for i in range(1, num+1):
        mylist = []
        for j in range(1, i+1):
            if i%j == 0:
                mylist.append(j)
        if len(mylist) == 2:
            num_of_prime.append(mylist)
    print(len(num_of_prime))
main()
