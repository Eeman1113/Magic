import streamlit as st
import random

class Card:
    """Represents a playing card with value and suit."""
    SUITS = ['♣', '♥', '♠', '♦']
    FACE_VALUES = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self, value: int, suit: str):
        """
        Initialize a card with validation.
        
        Args:
            value (int): Card value (1-13)
            suit (str): Card suit
        """
        if value not in range(1, 14):
            raise ValueError("Card value must be between 1 and 13")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Must be one of {self.SUITS}")
        
        self.value = value
        self.suit = suit

    @property
    def display_value(self) -> str:
        """
        Return a string representation of card value.
        
        Returns:
            str: Formatted card value
        """
        return self.FACE_VALUES.get(self.value, str(self.value))

    def __repr__(self) -> str:
        """
        String representation of the card.
        
        Returns:
            str: Card display (e.g., '7♥')
        """
        return f"{self.display_value}{self.suit}"

class TwentyOneCardTrick:
    """Implements the 21 Card Trick magic game."""

    def __init__(self):
        """Initialize game state."""
        self.deck = [Card(val, suit) for val in range(1, 14) for suit in Card.suits]
        random.shuffle(self.deck)
        self.packet = self.deck[:21]
        self.round = 0

    def collect_packets(self, row: int, packets: list) -> list:
        """
        Rearrange card packets based on selected row.
        
        Args:
            row (int): Selected row (1-3)
            packets (list): Three card packets
        
        Returns:
            list: Rearranged packet
        """
        if row not in range(1, 4):
            raise ValueError("Row must be between 1 and 3")
        
        # Rearrange packets with selected row in the middle
        if row == 1:
            return packets[1] + packets[0] + packets[2]
        if row == 2:
            return packets[0] + packets[1] + packets[2]
        return packets[0] + packets[2] + packets[1]

    def split_into_rows(self) -> tuple:
        """
        Split packet into three rows.
        
        Returns:
            tuple: Three card rows
        """
        return (
            self.packet[0::3],   # First row
            self.packet[1::3],   # Second row
            self.packet[2::3]    # Third row
        )

    def play_round(self, selected_row: int):
        """
        Play a round of the trick.
        
        Args:
            selected_row (int): User-selected row
        """
        rows = self.split_into_rows()
        self.packet = self.collect_packets(selected_row, rows)
        self.round += 1

def twenty_one_card_trick():
    """Main Streamlit app for the 21 Card Trick."""
    st.title("🃏 The 21 Card Trick 🎩")

    # Initialize or retrieve game state
    if 'game' not in st.session_state:
        st.session_state.game = TwentyOneCardTrick()
        st.session_state.game_over = False

    game = st.session_state.game

    if game.round >= 3:
        st.success(f"Your card is: {game.packet[10]}")
        st.balloons()
        
        if st.button("Play Again"):
            st.session_state.game = TwentyOneCardTrick()
            st.session_state.game_over = False
            st.experimental_rerun()
        return

    st.write("Think of a card from the following rows. Select the row containing your card!")

    # Display rows
    rows = game.split_into_rows()
    cols = st.columns(3)
    row_names = ["Row 1", "Row 2", "Row 3"]

    for i, (row, col) in enumerate(zip(rows, cols)):
        with col:
            st.write(row_names[i])
            for card in row:
                st.write(str(card))

    # Row selection
    selected_row = st.radio("Select the row with your card:", row_names)

    if st.button("Next"):
        row_map = {"Row 1": 1, "Row 2": 2, "Row 3": 3}
        selected_row_num = row_map[selected_row]
        
        game.play_round(selected_row_num)
        st.experimental_rerun()

def main():
    twenty_one_card_trick()

if __name__ == "__main__":
    main()
    
