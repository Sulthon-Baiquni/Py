terendah = 1
tertinggi = 50
print("Bilangan prima antara",terendah,"dan",tertinggi,":")
for num in range(terendah,tertinggi + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)