import os
import time
import zipfile 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import (MEDIA_SORT, 
                    PATH_IMAGES,
                    PATH_MUSIC, 
                    PATH_OTHER, 
                    PATH_TRASH, 
                    PATH_VIDEOS)

class Sort(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_trash):
            ext = filename.split('.')
            if len(ext) > 1 and ext[-1].lower() == 'jpg' or ext[-1].lower() == 'png' or ext[-1].lower() == 'jpeg'\
                or ext[-1].lower() == 'gif' or ext[-1].lower() == 'svg':
                file = folder_trash + '/' + filename
                new_path = folder_images + '/' + filename
                os.rename(file, new_path)
                
            elif len(ext) > 1 and ext[-1].lower() == 'wmv' or ext[-1].lower() == 'mp4' or ext[-1].lower() == 'avi'\
                or ext[-1].lower() == 'mov' or ext[-1].lower() == 'mkv':
                file = folder_trash + '/' + filename
                new_path = folder_videos + '/' + filename
                os.rename(file, new_path)
                
            elif len(ext) > 1 and ext[-1].lower() == 'mp3' or ext[-1].lower() == 'wav':
                file = folder_trash + '/' + filename
                new_path = folder_music + '/' + filename
                os.rename(file, new_path)
                
            else:
                file = folder_trash + '/' + filename
                new_path = folder_other + '/' + filename
                os.rename(file, new_path)
                

folder_trash = PATH_TRASH

folder_images = PATH_IMAGES
folder_videos = PATH_VIDEOS
folder_music = PATH_MUSIC
folder_other = PATH_OTHER

print('1 - Sort')
print('2 - Archiving')
mode = int(input('Select mode: '))

if mode == 1:
    sort = Sort()
    observer = Observer()
    observer.schedule(sort, folder_trash, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

elif mode == 2:
    name = input('Enter archive name: ')
    print('Creating archive...')
    zip_file = zipfile.ZipFile(name + '.zip', 'w')
    for root, dirs, files in os.walk(MEDIA_SORT):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()
    print('Archive created')
     
    print('Deleting files in the folder...')    
    for filename in os.listdir(folder_images):
        file = folder_images + '/' + filename
        os.remove(file)
        
    for filename in os.listdir(folder_videos):
        file = folder_videos + '/' + filename
        os.remove(file)
        
    for filename in os.listdir(folder_music):
        file = folder_music + '/' + filename
        os.remove(file)
        
    for filename in os.listdir(folder_other):
        file = folder_other + '/' + filename
        os.remove(file)
    print('Done')
        
else:
    print('Incorrect mode')
                
                