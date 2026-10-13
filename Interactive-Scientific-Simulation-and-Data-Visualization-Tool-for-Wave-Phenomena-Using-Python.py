import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

mpl.rcParams["font.family"] = "Times New Roman"

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

initial_amplitude = 1.0
initial_frequency = 1.0

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection="3d")

plt.subplots_adjust(left=0.35, bottom=0.25)

ax_freq = plt.axes([0.35, 0.12, 0.50, 0.03])
ax_amp = plt.axes([0.35, 0.06, 0.50, 0.03])

slider_freq = Slider(
    ax_freq,
    "Frequency",
    0.1,
    3.0,
    valinit=initial_frequency
)

slider_amp = Slider(
    ax_amp,
    "Amplitude",
    0.1,
    3.0,
    valinit=initial_amplitude
)

surf = [None]


def wave_surface(t):
    A = slider_amp.val
    f = slider_freq.val
    R = np.sqrt(X**2 + Y**2)
    Z = A * np.sin(f * R - t)
    return Z


def update(frame):
    if surf[0] is not None:
        surf[0].remove()

    Z = wave_surface(frame * 0.1)

    surf[0] = ax.plot_surface(
        X,
        Y,
        Z,
        cmap="viridis"
    )

    ax.set_title(
        "Water Wave Simulation With Varying Frequency and Amplitude",
        fontweight="bold"
    )

    ax.set_xlabel("X", fontweight="bold")
    ax.set_ylabel("Y", fontweight="bold")
    ax.set_zlabel("Wave Height", fontweight="bold")
    ax.set_zlim(-3, 3)


ani = FuncAnimation(
    fig,
    update,
    frames=400,
    interval=20
)

plt.show()