import os, random, datetime

def main():
    path = '/usr/share/backgrounds/'
    wallpaper_uri = path + random.choice(os.listdir(path))

    cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri ' + wallpaper_uri

    print('Wallpaper ' + wallpaper_uri + ' set at ' + datetime.datetime.now().strftime('%d/%m/%Y %H:%M'))

    return os.system(cmd)


main()