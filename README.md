# Project 400 — Confidence-Aware Open-Vocabulary Grounding of Remote Sensing Image Clusters

A benchmark of open-vocabulary remote sensing methods under a shared protocol. Every model and method is first verified against its own paper, then evaluated on common splits, prompts, and metrics.

## Phases
- **1a — CLIP-like VLMs** (CLIP, RemoteCLIP, GeoRSCLIP, SkyCLIP): image-level naming, accuracy.
- **1b — Pixel-based VLMs** (SegEarth-OV, SkySense-O): verified with mIoU, then a pixel→image adapter for the shared accuracy table.
- **2a — Image-level rejection** (MSP, energy, MCM, GL-MCM, NegLabel): incomplete vocabulary (easy/hard), AUROC, FPR95.
- **2b — Cluster-level naming** (mean embedding, majority vote, SCD): complete vocabulary, naming accuracy.
- **2c — Cluster-level naming + rejection**: 2a and 2b methods lifted to clusters, AUROC, FPR95, AURC.

## Layout
- `data/` dataset loading and fixed splits (`data/splits/`)
- `methods/` model adapters
- `scores/` confidence scores
- `eval/` metrics
- `notebooks/` named `<phase>_<nn>_<topic>.ipynb`
- `results/` result CSVs