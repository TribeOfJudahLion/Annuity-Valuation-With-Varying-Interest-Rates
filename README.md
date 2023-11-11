<br/>
<p align="center">
  <a href="https://github.com//Annuity-Valuation-With-Varying-Interest-Rates">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Maximize Your Annuity Insights: Harness the Power of Varying Interest Rates</h3>

  <p align="center">
    Transforming Annuity Analysis - Where Precision Meets Efficiency
    <br/>
    <br/>
    <a href="https://github.com//Annuity-Valuation-With-Varying-Interest-Rates"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com//Annuity-Valuation-With-Varying-Interest-Rates">View Demo</a>
    .
    <a href="https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/issues">Report Bug</a>
    .
    <a href="https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads//Annuity-Valuation-With-Varying-Interest-Rates/total) ![Contributors](https://img.shields.io/github/contributors//Annuity-Valuation-With-Varying-Interest-Rates?color=dark-green) ![Stargazers](https://img.shields.io/github/stars//Annuity-Valuation-With-Varying-Interest-Rates?style=social) ![Issues](https://img.shields.io/github/issues//Annuity-Valuation-With-Varying-Interest-Rates) ![License](https://img.shields.io/github/license//Annuity-Valuation-With-Varying-Interest-Rates) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario:

**Background**:
A financial analyst at a large pension fund is tasked with evaluating the total present value of a series of annuities. Each annuity consists of a series of cash flows and each cash flow has a corresponding interest rate. The challenge is that the fund has a vast number of these annuities, each with numerous individual cash flows. This data is stored in a large CSV file named 'annuity_data.csv'. The analyst needs a fast and efficient way to calculate the total present value of these annuities, as manual calculation is time-consuming and prone to errors.

**Specific Problem**:
The analyst is looking for a way to:
1. Automate the calculation of present values for a large number of cash flows with varying interest rates.
2. Efficiently process this large dataset to reduce computational time.
3. Ensure that the method used is scalable and can handle future increases in data volume.

### Proposed Solution with the Provided Code:

The provided Python script addresses the problem with the following approach:

1. **Automated Present Value Calculation**:
   - The `present_value` function automates the calculation of the present value for each cash flow. It uses the formula \( \text{cash_flow} / (1 + \text{interest_rate}) \) to calculate the present value, taking into account the varying interest rates for each cash flow.

2. **Efficient Data Processing with Pandas and NumPy**:
   - The script uses Pandas (`pd`) to read and manipulate the data from the CSV file. Pandas is highly efficient for data manipulation and is well-suited for large datasets.
   - NumPy (`np`) is used to split the data into chunks. This allows for processing smaller subsets of the data, which is more manageable and efficient.

3. **Parallel Processing with Multiprocessing**:
   - The script uses the `multiprocessing` module, specifically a `Pool` of worker processes, to enable parallel processing of the data chunks. This significantly speeds up the computation as it utilizes multiple CPU cores to process different chunks of data simultaneously.
   - This approach is particularly beneficial when dealing with large datasets, as it reduces the overall execution time.

4. **Scalability and Flexibility**:
   - The number of chunks (`n_chunks`) can be adjusted based on the size of the data and the available computing resources. This makes the script scalable and adaptable to different data volumes and system capabilities.
   - The script is also flexible to work with any CSV file containing annuity data, making it a versatile tool for the analyst.

5. **Execution Time Measurement**:
   - The script measures the execution time, providing valuable feedback on the efficiency of the data processing. This can help in benchmarking and optimizing performance.

6. **Summation of Results**:
   - After processing, the script sums up all the calculated present values to give the total present value of the annuities, providing the analyst with the desired information.

### How the Script Solves the Problem:

- By automating the present value calculation, the script eliminates manual errors and saves time.
- Parallel processing drastically reduces the time needed to process large datasets.
- The script's scalability ensures it remains effective even as the dataset grows.
- The final output gives the analyst the total present value of the annuities, directly addressing the core requirement of the task.

In conclusion, the script is an effective solution for the financial analyst's needs, offering automation, efficiency, scalability, and accuracy in calculating the total present value of annuities from a large dataset.

This Python script is designed to calculate the total present value of an annuity based on cash flows and interest rates provided in a CSV file. The script uses the Pandas and NumPy libraries for data manipulation, and the multiprocessing module for parallel processing to improve performance. Here's a detailed breakdown of its components and logic:

1. **Importing Libraries**:
   - `pandas` (as `pd`): For data manipulation and analysis.
   - `numpy` (as `np`): For numerical operations on arrays.
   - `Pool` from `multiprocessing`: For parallel processing to utilize multiple CPU cores.
   - `time`: To measure execution time.

