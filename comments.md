I'll read the referee report and the manuscript, then reconstruct both readings and audit each comment.

Status: markup and unmarked-edit checks are done. Now I'm verifying the compile log and trying to locate the Steinbring papers locally to check the attribution of the 0.650–0.735 range.

**Audit complete.** I reconstructed both readings, diffed the reconstructed original against the version on `main` to catch unmarked edits, checked the compile log and bibliography, and searched the local refs directory for the Steinbring papers (not present, so one attribution question stays open).

## Summary

The referee report contains 13 distinct items. Status: 10 ADDRESSED, 2 PARTIALLY ADDRESSED, 1 NOT ADDRESSED. The one NOT ADDRESSED item is the request for a Fermi-LAT estimate of α, and a reasoned refusal is available. The weakest spots are the handling of the Steinbring "detection" claim, the naming of the relation, and the unmarked appendix skeleton.

Markup was well formed: all 52 change commands balance, and every `\replaced` has its second argument as the old text. One structural defect: the appendix heading, its label, its four paragraph headings, and all five displayed equations are unmarked, so they appear in the ORIGINAL reading as bare content.

## Per-comment audit

| # | Referee item (quote) | Status | Evidence |
|---|---|---|---|
| 1 | "In optical photometry, this is typically refered to as a 'halo.' Mentioning this previous nomenclature" | ADDRESSED | [g1.tex:724](g1.tex:724) replaced, adds "the ``halo'' of optical photometry"; [g1.tex:730](g1.tex:730) added, pedestal as its counterpart |
| 2 | "both AGNs and GRBs have to be viewed ... as potentially extended sources; that should be mentioned" | ADDRESSED | [g1.tex:176](g1.tex:176) added; [g1.tex:248](g1.tex:248) replaced; new Appendix A [g1.tex:1743](g1.tex:1743) onward; [g1.tex:1070](g1.tex:1070) added (clump superposition) |
| 3 | "not merely scattering to the horizon ... any that don't fall within the resolution limits ... The authors can more clearly state that assumption at the outset" | ADDRESSED | [g1.tex:166](g1.tex:166) added paragraph states the deflection assumption and which bounds are immune |
| 4 | "does not sufficiently address how real telescopes actually sense photons ... treated as 'flat' ... assuming a single, monochromatic strength of blurring ... does not report an observed averaged effect over the bandpass" | ADDRESSED | [g1.tex:1833](g1.tex:1833) and [g1.tex:1849](g1.tex:1849) added (Parseval, core-only instruments); [g1.tex:1864](g1.tex:1864) added ("by assumption for LHAASO"); [g1.tex:811](g1.tex:811) added — the instrumental line-spread function is stated and disposed of for both GRB probes. See "Resolution of item 4" below. |
| 5 | "that result does not preclude the *range* ... 0.650 ≤ alpha ≤ 0.735 ... not merely a limit ... effectively dismissed here ... which is incorrect" | ADDRESSED | Reworked on the three-point skeleton — see "Resolution of items 5, 9, 13" below. Intro block rewritten, new Sec. V A 2 paragraph, abstract `\replaced`, conclusions `\added`. |
| 6 | "Steinbring, 2015, ApJ, 802, 38 approach; here uncited" | ADDRESSED | [g1.tex:126](g1.tex:126) added, cites Steinbring2015; entry present in references.bib and in g1.bbl |
| 7 | "not accounting for more-blurred, bluer photons reported in Steinbring, 2007 ... (also uncited)" | PARTIALLY | Citation added at [g1.tex:126](g1.tex:126) and [g1.tex:1871](g1.tex:1871). The specific "bluer photons more blurred" point is never stated; the added text only mentions acceptance limits. |
| 8 | "this should properly be referred to as the Ng-Steinbring relation ... Ng-Perlman would have been ruled out by GRB observations ... what the authors compare to in the abstract, and elsewhere" | PARTIALLY | "Ng--Perlman" dropped from the α label at [g1.tex:43](g1.tex:43), [g1.tex:1602](g1.tex:1602), [g1.tex:1888](g1.tex:1888). It survives unchanged at lines 243, 342, 1354, 1703. "Ng–Steinbring" appears nowhere. The localizability argument against a single-δ interpretation is not acknowledged. A reasoned refusal is plausible: the paper uses the α parametrization (Eq. 1) and the time-interval form, not a PSF model, and Sec. V A 2 line 989 already distinguishes the channels. |
| 9 | "Acknowledgement ... that the Steinbring (2023) result would then be a first detection ... in-orbit observed Fermi LAT PSF is, in fact, broadened" | ADDRESSED | Intro now attributes the window to [12] extended by [13], states its two-sidedness, and reports that those authors read it as a first detection with the LAT PSF foam-broadened. Attributed, not asserted in our voice. |
| 10 | "Can the authors estimate, if incorporating the Ng-Steinbring approach to alpha on the Fermi LAT data, that they too find a value of alpha>0.65 is favoured?" | NOT ADDRESSED | No marked change performs or discusses any LAT analysis. Reasoned refusal available: the paper's GRB line data are Fermi/GBM ([g1.tex:797](g1.tex:797)), the observable is spectral not angular, and Sec. IV B (line 749) already says cross-channel comparison is model-dependent. The width bound α≳0.63 does not contradict α>0.65. |
| 11 | "linewidth-jitter blurring ... already been looked for ... by Cooke et al., 2020 ... some discussion of how this current work compares ... cited" | ADDRESSED | [g1.tex:181](g1.tex:181) added, full comparison paragraph; bib entry present |
| 12 | "reference to [13] ... is now published. It should be ... Proceedings of Science ... CORFU2025 205" | ADDRESSED (outside g1.tex) | references.bib entry SteinbringNg2026 now reads PoS CORFU2025, 205 (2026) and renders so in g1.bbl. No g1.tex markup involved. |
| 13 | "does *not* move (although is consistent with) the currently-known limits ... 2/3 is still favoured; an alpha=0.65 was already ruled out by images of quasars with Hubble" | ADDRESSED | Abstract, Sec. V A 2 and conclusions now all state that the two pedestal-independent floors lie below the window and exclude no part of it, and that the channel is an independent check rather than a competitor. |

