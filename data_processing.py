import pandas as pd
import os
import matplotlib.pyplot as plt

def process_data(input_file, output_dir):
    # Read the data file
    data = pd.read_csv(input_file)
    
    # Perform some data processing (example)
    summary = data.describe()
    
    # Save summary report to output directory
    summary_file = os.path.join(output_dir, 'summary_report.csv')
    summary.to_csv(summary_file)

    # Generate a plot (example)
    plt.figure()
    data.hist()
    plt.savefig(os.path.join(output_dir, 'data_histogram.png'))
    plt.close()

if __name__ == '__main__':
    # Define input and output paths
    input_dir = 'input'  # Directory for input files
    output_dir = 'output'  # Directory for output files
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Find the first CSV file in the input directory
    found = False
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_dir, filename)
            process_data(input_file, output_dir)
            found = True
            break  # Stop after processing the first found CSV file

    if not found:
        print("No CSV file found in the input directory.")
