_function = input("请输入你要求解的表达式=")
_start_point = float(input("输入你估算的根="))
x = _start_point
time = 0

def fun(x):
    global value
    value = eval(_function)

while not 0 == eval(_function):
    '''
    previous2_x = previous_x
    previous_x = x
    '''
    if(time>50):x = x-100

    fun(x+0.001)

    if(abs((value-eval(_function)))==0):
        x = -_start_point
    
    fun(x+0.001)
    x = x - (0.001*eval(_function)/(value-eval(_function)))
    print(eval(_function))
    time = time + 1
    
    


print("完成，迭代次数为",time,"次")

print("x=",x)



