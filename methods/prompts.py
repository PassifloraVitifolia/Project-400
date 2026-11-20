# Named prompt template sets. Each set records where it comes from.

# Single template used in the RemoteCLIP paper text.
SINGLE = ["a satellite photo of {}."]

# 18-template ensemble from the CLIP repository for RESISC45.
CLIP_RESISC45 = [
    "satellite imagery of {}.", "aerial imagery of {}.", "satellite photo of {}.",
    "aerial photo of {}.", "satellite view of {}.", "aerial view of {}.",
    "satellite imagery of a {}.", "aerial imagery of a {}.", "satellite photo of a {}.",
    "aerial photo of a {}.", "satellite view of a {}.", "aerial view of a {}.",
    "satellite imagery of the {}.", "aerial imagery of the {}.", "satellite photo of the {}.",
    "aerial photo of the {}.", "satellite view of the {}.", "aerial view of the {}.",
]