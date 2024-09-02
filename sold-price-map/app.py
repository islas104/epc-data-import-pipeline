import matplotlib
matplotlib.use('Agg')  # Use the Agg backend to avoid GUI issues on macOS
import matplotlib.pyplot as plt
import numpy as np
import os
from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)

# Function to load data from the file
def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            x, y, p = map(int, line.strip().split())
            data.append({"x": x, "y": y, "p": p})
    return data

# Load the data
data_points = load_data('sold-price-data.txt')

# Function to generate the plot
def generate_plot():
    os.makedirs('static', exist_ok=True)  # Ensure the static directory exists
    
    x = np.array([point['x'] for point in data_points])
    y = np.array([point['y'] for point in data_points])
    p = np.array([point['p'] for point in data_points])

    # Define the color map based on percentiles
    colors = np.where(p <= np.percentile(p, 5), 'blue',
                      np.where(p <= np.percentile(p, 25), 'green',
                               np.where(p <= np.percentile(p, 75), 'yellow',
                                        np.where(p <= np.percentile(p, 95), 'orange', 'red'))))

    fig, ax = plt.subplots()
    ax.scatter(x, y, c=colors, s=50)  # Adjust the size here
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Sold Price Map')
    ax.grid(True)  # Add gridlines for better readability

    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close(fig)  # Close the figure to release memory


@app.route('/api/data')
def get_data():
    return jsonify(data_points)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    generate_plot()  # Generate the plot
    plot_url = url_for('static', filename='plot.png')
    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
