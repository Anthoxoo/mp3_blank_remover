# This quick script can be used to remove blank sound from a mp3, it is useful for some cases because when downloading a sound of soundcloud, it can happen that they have a sort of long blank sound at the end that can be pretty annoying.


## Installation : 
```pip install pydub```

**Python version** : 3.12

**NOTE :**
In order to use the script, you must have ffmpeg installed on your machine.

On **linux** : 
```sudo apt / pacman / dnf / ... install / -S ffmpeg```

You'll have to find out yourself how to do it on others Operating Systems.

**Usage :**
main.py path_to_mp3_file

### Todo :
- Adding an argument so the user can choose the directory he wants the cleard blank noise mp3 to go within the second argument.
- Port the script to rust and make it a clean looking cli.
