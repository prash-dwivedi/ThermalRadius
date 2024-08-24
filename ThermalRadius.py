################################################################################################################
#Melt/Thermal Radius Analysis Script
#Developed by: Prashant Dwivedi
#Description: This procedure outlines the steps for selecting melted regions within a material by excluding atoms
#below the melting temperature, then calculating the radius to encompass approximately 85% of these melted atoms using
#OVITO's scripting capabilities, enabling detailed analysis of material behavior under high-temperature conditions.
################################################################################################################

from ovito.data import *
from ovito.modifiers import ExpressionSelectionModifier
import numpy as np

def modify(frame: int, data: DataCollection, initial_radius=2.0, center=(392.5, 392.5, 600), target_percentage=0.85):
    total_particles = data.particles.count
    target_count = total_particles * target_percentage
    x1, y1, z1 = center

    radius = initial_radius
    selected_count = 0

    while selected_count < target_count:
        eq = f'((Position.X-{x1})^2 + (Position.Y-{y1})^2 + (Position.Z-{z1})^2 <= {radius**2})'
        modifier = ExpressionSelectionModifier(expression=eq)
        data.apply(modifier)

        selection_array = data.particles['Selection'].array
        selected_count = np.sum(selection_array)

        if selected_count >= target_count:
            # Store the required radius as a data attribute
            data.attributes['Radius_to_select_85_percent'] = radius
            print(f"Radius to select approximately 85% of particles: {radius} units")
            break

        radius += 2.5

    if selected_count < target_count:
        print("Unable to reach target selection percentage with the given initial radius.")

# Example usage would require a valid DataCollection 'data' object loaded with particle data.

# Note:
# Step 1: Initially, select the target area by removing unwanted regions such as the rim and ejecta.
#         In this specific case, we remove atoms around a 600 units boundary to focus on the area of interest.
#
# Step 2: Delete all atoms that are below the melting temperature. The melting temperature must be converted
#         to energy units (eV) for this operation. For our purposes, the melting temperature is 3874K, which
#         corresponds to 0.334 eV. This step ensures that only atoms above the melting temperature are considered
#         for further analysis, which is crucial for studying melted regions or phases.
#
# Step 3: Execute this script using the Python script modifier in OVITO. This script calculates the radius
#         required to encompass approximately 85% of the melted particles (those above 0.334 eV). The script
#         dynamically adjusts a spherical selection radius until this percentage is met, focusing on particles
#         that meet the energy criterion established in Step 2.
#
# Step 4: The final radius that selects 85% of the melted (above 0.334 eV) particles can be exported using the
#         Time Series Modifier in OVITO, or it can be directly printed on the screen. This output allows for
#         quantitative analysis of the melted region's size and distribution, facilitating further scientific
#         investigation and characterization of the material's behavior under specific conditions.
#
# This procedure is tailored for analyzing materials under extreme conditions, such as high temperatures, by
# focusing on melted regions. By following these steps, researchers can isolate and study the behavior of
# materials in conditions that mimic melting, providing valuable insights into their properties and dynamics.