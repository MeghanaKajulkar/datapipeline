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
    input_file = 'input_data.csv'  # Adjust this based on your setup
    output_dir = 'output'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process the data
    process_data(input_file, output_dir)
