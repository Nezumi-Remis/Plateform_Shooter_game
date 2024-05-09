class PlayerStats():
    def __init__(self, filename):
        self.filename = filename
        self.jumps = 0
        self.shots = 0
        self.grenades_thrown = 0

    def increment_jump(self):
        self.jumps += 1

    def increment_shot(self):
        self.shots += 1

    def increment_grenade(self):
        self.grenades_thrown += 1

    def save_stats(self):
        with open(self.filename, 'w') as f:
            f.write(f"Jumps: {self.jumps}\n")
            f.write(f"Shots: {self.shots}\n")
            f.write(f"Grenades thrown: {self.grenades_thrown}\n")