"""
Referee transparency material for the GRB 221009A line-width fit.

Imports the hardcoded seven-epoch Zhang et al. data and the chi2_dyn /
profile machinery from grb_multiepoch_fit.py WITHOUT modifying it, then:
  (1) prints the clean seven-point table + accuracy assessment of "0.10+/-0.01"
  (2) evaluates chi2_dyn on a 2-D (r_int, r_foam0) grid; locates the global
      minimum, the Delta chi2 = 2.71 contour, and the 95% upper-limit point
  (3) writes a single-column contour figure (PDF + PNG)
  (4) writes a small .txt with the numbers to cite

Does NOT edit g1.tex, references.bib, or grb_multiepoch_fit.py. Does NOT commit.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import grb_multiepoch_fit as fit

E_keV  = fit.E_keV
sig_keV = fit.sig_keV
r_obs  = fit.r_obs
dr_obs = fit.dr_obs
labels = fit.labels
E0_keV = fit.E0_keV
chi2_dyn = fit.chi2_dyn

E_MeV = E_keV / 1e3

# ---------------------------------------------------------------------------
# (1) Seven-point table
# ---------------------------------------------------------------------------
print("=" * 64)
print("(1) SEVEN SUB-INTERVAL MEASUREMENTS USED IN THE FIT")
print("=" * 64)
print(f"{'Interval [s]':<14}{'E [MeV]':>9}{'r_obs':>9}{'sigma_r':>10}")
print("-" * 64)
for i in range(len(labels)):
    print(f"{labels[i]:<14}{E_MeV[i]:>9.2f}{r_obs[i]:>9.3f}{dr_obs[i]:>10.3f}")
print("-" * 64)

w = 1.0 / dr_obs**2
r_wmean = np.sum(w * r_obs) / np.sum(w)
r_wmean_err = 1.0 / np.sqrt(np.sum(w))
chi2_const = np.sum(w * (r_obs - r_wmean)**2)

print(f"Weighted mean r_obs = {r_wmean:.4f} +/- {r_wmean_err:.4f}")
print(f"  unweighted mean   = {np.mean(r_obs):.4f}")
print(f"  sample std (scatter) = {np.std(r_obs, ddof=1):.4f}")
print(f"  min / max r_obs   = {r_obs.min():.4f} / {r_obs.max():.4f}")
print(f"  per-point sigma_r range = {dr_obs.min():.4f} .. {dr_obs.max():.4f}")
print(f"chi2 (constant model, dof=6) = {chi2_const:.2f}  (chi2/dof = {chi2_const/6:.2f})")

# ---------------------------------------------------------------------------
# (2) 2-D chi2 profile over (r_int, r_foam0)
# ---------------------------------------------------------------------------
print()
print("=" * 64)
print("(2) 2-D chi2 PROFILE  chi2_dyn(r_int, r_foam0)")
print("=" * 64)

r_int_grid  = np.linspace(0.02, 0.16, 561)
r_foam_grid = np.linspace(0.0,  0.50, 501)
RINT, RFOAM = np.meshgrid(r_int_grid, r_foam_grid)

CHI2 = np.empty_like(RINT)
for i in range(RINT.shape[0]):
    for j in range(RINT.shape[1]):
        CHI2[i, j] = chi2_dyn(RINT[i, j], RFOAM[i, j],
                              E_keV, r_obs, dr_obs, E0_keV)

# Global minimum on the grid
imin = np.unravel_index(np.argmin(CHI2), CHI2.shape)
chi2_min_grid = CHI2[imin]
rint_min = RINT[imin]
rfoam_min = RFOAM[imin]

# Use the script's own profiled answer for the reported minimum / limits
r_foam_95, chi2_min, r_int_best, r_int_at_max = fit.find_upper_limit(
    chi2_dyn, E_keV, r_obs, dr_obs, E0_keV, delta_chi2=2.71)

DCHI2 = CHI2 - chi2_min

print(f"Global minimum (grid):   r_int = {rint_min:.3f}, r_foam0 = {rfoam_min:.3f}, "
      f"chi2_min = {chi2_min_grid:.2f} (6 dof)")
print(f"Global minimum (profiled): r_int = {r_int_best:.4f}, r_foam0 = 0, "
      f"chi2_min = {chi2_min:.2f} (6 dof)")
print(f"Delta chi2 = 2.71 contour: 95% one-sided (boundary-corrected) level")
print(f"95% upper limit on r_foam0 = {r_foam_95:.4f}  at profiled r_int = {r_int_at_max:.4f}")

# ---------------------------------------------------------------------------
# (3) Contour figure
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.size": 9,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8,
    "figure.dpi": 200,
    "savefig.dpi": 300,
})

fig, ax = plt.subplots(figsize=(3.4, 3.0))

levels = [1.0, 2.71, 4.0]
lstyles = [":", "-", "--"]
lcolors = ["#666666", "#000000", "#666666"]
llabels = [r"$\Delta\chi^2=1$", r"$\Delta\chi^2=2.71$", r"$\Delta\chi^2=4$"]

# Filled background for the allowed (Delta chi2 < 2.71) region
ax.contourf(RINT, RFOAM, DCHI2, levels=[0, 2.71], colors=["#cfe3f7"], alpha=0.6)

cs_handles = []
for lev, ls, lc in zip(levels, lstyles, lcolors):
    cs = ax.contour(RINT, RFOAM, DCHI2, levels=[lev], colors=[lc],
                    linestyles=[ls], linewidths=1.4)
    cs_handles.append(cs)

# Band of the seven measured r_obs values (vertical span over r_int axis)
ax.axvspan(r_obs.min(), r_obs.max(), color="#f5d6a8", alpha=0.45, zorder=0)
ax.axvline(r_wmean, color="#b5651d", lw=1.0, ls="-.", zorder=1)

# Global best fit (on the r_foam0 = 0 boundary)
ax.plot([r_int_best], [0.0], marker="*", ms=12, color="#d62728",
        mec="black", mew=0.5, zorder=5, label="global best fit")

# 95% boundary point (r_foam0^max, r_int_at_max)
ax.plot([r_int_at_max], [r_foam_95], marker="o", ms=6, color="#1f77b4",
        mec="black", mew=0.5, zorder=5, label="95% upper limit")

ax.set_xlabel(r"$r_{\rm int}$")
ax.set_ylabel(r"$r_{\rm foam,0}$")
ax.set_xlim(0.02, 0.16)
ax.set_ylim(0.0, 0.50)

# Build a clean legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
legend_elems = [
    Line2D([0], [0], color=lcolors[i], ls=lstyles[i], lw=1.4, label=llabels[i])
    for i in range(3)
]
legend_elems += [
    Line2D([0], [0], marker="*", color="w", mfc="#d62728", mec="black",
           ms=11, label="best fit"),
    Line2D([0], [0], marker="o", color="w", mfc="#1f77b4", mec="black",
           ms=6, label="95% u.l."),
    Patch(facecolor="#f5d6a8", alpha=0.6, label=r"measured $r_{\rm obs}$ range"),
]
ax.legend(handles=legend_elems, loc="upper right", frameon=True,
          framealpha=0.9, handlelength=1.6, borderpad=0.4)

try:
    plt.rc("text", usetex=False)
except Exception:
    pass

fig.tight_layout(pad=0.4)
fig.savefig("grb_chi2_profile.pdf", bbox_inches="tight")
fig.savefig("grb_chi2_profile.png", bbox_inches="tight")
print()
print("Wrote grb_chi2_profile.pdf and grb_chi2_profile.png")

# ---------------------------------------------------------------------------
# (4) Small .txt of numbers to cite
# ---------------------------------------------------------------------------
with open("grb_chi2_profile.txt", "w") as f:
    f.write("GRB 221009A line-width fit -- referee transparency numbers\n")
    f.write("Source: Zhang et al. (2024) Table A3, seven sub-intervals\n")
    f.write("Generated by grb_chi2_profile_referee.py (imports grb_multiepoch_fit.py)\n")
    f.write("\n")
    f.write("Seven-point table  (interval [s], E [MeV], r_obs, sigma_r):\n")
    for i in range(len(labels)):
        f.write(f"  {labels[i]:<10} {E_MeV[i]:7.2f}  {r_obs[i]:7.3f}  {dr_obs[i]:7.3f}\n")
    f.write("\n")
    f.write(f"weighted mean r_obs   = {r_wmean:.3f} +/- {r_wmean_err:.3f}\n")
    f.write(f"min/max r_obs         = {r_obs.min():.3f} / {r_obs.max():.3f}\n")
    f.write(f"sample scatter (std)  = {np.std(r_obs, ddof=1):.3f}\n")
    f.write(f"per-point sigma_r     = {dr_obs.min():.3f} .. {dr_obs.max():.3f}\n")
    f.write(f"chi2 const model      = {chi2_const:.2f} / 6 dof  (chi2/dof = {chi2_const/6:.2f})\n")
    f.write("\n")
    f.write(f"global min: r_int = {r_int_best:.3f}, r_foam0 = 0, chi2_min = {chi2_min:.2f} (6 dof)\n")
    f.write(f"Delta chi2 = 2.71 : 95% one-sided boundary-corrected level\n")
    f.write(f"95% upper limit: r_foam0_max = {r_foam_95:.3f} at profiled r_int = {r_int_at_max:.3f}\n")
print("Wrote grb_chi2_profile.txt")
