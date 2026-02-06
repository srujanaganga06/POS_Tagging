from train_hmm import train_hmm
from app import run

print("Training HMM Model...")
train_hmm("training_data.txt")

print("\nPOS Tagging Started")
run()
