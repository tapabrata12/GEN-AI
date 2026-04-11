import streamlit as st
from backend import movie_json

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Movie Review Analyzer",
    page_icon="🎬",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0e0e0e;
    color: #f0ece4;
}

.main { background-color: #0e0e0e; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }

.header-block { border-left: 4px solid #c9a84c; padding-left: 1.2rem; margin-bottom: 2rem; }
.header-block h1 { font-size: 2.6rem; font-weight: 900; color: #f0ece4; margin-bottom: 0.2rem; }
.header-block p { color: #888; font-size: 0.95rem; font-weight: 300; }

.result-card { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; padding: 1.6rem 1.8rem; margin-top: 1.5rem; }
.movie-title { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700; color: #c9a84c; margin-bottom: 0.8rem; }

.tag { display: inline-block; background: #252525; border: 1px solid #3a3a3a; color: #d4c9b0; border-radius: 4px; padding: 0.2rem 0.65rem; font-size: 0.8rem; margin-right: 0.4rem; margin-bottom: 0.4rem; letter-spacing: 0.04em; text-transform: uppercase; }

.sentiment-badge { display: inline-block; border-radius: 20px; padding: 0.25rem 0.9rem; font-size: 0.85rem; font-weight: 500; letter-spacing: 0.05em; }
.sentiment-positive { background: #1a3a1a; color: #6fcf6f; border: 1px solid #2d5a2d; }
.sentiment-negative { background: #3a1a1a; color: #cf6f6f; border: 1px solid #5a2d2d; }
.sentiment-neutral  { background: #2a2a1a; color: #cfcf6f; border: 1px solid #5a5a2d; }

.score-bar-bg { background: #252525; border-radius: 6px; height: 10px; width: 100%; margin-top: 0.4rem; overflow: hidden; }
.score-bar-fill { height: 100%; border-radius: 6px; background: linear-gradient(90deg, #c9a84c, #f0d080); transition: width 0.6s ease; }

.section-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; color: #666; margin-bottom: 0.4rem; margin-top: 1rem; }
.summary-text { color: #c8c0b0; line-height: 1.7; font-size: 0.95rem; }
.thin-divider { border: none; border-top: 1px solid #2a2a2a; margin: 1rem 0; }

.stButton > button { background: #c9a84c; color: #0e0e0e; font-family: 'DM Sans', sans-serif; font-weight: 600; font-size: 0.95rem; border: none; border-radius: 6px; padding: 0.55rem 1.8rem; letter-spacing: 0.04em; transition: background 0.2s; }
.stButton > button:hover { background: #e0c060; color: #0e0e0e; }

.stTextArea textarea { background: #141414 !important; border: 1px solid #2e2e2e !important; color: #f0ece4 !important; border-radius: 8px !important; font-family: 'DM Sans', sans-serif !important; font-size: 0.95rem !important; }
.stTextArea textarea:focus { border-color: #c9a84c !important; box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important; }
</style>
""", unsafe_allow_html=True)


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-block">
    <h1>🎬 Movie Review Analyzer</h1>
    <p>Paste any movie review and extract structured insights instantly.</p>
</div>
""", unsafe_allow_html=True)

user_review = st.text_area(
    "Movie Review",
    placeholder="Paste your movie review here…",
    height=180,
    label_visibility="collapsed",
)

analyze_btn = st.button("Analyze Review")

if analyze_btn:
    if not user_review.strip():
        st.warning("Please enter a movie review before analyzing.")
    else:
        with st.spinner("Analyzing…"):
            try:
                result = movie_json(user_review)

                st.markdown('<div class="result-card">', unsafe_allow_html=True)

                st.markdown(f'<div class="movie-title">{result.get("title", "Unknown Title")}</div>', unsafe_allow_html=True) # type: ignore

                genres = result.get("genre", []) # type: ignore
                if genres:
                    st.markdown('<div class="section-label">Genre</div>', unsafe_allow_html=True)
                    st.markdown("".join(f'<span class="tag">{g}</span>' for g in genres), unsafe_allow_html=True) # type: ignore

                st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    sentiment = result.get("sentiment", "") # type: ignore
                    if sentiment:
                        st.markdown('<div class="section-label">Sentiment</div>', unsafe_allow_html=True)
                        s_lower = sentiment.lower() # type: ignore
                        css_class = (
                            "sentiment-positive" if "positive" in s_lower
                            else "sentiment-negative" if "negative" in s_lower
                            else "sentiment-neutral"
                        )
                        st.markdown(f'<span class="sentiment-badge {css_class}">{sentiment.capitalize()}</span>', unsafe_allow_html=True) # type: ignore

                with col2:
                    score = result.get("score") # type: ignore
                    if score is not None:
                        st.markdown('<div class="section-label">Score</div>', unsafe_allow_html=True)
                        pct = min(max(score / 10 * 100, 0), 100) # type: ignore
                        st.markdown(f"""
                        <div style="font-size:1.4rem;font-weight:700;color:#c9a84c;">{score:.1f}<span style="font-size:0.85rem;color:#666;"> / 10</span></div>
                        <div class="score-bar-bg"><div class="score-bar-fill" style="width:{pct}%"></div></div>
                        """, unsafe_allow_html=True)

                st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

                cast = result.get("cast", []) # type: ignore
                if cast:
                    st.markdown('<div class="section-label">Cast</div>', unsafe_allow_html=True)
                    st.markdown("".join(f'<span class="tag">{c}</span>' for c in cast), unsafe_allow_html=True) # type: ignore
                    st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

                st.markdown('<div class="section-label">Summary</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="summary-text">{result.get("summary", "")}</div>', unsafe_allow_html=True) # type: ignore

                st.markdown('</div>', unsafe_allow_html=True)

                with st.expander("View raw JSON"):
                    st.json(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")