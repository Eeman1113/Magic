import streamlit as st
import random

class Card:
    suits = ['♣','♥', '♠', '♦']
    
    def __init__(self, value, suit):
        if value not in range(1, 14):
            raise ValueError("Card value must be integer from 1 to 13")
        if suit not in self.suits:
            raise ValueError(f"Suit must be one of {self.suits}")
        self.value = value
        self.suit = suit
    
    @property
    def display_value(self):
        named_values = {1: "A", 11: "J", 12: "Q", 13: "K"}
        return named_values.get(self.value, str(self.value))
    
    def __repr__(self):
        return f"{self.display_value}{self.suit}"

def collect_packets(row, *packets):
    """
    Assemble packets such that the selected packet is sandwiched in the middle.
    """
    if len(packets) != 3 or row not in range(1, 4):
        raise ValueError(
            "collect_packets expects a 'row' value from 1-3 and three packets"
        )
    if row == 1:
        return packets[1] + packets[0] + packets[2]
    if row == 2:
        return packets[0] + packets[1] + packets[2]
    return packets[0] + packets[2] + packets[1]

def twenty_one_card_trick():
    # Initialize the deck
    if 'deck_initialized' not in st.session_state:
        deck = [Card(val, suit) for val in range(1, 14) for suit in Card.suits]
        random.shuffle(deck)
        st.session_state.packet = deck[:21]
        st.session_state.round = 0
        st.session_state.deck_initialized = True
        st.session_state.game_over = False
        st.session_state.row_selection = None

    # Display current state of the game
    st.title("🃏 The 21 Card Trick 🎩")
    
    # Check if game is over
    if st.session_state.game_over:
        st.success(f"Your card is the: {st.session_state.packet[10]}")
        if st.button("Play Again"):
            # Reset all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        return

    st.write("Think of a card from the following rows. When you've memorized your card, select the row it's in!")
    
    # Create three columns to display the rows
    col1, col2, col3 = st.columns(3)
    
    first_packet = []
    second_packet = []
    third_packet = []
    
    for i in range(0, 21, 3):
        first_packet.append(st.session_state.packet[i])
        second_packet.append(st.session_state.packet[i + 1])
        third_packet.append(st.session_state.packet[i + 2])
    
    with col1:
        st.write("Row 1")
        for card in first_packet:
            st.write(str(card))
    
    with col2:
        st.write("Row 2")
        for card in second_packet:
            st.write(str(card))
    
    with col3:
        st.write("Row 3")
        for card in third_packet:
            st.write(str(card))
    
    # Row selection
    row_selection = st.radio("Select the row containing your card:", 
                              ["Row 1", "Row 2", "Row 3"])
    
    # Confirm button
    if st.button("Confirm Row"):
        # Convert row selection to number
        row_num = {"Row 1": 1, "Row 2": 2, "Row 3": 3}[row_selection]
        
        # Update packet and increment round
        st.session_state.packet = collect_packets(row_num, first_packet, second_packet, third_packet)
        st.session_state.round += 1
        
        # Check if we've completed 3 rounds
        if st.session_state.round >= 3:
            st.balloons()
            st.session_state.game_over = True
            st.rerun()

def main():
    twenty_one_card_trick()

if __name__ == "__main__":
    main()