## Changes not mapped to any comment

- Abstract [g1.tex:28](g1.tex:28): foam "varying in space and in time" split into transverse decoherence vs temporal jitter. Supports item 3 framing.
- [g1.tex:49](g1.tex:49): deletion of "under the physical Planck-scale pedestal kernel", no replacement.
- [g1.tex:113](g1.tex:113): ℓ to D symbol fix. Already on `main`.
- [g1.tex:266](g1.tex:266): intensity preservation under time warping. Feeds Appendix A.
- [g1.tex:284](g1.tex:284): Ford and Ford–Svaiter light-cone-fluctuation motivation.
- [g1.tex:310](g1.tex:310) to [g1.tex:337](g1.tex:337): new caveat on transverse correlation filtering (Chen–Wen–Ma, Lee–Zurek–Chen), plus deletion of "on which all spectroscopic bounds below rest". Not requested; it weakens the paper's premise in a way the referee did not raise.
- [g1.tex:363](g1.tex:363) and [g1.tex:376](g1.tex:376): C_α paragraph rewritten to remove the "coarse-graining over the source's four-volume" reading.
- [g1.tex:569](g1.tex:569) to [g1.tex:595](g1.tex:595): Wiener–Khinchin normalization prefactor added; the 932-character stationarity paragraph deleted with only a one-sentence replacement.
- [g1.tex:610](g1.tex:610): Mössbauer recoil-free-fraction analogy.
- [g1.tex:660](g1.tex:660), [g1.tex:678](g1.tex:678), [g1.tex:982](g1.tex:982), [g1.tex:1301](g1.tex:1301): "photon number" conservation replaced by "flux" conservation.
- [g1.tex:964](g1.tex:964): the physics claim is reversed. The original said dynamical foam exchanges energy with the photon and the carrier redshift is the signature of that transfer. The revision says integrated flux and mean frequency are exactly conserved. This is a substantive unrequested change.
- [g1.tex:682](g1.tex:682): section retitled "Spectral Analogue of".
- [g1.tex:803](g1.tex:803): t₀≈226 s definition.
- [g1.tex:1264](g1.tex:1264): "normalized".
- [g1.tex:1647](g1.tex:1647): conclusions gain a "third condition" on transverse diffractive averaging. Possibly intended for item 4, but it concerns sub-λ foam structure, not telescope response.

## Problems introduced

