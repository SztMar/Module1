class MovieLibrary:
    def __init__(self, title, publishment_year, type_of, num_of_plays):
        self.title = title
        self.publishment_year = publishment_year
        self.type_of = type_of
        self.num_of_plays = num_of_plays

        print(self.title,self.publishment_year,self.type_of,self.num_of_plays)

    def play(self,plays= 1):
        self.num_of_plays+= plays
    
    def __str__(self):
        return (f"{self.title} ({self.publishment_year})")

    def add(self):
        movie_list = [self.title,self.publishment_year,self.type_of,self.num_of_plays]
        General_list.append(movie_list)
                   
    
class SerialLibrary(MovieLibrary):
    def __init__(self, title, publishment_year, type_of, num_of_plays, episode_num, season_num):
        super().__init__(title, publishment_year, type_of, num_of_plays)
        self.episode_num = episode_num
        self.season_num = season_num

        print(self.title,self.publishment_year,self.type_of,self.episode_num,self.season_num,self.num_of_plays)

    def play(self,plays= 1):
        super().play
        self.num_of_plays+= plays
    
    def __str__(self):
        if self.episode_num <10:
            self.episode_num = "0" + str(self.episode_num)
        if self.season_num <10:
            self.season_num = "0" + str(self.season_num)

        return(f"{self.title} S{self.season_num} E{self.episode_num}")

    def add(self):
        serial_list = [self.title,self.publishment_year,self.type_of,self.episode_num, self.season_num,self.num_of_plays]
        General_list.append(serial_list)




def get_movie():
    movie_list = []
    for movie in General_list:
        if len(movie) < 5:
            movie_list.append(movie)
            movie_list = sorted(movie_list)
    print(movie_list)
def get_serial():
    serial_list = []
    for serial in General_list:
        if len(serial) > 4:
            serial_list.append(serial[0])
            serial_list = sorted(serial_list)
    print(serial_list)
                

def search():
    search_phrase = input("Please type the serial or movie name:")
    for search_object in General_list:
        if search_object[0] == search_phrase and len(search_object) > 4:
            print(search_object)
            exit(1)
        elif search_object[0] == search_phrase and len(search_object) < 5:
            print(search_object)
            exit(1)
        else:
            pass
    
General_list = []

movie_1 = MovieLibrary(title= "Shrek", publishment_year= 2005, type_of= "comedy",num_of_plays= 1)
movie_2 = MovieLibrary(title="Toy Story",publishment_year= 2002,type_of= "comedy",num_of_plays= 1)
serial_1 = SerialLibrary(title= "The Walking Dead",publishment_year= 2010,type_of= "action",episode_num= 10,season_num= 1,num_of_plays= 1)
serial_2 = SerialLibrary(title= "Game of Thrones",publishment_year= 2012,type_of= "fantasy",episode_num= 5,season_num= 11,num_of_plays= 1)

General_list.append(movie_1)
General_list.append(movie_2)

print(General_list)

movie_2.add()
movie_1.add()
serial_1.add()
serial_2.add()

get_movie()
get_serial()
search()





