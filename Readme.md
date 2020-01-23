# Python3 based termial Game (JetPack Joyride/Mandolorian):
```sh
A terimal Based game using python3,coloroma and numpy
```
### REQUIREMENTS:
``` colorama, numpy ```
### RUN:
``` python3 main.py ```
### How to play:
```sh
Press 'w' to jump.
Press 'a' to move left.
Press 'd' to move right.
Press 'q' at any time to quit.
Press 'x' for shield.
Press "P"  for powermode.
press 'm' for shoot bullets.
```
### Non Blocking Input:
```sh
class _getChUnix:
   " def __init__(self):"
        import tty
        import sys

"    def __call__(self):"
       
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar
```
### USAGE(NBI)
```sh
def alarmhandler(signum, frame):

		raise AlarmException

	def user_input(timeout=0.15):
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)

		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
```
### ASCII Color Codes:
```sh
COLORS = {
    'Black': '\x1b[0;30m',
    'Blue': '\x1b[1;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[1;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Pink': '\x1b[38;5;200m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'Light Grey': '\x1b[1;37m',
    'Bridge Color': '\x1b[48;5;130m',
    'Bullets Color': '\x1b[38;5;208m',
    'Extras Bridge': '\x1b[38;5;82m',
    'Water Color': '\x1b[48;5;39m',
    'Fish Color': '\x1b[38;5;130m',
    'Moving Bridges': '\x1b[48;5;94m'
}

END_COLOR = '\033[m'
```
### Directory Structure:
```sh
        ├── Dragon.py
        ├── JetPacker.py
        ├── alarmexception.py
        ├── beams.py
        ├── board.py
        ├── colors.py
        ├── config.py
        ├── getch.py
        ├── magnet.py
        ├── main.py
        └── scenery.py
```
### Class Description:
``` sh
 Dragon: It has the Boss Enemy.
 DragonFire:It is a Bullets of Boss Enemy.
 Jetpacker:It is main hero
 beams:Fire Beams at H,V and 45 degree
 Magnet:Come in the middle of game ,pulls you towards it
 Sceney: has Ground ,Floor , Money
 Bullet: has Bullets for Jetpacker
```
