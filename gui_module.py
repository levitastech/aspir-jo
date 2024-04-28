# gui_module.py
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from core_module import fetch_years, fetch_indices, download_file


class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JORADP Downloader")
        self.destination_dir = os.path.join(os.path.expanduser("~"), "Documents", "joradp")
        self.setup_ui()

    def setup_ui(self):
        # Set up UI components
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Year dropdown
        year_label = ttk.Label(main_frame, text="Select Year:")
        year_label.grid(row=0, column=0, sticky="w")
        self.year_dropdown = ttk.Combobox(main_frame, state="readonly")
        self.year_dropdown.grid(row=0, column=1, sticky="we")
        self.year_dropdown.bind("<<ComboboxSelected>>", self.fetch_indices)

        # Index dropdown
        index_label = ttk.Label(main_frame, text="Select Index:")
        index_label.grid(row=1, column=0, sticky="w")
        self.indices_dropdown = ttk.Combobox(main_frame, state="readonly")
        self.indices_dropdown.grid(row=1, column=1, sticky="we")

        # Destination directory
        dest_dir_label = ttk.Label(main_frame, text="Destination Directory:")
        dest_dir_label.grid(row=2, column=0, sticky="w")
        self.dest_dir_entry = ttk.Entry(main_frame)
        self.dest_dir_entry.grid(row=2, column=1, sticky="we")
        self.dest_dir_entry.insert(0, self.destination_dir)
        browse_button = ttk.Button(main_frame, text="Browse", command=self.browse_directory)
        browse_button.grid(row=2, column=2, sticky="e")

        # Download buttons
        download_button = ttk.Button(main_frame, text="Download Publication", command=self.download_publication)
        download_button.grid(row=3, column=0, pady=10)
        download_all_button = ttk.Button(main_frame, text="Download All for Year", command=self.download_all_for_year)
        download_all_button.grid(row=3, column=1, pady=10)

        # Fetch available years and populate the year dropdown
        years = fetch_years()
        self.year_dropdown.config(values=years)

    def browse_directory(self):
        selected_dir = filedialog.askdirectory(initialdir=self.destination_dir)
        if selected_dir:
            self.dest_dir_entry.delete(0, "end")
            self.dest_dir_entry.insert(0, selected_dir)

    def fetch_indices(self, event):
        # Fetch indices for the selected year
        selected_year = self.year_dropdown.get()
        indices = fetch_indices(int(selected_year))

        # Populate the indices dropdown
        self.indices_dropdown.config(values=indices)

    def download_publication(self):
        # Get selected year, index, and destination directory
        selected_year = self.year_dropdown.get()
        selected_index = self.indices_dropdown.get()
        destination_dir = self.dest_dir_entry.get()

        # Call download_file function from core_module
        download_file(int(selected_year), int(selected_index), destination_dir)

        # Display success/error message
        # ...

    def download_all_for_year(self):
        # Get selected year and destination directory
        selected_year = self.year_dropdown.get()
        destination_dir = self.dest_dir_entry.get()

        # Fetch indices for the selected year
        indices = fetch_indices(int(selected_year))

        # Download each publication for the selected year
        for index in indices:
            download_file(int(selected_year), index, destination_dir)

        # Display success message
        # ...


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()
