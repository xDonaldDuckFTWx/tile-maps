from CreateMapFromFile import createMapFromFile

url = input("Enter the URL: \n")
savefile = input("\nEnter name of save-file: \n")

createMapFromFile(url, url=True)

with open("maps/final_maps/cache.json", "r") as cache:
    with open("maps/final_maps/{}.json".format(savefile), "w+") as save:
        json_s = cache.read()
        save.write(json_s)
        save.close()
    cache.close()
