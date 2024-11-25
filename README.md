# Pygassed

[![PyPI](https://img.shields.io/pypi/v/pygassed.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/pygassed.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pygassed)][pypi status]
[![License](https://img.shields.io/pypi/l/pygassed)][license]

[![Read the documentation at https://pygassed.readthedocs.io/](https://img.shields.io/readthedocs/pygassed/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/nanosystemslab/pygassed/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/nanosystemslab/pygassed/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/pygassed/
[read the docs]: https://pygassed.readthedocs.io/
[tests]: https://github.com/nanosystemslab/pygassed/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/nanosystemslab/pygassed
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

- Seamless control and interaction with Alicat flow and pressure meters
- Communicate with Alicat devices
- Retrieve data
- Control various parameters to meet your specific application requirements

## Requirements

- Python <4.0, >=3.9

## Alicat Flow and Pressure Meters

The Alicat M-Series Mass Flow Meters offer detailed flow analytics by simultaneously measuring mass flow, volumetric flow, gas pressure, and temperature for an array of gases, maintaining precision across a spectrum from 0.01% to 100% of full scale. In conjunction with these meters, the P-Series Pressure Transducers provide exact measurements with NIST-traceable accuracy to ±0.125% of full scale for non-corrosive gases. These transducers are adept at measuring both absolute and gauge pressure, featuring swift response times upon activation. They are designed for versatility and accuracy, displaying readings in a selection of engineering units for clear and immediate data interpretation, suitable for diverse applications and environments. You can find more information about these devices on Alicat's official website:

Link to the [Alicat M–Series: Mass Flow Meter](https://www.alicat.com/models/m-gas-mass-flow-meters/)

Link to the [Alicat P–Series: Absolute and Gauge Pressure Transducer](https://www.alicat.com/models/p-absolute-and-gauge-pressure-transducers/)

## Installation

You can install _Pygassed_ via [pip] from [PyPI]:

```console
$ pip install pygassed
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [GPL 3.0 license][license],
_Pygassed_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@nanosystemslab]'s [Nanosystems Lab Python Cookiecutter] template.

[@nanosystemslab]: https://github.com/nanosystemslab
[pypi]: https://pypi.org/
[nanosystems lab python cookiecutter]: https://github.com/nanosystemslab/cookiecutter-nanosystemslab
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/nanosystemslab/pygassed/blob/main/LICENSE
[contributor guide]: https://github.com/nanosystemslab/pygassed/blob/main/CONTRIBUTING.md
[command-line reference]: https://pygassed.readthedocs.io/en/latest/usage.html
