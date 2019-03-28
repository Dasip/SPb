from mymapapi import show_map
from mygeocoder import get_coordinates as get_core

def main():
    map_locations = 'll=30.097431,59.908131&spn=0.2,0.2'
    map_type = 'sat,skl'
    points = [
        "29.914783,59.891574",
        "30.105881,59.944074",
        "30.237944,59.916487",
        "30.266268,59.919073",
        "30.275489,59.930952",
        "30.310165,59.941203"
    ]
    line = 'pl=' + ','.join(points)
    show_map(map_locations, map_type, line)
    
if __name__ == '__main__':
    main()