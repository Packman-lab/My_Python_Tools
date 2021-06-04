#Packman-Lab
#21-May-2021
#Organizing files simple coding
import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    print("Organising your files intro [ images - music - video -executable - archive - torrent - document - code - design files]")
    for filename in os.listdir(dir_path):
        #image
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")):
            # If images folder doesnt exist then create new folder
            if not os.path.exists("images"):
                os.makedirs("images")
            shutil.copy2(filename, "images")
            os.remove(filename)

        # music
        if filename.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")):
            # If music folder doesnt exist then create
            if not os.path.exists("music"):
                os.makedirs("music")
            shutil.copy2(filename, "music")
            os.remove(filename)

        #video
        if filename.lower().endswith((".webm", ".mp4")):
            # If video folder doesnt exist then create
            if not os.path.exists("video"):
                os.makedirs("video")
            shutil.copy2(filename, "video")
            os.remove(filename)

        #executables
        if filename.lower().endswith((".exe", ".msi", ".deb" , "dmg")):
            # If executables folder doesnt exist then create
            if not os.path.exists("executables"):
                os.makedirs("executables")
            shutil.copy2(filename, "executables")
            os.remove(filename)

        #archive files
        if filename.lower().endswith((".rar", ".tar" , ".zip" , ".gz")):
            # If archive folder doesnt exist then create
            if not os.path.exists("archives"):
                os.makedirs("archives")
            shutil.copy2(filename, "archives")
            os.remove(filename)


        #torrent files
        if filename.lower().endswith((".torrent",)):
            # If torrent folder doesnt exist then create
            if not os.path.exists("torrent"):
                os.makedirs("torrent")
            shutil.copy2(filename, "torrent")
            os.remove(filename)

        #documents
        if filename.lower().endswith((".txt", ".pdf", ".docx" , "doc")):
            # If documents folder doesnt exist then create
            if not os.path.exists("documents"):
                os.makedirs("documents")
            shutil.copy2(filename, "documents")
            os.remove(filename)


        #code files
        if filename.lower().endswith((".py", ".php", ".html" , ".css" , ".js")):
            # If code folder doesnt exist then create
            if not os.path.exists("code"):
                os.makedirs("code")
            shutil.copy2(filename, "code")
            os.remove(filename)

        #design files
        if filename.lower().endswith((".psd", ".ai")):
            # If desgin folder doesnt exist then create
            if not os.path.exists("design-files"):
                os.makedirs("design-files")
            shutil.copy2(filename, "design-files")
            os.remove(filename)

except OSError:
    print("Error")
finally:
    # When script is finished clear screen and display message
    os.system("cls" if os.name == "nt" else "clear")
print("Finished organising your files")
