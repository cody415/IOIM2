class Robot:
    robot_type = "Humanoid Robot"

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I belong to {self.owner}.")
        print(f"I am a {Robot.robot_type}.")
        print("-" * 40)


robot1 = Robot("Tom", "Harsh")
robot2 = Robot("Jerry", "Harsh")

robot1.introduce()
robot2.introduce()
