#!/usr/bin/python3

movies= [{"scifi":{"best":"matrix","worst":"matrix reloaded"}},{"comedy":{"best":"spaceballs","worst":"click"}},{"horror":{"best":"conjuring","worst":"glass house"}},]

genre = input("Please enter movie genre: ")
choice = input("Please enter best/worst of this genre: ")

x = 0
for myTest in movies:
    if genre in myTest.keys():
        print(f"The {choice} of {genre} film is: {myTest[genre][choice]}")
   # print (myTest, movies[myTest])

   # x = x + 1

#print(f"The {choice} of {genre} film is: {test}")
