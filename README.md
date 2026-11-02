# foam-g1

Analysis code, input data and manuscript source for

> A. G. Kim, P. E. Nugent, and L. Wang, *Spectroscopy as a probe of spacetime
> foam*, Phys. Rev. D (2026), DOI [10.1103/j7z8-kbvr](https://doi.org/10.1103/j7z8-kbvr);
> arXiv:2610.26766.

## Contents

| File | Purpose |
|---|---|
| `g1.tex`, `references.bib`, `aas_macros.sty`, `*.pdf`/`*.png` figures | Manuscript source (`g1.pdf` is a compiled copy) |
| `grb_multiepoch_fit.py` | GRB 221009A line-width fit to the seven Zhang et al. MeV-line subintervals |
| `grb_chi2_profile_referee.py` | Delta-chi^2 profile in (r_int, r_foam) and the 95% CL limit (figure `grb_chi2_profile.pdf`) |
| `fit_firas.py` | COBE/FIRAS monopole fit for the foam deficit |
| `fisher_firas.py`, `fisher_nextgen.py` | Fisher forecasts for FIRAS, PIXIE, SuperPIXIE, Voyage 2050 |
| `make_cmb_fisher_figures.py` | Detection-SNR figure `cmb_snr_alpha.pdf` |
| `data/` | COBE/FIRAS monopole spectrum and low-frequency covariance matrix (public NASA LAMBDA products; Fixsen et al. 1996, Fixsen 2009) |

## Running

Python 3 with `numpy`, `scipy`, `astropy` and `matplotlib`. Run scripts from the
repository root, e.g. `python fit_firas.py`.

## License

Code: MIT (see `LICENSE`). The FIRAS files in `data/` are public data products
of the COBE/FIRAS mission distributed by NASA LAMBDA.
