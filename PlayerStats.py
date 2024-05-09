import time

class PlayerStats():
    def __init__(self, filename):
        self.filename = filename
        self.jumps = 0
        self.shots = 0
        self.grenades_thrown = 0
        self.time_played = 0

    def increment_jump(self):
        self.jumps += 1

    def increment_shot(self):
        self.shots += 1

    def increment_grenade(self):
        self.grenades_thrown += 1

    def add_time_played(self, time_to_add):
        self.time_played += time_to_add

    def save_stats(self):
        minutes_played = int(self.time_played / 60)
        seconds_played = int(self.time_played % 60)
        with open(self.filename, 'w') as f:
            f.write(f"Jumps: {self.jumps}\n")
            f.write(f"Shots: {self.shots}\n")
            f.write(f"Grenades thrown: {self.grenades_thrown}\n")
            f.write(f"Time played: {minutes_played} minutes {seconds_played} seconds\n")