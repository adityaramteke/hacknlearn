
sifi_authors = ["Jules Verne", "H. G. Wells", "Hugo Gernsback", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Isaac Asimov", "Ray Bradbury", "William Gibson", "Orson Scott Card", "Dafydd ab Hugh", "Alexander Abasheli", "Edwin Abbott Abbott"]

sifi_authors.sort(key=lambda name: name.split(" ")[-1].lower()) # Sort List by last name

print(sifi_authors)     # Sorted list 
