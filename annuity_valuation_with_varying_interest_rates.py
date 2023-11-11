import pandas as pd
import numpy as np
from multiprocessing import Pool
import time

def present_value(cash_flow, interest_rate):
    """
    Calculate the present value of a single cash flow.
    """
    return cash_flow / (1 + interest_rate)

def process_chunk(chunk):
    """
    Process a chunk of the DataFrame.
    """
    return chunk.apply(lambda row: present_value(row['cash_flow'], row['interest_rate']), axis=1)

def annuity_valuation(csv_file):
    """
    Calculate the total present value of an annuity from a CSV file.
    """
    start_time = time.time()

    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Split data into chunks for multiprocessing
    n_chunks = 10  # Adjust based on your data size and available cores
    chunks = np.array_split(data, n_chunks)

    # Use multiprocessing to process each chunk
    with Pool() as pool:
        results = pool.map(process_chunk, chunks)

    # Combine results and sum up the present values
    total_present_value = np.sum(np.concatenate(results))

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")
    return total_present_value

if __name__ == '__main__':
    csv_file = 'annuity_data.csv'  # Replace with your CSV file path
    total_value = annuity_valuation(csv_file)
    print(f"Total Present Value of Annuity: {total_value}")
