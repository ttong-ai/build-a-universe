import plotly.graph_objs as go
import plotly.io as pio
import numpy as np

# Define the curve to be rotated
theta = np.linspace(0.1, 20, 100)
x = 1 / theta
y = theta

# Create mesh grid for the surface coordinates
theta_mesh, phi_mesh = np.meshgrid(theta, np.linspace(0, 2 * np.pi, 100))
x_mesh = (1 / theta_mesh) * np.cos(phi_mesh)
y_mesh = (1 / theta_mesh) * np.sin(phi_mesh)
z_mesh = theta_mesh

# Create surface object and add it to a figure object
surface = go.Surface(x=x_mesh, y=y_mesh, z=z_mesh, colorscale='Viridis', name="Gabriel's Horn")
fig = go.Figure(surface)

# Set layout parameters and show the plot
fig.update_layout(
    title="Gabriel's Horn",
    scene=dict(
        xaxis_title='X axis',
        yaxis_title='Y axis',
        zaxis_title='Z axis'
    )
)

# Use the fig object from the previous code
html_string = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
print(html_string)
fig.show()
