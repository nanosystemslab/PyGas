# PyGas

[![Release](https://img.shields.io/github/v/release/nanosystemslab/pygas)](https://img.shields.io/github/v/release/nanosystemslab/pygas)
[![Build status](https://img.shields.io/github/actions/workflow/status/nanosystemslab/pygas/main.yml?branch=main)](https://github.com/nanosystemslab/pygas/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nanosystemslab/pygas)](https://img.shields.io/github/commit-activity/m/nanosystemslab/pygas)
[![License](https://img.shields.io/github/license/nanosystemslab/pygas)](https://img.shields.io/github/license/nanosystemslab/pygas)
[![DOI](https://zenodo.org/badge/732228171.svg)](https://zenodo.org/doi/10.5281/zenodo.10724912)

PyGas is a Python library designed to provide seamless control and interaction with Alicat flow and pressure meters. With PyGas, you can effortlessly communicate with Alicat devices, retrieve data, and control various parameters to meet your specific application requirements.

- **Github repository**: <https://github.com/nanosystemslab/pygas/>
- **Documentation** <https://nanosystemslab.github.io/pygas/>

## Alicat Flow and Pressure Meters

PyGas is compatible with Alicat flow and pressure meters. You can find more information about these devices on Alicat's official website:

### Alicat M-Series Mass Flow Meter

#### Quick Specifications

- **Mass Flow Ranges**: 0.5 SCCM–5000 SLPM
- **Accuracy**:
  - Standard: ±0.6% of reading
  - High: ±0.5% of reading
- **Measurement Range**: 0.01–100% of full scale
- **Response Time**:
  - Measurement Response: 10 ms
  - Control Response: 30 ms
- **Multi-gas Calibration**: 98+ pre-loaded gases
- **Repeatability**: 
  - Greater of ±0.1% of reading or ±0.02% of full scale
- **Communications**: Analog, RS–232, RS–485, DeviceNet, EtherCAT, EtherNet/IP, TCP/IP, Modbus RTU, PROFIBUS, PROFINET

- [Alicat Mass Flow Meters](https://www.alicat.com/models/m-gas-mass-flow-meters/)
### Alicat P-Series Pressure Transducer

#### Quick Specifications

- **Available Ranges**:
  - PSIA: 0–3000 max; 0–15 min
  - PSIG: 0–3000 max; 0–0.07 min
  - PSID: 2 inH₂O to 500
- **Accuracy**:
  - Standard: ±0.25% of full scale
  - High: ±0.125% of full scale
- **Steady State Control Range**: 0.01–100% of full scale
- **Response Time**:
  - Measurement Response: 10 ms
  - Control Response: 30 ms
- **Repeatability**: 0.08% of full scale
- **Communications**: Analog, RS–232, RS–485, DeviceNet, EtherCAT, EtherNet/IP, Modbus RTU, TCP/IP, PROFIBUS, PROFINET

- [Alicat Pressure Transducers](https://www.alicat.com/models/p-absolute-and-gauge-pressure-transducers/)


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
