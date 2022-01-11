def power(num, pow):
    result = 1
    for x in range(pow):
        result = result * num
    return result


print(power(5,2))