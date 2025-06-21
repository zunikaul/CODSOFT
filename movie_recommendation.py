
def recommend_movies(category):
    category = category.lower()

   
    recommendations = {
        "happy": [
            "Zindagi Na Milegi Dobara",
            "The Intouchables",
            "Paddington 2"
        ],
        "sad": [
            "The Pursuit of Happyness",
            "Blue Valentine",
            "Masaan"
        ],
        "thriller": [
            "Kahaani",
            "Gone Girl",
            "Andhadhun"
        ],
        "sci-fi": [
            "Interstellar",
            "Inception",
            "Edge of Tomorrow"
        ],
        "bollywood": [
            "3 Idiots",
            "Queen",
            "Barfi!"
        ],
        "hollywood": [
            "The Shawshank Redemption",
            "Forrest Gump",
            "La La Land"
        ]
    }

   
    if category in recommendations:
        print(f"\n🎬 Movie Recommendations for '{category}':")
        for movie in recommendations[category]:
            print(f" - {movie}")
    else:
        print("\n❗ Sorry, I don't have recommendations for that category.")
        print("Try one of these: happy, sad, thriller, sci-fi, bollywood, hollywood.")


print(" Welcome to the Movie Recommendation System!")
print("Let me help you choose a movie based on your mood or favorite genre.")
print("Available categories: happy, sad, thriller, sci-fi, bollywood, hollywood")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye! Hope you enjoy your movie!")
        break
    else:
        recommend_movies(user_input)
