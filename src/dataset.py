import pandas as pd
import numpy as np
import ftfy
import os, sys
import preprocessor as p
import re
from tqdm import tqdm
from cleantext import clean

def load_dataset():
    '''Load dataset CSV files into pandas DataFrames.
    Returns:
        tuple: A tuple containing four pandas DataFrames in the order:
               (train, test, mapping, output_format)
    '''

    script_dir = os.path.dirname(__file__)

    mapping = pd.read_csv(f'{script_dir}/../data/Mapping.csv')
    output_format = pd.read_csv(f'{script_dir}/../data/OutputFormat.csv')
    test = pd.read_csv(f'{script_dir}/../data/Test.csv')
    train = pd.read_csv(f'{script_dir}/../data/Train.csv')

    # Drop first column
    mapping = mapping.drop(mapping.columns[0], axis=1)
    test = test.drop(test.columns[0], axis=1)
    train = train.drop(train.columns[0], axis=1)

    return train, test, mapping, output_format

def load_preprocessed_dataset(remove_urls=True, remove_hashtags=True, remove_mentions=True):
    '''Load preprocessed dataset CSV files into pandas DataFrames.
    Args:
        remove_links (bool): Whether to remove links from the sample.
        remove_hashtag (bool): Whether to remove hashtags from the sample.
        remove_mentions (bool): Whether to remove mentions from the sample.
    Returns:
        tuple: A tuple containing two pandas DataFrames in the order:
               (train, test)
    '''

    script_dir = os.path.dirname(__file__)
    cleaned_train_path = f'{script_dir}/../data/cleaned/cleaned_train_{int(remove_urls)}{int(remove_hashtags)}{int(remove_mentions)}.csv'
    cleaned_test_path = f'{script_dir}/../data/cleaned/cleaned_test_{int(remove_urls)}{int(remove_hashtags)}{int(remove_mentions)}.csv'

    if os.path.exists(cleaned_train_path) and os.path.exists(cleaned_test_path):
        print("Loading preprocessed dataset from disk...")
        train = pd.read_csv(cleaned_train_path)
        test = pd.read_csv(cleaned_test_path)
        return train, test

    tqdm.pandas()

    train, test, _, _ = load_dataset()
    
    def clean_tweet(text):
        opts = [p.OPT.RESERVED]
        if remove_urls:
            opts.append(p.OPT.URL)
        if remove_mentions:
            opts.append(p.OPT.MENTION)
        if remove_hashtags:
            opts.append(p.OPT.HASHTAG)

        p.set_options(*opts)

        re_patterns = {
            r'#\s+': '#',
            r'@\s+': '@'
        }
        for pattern, repl in re_patterns.items():
            text = re.sub(pattern, repl, text)

        text = p.clean(text)
        text = ftfy.fix_text(text)
        text = clean(
            text,
            fix_unicode=True,
            to_ascii=False,
            lower=True,
            no_line_breaks=True,
            no_numbers=False,
            no_punct=False,
        )
        return text

    print("Preprocessing tweets...")
    train['TEXT'] = train['TEXT'].progress_apply(clean_tweet)
    test['TEXT'] = test['TEXT'].progress_apply(clean_tweet)

    print("Saving preprocessed dataset to disk...")
    train.to_csv(cleaned_train_path, index=False)
    test.to_csv(cleaned_test_path, index=False)

    return train, test