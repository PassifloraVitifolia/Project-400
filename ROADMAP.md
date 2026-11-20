# Roadmap

`[x]` done · `[ ]` to do

## Approach
1. **Build each level's baselines on their own:** every model and method is reproduced under its own paper's conditions (model, data, metric).
2. **Then connect the levels (section 3):** adapters and shared-protocol decisions are made only after all levels have verified baselines.

## Shared protocol (used in section 3 and for 1a comparisons)
- **Data:** RESISC45 with our stratified split `data/splits/resisc45_seed0.csv` (420 / 140 / 140 images per class). More datasets later.
- **Backbone:** ViT-B-32 wherever available.
- **Prompts:** report both `SINGLE` and `CLIP_RESISC45` (`methods/prompts.py`).
- **Tuning:** thresholds and hyperparameters are chosen on `val` only, never on `test`.

## 0 — Setup
- [x] Environment and model loading (`00_model_check`)
- [x] Shared code: `data/resisc45.py`, `methods/vlm.py`, `methods/prompts.py`, `eval/metrics.py`
- [x] `FINDINGS.md` for results and observations

## 1a — CLIP-like VLMs (image-level naming)
Output: image × class scores. Metric: top-1 accuracy (+ per-class).
- [x] CLIP + RemoteCLIP: reproduce RemoteCLIP Table III on RESISC45 (`1a_01`)
- [ ] GeoRSCLIP: read paper, reproduce (`1a_02`); check `strict=False` loading
- [ ] SkyCLIP: read paper, reproduce (`1a_03`)
- [ ] Optional: RemoteCLIP activation check (GELU vs. QuickGELU)
- [ ] Comparison: all VLMs × both prompt sets, per-class plot (`1a_99`), saved to `results/1a_accuracy.csv`

## 1b — Pixel-based VLMs (pixel-level naming)
Output: pixel × class scores. Metric: mIoU.
- [ ] Pick segmentation dataset(s) used in the papers
- [ ] SegEarth-OV: reproduce mIoU (`1b_01`)
- [ ] SkySense-O: check weight availability, reproduce mIoU (`1b_02`)

## 2a — Image-level rejection
Output: (name, confidence) per image. Metrics: AUROC, FPR95.
Verification setting: CLIP ViT-B/16, ImageNet-1k val (ID) vs. Textures (OOD); extend to more OOD sets if time allows.
- [ ] Data: ImageNet-1k val (gated on Hugging Face) and Textures (DTD)
- [ ] Add AUROC and FPR95 to `eval/metrics.py`
- [ ] MSP and Energy (as reported in the MCM / NegLabel tables) (`2a_01`)
- [ ] MCM (`2a_01`)
- [ ] GL-MCM (`2a_02`)
- [ ] NegLabel (`2a_03`)

## 2b — Cluster-level naming
Output: name per cluster. Metric: cluster naming accuracy (as defined in each paper).
- [ ] SCD: read paper, pick its smallest reported setting, reproduce (`2b_01`)
- [ ] Mean embedding and majority vote as simple baselines in the same setting

## 2c — Cluster-level naming + rejection
Output: (name, confidence) per cluster. Metrics: AUROC, FPR95, AURC.
- [ ] Literature check: any native method? (none found so far; this is the project gap)

## 3 — Connecting levels (shared RS benchmark)
Adapter decisions are made here.
- [ ] Known/unknown class splits on RESISC45: easy and hard, 10 of 45 unknown, 5 seeds (closeness from text embeddings averaged over all 1a VLMs)
- [ ] 1b → 1a: pixel → image adapter (pixel majority, mean score)
- [ ] 1a × 2a: every VLM with every rejection score
- [ ] Clusters on RESISC45: ground-truth clusters (purity 100 / 80 / 60%), then computed clusters (k-means)
- [ ] 1a × 2b: every VLM with every naming strategy
- [ ] 2a → 2c: image scores lifted to clusters
- [ ] 2b → 2c: native cluster confidences (mean-embedding softmax, vote ratio)
- [ ] Full comparison table and weakness analysis → ENS 492 directions

## Adding a new paper
1. Read it: weights, output type, reported numbers and protocol, training data (leakage check).
2. Place it:
   - image/text embeddings → 1a
   - pixel-level outputs → 1b
   - image-level confidence → 2a
   - cluster naming → 2b
   - cluster naming + rejection → 2c
   - prompts or vocabulary → `methods/prompts.py`
3. Reproduce under its own paper's conditions → add a line in its section → connect it in section 3.

## Findings
See `FINDINGS.md`.