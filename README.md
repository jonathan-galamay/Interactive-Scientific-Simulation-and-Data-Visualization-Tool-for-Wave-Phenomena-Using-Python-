# Interactive Scientific Simulation and Data Visualization Tool for Wave Phenomena Using Python

## Project Overview

This project is an interactive scientific simulation and data visualization tool developed in Python to model and visualize radial wave propagation across a two-dimensional surface. Using a three-dimensional animated visualization, the simulation demonstrates how wave amplitude changes across space and time.

The application includes interactive sliders that allow users to adjust wave frequency and amplitude in real time, making it useful for exploring wave behavior and scientific visualization concepts.

## Features

- Real-time 3D animation of radial wave propagation
- Interactive frequency and amplitude sliders
- Adjustable wave parameters during simulation
- Scientific visualization using NumPy and Matplotlib
- Dynamic surface rendering with color mapping

## Mathematical Model

The simulated wave surface is represented by:

\[
Z = A\sin(fR-t)
\]

where:

- \(Z\) is the wave displacement
- \(A\) is the wave amplitude
- \(f\) is the wave frequency parameter
- \(R=\sqrt{X^2+Y^2}\) is the radial distance from the origin
- \(t\) is time

The model produces concentric wave patterns that propagate across the surface.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/jonathan-galamay/Interactive-Scientific-Simulation-and-Data-Visualization-Tool-for-Wave-Phenomena-Using-Python-.git
cd Interactive-Scientific-Simulation-and-Data-Visualization-Tool-for-Wave-Phenomena-Using-Python-
```

### 2. Create and activate a virtual environment (optional)

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the simulation

```powershell
python Interactive-Scientific-Simulation-and-Data-Visualization-Tool-for-Wave-Phenomena-Using-Python.py
```

Use the sliders in the visualization window to adjust the wave frequency and amplitude.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Matplotlib animation and interactive widgets

## Project Purpose

This project explores computational modeling and scientific data visualization through an interactive representation of wave phenomena. It demonstrates the use of mathematical functions, numerical computation, animation, and interactive controls to communicate scientific concepts visually.

## Author

**Jonathan A. Galamay**  
BS Physics Graduate  
Cagayan State University – Carig Campus
