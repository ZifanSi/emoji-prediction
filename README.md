# Emoji Prediction Using Sentiment & Context Analysis  

**Course:** COMPSCI/SFWRENG 4AL3 – Final Project Proposal  

**Team Members**  
- Zifan (Frank) Si – siz@mcmaster.ca  
- Xianzhao (Paul) Duan – duanx15@mcmaster.ca  

---

## 📖 Project Motivation  

Emojis are an essential part of modern digital communication, helping users convey tone, emotion, and intention. However, selecting appropriate emojis can be slow and inconvenient, especially in platforms like MS Teams where emojis are spread across many categories.  

Most existing input tools rely on **keyword matching** rather than true **context or sentiment analysis**. For example:  
- Typing *“pizza”* → 🍕 (works).  
- Typing *“I’m so hungry right now”* → no useful suggestion.  

Our project aims to close this gap by developing a **context-aware emoji prediction model** that improves efficiency, expressiveness, and clarity in online communication.  

---

## 📝 Problem Definition  

**Task:** Given partial or full input text, predict the most likely emoji that fits the sentiment and context.  

- **Input:** Text (string)  
- **Output:** Emoji (single-label classification)  
- **Classes:** 20 emojis  
- **Data type:** Text  
- **Task type:** Classification  

**Impact:**  
- Improves communication efficiency.  
- Allows users to express emotions and intentions more accurately.  
- Enhances reader understanding by making hidden emotional cues more explicit.  

---

## 📊 Dataset  

We will use the **[Twitter Emoji Prediction Dataset](https://www.kaggle.com/datasets/hariharasudhanas/twitter-emoji-prediction)**.  

- **Size:** ~70,000 labeled samples  
- **Features:** Single feature (`text`)  
- **Labels:** 20 emojis (single-label classification)  

**Examples:**  

| Text | Label | Emoji |  
|------|-------|-------|  
| "I love my dog more than most humans @ North Gate" | 8 | 😘 |  
| "Dragged my loving husband to a live episode of #hellofromthemagictavern @ Javits Center" | 9 | ❤ |  
| "Happy 4th ya'll! @ Sausalito, California" | 11 | 🇺🇸 |  

---

## 💡 Proposed Solution  

We will implement the project in **two stages**:  

### Stage 1 – Baseline Model  
- Approach: Bag-of-Words / TF-IDF features + Logistic Regression.  
- Library: scikit-learn.  
- Purpose: Capture basic word–emoji associations.  
- Metric: Accuracy.  

### Stage 2 – Advanced Model  
- Approach: LSTM or transformer-based embeddings (PyTorch / Hugging Face).  
- Purpose: Capture deeper context and sentiment.  
- Metric: Macro F1-score (ensures fairness across emojis).  

### Tools & Libraries  
- **scikit-learn** – baseline classification  
- **PyTorch / Hugging Face** – advanced NLP models  
- **Pandas, NumPy, Matplotlib** – preprocessing & visualization  

---

## 📈 Evaluation Plan  

1. Split dataset into training (80%) and testing (20%).  
2. Train baseline model → measure accuracy.  
3. Train advanced model → measure accuracy & F1-score.  
4. Compare results and analyze strengths/weaknesses.  

---

## 📚 References  

1. Hariharasudhan A. S. – *Twitter Emoji Prediction Dataset* (Kaggle).  
   [Link](https://www.kaggle.com/datasets/hariharasudhanas/twitter-emoji-prediction)  

2. Barbieri, F., Ballesteros, M., & Saggion, H. (2017). *Are Emojis Predictable?*  
   Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics (EACL).  
   [PDF](https://aclanthology.org/E17-2117.pdf)  

3. Singh, A., et al. (2023). *Emoji Prediction Using Deep Learning.* IEEE.  
   [DOI](https://ieeexplore.ieee.org/document/10085173)  

---

## 🗓️ Timeline  

- **Week 1–2:** Data preprocessing + baseline model.  
- **Week 3–4:** Advanced model implementation.  
- **Week 5:** Evaluation & results.  
- **Week 6:** Prepare final demo + report.  

---

## ⚙️ Tech Stack  

- Python 3.11  
- scikit-learn  
- PyTorch / Hugging Face  
- Jupyter Notebooks  

---

## 🚀 Future Directions  

- Expand dataset beyond 20 emojis.  
- Test transformer-based models (BERT, RoBERTa).  
- Integrate into a real-time messaging extension (e.g., MS Teams plugin).  

---
