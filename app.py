import random
import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="wide"
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "ties" not in st.session_state:
    st.session_state.ties = 0

if "round_number" not in st.session_state:
    st.session_state.round_number = 0

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "rounds" not in st.session_state:
    st.session_state.rounds = 3

# ---------------------------------------------------------
# GAME FUNCTIONS
# ---------------------------------------------------------

choices = ["Rock", "Paper", "Scissors"]

winning_moves = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}


def determine_winner(player, computer):

    if player == computer:
        return "Tie"

    if winning_moves[player] == computer:
        return "Player"

    return "Computer"


def reset_game():

    st.session_state.history = []
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.round_number = 0
    st.session_state.game_started = False
    st.session_state.game_over = False


def play_round(player_choice):

    if st.session_state.game_over:
        return

    computer_choice = random.choice(choices)

    result = determine_winner(
        player_choice,
        computer_choice
    )

    st.session_state.round_number += 1

    if result == "Player":
        st.session_state.player_score += 1

    elif result == "Computer":
        st.session_state.computer_score += 1

    else:
        st.session_state.ties += 1

    st.session_state.history.append({
        "Round": st.session_state.round_number,
        "Your Choice": player_choice,
        "Computer Choice": computer_choice,
        "Result": result
    })

    if (
        st.session_state.round_number
        >= st.session_state.rounds
    ):
        st.session_state.game_over = True


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🎮 Rock Paper Scissors")

st.markdown(
    "### Professional Python Mini Project"
)

st.divider()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Game Settings")

    player_name = st.text_input(
        "👤 Player Name",
        placeholder="Enter your name"
    )

    rounds = st.selectbox(
        "🎯 Number of Rounds",
        [3, 5]
    )

    if not st.session_state.game_started:

        if st.button(
            "🚀 Start Game",
            width="stretch"
        ):

            if not player_name.strip():

                st.warning(
                    "Please enter your name first."
                )

            else:

                st.session_state.rounds = rounds
                st.session_state.game_started = True
                st.session_state.game_over = False

                st.rerun()

    if st.button(
        "🔄 New Game",
        width="stretch"
    ):

        reset_game()
        st.rerun()

    st.divider()

    st.info(
        "Choose Rock, Paper or Scissors "
        "to play against the computer."
    )

# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏆 Your Score",
        st.session_state.player_score
    )

with col2:
    st.metric(
        "🤖 Computer",
        st.session_state.computer_score
    )

with col3:
    st.metric(
        "🤝 Ties",
        st.session_state.ties
    )

with col4:
    st.metric(
        "🎯 Round",
        f"{st.session_state.round_number}/{st.session_state.rounds}"
    )

st.divider()

# ---------------------------------------------------------
# GAME AREA
# ---------------------------------------------------------

if not st.session_state.game_started:

    st.info(
        "👈 Enter your name and click "
        "**Start Game** to begin."
    )

else:

    if not st.session_state.game_over:

        st.subheader(
            f"🎮 Good luck, {player_name}!"
        )

        st.write(
            "Choose your move:"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                "🪨 Rock",
                width="stretch"
            ):

                play_round("Rock")
                st.rerun()

        with col2:

            if st.button(
                "📄 Paper",
                width="stretch"
            ):

                play_round("Paper")
                st.rerun()

        with col3:

            if st.button(
                "✂️ Scissors",
                width="stretch"
            ):

                play_round("Scissors")
                st.rerun()

    else:

        st.success(
            "🏁 Match Completed!"
        )

        if (
            st.session_state.player_score
            > st.session_state.computer_score
        ):

            st.balloons()

            st.success(
                f"🎉 Congratulations {player_name}! "
                "You won the match!"
            )

        elif (
            st.session_state.computer_score
            > st.session_state.player_score
        ):

            st.error(
                "🤖 Computer won the match!"
            )

        else:

            st.warning(
                "🤝 The match ended in a draw!"
            )

# ---------------------------------------------------------
# ROUND HISTORY
# ---------------------------------------------------------

if st.session_state.history:

    st.divider()

    st.subheader("📜 Round History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        width="stretch",
        hide_index=True
    )

    csv = history_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Match Report",
        data=csv,
        file_name="rock_paper_scissors_report.csv",
        mime="text/csv"
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "🎮 Rock Paper Scissors | "
    "Built with Python & Streamlit | "
    "Author: Sunny Thakur"
)