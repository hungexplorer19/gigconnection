import random

class GigConnectChatbot:
    def __init__(self):
        self.genres = {
            'rock': ['Rock Band A', 'Rock Band B', 'Solo Rock Artist'],
            'pop': ['Pop Band X', 'Solo Pop Artist'],
            'jazz': ['Jazz Ensemble Y', 'Jazz Pianist Z'],
            # Add more genres and associated musicians as needed
        }

    def get_genre_suggestions(self, event, num_people):
        suggestions = []
        if event == 'wedding':
            suggestions = self.genres['pop'] + self.genres['jazz']
        elif event == 'birthday':
            suggestions = self.genres['pop'] + self.genres['rock']
        elif event == 'corporate_event':
            suggestions = self.genres['jazz']
        # Add more event-specific suggestions as needed

        # Filter suggestions based on the number of people
        filtered_suggestions = [genre for genre in suggestions if len(self.genres[genre]) >= num_people]

        return filtered_suggestions

    def chat(self):
        print("Welcome to GigConnect! I'm here to help you find the perfect musicians for your event.")

        while True:
            event = input("What type of event are you planning? (e.g., wedding, birthday, corporate_event): ").lower()
            num_people = int(input("How many people will be attending your event? "))
            
            if event not in self.genres or num_people <= 0:
                print("Sorry, we don't have suggestions for that combination. Please try again.")
                continue

            suggestions = self.get_genre_suggestions(event, num_people)

            if suggestions:
                print(f"Great! Here are some musician suggestions for your {event} with {num_people} people:")
                for genre in suggestions:
                    print(f"{genre.capitalize()}: {', '.join(self.genres[genre])}")
            else:
                print("Sorry, we couldn't find suitable musicians for your event. Please try a different combination.")

            another_request = input("Do you have another event to plan? (yes/no): ").lower()
            if another_request != 'yes':
                print("Thank you for using GigConnect. Have a great day!")
                break

if __name__ == "__main__":
    chatbot = GigConnectChatbot()
    chatbot.chat()
