playlist = {'title': 'patagonia bus',
            'creator': 'Colt Steele',
            'num_songs': 13,
            'length': '50',
            'songs': [
                {'title': 'Turn it Off',
                 'artists': ['Culture Abuse'],
                 'album': 'Peach',
                 'date_added': '2017-10-31',
                 'length': '3:37'}
            ]}

playlist = []

with open("playlist.txt") as f:
    for song in f:
        song = song.strip().split(",")
        playlist.append({
            'title': song[0],
            'artist': song[1],
            'album': song[2],
            'date_added': song[3],
            'length': song[4]
        })

print(playlist)
