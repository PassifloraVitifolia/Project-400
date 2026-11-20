# Findings

One entry per finding: what we observed, the evidence (notebook + numbers), and what it means for the benchmark. Newest entries at the bottom.

## 1a — CLIP-like VLMs

### F1. Prompt choice changes the CLIP vs. RemoteCLIP gap
- **Observation:** With the single template `"a satellite photo of {}."`, CLIP drops 6.7 points compared to the 18-template ensemble, while RemoteCLIP changes by only 0.8.
- **Evidence:** `1a_01`, RESISC45 test (6,300 images):

  | Model | Single template | 18 templates | Paper |
  |---|---|---|---|
  | CLIP ViT-B-32 | 52.65 | 59.32 | 60.92 |
  | RemoteCLIP ViT-B-32 | 68.54 | 69.37 | 70.33 |

- **Meaning:** The single template exaggerates RemoteCLIP's gain over CLIP (16 vs. 10 points). The benchmark fixes the prompt set for all models and reports both settings.

### F2. RemoteCLIP's stated protocol likely does not match its numbers
- **Observation:** The paper says "standard template-based prompting, e.g., 'a satellite photo of {class name}.'" Only the 18-template ensemble reproduces its CLIP number.
- **Evidence:** F1 table. The "e.g." suggests the stated template may be one of several.
- **Meaning:** Consistent with ensemble prompting, but cannot be confirmed without the authors' evaluation code.

### F3. RemoteCLIP is not better on every class
- **Observation:** CLIP is clearly better on golf course, mobile home park, sea ice, airport, stadium, island, and railway station. CLIP almost fails on medium residential (~4%) and terrace (~1%). Terrace, wetland, and palace are hard for both.
- **Evidence:** `1a_01`, section 3.3 (per-class plot, 18 templates).
- **Meaning:** A single accuracy number hides class-level differences. The benchmark reports per-class results.

## Protocol

### P1. Classification splits are under-reported
- **Observation:** CLIP reports RESISC45 split sizes (3,150 train / 25,200 test) but not the exact images. RemoteCLIP does not report its classification split at all. The `timm/resisc45` test split is not stratified (115–169 images per class).
- **Evidence:** CLIP paper Table 9; RemoteCLIP Section IV; `1a_01` section 1.2.
- **Meaning:** We use and publish our own stratified split (`data/splits/resisc45_seed0.csv`, seed 0).