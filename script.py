from bs4 import BeautifulSoup as soup
import re
import requests as req

print('Welcome to the movie suggestion program! \n')
print("What genre of movie would you like to watch?\nPress the number key alongside the genre to confirm your selection.\n")

#Taking input from user for the genre of the movie they would be interested to watch
x = int(input(" 1. Action and adventure \n 2. Animation \n 3. Comedy\n 4. Documentaries\n 5. Drama\n 6. Horror\n 7. Roamnce\n 8. Science Fiction and Fantasy\n 9. Kids\n\n\n\n Press the number key now\n\n\n"))

#defining thee function used for giving recommendations

#I have used rottentomatoes links to generate recommendations
#using the same , 

def main (x):
    if (x==1):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'

    if (x==2):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/'

    if (x == 3):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/'

    if (x==4):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/'

    if (x==5):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/'

    if (x == 6):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/'

    if (x == 7):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/'

    if (x == 8):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/'

    if (x==9):
        onurl = 'https://www.rottentomatoes.com/top/bestofrt/top_100_kids__family_movies/'

# Using request to get data on webpage to our program

    response = req.get(onurl)
    data = response.text

# Parsng the data using BeautifulSoup

    s = soup (data , 'html.parser')
# Now , retrieving the tiltle and rating for the movies

    for line in s:

    #title = soup.find_all("a", attrs = {"href"} , class_= 'unstyled articleLink').text
        r = ()
        r= s.find('td', class_="unstyled articleLink")
            #r = []
        #i == 0
        for i in r:
            print(i)
