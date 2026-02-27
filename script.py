#  اعداد سه رقمی
# صفر نداشته باشد
# حداقل دو رقم شبیه هم باشند
# عدد فرد باشد
for i in range(100,1000):
    s = str(i)
    no_zero='0' not in s
    is_odd=i % 2 ==1
    two_same=(s[0]==s[1]) or (s[0]==s[2]) or (s[1]==s[2])

    if no_zero and is_odd and two_same:
        print(i)