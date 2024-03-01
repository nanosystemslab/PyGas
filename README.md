# PyGas

[![Release](https://img.shields.io/github/v/release/nanosystemslab/PyGas)](https://img.shields.io/github/v/release/nanosystemslab/PyGas)
[![Build status](https://img.shields.io/github/actions/workflow/status/nanosystemslab/PyGas/main.yml?branch=main)](https://github.com/nanosystemslab/PyGas/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nanosystemslab/PyGas)](https://img.shields.io/github/commit-activity/m/nanosystemslab/PyGas)
[![License](https://img.shields.io/github/license/nanosystemslab/PyGas)](https://img.shields.io/github/license/nanosystemslab/PyGas)
[![DOI](https://zenodo.org/badge/732228171.svg)](https://zenodo.org/doi/10.5281/zenodo.10724912)

PyGas is a Python library designed to provide seamless control and interaction with Alicat flow and pressure meters. With PyGas, you can effortlessly communicate with Alicat devices, retrieve data, and control various parameters to meet your specific application requirements.

- **Github repository**: <https://github.com/nanosystemslab/PyGas/>
- **Documentation** <https://nanosystemslab.github.io/PyGas/>

## Alicat Flow and Pressure Meters

The Alicat M-Series Mass Flow Meters offer detailed flow analytics by simultaneously measuring mass flow, volumetric flow, gas pressure, and temperature for an array of gases, maintaining precision across a spectrum from 0.01% to 100% of full scale. In conjunction with these meters, the P-Series Pressure Transducers provide exact measurements with NIST-traceable accuracy to ±0.125% of full scale for non-corrosive gases. These transducers are adept at measuring both absolute and gauge pressure, featuring swift response times upon activation. They are designed for versatility and accuracy, displaying readings in a selection of engineering units for clear and immediate data interpretation, suitable for diverse applications and environments. You can find more information about these devices on Alicat's official website:

Link to the [Alicat M–Series: Mass Flow Meter](https://www.alicat.com/models/m-gas-mass-flow-meters/)

Link to the [Alicat P–Series: Absolute and Gauge Pressure Transducer](https://www.alicat.com/models/p-absolute-and-gauge-pressure-transducers/)

## Citation

If you use this project in your research, please cite it using the following BibTeX entry:

```bibtex
@software{pygas,
  author       = {Nakamura, Matthew and Murillo Martinez, Andrea, and Renzo Clauido, Josh},
  title        = {PyGas: Python library to control Alicat flow and pressure meter},
  month        = feb,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {10.5281/zenodo.10724912},
  url          = {https://zenodo.org/records/10724913}
}
```

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
