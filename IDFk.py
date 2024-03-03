from imdb import IMDb

im = IMDb()
m =im.get_movie('0133093')

print(m.data.keys())
boop = input("use this to keep open")