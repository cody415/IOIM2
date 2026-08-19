from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Instrument: {self.name}")

    @abstractmethod
    def play_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name, strings):
        super().__init__(name)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} with {self.strings} strings strums: Twang! Twang!")

class Piano(Instrument):
    def __init__(self, name, keys):
        super().__init__(name)
        self.keys = keys

    def play_sound(self):
        print(f"{self.name} with {self.keys} keys plays: Plink! Plonk!")

class Drum(Instrument):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def play_sound(self):
        print(f"{self.name} ({self.size} size) beats: Boom! Boom!")

guitar = Guitar("Acoustic Guitar", 6)
piano = Piano("Grand Piano", 88)
drum = Drum("Bass Drum", "Large")

print("=== Music Instrument Sound Show ===\n")
for instrument in [guitar, piano, drum]:
    instrument.display()
    instrument.play_sound()
    print()
