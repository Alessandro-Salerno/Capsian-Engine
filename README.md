[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![](https://tokei.rs/b1/github/Alessandro-Salerno/Capsian-Engine)


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
    -   [Scripting](#scripting)
-   [Getting Started](#getting-started)
    -   [Requirements](#requirements)
-   [License](#license)
-   [Acknowledgements](#acknowledgements)

## Performance

<p>Capsian performs quite well, especially when you consider Python's notorious performance issues. In terms of framerate, batched scenes tend to hover around 1000 - 4000 FPS depending on the resolution, while more dynamic scenes can be a bit harder on the CPU, leading to poor performance.
<br>
</p>
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

### Scripting

<p>Currently, Python is the only option for Capsian scripting. Scripts are organized in an Object-Oriented fashion, with "Script" classes, input handlers and "IndependentComponent" decorators. All Capsian scripts are handled as entity components, as such, they must be attached to an entity, either manually or automatically via the already mentioned "IndependentComponent" decorator. The Capsian Script Manager can help you set up scripts with little to no effort.
  <br>
</p>

<!-- GETTING STARTED -->

### Requirements

* A Python installation (3.7.3 Recommended)
* An OpenGL-Compatible Graphics Card
  
You can install all dependencies using the `prepare.py` script.

<!-- ROADMAP -->

<!-- LICENSE -->

## License

Distributed under the Apache license 2.0. See `LICENSE` for more information.

<!-- CONTACT -->

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

-   [Carpal](https://github.com/Carpall) ( for [Capsianline](https://github.com/Carpall/Capsianline) )
-   [Liam](https://github.com/Gyro7) ( for the README)
-   [lolloberga](https://github.com/lolloberga?tab=overview&from=2022-03-01&to=2022-03-08)
-   [Pyglet](http://pyglet.org/) ( for providing the amazing toolkit used to make Capsian possible )
-   [Myself](https://github.com/tzyvoski)

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
