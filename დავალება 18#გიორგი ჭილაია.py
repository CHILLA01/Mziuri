class FootballPlayer:
    def __init__(self, name, position, skill_level, team="Free Agent"):
        self.name = name
        self.position = position
        self.skill_level = skill_level
        self.team = team

    def __str__(self):
        return f"Player: {self.name}, Position: {self.position}, Skill Level: {self.skill_level}, Team: {self.team}"

    def tryout(self):
        if self.skill_level > 90:
            self.team = "Barcelona"
        elif self.skill_level > 85:
            self.team = "Real Madrid"
        elif self.skill_level > 80:
            self.team = "Manchester City"
        elif self.skill_level > 75:
            self.team = "Bayern Munich"
        elif self.skill_level > 70:
            self.team = "AC Milan"
        elif self.skill_level > 65:
            self.team = "Juventus"
        elif self.skill_level > 60:
            self.team = "Arsenal"
        else:
            self.team = "Leeds United"

    def update_skill(self, new_skill_level):
        self.skill_level = new_skill_level


def main():
    players = [
        FootballPlayer("Lionel Messi", "Forward", 99),
        FootballPlayer("Cristiano Ronaldo", "Forward", 92),
        FootballPlayer("Kevin De Bruyne", "Midfielder", 89),
        FootballPlayer("Robert Lewandowski", "Striker", 87),
        FootballPlayer("Paolo Maldini", "Defender", 80),
        FootballPlayer("Gianluigi Buffon", "Goalkeeper", 78),
        FootballPlayer("Thierry Henry", "Striker", 72),
        FootballPlayer("Kalvin Phillips", "Midfielder", 65)
    ]

    while True:
        try:
            num_players = int(input("Enter the number of additional players: "))
            if num_players < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    for _ in range(num_players):
        name = input("Enter player name: ")
        position = input("Enter player position: ")
        while True:
            try:
                skill_level = int(input("Enter player skill level (0-100): "))
                if 0 <= skill_level <= 100:
                    break
                else:
                    print("Please enter a skill level between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid number between 0 and 100.")

        player = FootballPlayer(name, position, skill_level)
        players.append(player)

    for player in players:
        player.tryout()

    print("\nAfter Tryouts:")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
