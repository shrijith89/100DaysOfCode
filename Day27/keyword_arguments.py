def keyword_arg(**a):
    total_value = 0
    for i, j in a.items():
        total_value += j
        print(total_value)


keyword_arg(sum=9, multiply=100)
