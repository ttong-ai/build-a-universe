import numpy as np
import plotly.graph_objs as go


def cross_product_matrix(k):
    """
    Compute the cross-product matrix of a 3D vector k.

    k: the 3D vector (numpy array)
    """
    return np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])


def hopf_fibration_circle(phi, theta, num_points, R=1.0, r=0.5):
    t = np.linspace(0, 2 * np.pi, num_points)
    circle_center_x = R * np.cos(phi)
    circle_center_y = R * np.sin(phi)

    x = r * np.cos(t)
    y = 0.0 * np.ones(t.shape)
    z = r * np.sin(t)
    circle = np.array((x, y, z))

    # phi rotation
    R_phi = np.array(((np.cos(phi), -np.sin(phi), 0), (np.sin(phi), np.cos(phi), 0), (0, 0, 1)))
    circle = np.dot(R_phi, circle)

    # Rotation along the axial direction (cos(phi), sin(phi), 0)
    # Unit direction vector (cos(phi), sin(phi), 0)
    direction = np.array([np.cos(phi), np.sin(phi), 0])

    # Cross-product matrix of the direction vector
    K = cross_product_matrix(direction)

    # Identity matrix
    I = np.eye(3)

    # Rotation matrix around the direction vector by angle theta
    R_theta = I + np.sin(theta) * K + (1 - np.cos(theta)) * np.dot(K, K)
    circle = np.dot(R_theta, circle)

    # Add center location
    circle[0] += circle_center_x
    circle[1] += circle_center_y
    return circle[0], circle[1], circle[2]


num_circles = 50
num_points = 200
R = 1.0
r = 1.5
theta = np.pi / 6
axis_range = R + r + 0.2


def main():
    # Generate circle data
    data = []
    for i in range(num_circles):
        phi = 2 * np.pi * i / num_circles
        x, y, z = hopf_fibration_circle(phi, theta, num_points, R=R, r=r)
        trace = go.Scatter3d(x=x, y=y, z=z, mode="lines")
        data.append(trace)

    # Create layout and figure
    layout = go.Layout(scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",
                                  xaxis=dict(range=[-axis_range, axis_range]),
                                  yaxis=dict(range=[-axis_range, axis_range]),
                                  zaxis=dict(range=[-r, r])))
    fig = go.Figure(data=data, layout=layout)

    # Create frames for the animation
    frames = [
        go.Frame(
            layout=dict(
                scene=dict(
                    camera=dict(
                        eye=dict(
                            x=2 * np.sin(np.pi / 4) * np.cos(2 * np.pi * i / 180),
                            y=2 * np.sin(np.pi / 4) * np.sin(2 * np.pi * i / 180),
                            z=2 * np.cos(np.pi / 4),
                        )
                    )
                )
            )
        )
        for i in range(180)
    ]

    # Add frames to the figure
    fig.frames = frames

    # Add animation settings
    animation_settings = dict(frame=dict(duration=100, redraw=True), fromcurrent=True, showlegend=False)

    # Update layout to include the animation settings
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[dict(label="Play", method="animate", args=[None, animation_settings])],
            )
        ]
    )

    # Show the interactive 3D plot
    fig.show()


if __name__ == "__main__":
    main()
