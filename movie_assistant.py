'''
# -----------------------------------------------------------------------------------------------------------
# Pre-requisites
# -----------------------------------------------------------------------------------------------------------
#%% Configure Host environment
#@title # Run this cell before you start coding { display-mode: "form" }
#@markdown Don’t worry about what’s in this collapsed cell, you’re not expected to understand the code inside
#!pip install movie-rec-marking-aicore --upgrade --quiet
#!wget https://aicore-files.s3.amazonaws.com/Movie-Recommendation/movies-head.json --quiet
#!pip install powershell_kernel python -m powershell_kernel.install

'''
#%% Import Libraries

import json
import subprocess # to load powershell framework
p = subprocess.Popen(["powershell","/home/vmuser/aicore/movie_assistant/framework/utility/helloworld.ps1"], stdout=subprocess.PIPE) 
# load framework (powershell) related objects
#p = subprocess.Popen(["dir","/"], stdout=subprocess.PIPE) 
p_out, p_err = p.communicate()
print(p_out) # to access the result

#%% Load movies
def load_test_movies():
  with open('/home/vmuser/aicore/movie_assistant/movies-head.json', 'r') as f:
    movies = json.load(f)
    return movies

def load_movies_data():
  with open('/home/vmuser/aicore/movie_assistant/movies.json', 'r') as f:
    movies = json.load(f)
    return movies

movies = load_movies_data()
#%% ------------------------------------------------------------------------------------------------------------
# Milestone 1: Understand the Data
# ------------------------------------------------------------------------------------------------------------
 #%% Task 1: Count the number of movies in the list
 #%% Task 2: Select the first movie
first_movie = movies[0]
data_type = type(first_movie)
# print out the solution
solution = {'data_type':data_type,'first_movie': first_movie["title"]}
#print('data_type: {data_type}, fist_movie: {first_movie}'.format(**solution))

 #%% Task 3: Explore the first movie
last_10_chars_link = first_movie["link"][-10:]
#%% ------------------------------------------------------------------------------------------------------------
# Milestone 2: Explore the Data
# ------------------------------------------------------------------------------------------------------------
#%% Task 1: Display all the movies 'titles"
#print(movies[0]["title"])
titles = []

def print_every_movie_title():
    titles = []
    for i in range(len(movies)):
        titles.append(f"{movies[i]['title']}")
    for index, item in enumerate(titles):
      #return f"Title {index+1} :", f"{item}"
      print(f"Title {index+1} :", f"{item}")

      
#print_every_movie_title()



#%% Task 2: What is the length of a given movie's description?
def get_movie_description_length(one_movie):
  # iterate through the given movie to find the description 
  for key, value in one_movie.items():
    match key:
      case "description":
        # when found convert count its legth and return it as integer 
        description = str(value) 
        formated = int(len(description))       
        return formated
        
#%% Task 3:  What is the avarage length of
def get_avg_movie_description_length():
  """
  returns the average number of characters in each movie description, 
  averaged across the whole dataset.

  Returns:
      _int_: avarage description length acrross whole data set.
  """
  import statistics as st #statistics package
  movie_description_length = [] 
  # iteratate through movies dict
  for i in range(len(movies)):
    # add every description legth to the list
    movie_description_length.append(get_movie_description_length(movies[i]))
    # calculate the avg of all description lengths
  avg = st.mean(movie_description_length)
  return (round(avg,1))

