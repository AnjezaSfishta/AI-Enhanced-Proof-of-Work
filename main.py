import tkinter as tk
from tkinter import messagebox
from blockchain import create_genesis_block, create_new_block
from mining_node import mine_block
from ai_model import predict_success

class BlockchainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain Mining Optimization")

        self.difficulty = tk.IntVar(value=4)
        self.hash_rate = tk.IntVar(value=1050)
        self.success_rate = tk.DoubleVar(value=0.7)
        self.node_id = 1  # Start with node ID 1

        # GUI Components (No Node ID input needed now)
        tk.Label(root, text="Difficulty:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.difficulty).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Hash Rate:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.hash_rate).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Success Rate:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.success_rate).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(root, text="Predict and Mine", command=self.predict_and_mine).grid(row=3, column=0, columnspan=2, pady=10)

    def predict_and_mine(self):
        difficulty = self.difficulty.get()
        hash_rate = self.hash_rate.get()
        success_rate = self.success_rate.get()

        prediction = predict_success(difficulty, hash_rate, success_rate)
        messagebox.showinfo("Prediction", f"AI Prediction: {prediction}")

        if prediction == "High Success":
            genesis_block = create_genesis_block()
            new_block = create_new_block(genesis_block)
            mine_block(self.node_id, new_block)  # Perdorni id aktuale te nyjës
            messagebox.showinfo("Mining Status", f"Block mined with hash: {new_block.hash}")
            
            # Rritni ID-në e nyjës pas gërmimit të suksesshëm
            self.node_id += 1  
        else:
            messagebox.showinfo("Mining Status", "AI suggests delaying mining.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()