1. **Unmarked appendix skeleton.** `\appendix`, the section heading, `\label{app:extended}`, four `\paragraph` headings, and equations at [g1.tex:1751](g1.tex:1751), 1758, 1771, 1791, 1813 carry no markup. In the original reading the appendix shows up as headings and orphan equations. Anyone reading the marked-up PDF will see the derivation's equations as pre-existing.
2. **Other unmarked edits** (harmless but detectable): the comma after Eq. (sigmaphi_cosmo) became a period at [g1.tex:307](g1.tex:307), leaving the original reading as "(D_C). on which all spectroscopic bounds below rest"; label `eq:sigmaDelta_exponential` renamed to `eq:diffVarExt_exponential` at [g1.tex:1312](g1.tex:1312) (never referenced, so no dangling ref); bibliography path changed; the `\verify` macro and protect comments removed.
3. **Normalization inconsistency.** Eq. (WK_obs) at [g1.tex:573](g1.tex:573) now carries a ⟨|E_obs|²⟩ prefactor, but Eq. (Sobs_gauss), the statement "∫S_ped dν = 1−e^{−σ²}" at [g1.tex:659](g1.tex:659), and Eq. (CMB_spectrum) remain unit-normalized.
4. **Internal tension on what is already excluded.** Unchanged [g1.tex:117](g1.tex:117) says PKS 1413+135 only "marginally rules out" α=1/2, while added [g1.tex:144](g1.tex:144) says α≤0.65 is already excluded by galaxy and AGN images. Both now sit in the same section.
5. **TeV bound vs the referee's window.** The added paragraph introduces 0.65 to 0.735 as the admissible window, but the abstract, [g1.tex:875](g1.tex:875), and conclusions keep α≳0.74 as the conditional exclusion of 2/3 with no comment on the overlap. The referee will read this as the "dismissal" they objected to.
6. **Attribution of the window.** The referee credits the range and detection to [12] (Steinbring 2023); the revision credits [13]. Neither paper is in the refs directory, so I could not check which is right.
7. **Overclaim at a seam.** [g1.tex:176](g1.tex:176) says source extension is "immaterial"; Appendix A's own closing sentence [g1.tex:1875](g1.tex:1875) makes it conditional on statistical homogeneity.
8. **Hedge in place of analysis.** "The bounds derived below are independent of that interpretation" at [g1.tex:150](g1.tex:150) is the only reply to the request for a LAT estimate; a referee will read this as non-responsive unless the response letter argues the scope point.
9. **Deleted justification.** The removed paragraph at [g1.tex:582](g1.tex:582) held the T_int ≫ τ_foam condition and the slow-kinematics vs fast-foam separability that the "each epoch" treatment in Sec. V A relies on. Nothing else in the paper now states it.
10. **Unverified specifics in the Cooke paragraph** at [g1.tex:185](g1.tex:185): z≈2.34, Fe II, and "ruled out α≤0.634" should be checked against the paper. Two double-space typos at lines 183 and 189.
11. **Compile status.** The log shows no undefined references or citations. Five hyperref "Token not allowed in a PDF string" warnings are likely from the `\replaced` inside the section title.

## What remains, most consequential first

1. ~~**Reconcile the paper's bounds with the Steinbring window** (items 5, 9, 13).~~ **DONE** — see "Resolution of items 5, 9, 13" below.
2. **Mark up the appendix.** Wrap `\appendix`, the heading, label, paragraph headings, and the five equations in `\added{}` (equations can go inside a single `\added` block, or add a comment noting the whole appendix is new).
3. **Decide on the naming** (item 8). Either adopt "Ng–Steinbring" where the imaging PSF treatment is meant, or keep "Ng–Perlman" for Eq. (1) and add one sentence at [g1.tex:243](g1.tex:243) saying the paper uses only the variance relation and time-interval form, and that the PSF-interpretation critique in Refs. Steinbring 2007, 2015 does not bear on that relation. The response letter then has a defensible refusal.
4. **Answer the LAT question** (item 10) in the paper, not only in the letter. One paragraph in Sec. IV B or the conclusions: the spectroscopic channel cannot be applied to LAT imaging data; the paper's floors are compatible with α>0.65 being favoured; a joint fit is model-dependent per the caveats at [g1.tex:749](g1.tex:749).
5. **State the bluer-photon point** (item 7) in one sentence at [g1.tex:126](g1.tex:126): σ_φ ∝ 1/λ makes bluer photons more blurred, which is the Steinbring 2007 observation, and here it is built into Eq. (3).
6. ~~**Bandpass averaging** (item 4).~~ **DONE** — see "Resolution of item 4" below. The recommendation as originally written was misdirected: the issue is the instrumental line-spread function, not a bandpass average of e^{−σ_φ²(ν)}, and it is disposed of by the resolution numbers rather than by an estimate.
7. **Fix the normalization** in Eq. (Sobs_gauss), line 659, and Eq. (CMB_spectrum) to carry the prefactor, or state once that S is unit-normalized thereafter.
8. **Resolve the "marginally rules out α=1/2" vs "α≤0.65 excluded" tension** at [g1.tex:117](g1.tex:117), and give the 0.65 exclusion its own citation.
9. **Restore a one-line T_int ≫ τ_foam statement** near [g1.tex:580](g1.tex:580).
10. **Soften "immaterial"** at [g1.tex:176](g1.tex:176) to match the appendix's condition, verify the Cooke numbers, and fix the double spaces.

