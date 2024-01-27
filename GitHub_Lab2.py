def main():
    return

# TODO: step 2 - create a complex data structure
about_me = {
    'full_name': 'David Owolala',
    'student_id': 10329741,
    'pizza_toppings': ['PEPPERONI', 'CHICKEN', 'PINEAPPLE'],
    'movies': [
        {'title': 'squid game', 'genre': 'melodrama'},
        {'title': 'the originals', 'genre': 'action'},
     ],
       }
 
 # TODO: step 3 - Add another movie to the data stucture
new_movie = {'title': 'the avengers', 'genre': 'action'}
about_me['movies'].append(new_movie)

# TODO: step 4 - functions that prints student name and ID
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = full_name.split()[0]
    student_id = about_me['student_id']
    print(f'My name is {full_name}, but you can call me Sir {first_name}.\nMy stuent ID is {student_id}.')
    return
# TODO: step 5 - functions that prints add pizza toppings to data structure
new_toppings = ('onions', 'extra cheese')
def add_pizza_toppings (about_me, new_toppings):
    about_me['pizza_toppings'].extend(new_toppings)
    about_me['pizza_toppings'] = sorted
    (about_me['pizza_toppings'])
    about_me['pizza_toppings'] = [word.lower()for word in about_me['pizza_toppings']]
    return

# TODO: step 6 function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('my favourite pizza toppings are:')
    for toppings in about_me['pizza_toppings']:
        print(f'-{toppings}')
        return
    
    # TODO: step 7 - function that prints comma-seperated list of movie genres
    def print_movie_genres(about_me):
        list_of_genres = [movies['genre']for movies in about_me['movies']]
        print (f'i like to watch {",".join(list_of_genres)} movies.\n')
        return
    
    # TODO: step 8 - function that prints comma-seperated list of movie titles
    def print_movie_titles(movie_list):
        titles = [movie['title'].title()for movie in movie_list]
        print(f'some of my favourite movies are {", ".join(titles)}!\n')
        return
    
    if __name__ == '__main__':
        main()