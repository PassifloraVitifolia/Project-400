import torch

def zero_shot_accuracy(name, img_emb, text_emb, labels, paper_acc=None):
    # Zero-shot top-1 accuracy: each image gets the class with the highest cosine similarity.
    preds = (img_emb @ text_emb.T).argmax(dim=-1)
    correct = (preds == labels).float()
    acc = correct.mean().item() * 100
    per_class = torch.stack([correct[labels == c].mean() for c in range(text_emb.shape[0])]) * 100
    line = f"{name}: ours {acc:.2f}"
    if paper_acc is not None:
        line += f" | paper {paper_acc} | difference {acc - paper_acc:+.2f}"
    print(line)
    return preds, per_class