# CDesmos

A C-like programming language that compiles to Desmos.

## Description

CDesmos is an open source programming language that compiles to Desmos using [Desmos.py]("https://github.com/4xvoid/Desmos.py").

## Getting Started

### Dependencies

* Python 3 or later.
* Any web browser capable of opening HTML files.
* 5 (or more) braincells

### Installing

* Download the CDesmos `.\scr` folder.
* Move to desired path.

### Executing program

```
$ python CDesmos.py [Source] [Output]
```

## Help

### Sine Wave Example

main.cd
```python
include "data.cd"
Wave_(5, 5)
```

data.cd
```python
define sin "\\sin"
Wave_(Amplitude_, Frequency_, x) = sin(x * Frequency_) * Amplitude_
```

## Authors

Contributors names and contact info

* [Me]("https://github.com/4xvoid/")

## Version History

* 0.1
    * Added enhanced error handling.
    * New `color "#000000"` function.
* 0.1
    * Initial release.

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [desmoscript](https://github.com/radian628/desmoscript)