# Project 400 — Confidence-Aware Open-Vocabulary Grounding of Remote Sensing Image Clusters

A benchmark of open-vocabulary remote sensing methods under a shared protocol. Every model and method is first verified against its own paper, then evaluated on common splits, prompts, and metrics.

## Phases
- **1a — CLIP-like VLMs** (CLIP, RemoteCLIP, GeoRSCLIP, SkyCLIP): scene classification, accuracy.
- **1b — Pixel-based VLMs** (SegEarth-OV, SkySense-O): segmentation (mIoU), then a pixel→image adapter for the shared accuracy table.
- **2 — Cluster-level methods**: naming strategies × confidence scores, incomplete vocabulary (easy/hard), AUROC, FPR95, AURC.

## Layout
- `data/` dataset loading and fixed splits (`data/splits/`)
- `methods/` model adapters
- `scores/` confidence scores
- `eval/` metrics
- `notebooks/` named `<phase>_<nn>_<topic>.ipynb`
- `results/` result CSVs