## Resolution of item 4

Applied at [g1.tex:811](g1.tex:811), in Sec. V A immediately after the
definition of `r_obs = 0.111 ± 0.014`:

> The line is resolved.  The BGO energy resolution near an MeV is ≈10% FWHM,
> or σ_LSF/E ≈ 0.04, well below the measured r_obs, and the spectral fits of
> Ref. [YQZhang2024] forward-fold the detector response, so the widths quoted
> there are already corrected for it.  The instrumental line-spread function
> therefore does not enter the fractional-width bound.  Nor does it enter the
> TeV survival bound, which counts photons rather than measuring a profile.

Sourced from Zhang et al. (`refs/2403.12851v2.pdf`), who state the BGO
resolution near MeV is about 10% FWHM, note it is "much less than the detected
spectral line widths", and confirm "the spectral fitting already considered the
detector energy resolution", so their quoted width "is the intrinsic width of
the spectral line itself".  Since FWHM = 2.36σ, σ_LSF/E ≈ 0.042 against
r_obs = 0.111 — the line sits at ≈2.6× the LSF σ.

The three probes answer the referee in three different ways, and only the first
needed new text:

- **GRB line width** — a ratio measurement on a resolved line, with the
  response already deconvolved by the data paper.
- **TeV survival** — a disappearance (counting) measurement; no profile is
  measured, so spectral response is irrelevant.
- **CMB** — see the response-letter note below.

### Note for the response letter

The CMB half of this comment is not addressed in the manuscript and should be
answered in the letter instead, where it costs nothing.  The point: the FIRAS
constraint is not a monochromatic measurement at all.  The fit runs over the
**43 FIRAS channels** ([g1.tex:1226](g1.tex:1226)) with per-channel noise
([g1.tex:1451](g1.tex:1451)), and the ν-dependence of e^{−σ_φ²(ν)} is precisely
the spectral *shape* the fit constrains rather than an assumption imposed on
it.  The bound is therefore insensitive to the response of any individual
channel — it is driven by the deficit's run across the band.


## Resolution of items 5, 9, 13

Taken together, since they are one argument. Presented on a three-point
skeleton, in this order:

1. positive acknowledgement of the previous result, 0.650 ≤ α ≤ 0.735;
2. this measurement is a complementary channel with different assumptions;
3. our results do not exclude that range.

Order matters. An earlier draft led with our own joint-τ_foam result, which
reads as changing the subject; leading with acknowledgement reads as
responsive. Point 2 is also pre-endorsed by the referee, who writes that "a
healthy approach for this field is to consider different ways of calculating
this scattering effect, and so whether those approaches at least give
consistent results."

Two refinements were needed on top of the bare skeleton:

- **Point 1 must carry the detection language**, or item 9 stays open.
  "Acknowledgement" alone is compatible with acknowledging a *limit*, and the
  referee's complaint is precisely that a detection was treated as a limit.
  The text therefore states that the agreement fails for α above *or* below
  the window — the two-sidedness is what makes it a measurement — and reports
  that those authors read it as a first detection with the in-orbit Fermi-LAT
  PSF foam-broadened. Kept attributed ("those authors find / read it as"),
  since neither Steinbring paper is in refs/ and we have no independent check.
- **Point 3 is false if stated flatly.** Our conditional TeV bound is
  α ≳ 0.74 against a window topping out at 0.735, so under near-Planck-refresh
  foam it excludes the *entire* window — and the abstract said so in those
  words. A referee who has read Sec. V A 2 would have caught the
  contradiction. The honest form: the two pedestal-independent bounds exclude
  no part of the window; the TeV bound would, but only for
  τ_foam ≲ 4×10⁻²⁸ s; so if their detection stands, τ_foam ≳ 4×10⁻²⁸ s. The
  one exception becomes a joint constraint on foam refresh rate instead of a
  conflict passed over in silence.