#%% Task 4: What is the maximum length of any movie name?
def get_max_movie_name_length():
    all_movie_title_length = []
    # iteratate through movies dict and gather dataset
    for i in range(len(movies)):
      single_movie = movies[i]
      for key, value in single_movie.items():
        movie_index = i+1
        single_movie_items = key
        single_movie_content = value
        length = len(str(single_movie_content))
        # write dataset to a new dictionary
        retrieved_dataset = {"Movies_Index" : movie_index,"Movies_Item":single_movie_items, "Item_Content":single_movie_content, "Item_Length":int(length)}
        # filter the new dictionary for "Title" items only
        match key:
          case "title":
            # assemble filtered datasets and collect into a new dictionary
            title_index = '{Movies_Index}'.format(**retrieved_dataset)
            title_name = '{Item_Content}'.format(**retrieved_dataset)
            title_length = '{Item_Length}'.format(**retrieved_dataset)
            filtered_dataset={"Title_Index" : title_index,"Movie_Title":title_name, "Title_Length":int(title_length)}
            # Loop through the filtered dataset generate a list containing all lengths   
            all_movie_title_length.append(filtered_dataset.get("Title_Length"))
            max_length = max(all_movie_title_length)
            # if its the longest movie save into the result dictionay
            if length == max_length:
              longest_name=filtered_dataset.get("Movie_Title")
              longest_length=filtered_dataset.get("Title_Length")
              #print(longest_length)
              longest_movie={"Max_Name" : longest_name, "Max_Length: " : int(longest_length)}
              
              return longest_length,longest_name
              #print('{Max_Length}'.format(**longest_movie))
              #print('{Max_Name}'.format(**longest_movie))
#%%------------------------------------------------------------------------------------------
# Milestone 3:
# ------------------------------------------------------------------------------------------
#%% Task 1: load movies.json
#%%Task 2: What are the unique genres?
def get_unique_genres():
    all_genre = []
    # iteratate through movies dict to access single movies
    for i in range(len(movies)):
      single_movie = movies[i]
      # going through a single movie to collect the genres 
      for key, value in single_movie.items():
        match key:
          case "genre":
            all_genre.append(value)
            unique_genres = set(all_genre)
            
    return unique_genres


#%% Task 3: filter movies by genre.

def get_movies_in_genre(arg1):
  # check the input is a string
  genre = str(arg1)
  for movie in movies:
    # filter movie for their genre
    filtered_movies = filter(lambda movie : genre in movie["genre"], movies)
    return list(filtered_movies)   

#get_movies_in_genre("Action")

#%%# -----------------------------------------------------------------------------------------
# Milestone 4:
# -----------------------------------------------------------------------------------------
#
#%% Task 1: Ask the user what genre they are interested in
'''
def get_user_genre_choice():
  print("Select a genre from the following set:")
  print(get_unique_genres())
  genre_choice = input("Type a genre then hit enter... \n")
  return genre_choice
#get_user_genre_choice()
'''

#%% Task 2: Show the movies in the selected genre
def show_selected_genre_titles():
  genre_choice = get_user_genre_choice()
  genre_movies = get_movies_in_genre(genre_choice)
  titles = []
  for i in range(len(genre_movies)):
      titles.append(f"{genre_movies[i]['title']}")
  for index, item in enumerate(titles):
    #return f"Title {index+1} :", f"{item}"
    print(f"Title {index+1} :", f"{item}")
    return genre_movies
    

#%% Task 3: Select and display the details of a movie
def get_movie_by_index():
  genre_movies = show_selected_genre_titles()
  print("Please select a movie tile from the list.")
  movie_choice = input()
  print(int(movie_choice))
  return genre_choice

#%%
# %% Task 4: Select and display the details of a movie
def get_movie_by_index():
  genre_movies = show_selected_genre_titles()
  print("")
  selected_movie_index = input("Type the movie number and hit enter...\n")
  selected_movie_index = int(selected_movie_index)
  for key, value in genre_movies[selected_movie_index-1].items():
    print('{}: {}'.format(key,value))

# %%-------------------------------------------------------------------------------------- 
# Milestone 5: Error Handling
# ---------------------------------------------------------------------------------------
#
#%% Task 1: redefine the user's genre choice to validate input
def get_user_genre_choice():
    genres = get_unique_genres()
    print("Select a genre from the following set:")
    print(get_unique_genres())
    try:  
      genre_choice = input("Type a genre then hit enter...\n")
      while genre_choice not in genres:           
          raise ValueError        
    except ValueError: # invalid input
        print(f'{genre_choice} is not a valid genre.\nPlease try again..')
        genre_choice = input("Type a genre then hit enter...\n")
    return genre_choice  # valid input
  
#get_user_genre_choice()
# %%
