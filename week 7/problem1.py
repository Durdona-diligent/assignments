#Video Game aPlayer Profile
class PlayerProfile:
    def __init__(self, username):
        self.username = username
        self.score = 0

    def add_points(self, points):
        self.score += points

    def display_status(self):
        print(f"Player: {self.username}, Score: {self.score}")

player1 = PlayerProfile("ShadowNinja")
player2 = PlayerProfile("CyberSamurai")

player1.display_status()

player1.add_points(50)
player1.add_points(25)
player2.add_points(100)

player1.display_status()
player2.display_status()