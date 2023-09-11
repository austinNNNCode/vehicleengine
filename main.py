import time
import threading
import tkinter as tk
from engine.engine import Engine
from gasoline.gasoline import GasPortion
from pedal import pedal

def display_stats(engine, label):
    while True:
        label.config(text=f"Rotations: {engine.rotations}")
        time.sleep(1)

def main():
    # Create an instance of the Engine class
    my_engine = Engine.produce_a_standard_benzine_engine()

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Engine Stats")

    # Calculate the user's screen resolution
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window dimensions to match the screen resolution
    root.geometry(f"{screen_width}x{screen_height}")

    # Create a label to display engine stats
    stats_label = tk.Label(root, text="", font=("Arial", 16))
    stats_label.pack(pady=20)

    # Create a thread to display the engine stats
    stats_thread = threading.Thread(target=display_stats, args=(my_engine, stats_label))
    stats_thread.daemon = True
    stats_thread.start()

    # Example: Supply some gas for 10 secondss
    gas_portion = GasPortion(gasoline=my_engine.gasoline, volume_liters=5)
    rotations = my_engine.supply(gas_portion, seconds=10)

    print("Engine is running...")
    root.mainloop()

if __name__ == "__main__":
    main()