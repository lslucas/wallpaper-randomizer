## Wallpaper Randomizer

To install, simple download this script on a desired location and configure a crontab job to execute it every time you want.

If your wallpaper are in a different path, modify accordinly on the script
Same apply for `/usr/bin/gsettings`

### Crontab example
```bash
# change wallpaper every 15min. Change {usr} or the whole location to match yours!!!
*/15 * * * * python3 /home/{usr}/wallpaper-randomizer/wall-randomizer.py
```
