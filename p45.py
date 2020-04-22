def receive():#Function for inputting integers
    count=0
    while count==0:
        a=input('Enter the integer :')
        try:
            val=int(a)
            count+=1
            return val
        except ValueError:
            try:
                val=float(a)
                print('You entered a float. ')
            except ValueError:
                print('You did not enter a number. ')
def reverse(x):#Function for reversing integers
    digit_list=[]
    count=0
    while x!=0:
        digit_list.append(x%10)
        x=int(x/10)
        count+=1
    s=0
    for i in range(count):
        s+=digit_list[i]*pow(10,count-i-1)
    return s
while True:
    num=receive()
    num=reverse(num)
    print('Reverse of the number you entered is',num)

    
    
