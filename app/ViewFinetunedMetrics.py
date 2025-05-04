import streamlit as st
import pandas as pd
import os

MODEL_NAMES = [
    "bart-large-cnn",
    "pegasus-xsum",
    "pegasus-multi_news",
    "pegasus-cnn_dailymail"
]

def load_metrics_csv(model_name):
    file_path = f"data/{model_name}/summary_metrics_{model_name}.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        st.warning(f"Metrics file not found for model: {model_name}")
        return None

def main():
    st.title("📊 Fine-tuned Model Metrics")

    model_name = st.selectbox("Select a model:", MODEL_NAMES)

    df = load_metrics_csv(model_name)

    if df is not None and not df.empty:
        if 'title' not in df.columns:
            st.error("CSV file does not contain a 'title' column for article selection.")
            return

        article_titles = df['title'].unique()
        selected_title = st.selectbox("Select an article by title:", article_titles)

        article_row = df[df['title'] == selected_title].iloc[0].to_dict()

        # Display Title
        st.subheader(f"📝 {selected_title}")

        # Show Content
        if 'content' in article_row:
            st.text_area("Original Content", article_row['content'], height=250)

        # Show Preprocessed Content
        if 'clean_content' in article_row:
            st.text_area("Preprocessed Content", article_row['clean_content'], height=250)

        # Show Summaries
        st.markdown("### 📝 Summaries Comparison")
        if 'reference_summary' in article_row:
            st.markdown(f"**Reference Summary:**\n\n{article_row['reference_summary']}")

        if 'predicted_summary' in article_row:
            st.markdown(f"**Predicted Summary:**\n\n{article_row['predicted_summary']}")

        # Filter metrics (exclude specific columns)
        metric_keys = [key for key in article_row.keys() 
                       if key not in ['title', 'article_idx', 'reference_name', 'content', 'clean_content', 'reference_summary', 'predicted_summary']]

        if metric_keys:
            metrics_df = pd.DataFrame(
                {"Metric": metric_keys, "Value": [article_row[key] for key in metric_keys]}
            )
            st.markdown("### 📐 Evaluation Metrics")
            st.table(metrics_df)

        with st.expander("ℹ️ What do these metrics mean?"):
            st.markdown("""
            ### ✨ Evaluation Metrics Explained

            #### 🔴 **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**

            ROUGE measures the overlap between the predicted summary and the reference summary.

            - **ROUGE-N:** Overlap of n-grams (contiguous sequences of n words).
            - **ROUGE-L:** Longest common subsequence.

            The general formula for ROUGE-N recall is:

            $$
            ROUGE\\text{-}N = \\frac{\\text{Number of overlapping n-grams}}{\\text{Total number of n-grams in reference}}
            $$

            ✅ **Example:**

            - Reference: `"The cat sat on the mat."`
            - Prediction: `"A cat was on the mat."`

            1-grams in reference: `["the", "cat", "sat", "on", "the", "mat"]`  
            1-grams in prediction: `["a", "cat", "was", "on", "the", "mat"]`

            Overlapping 1-grams: `["cat", "on", "the", "mat"]`

            $$
            ROUGE\\text{-}1 = \\frac{4}{6} \\approx 0.6667
            $$

            ---

            #### 🔵 **BLEU (Bilingual Evaluation Understudy)**

            BLEU measures **precision** (how many predicted n-grams are in the reference):

            $$
            BLEU\\text{-}N = BP \\cdot \\exp\\left(\\sum_{n=1}^{N} w_n \\log p_n\\right)
            $$

            where:
            - \( p_n \) = precision for n-grams
            - \( w_n \) = weight (usually equal weights)
            - \( BP \) = brevity penalty (penalizes too-short predictions)

            ✅ **Example:**

            Reference: `"the cat is on the mat"`  
            Prediction: `"the cat the cat on the mat"`

            - Precision drops due to repetition.
            - BLEU penalizes repetitive/ungrammatical outputs.

            ---

            #### 🟢 **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**

            METEOR improves over BLEU by including **stemming**, **synonymy**, and **ordering penalties**.

            It’s calculated as:

            $$
            METEOR = F_{mean} \\cdot (1 - Penalty)
            $$

            - \( F_{mean} \): harmonic mean of precision & recall
            - \( Penalty \): proportional to chunks (longer aligned sequences → lower penalty)

            ✅ **Strength:** sensitive to synonyms (e.g., "boy" ≈ "kid").

            ---

            #### 🟣 **BERTScore**

            BERTScore uses contextual embeddings from BERT:

            - Computes cosine similarity between token embeddings.
            - Captures **semantic similarity** instead of just surface overlap.

            ✅ **Advantage:** can detect paraphrases, latent meaning similarity.

            ---
            
            #### 📝 **Factual Score (QA-based Consistency)**

            **Definition:**
            
            The **factual score** measures how many factual statements in a summary are supported by the original content.

            This implementation uses a **Question Answering (QA) approach:**
            1. Extract **noun phrases** from the summary (e.g., people, organizations, places).
            2. For each noun phrase, automatically generate a question:  
            `"What about <noun phrase>?"`
            3. Use a **QA model** to check if the content can answer the question.
            4. If the content provides a valid answer → count as **factual**.
            
            """)

            st.latex(r"Factual\_Score = \frac{\text{Number of answerable questions}}{\text{Total number of noun phrases}}")
            
            st.markdown("""
            ✅ **Interpretation:**
            
            A factual score of `1.0` → all key facts in the summary are verifiable in the content.  
            A factual score of `0.0` → no key facts are verifiable.


            **Example:**

            Summary:  
            > "Apple announced new iPhones and MacBooks at the September event."

            Generated questions:
            - "What about Apple?"
            - "What about iPhones?"
            - "What about MacBooks?"
            - "What about the September event?"

            For each question, the QA model checks if the original article provides an answer.

            This method approximates **factual consistency** by checking if the summary is supported by the content via automated QA.
             
            ---

            ### 🤔 **What is a hallucination?**

            In summarization, **hallucination** refers to when a model generates content that **was not present or implied in the source text.**

            ❌ Example hallucination:

            Original article:  
            `"The CEO announced record profits."`

            Model summary:  
            `"The CEO announced record profits and plans to acquire a competitor."`  
            → ⚠️ The acquisition part is **invented**.

            > Hallucinations harm trust and factual correctness.

            ---
            ### 💡 **Key Takeaways:**

            - Higher scores ≠ always better → depends on **task & evaluation goal**.
            - Metrics favor **surface-level overlap** → semantic quality may require human review.
            - Always check for **hallucinations**, especially in critical domains (e.g., medical, legal).

            ### 📚 **Bibliography**

            - [ROUGE Metric in NLP: Complete Guide](https://spotintelligence.com/2024/08/12/rouge-metric-in-nlp/)
            - [Intro to ROUGE & how to evaluate summaries](https://www.freecodecamp.org/news/what-is-rouge-and-how-it-works-for-evaluation-of-summaries-e059fb8ac840/)
            - [Understanding BLEU Score](https://codelabsacademy.com/en/blog/understanding-bleu-score-in-nlp-evaluating-translation-quality)
            - [BLEU (Wikipedia)](https://en.wikipedia.org/wiki/BLEU)
            - [BERTScore for LLM Evaluation](https://www.comet.com/site/blog/bertscore-for-llm-evaluation/)
            - Lin, C.-Y. (2004). [ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/).
            - Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). [BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/).
            - Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., & Artzi, Y. (2020). [BERTScore: Evaluating Text Generation with BERT](https://arxiv.org/abs/1904.09675).
            - Banerjee, S., & Lavie, A. (2005). [METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments](https://aclanthology.org/W05-0909/). *ACL Workshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation and/or Summarization*.
            - Kryściński, W., McCann, B., Xiong, C., & Socher, R. (2020). [Evaluating the Factual Consistency of Abstractive Text Summarization](https://arxiv.org/abs/2005.00661).
            - Wang, A., Cho, K., & Lewis, M. (2020). [QAGS: Evaluating Factual Consistency in Summarization with Question Answering](https://arxiv.org/abs/2004.04228).
            """)

    else:
        st.info("No metrics available for this model.")


