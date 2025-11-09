from src.dataset import load_dataset

_, _, mapping, _ = load_dataset()
def label_to_emoji(label):

    label_emoji_mapping = dict(zip(mapping['number'], mapping['emoticons']))
    
    return label_emoji_mapping.get(label, "❓")

def labels_to_emojis(labels):
    return [label_to_emoji(label) for label in labels]