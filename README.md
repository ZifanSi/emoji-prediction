# 💬 Text2Moji 😏




## 😏 Feature Overview

- 😄 **Text → Vector**
  - TF–IDF on unigrams + bigrams
  - Configurable vocab size, `min_df`, `max_df`
- 😇 **Text cleaning**
  - Unicode fixes, lowercasing
  - Optional removal of URLs / @mentions / #hashtags
  - Caching of cleaned text for fast iteration
- 🤖 **Models (v1 baselines)**
  - Keyword / Bag-of-Words Weighted Classifier  
  - Nearest-Centroid (cosine) Classifier
- 🤓 **Evaluation**
  - Top-1 / Top-3 / Top-5 accuracy
  - Macro + weighted precision / recall / F1
  - Per-class reports and qualitative top-k examples 

- 😬 **Trained models**
  - Logistic Regression (OvR) on TF–IDF
  - Linear SVM & Multinomial Naive Bayes
- 🤨 **Better UX metrics**
  - Confusion matrices
  - Per-emoji “failure stories” (where the model gets the vibe wrong)
- 😃 **Integration experiments**
  - Minimal REST API (FastAPI/Flask) for `/predict` calls
  - Tiny web demo: type a message, see top-5 emojis live
- 😈 **Stretch goals**
  - fastText-style baseline
  - Tiny transformer/embedding model
  - Browser / VS Code prototype extension for emoji suggestion

---

## 😌 Architecture at a Glance

```text
          ┌───────────────────────┐
          │       CSV Data        │
          │  (TEXT, Label, Map)   │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │     Data Layer        │
          │  load + clean + cache │
          └─────────┬─────────────┘
                    │
          ┌─────────▼─────────────┐
          │   Features Layer      │
          │  TF–IDF (uni/bi-gram) │
          └─────────┬─────────────┘
                    │
      ┌─────────────▼──────────────┐
      │       Model Layer          │
      │ Keyword / Centroid / LR    │
      └─────────────┬──────────────┘
                    │
          ┌─────────▼─────────────┐
          │ Evaluation & Reports  │
          │  top-k, F1, plots, ex │
          └───────────────────────┘
