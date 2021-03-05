[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<p align="center">
<h1 align="center">Capsian Engine</h1>

  <p align="center">
    Capsian is a weird, incomplete and performant Python game engine. The project was initially named "KeyFire Engine" but was later renamed to Capsian due to trademark related issues.
    <br />
    <br />
    <a href="https://github.com/tzyvoski/Capsian-Engine/issues">Report Bug</a> ||
    <a href="https://github.com/tzyvoski/Capsian-Engine/pulls">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

-   [About the Project](#performance)
    -   [Built With](#built-with)
    -   [Languages](#languages)
-   [Getting Started](#getting-started)
    -   [Requirements](#requirements)
    -   [Setup](#setup)
-   [Older versions and Roadmap](#older-versions)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)
-   [Acknowledgements](#acknowledgements)

## Performance

<p>The latest version of Capsian brings with it numerous improvements to performance. Previous versions struggled to handle over 500 non-batched objects in a scene. This version, though, with the new clock and ticking mechanics, pushes performance to the sky: with an average of 2000 FPS at 5120x2880 and 4700FPS at 1280x720. You can read the code in files "Capsian/video/scene.py" , "Capsian/video/window.py" and "Capsian/world/clock.py" to find out what makes it so performant.
<br>
</p>
<i><strong>ALL TESTS WERE CONDUCTED ON A GTX 1080 AND INTEL CORE i7 8700K 3.70GHz</strong></i>
  <br>
  <br>
<div align="center">
  <img src="https://i.imgur.com/rhKtgp7.png" alt="Snow" width="800">
<br><br>
  <img src="https://i.imgur.com/VZgMAci.png" alt="Forest" width="800">
</div>

### Built With

-   [Python](https://www.python.org/)
-   [OpenGL](https://www.opengl.org/)
-   [Pyglet](http://pyglet.org/)

### Languages

<p>Capsian uses Python as both its scripting language and its source language (TCL, C, C++ and the others you see on the right come from libs and the venv). Until a while ago, there was also support for a custom parsed language called "tzylang", but it's since been removed due to parsing related issues. Other scripting languages will probably be added in the futures (C# Being my main focus), but for now this is what you get.
  <br>
</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Requirements

<p>Capsian now includes a Python Virtual Environment (venv) to insure everybody has the same experience, regardless of what they have installed on their machine. This doesn't mean, though, that there's nothing you need or may want to do to improve your coding experience.

    - Windows 10
    - Visual Studio Code with all the necessary extensions

Unfortunately I don't have a Linux machine (And not even a VM right now), thus worsening your coding experience on Linux. This doesn't mean you can't use Capsian on Linux though. Yuo can, it's just that you'll have to install pyglet 1.5.6 and Python 3.7.3 on your machine for now.
The Linux version will probably be available in March 2021 thanks to a contributor and friend [ [Gyro](https://github.com/Gyro7/) ].

Visual Studio Code is a great text editor as it doesn't force you to use your machine's Python Interpreter, but allows you to choose it. Read the next block for more information.
  <br>
</p>


### Setup
Using VSCode:
```shell
# In the bottom-left of the VS Code window, you should see a few buttons

    - Make sure you have the Python extension installed
    - Select your python interpreter (Recommended: Python/Windows/python.exe)
    - Always run your app with the "WinRuntime.bat" file!

```

<!-- ROADMAP -->

## Older Versions

See the [open issues](https://github.com/tzyvoski/Capsian-Engine/issues) for a list of proposed features (and known issues).<br>
You can find all older versions of Capsian (KeyFire) at: https://tzyvoski.wixsite.com/keyfire

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
<br><br>```But please follow these simple rules:```<br><br>
- Please do NOT commit and push to the master branch.
- You can clone the repository or create another branch as stated by the license in the LICENSE.txt file. 
- If you think your contributions could help a lot, then write to my email address (miro.salerno@icloud.com).
- I may or may not accept the contribution and implement it in the engine directly. In case I do, you'll be listed in the credits

<!-- LICENSE -->

## License

Distributed under the Pyglet license and my own license. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Tzyvoski: [E-mail](mailto:miro.salerno@icloud.com)<br>
Project Link: [Link](https://github.com/tzyvoski/Capsian-Engine/)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

-   [Carpal](https://github.com/Carpall) ( for [CapsianLine](https://github.com/Carpall/capsianline) )
-   [Liam](https://github.com/Gyro7) ( for the README and the future Linux version )
-   Lorenzo Bergadano, a friend of mine
-   [Pyglet](http://pyglet.org/) ( for providing the amazing toolkit used to make Capsian possible )
-   [Myself](https://github.com/tzyvoski), Alessandro Salerno, AKA tzyvoski. I was born in Italy and I still live there, and yes, I love Pizza. I study IT in high school and I have been working on Capsian (And its predecessors) for one and a half years.

[contributors-shield]: https://img.shields.io/github/contributors/tzyvoski/Capsian-Engine.svg?style=flat-square
[contributors-url]: https://github.com/tzyvoski/Capsian-Engine/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tzyvoski/Capsian-Engine.svg?style=flat-square
[forks-url]: https://github.com/tzyvoski/Capsian-Engine/network/members
[stars-shield]: https://img.shields.io/github/stars/tzyvoski/Capsian-Engine.svg?style=flat-square
[stars-url]: https://github.com/tzyvoski/Capsian-Engine/stargazers
[issues-shield]: https://img.shields.io/github/issues/tzyvoski/Capsian-Engine.svg?style=flat-square
[issues-url]: https://github.com/tzyvoski/Capsian-Engine/issues
[license-shield]: https://img.shields.io/github/license/tzyvoski/Capsian-Engine.svg?style=flat-square
[license-url]: https://github.com/tzyvoski/Capsian-Engine/blob/master/LICENSE.txt
