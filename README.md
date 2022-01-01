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
<i><strong>ALL TESTS WERE CONDUCTED ON A GTX 1080 AND INTEL CORE i7 8700K 3.70GHz (Windows 10)</strong></i>
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
-   [Pyinstaller](https://www.pyinstaller.org/)

### Languages

<p>Capsian uses Python as both its scripting language and its source language (TCL, C, C++ and the others you see on the right come from libs and the venv). Until a while ago, there was also support for a custom parsed language called "tzylang", but it's since been removed due to parsing related issues. Other scripting languages will probably be added in the futures (C# Being my main focus), but for now this is what you get.
  <br>
</p>

<!-- GETTING STARTED -->

### Requirements

<p>
To get the libs, just run the `prepare.py` file.
To build an executable, just run the `app build` command in Capsianline (`console.py`) and wait.
It should be able to build for any desktop platform given that you're running on such platform. 

Capsianline will be your best friend while using Capsian. You can use it to run, debug and build your game among other things.
* Debug: `app debug`
* Run: `app run`
* Build: `app build`
You can also use the `package install` command to install packages
  <br>
</p>

<!-- ROADMAP -->

## Older Versions

See the [open issues](https://github.com/tzyvoski/Capsian-Engine/issues) for a list of proposed features (and known issues).<br>
You can find all older versions of Capsian (KeyFire) at: [here](https://tzyvoski.wixsite.com/keyfire)

<!-- LICENSE -->

## License

Distributed under the Pyglet license and the Apache license. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Tzyvoski: [E-mail](mailto:miro.salerno@icloud.com)<br>
Project Link: [Link](https://github.com/tzyvoski/Capsian-Engine/)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

-   [Carpal](https://github.com/Carpall) ( for [Capsianline](https://github.com/Carpall/Capsianline) )
-   [Liam](https://github.com/Gyro7) ( for the README and the future Linux version )
-   [lolloberga](https://github.com/lolloberga?tab=overview&from=2022-03-01&to=2022-03-08)
-   [Pyglet](http://pyglet.org/) ( for providing the amazing toolkit used to make Capsian possible )
-   [Myself](https://github.com/tzyvoski), AKA A. Salerno, AKA tzyvoski

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
