def my_function(b, *a):
    fun_sum = b
    print(fun_sum)
    for i in a:
        fun_sum += i
    return fun_sum


numbers = [2, 4, 5, 100, 7]
print(my_function(1, *numbers))
