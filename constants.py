# hardcoded constants
class Constant:
    # WINDOW
    title = 'Langton\'s Ant'
    W = 1700
    aspectratio = 9/16
    H = int(W*aspectratio)
    
    # UI
    uioffset = 0.8
    uisize = 0.2
    
    # FRAMES
    FPS = 60

    # COLORS
    backcolor = (0,0,0)
    uibackcolor = (150,150,150)

# default values / can be updated
class Default:
    stepsize = 1 #per frame
    GW = 100
    GH = 100
    