Applied as four edits: intro block rewritten, new Sec. V A 2 paragraph after
the existing channel-separation paragraph, abstract `\replaced`, conclusions
`\added`. ≈290 words.

### Note for the response letter

Three things to say, in the skeleton's order:

1. **Acknowledge.** State plainly that the imaging window is a two-sided
   result with the holographic value at its midpoint, not a one-sided limit,
   and that the manuscript now says so in the introduction, Sec. V A 2, the
   abstract and the conclusions. Quote the added sentences. This is the item
   the referee cares most about — the complaint was that a positive result was
   "effectively dismissed."
2. **Complementary channel.** Use the referee's own words back: they write
   that "a healthy approach for this field is to consider different ways of
   calculating this scattering effect, and so whether those approaches at
   least give consistent results." That is exactly what the paper offers — a
   spectral rather than angular observable, temporal rather than transverse
   correlations, an uncertain source spectrum in place of a known aperture.
   The agreement of two independent routes is the result, not a rival bound.
3. **Non-exclusion, stated honestly.** The two pedestal-independent floors
   (α ≳ 0.63, α ≳ 0.52) lie below the window and exclude no part of it. Do
   *not* claim this for the TeV bound: α ≳ 0.74 exceeds the window's 0.735 and
   would exclude it outright, but only for τ_foam ≲ 4×10⁻²⁸ s. Volunteer that
   rather than letting the referee find it, and give the consequence — if the
   imaging result stands, τ_foam ≳ 4×10⁻²⁸ s. The apparent conflict is then a
   joint constraint on foam refresh rate, which is a result neither channel
   reaches alone.

Also carry over the item-4 note: the FIRAS constraint is not monochromatic,
the fit running over 43 channels with the frequency dependence of the deficit
being the shape it constrains, so it is insensitive to any single channel's
response.

On the correction below, say in the letter that the attribution has been
checked against the source and corrected, and that the description of the
0.735 endpoint has been fixed. Better to own this than to have it noticed.

### Attribution — RESOLVED, and a correction to make

Checked against the full text of arXiv:2603.18277 (obtained and read; the
published PoS version is [13]).

**The window is in [13], not [12].** Both endpoints appear in [13]: "shown for
α = 0.650, z = 0.151" and "The lower limit where blurring must necessarily
rise above the nominal resolution (Φ_Res) then occurs at α = 0.735". The
abstract of Steinbring 2023 [12] gives only a limiting bound of about 1 degree
consistent with holographic QG — no two-sided range. **The referee
mis-attributed the range to [12], and the applied edit followed them.** Revert
the attribution to [13], with [12] cited as the earlier GRB221009A imaging
analysis it builds on.

**The gloss of 0.735 is backwards and must be fixed.** The manuscript says
α ≈ 0.735 is "the point beyond which foam blurring no longer rises above the
nominal instrumental resolution." In [13] it is the *weakest-blurring* end of
the bracket — the curve scaled to the resolution limit: "the weakest possible
Φ_Theta (black on white curve, α = 0.735, z = 0.151) is still consistent with
localization of GRB221009A." The other endpoint, α = 0.650, is the
FoV-scaled case. The two therefore bracket instrumental scaling from field of
view down to resolution limit, and [13] observes that "the half-way point for
α ... happens to coincide with α = 0.667, which is the holographic value
favored by QG models." That midpoint coincidence is the actual structure of
their argument and is worth stating, since it is what makes the window
two-sided in a way that singles out 2/3.

**"First detection" is the referee's phrase, not [13]'s.** The paper never
uses it, and is careful in the other direction about the quasar work: "As
high-z quasars can be partially resolved, this cannot be called a detection of
foam, but did set limits on it." What [13] does claim, and what we should
report instead, is stronger on the evidence and safer to attribute:

- "Clearly, LAT images are not limited by diffraction but scale with it as
  predicted by foam-induced blurring, which sets a resolution floor."
- A section headed "Seeing a Halo Attributable to HQF-Blurring."
- "It is indeed an excellent fit to all of the data."

Reporting these rather than the word "detection" satisfies item 9 — which asks
for acknowledgement and context — without putting a claim in those authors'
mouths that they declined to make themselves.

### Bibliography

All four Steinbring entries are present and correct in references.bib:
Steinbring2007 (ApJ 655, 714), Steinbring2015 (ApJ 802, 38), Steinbring2023
(Galaxies 11, 115), SteinbringNg2026 (PoS CORFU2025, 205). Nothing to add.
