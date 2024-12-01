import streamlit as st
import random

class MindReadingTrick:
    def __init__(self):
        # Enhanced magic cards with more interesting presentation
        self.magic_cards = [
            {"title": "🌟 Cosmic Numbers", "numbers": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], "hint": "Sparkling odd numbers"},
            {"title": "🔢 Binary Signals", "numbers": [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31], "hint": "Digital wave patterns"},
            {"title": "🧩 Puzzle Pieces", "numbers": [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31], "hint": "Interlocking sequences"},
            {"title": "🌈 Color Spectrum", "numbers": [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31], "hint": "Chromatic variations"},
            {"title": "🌙 Lunar Sequence", "numbers": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], "hint": "Moonlight whispers"},
            {"title": "⚡ Energy Nodes", "numbers": [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], "hint": "Power frequencies"},
            {"title": "🌐 Global Network", "numbers": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], "hint": "Connection matrix"}
        ]
        
        # AI-like explanations
        self.ai_explanations = [
            "Quantum probability algorithms detecting your thought pattern...",
            "Neural network analyzing your cognitive number selection...",
            "Decrypting your mental number signature...",
            "Synchronizing thought waves with numeric frequencies...",
            "Calibrating psycho-numeric prediction model...",
            "Extracting hidden numerical consciousness..."
        ]

    def create_card_display(self, card):
        """Create an attractive card display"""
        st.markdown(f"""
        ### {card['title']}
        *{card['hint']}*
        
        <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;  
                     border-radius: 10px; 
                     padding: 15px;">
            {''.join([f'<div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; min-width: 40px; text-align: center;">{num}</div>' for num in card['numbers']])}
        </div>
        """, unsafe_allow_html=True)

    def magic_trick_app(self):
        # Custom CSS for a more magical feel
        st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f6;
            background-image: radial-gradient(rgba(100,100,255,0.1) 10%, transparent 10%);
            background-size: 20px 20px;
        }
        </style>
        """, unsafe_allow_html=True)

        # Initialize session state
        if 'step' not in st.session_state:
            st.session_state.step = 0
            st.session_state.secret_number = 0
            st.session_state.ai_mode = False

        # Title with magic flair
        st.title("🔮 Quantum Mind Reading Experience 🌟")
        
        # AI Mode Toggle
        st.session_state.ai_mode = st.checkbox("🤖 Activate AI Prediction Mode", 
                                               help="Enhance the mystical experience with AI-like narration")

        # Trick progression
        if st.session_state.step < len(self.magic_cards):
            current_card = self.magic_cards[st.session_state.step]
            
            # AI-like narration if mode is on
            if st.session_state.ai_mode:
                st.info(random.choice(self.ai_explanations))
            
            # Display current card
            self.create_card_display(current_card)
            
            # User interaction
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("✅ YES, My Number is Here"):
                    st.session_state.secret_number += current_card['numbers'][0]
                    st.session_state.step += 1
                    st.rerun()
            
            with col2:
                if st.button("❌ NO, My Number is Not Here"):
                    st.session_state.step += 1
                    st.rerun()

        # Final reveal
        else:
            st.balloons()
            
            # Dramatic reveal with AI flair
            if st.session_state.ai_mode:
                st.markdown("### 🌐 Quantum Prediction Complete!")
                st.write("Processing final cognitive resonance...")
                st.write("Synchronizing thought patterns...")
            
            st.title(f"🎉 Your Number is Magically... {st.session_state.secret_number}! 🎉")
            
            # # Explanation of the trick
            # with st.expander("🧠 How Does This Work?"):
            #     st.markdown("""
            #     This trick uses binary representation:
            #     - Each card represents a binary digit
            #     - By tracking which cards contain your number
            #     - We reconstruct the exact number through binary magic! 
            #     """)
            
            # Play Again
            if st.button("🔁 Play Again"):
                st.session_state.step = 0
                st.session_state.secret_number = 0
                st.rerun()

# Run the Streamlit app
def main():
    trick = MindReadingTrick()
    trick.magic_trick_app()

if __name__ == "__main__":
    main()
