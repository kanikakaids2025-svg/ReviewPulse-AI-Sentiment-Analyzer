import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page configuration
st.set_page_config(
    page_title="ReviewPulse AI",
    page_icon="💬",
    layout="centered"
)


# Load the sentiment analysis model
@st.cache_resource
def load_model():
    return SentimentIntensityAnalyzer()


analyzer = load_model()


# Application heading
st.title("ReviewPulse AI")
st.subheader("AI-Powered Product Review Sentiment Analyzer")

st.write(
    "Enter an English product review below. "
    "Our sentiment analysis model will predict whether "
    "the review is Positive, Negative, or Neutral."
)

# Review input
review = st.text_area(
    "Enter your product review",
    placeholder="Example: This product is amazing. I love it!",
    height=130
)


# Analyze button
if st.button("Analyze Sentiment", type="primary"):

    if not review.strip():
        st.warning("Please enter a product review first.")

    else:
        # Get sentiment scores from VADER
        scores = analyzer.polarity_scores(review)
        compound = scores["compound"]

        # Classify the sentiment
        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Display prediction
        st.markdown("### Sentiment Prediction")

        if sentiment == "Positive":
            st.success("Positive 😊")
        elif sentiment == "Negative":
            st.error("Negative 😞")
        else:
            st.info("Neutral 😐")

        # Display scores
        st.markdown("### Sentiment Scores")

        col1, col2, col3 = st.columns(3)

        col1.metric("Positive", f'{scores["pos"]:.2f}')
        col2.metric("Neutral", f'{scores["neu"]:.2f}')
        col3.metric("Negative", f'{scores["neg"]:.2f}')

        st.metric("Compound Score", f"{compound:.3f}")

        st.caption(
            "Compound score ranges from -1 (most negative) "
            "to +1 (most positive)."
        )


# Sample reviews
st.divider()
st.markdown("### Try These Example Reviews")

st.write("**Positive example:**")
st.code("This product is amazing. I love it!")

st.write("**Negative example:**")
st.code("Terrible quality. It stopped working after one day.")

st.write("**Neutral example:**")
st.code("The package arrived today. The box is blue.")

# Model information
st.divider()
st.markdown("### About This Project")

st.write(
    "ReviewPulse AI uses the VADER sentiment analysis model "
    "through the vaderSentiment Python library. It analyzes "
    "English text and classifies the overall sentiment."
)

st.caption(
    "Task 2 - Model or API Integration | "
    "Prototype built with Python and Streamlit."
)