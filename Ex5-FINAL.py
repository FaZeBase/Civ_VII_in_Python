tile_skel = { "terrain": "water",
              "production": {"food": 0,
                            "materials": 0,
                            "gold": 0},
            }
tile_debug = { "terrain": "forest",
              "production": {"food": 2,
                            "materials": 3,
                            "gold": 4},
            "city": "Free City",
            "owner": "FaZeBasescu"
            }

tile_iamtoolazyforthis = { "terrain": "forest",
                           "production": {"food": 5,
                           "materials": 6,
                           "gold": 7},
                           "city": "Free Dos",
                           "owner": "FaZeBasescu"
                           }


def modify_production(tile: dict, resource: str, amount: int) -> None :
    if tile["production"][resource] + amount <= 0 :
        print("Il y a un problème avec le programme")
    else :
        tile["production"][resource] += amount #comment modifier un dictionnaire dans un dictionnaire

def new_tile(terrain: str)  ->  dict :
    tile = tile_skel
    if terrain == "water" :
        tile["production"]["food"] = 1
        return tile
    elif terrain == "plain" :
        tile["production"]["food"] = 2
        return tile
    elif terrain == "forest" :
         tile["production"]["food"] = 1
         tile["production"]["materials"] = 1
         return tile
    elif terrain == "mountain" :
        tile["production"]["materials"] = 1
        return tile
    else :
        print("Il y a un problème avec le programme")
        return None

def has_owner(tile: dict, name: str = None) -> bool :
    if "owner" in tile : # Attention ! Pour retrouver une clé dans un dico, utiliser "in"
        return True
    else :
        return False
    
def has_city(tile: dict) -> bool :
    if "city" in tile :
        return True
    else :
        return False
    
def has_tradepost(tile: dict) -> bool :
    if "tradepost" in tile:
        return True
    else :
        return False
    
def can_build_city(tile: dict) -> bool :
    if has_city(tile) == False and has_tradepost(tile) == False and \ # on peut aussi utiliser des slashs (\) pour mettre une condition sur plusieurs lignes
       has_owner(tile) and tile["terrain"] == "plain" :
        print("It's True")
        return True
    else :
        print("It's False")
        return False

def can_build_tradepost(tile: dict) -> bool :
    if has_city(tile) == False and has_tradepost(tile) == False and \
       has_owner(tile) and tile["terrain"] != "water" :
        print("It's True")
        return True
    else :
        print("It's False")
        return False

def can_upgrade(tile: dict) -> bool :
        if has_city(tile) == False and has_tradepost(tile) and \
           has_owner(tile) and tile["terrain"] == "plain" :
            print("It's True")
            return True
        else :
            print("It's False")
            return False
        
def build_tradepost(tile: dict) -> None :
    if can_build_tradepost(tile) :
        tile["tradepost"] = True

def build_city(tile: dict, name: str) -> None :
    if can_build_city(tile) == True :
        tile["city"] = name
    elif can_upgrade(tile) == True:
        del tile["tradepost"]
        tile["city"] = name
    else :
        print("Ceci n'est pas possible")

def cut_forest(tile: dict) -> None :
    if tile["terrain"] == "forest" :
        tile["terrain"] = "plain"
    else :
        print("Ceci n'est pas une forêt et elle ne peut pas être coupée")

def change_owner(tile: dict, name: str = None) -> str :
    old_name = tile.pop("owner")
    tile["owner"] = name
    return old_name
    
def demolish_building(tile: dict) -> bool :
    if has_city(tile) :
        del tile["city"]
    elif has_tradepost(tile) :
        del tile["tradepost"]
    else :
        print("Il n'y a rien à démolir")

def count_cities(tiles: list, name: str) -> int :
    counter = 0
    for tile in tiles :
        if "city" in tile and tile["owner"] == name :
            counter += 1
    return counter

def count_total_production(tiles: list, name: str) -> dict :
    total = 0
    for tile in tiles :
        food, materials, gold = tiles[tiles.index(tile)]["production"]["food"], \
        tiles[tiles.index(tile)]["production"]["materials"], \
        tiles[tiles.index(tile)]["production"]["gold"]
        total += food + materials + gold
    return total

modify_production(tile_skel, "food", 5)
tile = new_tile("forest")
print(tile)
print(has_owner(tile))
print(has_city(tile))
build_city(tile_debug, "Family Friendly Names Please")
cut_forest(tile_debug)

print(change_owner(tile_debug,"WeedMaster420"))
print(tile_debug)
print(change_owner(tile_debug,"FaZeBasescu"))
tiles = [tile_debug, tile_iamtoolazyforthis]
print(count_cities(tiles, "FaZeBasescu"))
print(count_total_production(tiles, "FaZeBasescu"))

