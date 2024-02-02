class CLI:
    def __init__(self):
        #empty
        nothing = 'nothing'
    def search_movie(self, movie_name):
        print("I have not connected to the database yet.")
    def run(self):
        while True:
            command = input("what do you want to do ?  \n  some suggestions : (search_movie, search_actor, exit): ").strip()
            if command == 'exit':
                print("Exiting")
                break
            elif command == 'search_movie':
                movie_name = input("Enter movie name: ")
                self.search_movie(movie_name)
            else:
                print("Invalid command. Please try again.")




if __name__ == "__main__":
    my_cli = CLI()
    my_cli.run()
