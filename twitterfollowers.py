from bs4 import BeautifulSoup
import requests
from googlesearch import search

lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()

    lst.append(ele)  # adding the element

#print(lst)

followerlist = []

for college in lst:
    for url in search(college + "twitter", stop=1):
        #print(url)

     r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")

    f = soup.find('li', class_="ProfileNav-item--followers")
    title = f.find('a')['title']
    num_followers = int(title.split(' ')[0].replace(',', ''))
    #print(num_followers)
    followerlist.append(num_followers)
    #print(lst)
    #print(followerlist)

    for i in range(1, len(followerlist)):

        key = followerlist[i]
        key2 = lst[i]

        j = i - 1
        while j >= 0 and key < followerlist[j]:
            followerlist[j + 1] = followerlist[j]
            lst[j + 1] = lst[j]
            j -= 1
        followerlist[j + 1] = key
        lst[j + 1] = key2
    # print(lst)

    # print(followerlist)

rank = 1
k = n - 1
while k >= 0:
    print(str(rank) + ":  " + lst[k] + ": " + str(followerlist[k]))
    rank = rank + 1

    k = k - 1