2. **Function `present_value(cash_flow, interest_rate)`**:
   - **Purpose**: Calculates the present value of a single cash flow.
   - **Parameters**:
     - `cash_flow`: The cash flow amount.
     - `interest_rate`: The interest rate (discount rate).
   - **Returns**: The present value calculated using the formula \(\frac{\text{cash_flow}}{1 + \text{interest_rate}}\).

3. **Function `process_chunk(chunk)`**:
   - **Purpose**: Processes a chunk of the DataFrame.
   - **Parameter**: `chunk` - A subset of the original DataFrame.
   - **Process**:
     - Applies the `present_value` function to each row of the DataFrame chunk.
     - Uses `.apply()` with a lambda function that calls `present_value` for each row.
   - **Returns**: A Series (or array) of present values for the chunk.

4. **Function `annuity_valuation(csv_file)`**:
   - **Purpose**: Calculates the total present value of an annuity from a CSV file.
   - **Process**:
     - **Reading CSV**: Uses `pd.read_csv` to read the CSV file into a DataFrame.
     - **Chunking Data**:
       - Splits data into chunks using `np.array_split`.
       - `n_chunks` is set to 10 (can be adjusted based on data size and available CPU cores).
     - **Parallel Processing**:
       - Initializes a pool of worker processes using `with Pool() as pool`.
       - Processes each chunk in parallel using `pool.map(process_chunk, chunks)`.
     - **Combining Results**:
       - Concatenates the results from each chunk.
       - Calculates the total present value by summing up all individual present values.
     - **Execution Time**:
       - Measures and prints the execution time.
   - **Returns**: Total present value of the annuity.

5. **Main Execution Block (`if __name__ == '__main__':`)**:
   - Sets the `csv_file` variable to the path of the CSV file.
   - Calls `annuity_valuation` with this CSV file.
   - Prints the total present value of the annuity.

**Key Points**:
- The script is a typical example of how to efficiently process large datasets using parallel processing in Python.
- It specifically addresses financial calculations, making it useful in scenarios like financial modeling or actuarial analysis.
- The use of multiprocessing can significantly reduce computation time, especially for large datasets.

The output results from running the `annuity_valuation_with_varying_interest_rates.py` script in Python provide several key pieces of information. Let's break down each component of the output:

1. **Python Environment Information**:
   - `C:\Users\Rxque\PycharmProjects\tensorflow_training\venv\Scripts\python.exe` indicates the path to the Python executable that was used to run the script. This shows that the script was run in a Python environment located at the specified path, likely a virtual environment created for the project.

2. **Script Path**:
   - `C:\Users\Rxque\PycharmProjects\tensorflow_training\Original Programs\annuity_valuation_with_varying_interest_rates.py` is the path to the Python script that was executed. This tells us the location of the script within the user's file system.

3. **Warning Message**:
   - `FutureWarning: 'DataFrame.swapaxes' is deprecated and will be removed in a future version. Please use 'DataFrame.transpose' instead.`: This is a warning message from the NumPy library, indicating that a function used in the script (`DataFrame.swapaxes`) is deprecated and will be removed in a future version of the library. It suggests using `DataFrame.transpose` as a replacement. This warning doesn't indicate an error; rather, it is an alert for future-proofing the code.

4. **Execution Time**:
   - `Execution Time: 2.935394763946533 seconds`: This indicates the total time taken to execute the script, measured in seconds. The script took approximately 2.94 seconds to complete its execution. This is a relatively quick execution time, suggesting efficient processing, possibly due to the use of multiprocessing.

5. **Total Present Value of Annuity**:
   - `Total Present Value of Annuity: 521981203.68506205`: This is the key output of the script. It represents the total present value of the annuity calculated based on the data in the CSV file. The value is given as a floating-point number, which is approximately 521.98 million. This value is the sum of the present values of all individual cash flows in the annuity, adjusted for their respective interest rates.

6. **Process Exit Code**:
   - `Process finished with exit code 0`: This indicates that the Python script finished its execution successfully. An exit code of 0 typically means that the program ended without any errors.

**Summary**:
- The script successfully calculated the total present value of an annuity, taking about 2.94 seconds to complete.
- The output result, a significant monetary value, suggests that the script may have processed a substantial amount of financial data.
- The warning about the deprecated function usage suggests a need to update the code for compatibility with future versions of the NumPy library.
- The successful exit code confirms that the script ran without encountering any runtime errors.

## Built With

This project is built with a combination of powerful programming tools and libraries, each serving a critical role in its functionality. Below is a detailed description of the components used:

