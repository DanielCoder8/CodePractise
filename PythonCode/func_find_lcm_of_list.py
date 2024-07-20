# func_find_lcm_of_list.py
def func_find_lcm_of_list(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return abs(a*b) // gcd(a, b)

    lcm_value = lst[0]
    for num in lst[1:]:
        lcm_value = lcm(lcm_value, num)

    return lcm_value

print(func_find_lcm_of_list([12, 15, 20]))
