word=input("enter the word:")
vowels='aeiouAEIOU'
vowels_list=[]
for each in word:
    if each in vowels:
        vowels_list.append(each)
print("vowels is word are:",vowels_list)
