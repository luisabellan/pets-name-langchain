import streamlit as st
import langchain_helper as lch
import textwrap

st.set_page_config(page_title="Pets Name Generator", page_icon="🐶", layout="centered")
st.title("🐶 Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Rat", "Snake", "Lizard", "Cow", "Monkey"))

animal_labels = {
    "Dog": "What color is your dog?",
    "Cat": "What color is your cat?",
    "Hamster": "What color is your hamster?",
    "Rat": "What color is your rat?",
    "Snake": "What color is your snake?",
    "Lizard": "What color is your lizard?",
    "Cow": "What color is your cow?",
    "Monkey": "What color is your monkey?",
}

pet_color = st.sidebar.text_area(
    label=animal_labels[animal_type],
    max_chars=25,
)
response = lch.generate_pet_name(animal_type, pet_color)
st.text(textwrap.fill(response['pet_name'], width=80,  fix_sentence_endings=True, replace_whitespace=False, drop_whitespace=True))