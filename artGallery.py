class ArtGallery:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.artworks = []
        print(f"Gallery '{self.name}' at {self.location} created.")

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"Artwork '{artwork}' added to {self.name}.")

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"Artwork '{artwork}' removed from {self.name}.")
        else:
            print(f"Artwork '{artwork}' not found in {self.name}.")

    def display_artworks(self):
        if self.artworks:
            print(f"Artworks in {self.name}:")
            for art in self.artworks:
                print(f"- {art}")
        else:
            print(f"No artworks in {self.name}.")

    def __del__(self):
        print(f"Gallery '{self.name}' at {self.location} is now closed.")


def main():
    gallery_name = input("Enter gallery name: ")
    gallery_location = input("Enter gallery location: ")
    gallery = ArtGallery(gallery_name, gallery_location)

    while True:
        print("\n--- Art Gallery Menu ---")
        print("1. Add Artwork")
        print("2. Remove Artwork")
        print("3. Display Artworks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            artwork = input("Enter artwork name: ")
            gallery.add_artwork(artwork)
        elif choice == "2":
            artwork = input("Enter artwork name to remove: ")
            gallery.remove_artwork(artwork)
        elif choice == "3":
            gallery.display_artworks()
        elif choice == "4":
            print("Exiting program...")
            del gallery
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
