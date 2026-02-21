duration=[]
n=int(input("Enter the number of songs: "))
for i in range(n):
    d=int(input("Enter duration: "))
    duration.append(d)  

invalid=False
tooshort=False
toolong=False
twenty21=False
for d in duration:
    if d < 0:
        invalid=True
        break
if invalid:
    print("Invalid entries found. Please enter non-negative durations.")
else:
    total_duration = sum(duration)
    number_of_songs = len(duration)

    if total_duration <300:
        if total_duration ==21:
            twenty21=True
           
        tooshort=True
        catetgory = "Too Short Playlist"
        recommendation = "Add more songs to your playlist."
    elif total_duration >300 and  total_duration > 3600:
        toolong=True
        catetgory = "Too long Playlist"
        recommendation = "Consider shortening your playlist."

    elif len(duration)!=len(set(duration)):
        catetgory = "Repettitive Playlist"
        recommendation = "Add variety"
    elif  invalid==False and tooshort==False and toolong==False:
        catetgory = "Balanced Playlist"
        recommendation = "Good Listening experience."
    else:
        catetgory = "Irregular Playlist"
        recommendation = "adjust your playlist"



if twenty21:
          number_of_songs +=1
  
print("total duration of playlist is:",total_duration)
print("number of songs in playlist is:",number_of_songs)
print("category:",catetgory)
print("recommendation:",recommendation)
