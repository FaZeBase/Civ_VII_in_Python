tile_skel = { "terrain": "water",
              "production": {"food": 0,
                            "materials": 0,
                            "gold": 0},
            }
tile_debug = { "terrain": "plain",
               "production": {"food": 2,
                            "materials": 3,
                            "gold": 4},
               "city": "Free City",
            }

tile_iamtoolazyforthis = { "terrain": "forest",
                           "production": {"food": 5,
                           "materials": 6,
                           "gold": 7},
                           "city": "Free Dos",
                           "owner": "FaZeBasescu-AG"
                           }


def modify_production(tile: dict, resource: str, amount: int) -> None :
    if tile["production"][resource] + amount < 0 :
        print("Il y a un problème avec le programme")
    else :
        tile["production"][resource] += amount #comment modifier un dictionnaire dans un dictionnaire

def new_tile(terrain: str)  ->  dict :
    tile = tile_skel
    if terrain == "water" :
        tile["production"]["food"] = 1
    elif terrain == "plain" :
        tile["production"]["food"] = 2
    elif terrain == "forest" :
         tile["production"]["food"] = 1
         tile["production"]["materials"] = 1
    elif terrain == "mountain" :
        tile["production"]["materials"] = 1
    else :
        print("Type de tile invalide")
        return None
    return tile

def has_owner(tile: dict, name: str = None) -> bool :
    return "owner" in tile : # Attention ! Pour retrouver une clé dans un dico, utiliser "in"
      
def has_city(tile: dict) -> bool :
    return "city" in tile :
    
def has_tradepost(tile: dict) -> bool :
    return "tradepost" in tile :
    
def can_build_city(tile: dict) -> bool :
    # on peut aussi utiliser des slashs (\) pour mettre une condition sur plusieurs lignes
    return not has_city(tile) and not has_tradepost(tile) and \
       has_owner(tile) and tile["terrain"] == "plain" :

def can_build_tradepost(tile: dict) -> bool :
    return not has_city(tile) and not has_tradepost(tile) and \
       has_owner(tile) and tile["terrain"] != "water" :

def can_upgrade(tile: dict) -> bool :
    return not has_city(tile) and has_tradepost(tile) and \
           has_owner(tile) and tile["terrain"] == "plain" :
        
def build_tradepost(tile: dict) -> None :
    if can_build_tradepost(tile) :
        tile["tradepost"] = True

def build_city(tile: dict, name: str) -> None :
    if can_build_city(tile) :
        tile["city"] = name
    elif can_upgrade(tile) :
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
    if not has_owner(tile) :
        old_name = None
    else :
        old_name = tile["owner"]
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
        if "city" in tile and "owner" in tile and tile["owner"] == name :
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
print(change_owner(tile_debug,"IDK-TBH"))
print(tile_debug)
print(change_owner(tile_debug,"FaZeBasescu-AG"))
tiles = [tile_debug, tile_iamtoolazyforthis]
print(count_cities(tiles, "FaZeBasescu-AG"))
print(count_total_production(tiles, "FaZeBasescu-AG"))
tile_new = change_owner(tile_debug, "Test")
print(tile_debug)

