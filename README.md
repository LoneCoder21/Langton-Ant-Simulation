# Langton's Ant
## Basic Requirements
1. [x] Cell Class (Color + Rule State Id (Rule String))
2. [x] Ant Class (Position + Direction)
3. [x] Rule Class (Color + Character (Direction To Turn))
4. [x] Square Grid of W X H cells
5. [x] Rule/Ant Array
6. [x] Simulation Steps
7. [x] Functions in Game to be called from the UI Class (Updates game object)

## UI Requirements
### Sliders
1. [ ] Modify Grid Size (W and H) (each 0-2000)
2. [ ] Grid Cell Size (0-100)
3. [ ] Multiple Ants (0-100)
4. [ ] Simulation speed/Pause (0-2x)

### Buttons
1. [ ] Randomize Ants (Connects to Ants Slider)
2. [ ] Simulation Speed Buttons (Maybe 0.25,0.5x,1.0x,1.5x,2.0x)
3. [x] Randomize Color
3. [x] Randomize Rule Sets

### Text Field
1. [x] Rule sets (Accepts Text String)

### Radio Button
1. [x] Ant Death on Edge or Warp Grid (Binary Option) (IGNORE)

## Rendering Requirements
1. [x] Grid Position
2. [x] Draw Wireframe (IGNORE)
3. [x] Game Loop
4. [x] Draw Square
5. [x] Draw Hexagons (IGNORE)

## Hard (Optional extensions)
1. [x] Random colors schemes using HSL color model (Color model in UI)
2. [x] Hexagon grid structure (IGNORE)
3. [x] Ant Death/Warp Grid (IGNORE)

## Resources

Wiki page: https://en.wikipedia.org/wiki/Langton%27s_ant

Pygame: https://pyga.me/docs/

Pygame GUI: https://pygame-gui.readthedocs.io/en/v_069/quick_start.html#quick-start

GUI Themes for later: https://pygame-gui.readthedocs.io/en/v_069/theme_guide.html#theme-guide

Hexagon Grid: https://www.redblobgames.com/grids/hexagons/#wraparound

## Installation
pip3 install pygame-ce

pip install pygame_gui
