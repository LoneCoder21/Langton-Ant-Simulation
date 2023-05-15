# Langton's Ant
## Basic Requirements
1. Cell Class (Color + Rule State Id (Rule String)) (DONE)
2. Ant Class (Position + Direction) (DONE)
3. Rule Class (Color + Character (Direction To Turn)) (DONE)
4. Square Grid of W X H cells (DONE)
5. Rule/Ant Array (DONE)
6. Simulation Steps (TODO)
7. Functions in Game to be called from the UI Class (Updates game object) (DONE)

## UI Requirements
### Sliders
1. Modify Grid Size (W and H) (each 0-2000) (TODO)
2. Grid Cell Size (0-100) (TODO)
3. Multiple Ants (0-100) (TODO)
4. Simulation speed/Pause (0-2x) (TODO)

### Buttons
1. Randomize Ants (Connects to Ants Slider) (TODO)
2. Simulation Speed Buttons (Maybe 0.25,0.5x,1.0x,1.5x,2.0x) (TODO)
3. Randomize Color (DONE)
3. Randomize Rule Sets (DONE)

### Text Field
1. Rule sets (Accepts Text String) (DONE)

### Radio Button
1. Ant Death on Edge or Warp Grid (Binary Option) (IGNORE)

## Rendering Requirements
1. Grid Position (DONE)
2. Draw Wireframe (IGNORE)
3. Game Loop (DONE)
4. Draw Square (DONE)
5. Draw Hexagons (IGNORE)

## Hard (Optional extensions)
1. Random colors schemes using HSL color model (Color model in UI) (DONE)
2. Hexagon grid structure (IGNORE)
3. Ant Death/Warp Grid (IGNORE)

## Resources

Wiki page: https://en.wikipedia.org/wiki/Langton%27s_ant

Pygame: https://pyga.me/docs/

Pygame GUI: https://pygame-gui.readthedocs.io/en/v_069/quick_start.html#quick-start

GUI Themes for later: https://pygame-gui.readthedocs.io/en/v_069/theme_guide.html#theme-guide

Hexagon Grid: https://www.redblobgames.com/grids/hexagons/#wraparound

## Installation
pip3 install pygame-ce

pip install pygame_gui
