import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Probability Simulator App")
st.write("Simulate coin tosses and dice rolls")

# Select experiment
experiment = st.selectbox(
    "Choose an Experiment",
    ["Coin Toss", "Dice Roll"]
)

# Number of trials
trials = st.slider("Select Number of Trials", 1, 1000, 100)

# Run simulation button
if st.button("Run Simulation"):

    # Coin Toss Simulation
    if experiment == "Coin Toss":
        results = [random.choice(["Heads", "Tails"]) for _ in range(trials)]

        heads_count = results.count("Heads")
        tails_count = results.count("Tails")

        experimental_heads = heads_count / trials
        experimental_tails = tails_count / trials

        # Display results
        st.subheader("Frequency")
        st.write(f"Heads: {heads_count}")
        st.write(f"Tails: {tails_count}")

        st.subheader("Probability")
        st.write(f"Experimental Probability of Heads: {experimental_heads:.2f}")
        st.write(f"Experimental Probability of Tails: {experimental_tails:.2f}")
        st.write("Theoretical Probability of Heads: 0.50")
        st.write("Theoretical Probability of Tails: 0.50")

        # Chart
        fig, ax = plt.subplots()
        ax.bar(["Heads", "Tails"], [heads_count, tails_count])
        ax.set_title("Coin Toss Results")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Dice Roll Simulation
    elif experiment == "Dice Roll":
        results = [random.randint(1, 6) for _ in range(trials)]

        counts = {}
        for i in range(1, 7):
            counts[i] = results.count(i)

        st.subheader("Frequency")
        for number, count in counts.items():
            st.write(f"{number}: {count}")

        st.subheader("Probability")
        for number, count in counts.items():
            experimental_probability = count / trials
            st.write(f"Experimental Probability of {number}: {experimental_probability:.2f}")

        st.write("Theoretical Probability of each number: 0.17")

        # Chart
        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values())
        ax.set_title("Dice Roll Results")
        ax.set_xlabel("Dice Number")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)