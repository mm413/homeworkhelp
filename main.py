#main.py
import csv


def main():
    movies = []
    ratings = []
    render(movies, ratings)
    #dict = makeDict(movies, ratings) #movie ID is key, value is a list of all reviews for that movie.
    getAverages(movies, ratings)
    part1(movies, ratings)
    print("======================================================")
    part2(movies, ratings)
    part3()


def part1(movies, ratings):
    top10 = []
    print("Calculating part 1...")
    for rating in ratings:
        if len(top10) < 10:
            for movie in movies:
                if movie not in top10:
                    if movie.getID() == rating.getMovieID():
                        top10.append(movie)
                        top10.sort(key=lambda x: x.getAverage(), reverse=True)
                        break

        else:
            for movie in movies:
                if movie not in top10:
                    if movie.getID() == rating.getMovieID():
                        if top10[9].getAverage() < movie.getAverage():
                            top10.pop()
                            top10.append(movie)
                            top10.sort(key=lambda x: x.getAverage(), reverse=True)
                            break
    print("Top 10 movies by rating:")
    print("ID ---- TITLE --------- AVERAGE RATING")
    for movie in top10:
        print("| ", movie.getID(), " | ", movie.getName(), " | ", movie.printAverage(), " |")




def part2(movies, ratings):
    top10 = []
    print("Calculating part 2...")
    for rating in ratings:
        if len(top10) < 10:
            for movie in movies:
                if movie not in top10:
                    if movie.getID() == rating.getMovieID():
                        top10.append(movie)
                        top10.sort(key=lambda x: x.getAverage())
                        break

        else:
            for movie in movies:
                if movie not in top10:
                    if movie.getID() == rating.getMovieID():
                        if top10[0].getAverage() > movie.getAverage():
                            top10.pop()
                            top10.append(movie)
                            top10.sort(key=lambda x: x.getAverage())
                            break
    print("Bottom 10 movies by rating:")
    print("ID ---- TITLE --------- AVERAGE RATING")
    for movie in top10:
        print("| ", movie.getID(), " | ", movie.getName(), " | ", movie.printAverage(), " |")


def part3():
    return
    #find out all genres and add them to a list that doesn't allow duplications.
    #Then use a two dimensional list (a list of lists) to house each genre, and each movie of that genre inside of it.
    #find average of each genre through a nested loop


def render(movies, reviews):
    print("Extracting CSV files into objects....")
    reader = csv.reader(open('movies.csv', newline=''))
    count = 0
    for row in reader:
        if count > 0:
            movies.append(Movie(row[0], row[1], row[2]))
        count += 1

    reader = csv.reader(open('ratingsTEST.csv', newline=''))
    #count = 0
    for row in reader:
        if count > 0:
            reviews.append(Rating(row[0], row[1], row[2], row[3]))
        count += 1
    print("Done!")


def makeDict(movies, ratings):
    dict = {}  #key = movieID , value = list of associated reviews.
    for movie in movies:
        dict[movie] = []
    for rating in ratings:
        for key in dict.keys():
            if str(rating.getMovieID()) == (str(key)):
                currentList = dict[key]
                currentList.append(rating)
                dict[key] = currentList
    return dict


def getAverages(movies, ratings):
    print("Getting average movie ratings...")
    for rating in ratings:
        for movie in movies:
            if rating.getMovieID() == movie.getID():
                movie.updateAverage(rating.getRating())
    print("Done!")



#CLASSES BELOW:

class Movie:
    def __init__(self, id, name, genre):
        self.timesCalled = 0
        self.averageRating = 0
        self.id = id
        self.name = name
        self.genre = genre

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def updateAverage(self, rating):
        if self.timesCalled == 0:
            self.averageRating = float(rating)
            self.timesCalled = 1
            return
        self.timesCalled += 1
        self.averageRating = ((int(self.timesCalled)-1) * float(self.averageRating) * float(rating)) / int(self.timesCalled)
        return self.averageRating

    def getAverage(self):
        return self.averageRating

    def printAverage(self):
        return str(self.averageRating)

    def __repr__(self):
        return str(self.id) #repr is ID, since it is the key of the dictionary.



class Rating:
    def __init__(self, userid, movieid, rating, timestamp):
        self.userID = userid
        self.movieID = movieid
        self.rating = rating
        self.timestamp = timestamp

    def getUserID(self):
        return self.userID

    def getMovieID(self):
        return self.movieID

    def getRating(self):
        return self.rating

    def getTimestamp(self):
        return self.timestamp

    def __repr__(self):
        return "USERID = " + str(self.userID) + " | " "MOVIEID = " + str(self.movieID)
main()


