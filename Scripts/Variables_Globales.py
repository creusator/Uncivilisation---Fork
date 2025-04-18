SCREEN_WIDTH = 1170
SCREEN_HEIGHT = 940
FRAMERATE = 75

HEX_RADIUS = 50

DEPART_X = 0
DEPART_Y = 0

COLOR_RED = (255, 0, 0)

biomes_disponibles = ["montagne", "plaine", "foret", "sable", "lac"]
biome_weights = {
    "plaine":     {"plaine": 40, "foret": 50, "sable": 10},
    "foret":      {"foret": 30, "plaine": 10, "montagne": 60},
    "montagne":   {"montagne": 40, "foret": 30, "plaine": 30},
    "sable":      {"sable": 30, "plaine": 15, "lac": 55},
    "lac":        {"lac": 70, "sable": 25, "plaine": 5}
}