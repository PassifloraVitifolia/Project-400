import torch
import open_clip
from huggingface_hub import hf_hub_download

DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"
TEMPLATE = "a satellite photo of {}."


def load_clip():
    # OpenAI CLIP weights were trained with QuickGELU, so we use the matching config.
    model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32-quickgelu", pretrained="openai")
    tokenizer = open_clip.get_tokenizer("ViT-B-32-quickgelu")
    return model.to(DEVICE).eval(), preprocess, tokenizer


def load_remoteclip(cache_dir):
    # Follows the RemoteCLIP README: empty ViT-B-32 model + RemoteCLIP weights.
    ckpt_path = hf_hub_download("chendelong/RemoteCLIP", "RemoteCLIP-ViT-B-32.pt", cache_dir=cache_dir)
    model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32")
    tokenizer = open_clip.get_tokenizer("ViT-B-32")
    model.load_state_dict(torch.load(ckpt_path, map_location="cpu"))
    return model.to(DEVICE).eval(), preprocess, tokenizer


def encode_images(model, preprocess, images, batch_size=64):
    # Returns L2-normalized image embeddings, one row per image.
    all_emb = []
    for start in range(0, len(images), batch_size):
        batch = torch.stack([preprocess(img.convert("RGB")) for img in images[start:start + batch_size]]).to(DEVICE)
        with torch.no_grad():
            emb = model.encode_image(batch)
        all_emb.append((emb / emb.norm(dim=-1, keepdim=True)).cpu())
    return torch.cat(all_emb)


def encode_texts(model, tokenizer, class_names, template=TEMPLATE):
    # Returns L2-normalized text embeddings, one row per class name.
    text_input = tokenizer([template.format(c) for c in class_names]).to(DEVICE)
    with torch.no_grad():
        emb = model.encode_text(text_input)
    return (emb / emb.norm(dim=-1, keepdim=True)).cpu()