import random
from datetime import date


class Films:
    def __init__(self, title, year, genre, plays):
        self.title = title # tytuł
        self.year = year #rok wydania
        self.genre = genre #gatunek
        self.plays = plays #Liczba odtworzeń


        #Variables
        self._no_plays = 0


    def __str__(self):
        return f'{self.title}, ({self.year})'    
    def __repr__(self):
        return f" title = {self.title} year = {self.year}"

    @property
    def current_no_plays(self):
        return self._no_plays

    @current_no_plays.setter
    def current_no_plays(self, value):
        self._no_plays = value


    def next_play(self, step =1): #Zwiększenie liczby odtworzeń o "step"
        self.current_no_plays += step
        print(f'Liczba odtworzeń {self.title} zwiększyła się o {step}')  
        
       

film1 = Films(title = "Twierdza", year ="1996", genre ="Sensacyjny", plays = 0)
film2 = Films(title = "Gladiator", year = "2000", genre = "Akcja", plays = 0)
film3 = Films(title = "Helikopter w ogniu", year = "2001", genre = "Wojenny", plays = 0)
film4 = Films(title = "Łzy słońca", year = "2003", genre = "Fabularny", plays = 0)
film5 = Films(title = "Bracia Kliczko", year = "2011", genre = "Dokument", plays = 0)
film_list = [film1, film2, film3, film4, film5]


class Series(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
        #Variables
        self.episode = format(episode,'02d')  #zapis w forime dwucyfrowej 01 etc
        self.season = format(season, '02d')
    def __str__(self):
        return f'{self.title}, S{self.season}E{self.episode}'

series1 = Series(title = "Gra o Tron", year = "2011 - 2019", genre = "Fantasy",plays = 0, episode = 0, season= 0)
series2 = Series(title ="JNarcos", year = "2015 - 2017", genre="Dramat",plays = 0, episode = 0, season= 0)
series3 = Series(title = "Dom z papieru", year = "2013 - 2018", genre = "Dramat/Polityczny",plays = 0, episode = 0, season= 0)
series4 = Series(title = "Dexter", year = "2006 - 2013", genre = "Kryminal",plays = 0, episode = 0, season= 0)
series5 = Series(title = "TWataha", year = "2014 - 2020 " , genre = "Sensacyjny",plays = 0, episode = 0, season= 0)
series_list = [series1, series2, series3, series4, series5]




Library_list = film_list + series_list 
class Library: #Klasa dla filmów i seriali
    
    def __init__(self):
        self._database = []

    @property
    def database(self):
        return self._database
    
    def add(self, film_or_series):
        self._database.append(film_or_series)

        

    def get_movies(self):
        by_title = sorted(film_list, key=lambda film: film.title) #sortowanie
        print(by_title)
        


    def get_series(self):
        by_title = sorted(series_list, key=lambda series: series.title) #sortowanie
        print(by_title)

    def search(self,title):
        for item in self._database:
            if item.title == title:
                return item


    def generate_views():
        item  = random.choice(Library_list) #Losowy film/serial
        item.plays = random.randint(1,100) #Losowa liczba odtworzeń
        return item.plays
        

    def generate_views_x10():
        for i in range(10):
            Library.generate_views()


    def top_titles(titles_number, content_type='all'):
        if content_type == 'Films':
            films = []
            for item in film_list:
                if isinstance(item, Series):
                    continue
                films.append(item)
            top_titles = sorted(films,key=lambda films: films.plays)
            return top_titles[:titles_number]
        elif content_type == 'Series':
            series = []
            for item in series_list:
                if isinstance(item, Series):
                    series.append(item)
            top_titles = sorted(series, key=lambda series: series.plays)
            return top_titles[:titles_number]
        else:
            top_titles = sorted(film_list, key=lambda titles: titles.plays, reverse = True)
        return top_titles[:titles_number]


if __name__ == '__main__':
    print("Biblioteka filmów i seriali")
    Library.generate_views()
    print(f'Najbardziej popularne filmy i seriale na dziś to {date.today(): %d.%m.%y}: ')
    for title in Library.top_titles(3):
        print(title)

#Kompletna bibliotka "library" dla _database 
library = Library()
library.add(film1)
library.add(film2)
library.add(film3)
library.add(film4)
library.add(film5)
library.add(series1)  
library.add(series2)
library.add(series3)
library.add(series4)
library.add(series5)


