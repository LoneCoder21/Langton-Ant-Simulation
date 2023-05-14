# Hardcoded Constants
class Constant:
    # WINDOW
    title = "Langton's Ant"
    W = 1700
    aspectratio = 9 / 16
    H = int(W * aspectratio)

    # UI
    uioffset = 0.8
    uisize = 0.2
    uiupdate_ms = 200

    # FRAMES
    FPS = 60

    # COLORS
    backcolor = (0, 0, 0)
    uibackcolor = (150, 150, 150)
    
    # ASSETS
    wheelimage = "wheel.png"
    wheelscale = 250
    polarimage = "polar_coords.png"
    polarscale = 100

# Default Values for Game State
class Default:
    #State
    stepsize = 1  # per frame
    GW = 100
    GH = 100
    ants = 1
    rules = "RL"
    colors = [(0,0,0), (255,255,255)]
    
    #Rendering
    xoff = 70
    yoff = 30
    cellsize = 5