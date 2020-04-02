from bs4 import BeautifulSoup as soup
import re
import requests as req

print('Welcome to the movie suggestion program! \n')
print("What genre of movie would you like to watch?\nPress the number key alongside the genre to confirm your selection.\n")

#Taking input from user for the genre of the movie they would be interested to watch
x = int(input(" 1. Action and adventure \n 2. Animation \n 3. Comedy\n 4. Documentaries\n 5. Drama\n 6. Horror\n 7. Roamnce\n 8. Science Fiction and Fantasy\n 9. Kids\n\n\n\n Press the number key now\n\n\n"))

#defining thee function used for giving recommendations

#I have used rottentomatoes links to generate recommendations
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

    s1 = soup (data , 'lxml')

# Now , retrieving the tiltle and rating for the movies

    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title


# Driver function

if __name__ == '__main__':

    a = main(x)

# Here , x is the genre of the movie that the user opted for.
if( x == 1 or x ==2 or x==3 ):

    for i in a:

        # Splitting each line of the
        # IMDb data to scrape movies
        tmp = str(i).split('>;')

        if(len(tmp) == 3):
            print(tmp[1][:-3])

            if(count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if(len(tmp) == 3):
                print(tmp[1][:-3])

            if(count > 11):
                break
            count+=1
