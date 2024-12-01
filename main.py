import streamlit as st

def magic_number_trick():
    # Magic cards with numbers
    magic_cards = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
        [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
        [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    ]

    # Streamlit app layout
    st.title("🔮 Mind Reading Number Trick 🎩")
    st.write("Think of a number between 1 and 63. I'll guess it!")

    # Initialize session state for tracking the trick
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.secret_number = 0

    # Instructions
    st.markdown("""
    ### How to Play:
    1. Think of a number between 1 and 63
    2. Look at each card carefully
    3. Click 'YES' if your number appears on the card
    4. Click 'NO' if your number is not on the card
    """)

    # Display current card
    if st.session_state.step < len(magic_cards):
        current_card = magic_cards[st.session_state.step]
        
        st.write(f"### Card {st.session_state.step + 1}")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("YES, my number is on this card"):
                # Add the first number of the card to the secret number
                st.session_state.secret_number += current_card[0]
                st.session_state.step += 1
                st.experimental_rerun()
        
        with col2:
            if st.button("NO, my number is not on this card"):
                st.session_state.step += 1
                st.experimental_rerun()
        
        # Display the current card's numbers
        st.write("Numbers on this card:")
        st.write(', '.join(map(str, current_card)))

    # Final reveal
    else:
        st.balloons()
        st.title(f"🎉 Your number is... {st.session_state.secret_number}! 🎉")
        
        # Reset button
        if st.button("Play Again"):
            st.session_state.step = 0
            st.session_state.secret_number = 0
            st.experimental_rerun()

# Run the Streamlit app
if __name__ == "__main__":
    magic_number_trick()
