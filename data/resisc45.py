from pathlib import Path
import pandas as pd
from datasets import load_dataset, concatenate_datasets

SPLIT_FILE = Path(__file__).parent / "splits" / "resisc45_seed0.csv"

def load_resisc45(split, cache_dir):
    # Merge timm's train + validation + test in a fixed order (31,500 images),
    # then keep only the images assigned to `split` in our stratified split file.
    parts = load_dataset("timm/resisc45", cache_dir=cache_dir)
    full = concatenate_datasets(list(parts.values()))
    class_names = [name.replace("_", " ") for name in full.features["label"].names]
    table = pd.read_csv(SPLIT_FILE)
    idx = table["index"][table["split"] == split].tolist()
    return full.select(idx), class_names