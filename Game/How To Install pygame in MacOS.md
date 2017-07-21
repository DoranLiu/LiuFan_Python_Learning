### This is the best method I've found for installing on OS X (and works with Python 3):

1. Install XCode command line tools

XCode is the tool from Apple for creating Mac and iOS applications. It can be installed from the App Store (it’s free). When it’s finished, type the following at the command line:

```$ xcode-select --install```

2. Install Homebrew (http://brew.sh)

Homebrew is a tool to easily install all kinds of software from the command line. It saves you having to go to a bunch of different sites and download lots of individual installers. Copy and paste this on the command line:

```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```
and follow the directions. You’ll also need to install Homebrew Cask (http://caskroom.io):

```$ brew install caskroom/cask/brew-cask```

3. Install the rest of the software

Now we can start installing all the requirements for Pygame. Just type the following commands one at a time and let the computer do its thing:

```
$ brew cask install xquartz

$ brew install python3

$ brew install python

$ brew linkapps python3

$ brew linkapps python

$ brew install git

$ brew install sdl sdl_image sdl_ttf portmidi libogg libvorbis

$ brew install sdl_mixer --with-libvorbis

$ brew tap homebrew/headonly

$ brew install smpeg

$ brew install mercurial

$ pip3 install hg+http://bitbucket.org/pygame/pygame
```

4. See if it works!

Now we can see if it works. Run Python from the command line:

``$ python3```
and try loading Pygame:
```
>>> import pygame
```
If you don’t see an error message, you’re all set!