#### 1. Python
- **Version**: [Python 3.X](https://www.python.org/downloads/) (Exact version can vary)
- **Role**: Python serves as the backbone programming language for this project. Known for its simplicity and readability, it's an ideal choice for data processing and financial calculations.

#### 2. Pandas
- **Library**: [Pandas](https://pandas.pydata.org/)
- **Role**: Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation library built on top of Python. In this project, Pandas is primarily used for reading the CSV file into a DataFrame, providing a convenient structure for data manipulation.

#### 3. NumPy
- **Library**: [NumPy](https://numpy.org/)
- **Role**: NumPy, short for Numerical Python, is a fundamental package for scientific computing in Python. It is used here to efficiently handle numerical operations on arrays, particularly for splitting the data into chunks, which is a key part of the parallel processing approach.

#### 4. Multiprocessing
- **Module**: [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- **Role**: The multiprocessing module allows the program to run parallel processes using an API similar to the threading module. It is used to create a pool of worker processes that can handle different parts of the data simultaneously, significantly improving the execution speed for large datasets.

#### 5. Time
- **Module**: [Time](https://docs.python.org/3/library/time.html)
- **Role**: The time module provides various time-related functions. In this project, it is used to measure the execution time of the script, which is crucial for performance monitoring and optimization.

#### 6. CSV File Format
- **Data Format**: Comma-Separated Values (CSV)
- **Role**: CSV is a simple file format used to store tabular data, such as a spreadsheet or database. It is used to store the annuity data that the script processes. The data includes cash flows and their corresponding interest rates for annuity valuation.

### Summary

The synergy of these components creates a robust and efficient environment for financial data processing. Python's versatility, combined with Pandas' data manipulation capabilities, NumPy's numerical efficiency, and the multiprocessing module's parallel processing power, makes this project well-suited for tasks involving large datasets and complex calculations. The use of a CSV file for data input ensures that the tool can be easily integrated into various financial analysis workflows.Here are a few examples.

## Getting Started

This section guides you through setting up and running the annuity valuation script on your local machine for development and testing purposes. Follow these instructions to get a copy of the project up and running.

#### Prerequisites

Before running the script, ensure you have the following installed:

1. **Python**: The script is written in Python, so you will need Python installed on your machine. You can download the latest version from [Python's official website](https://www.python.org/downloads/).

2. **Required Libraries**:
   - **Pandas**: For data manipulation and analysis.
   - **NumPy**: For handling large, multi-dimensional arrays and matrices.
   - **Multiprocessing**: Typically included in the standard Python library.

   You can install these libraries using pip (Python's package installer). Run the following command in your terminal:
   ```
   pip install pandas numpy
   ```

#### Installation

1. **Clone or Download the Repository**:
   - If you are familiar with Git, you can clone the repository using:
     ```
     git clone [repository URL]
     ```
   - Alternatively, you can download the project as a ZIP file and extract it on your computer.

2. **Prepare Your Data File**:
   - Ensure you have a CSV file with annuity data. The file should contain columns for `cash_flow` and `interest_rate`.
   - Place this CSV file in a known directory on your machine.

#### Running the Script

1. **Open Terminal or Command Prompt**:
   - Navigate to the directory where the script is located.

2. **Set Up Your Environment**:
   - If you're using a virtual environment, activate it. If not, ensure that Python and the required libraries are installed globally on your machine.

3. **Run the Script**:
   - Run the script by executing:
     ```
     python annuity_valuation.py
     ```
   - Replace `annuity_valuation.py` with the actual name of the script if it's different.
   - Ensure the script points to the correct CSV file path. Modify `csv_file = 'annuity_data.csv'` in the script with the path to your CSV file.

#### Expected Outcome

- The script will read the CSV file, process the data, and calculate the total present value of the annuities.
- The total present value, along with the execution time, will be printed in the console.

#### Troubleshooting

- **CSV File Not Found**: Ensure the CSV file path in the script matches the actual path where your CSV file is located.
- **Module Not Found Errors**: Make sure all required Python libraries are installed. Re-run the installation commands if necessary.
- **Performance Issues**: Adjust the `n_chunks` variable to better suit your machine's capabilities, especially if you're working with very large datasets.

#### Contributing

- Contributions to enhance the script or its efficiency are always welcome. Please read `CONTRIBUTING.md` for details on the code of conduct and the process for submitting pull requests.

By following these steps, you should be able to successfully run and utilize the annuity valuation script for your financial data analysis.

## Roadmap

See the [open issues](https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Annuity-Valuation-With-Varying-Interest-Rates/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
