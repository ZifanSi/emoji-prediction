from src.dataset import load_dataset

def label_to_emoji(label):
    _, _, mapping, _ = load_dataset()

    label_emoji_mapping = dict(zip(mapping['number'], mapping['emoticons']))
    
    return label_emoji_mapping.get(label, "❓")