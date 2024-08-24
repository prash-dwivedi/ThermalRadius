# **Melt/Thermal Radius Analysis Script**

### **Overview**
The **Melt/Thermal Radius Analysis Script** is a powerful tool developed for detailed analysis of material behavior under high-temperature conditions such as high velocity impact. This script is designed to select melted regions within a material by excluding atoms that are below the melting temperature, then calculating the radius needed to encompass approximately 85% of these melted atoms using OVITO's scripting capabilities. This method allows for precise analysis of material properties and behaviors, particularly in extreme conditions where phase transitions like melting are significant.

### **Features**
- **Automated Selection of Melted Regions**: The script initially excludes atoms below the melting temperature, isolating regions of interest for analysis.
- **Dynamic Radius Calculation**: The script iteratively adjusts a spherical selection radius to include approximately 85% of the melted particles, ensuring a focus on the most relevant material regions.
- **High-Temperature Material Analysis**: By focusing on melted regions, the script facilitates the study of material behavior under extreme thermal conditions, offering insights into phase transitions, thermal stress responses, and other critical phenomena.

<img src="https://github.com/user-attachments/assets/042fe811-f5cf-4c59-ba25-6a6a701b7fc0" alt="Fig_3_1" width="400"/>

### **How It Works**
1. **Target Area Selection**: 
   - The first step involves selecting the target area by removing unwanted regions, such as the rim and ejecta, from the analysis. In this specific case, atoms around a 600-unit boundary are removed to focus on the central area of interest.

2. **Exclusion of Non-Melted Atoms**: 
   - Atoms below the melting temperature are excluded from further analysis. The melting temperature, converted to energy units (eV), is set at 0.334 eV, corresponding to 3874K. This step ensures that only atoms above the melting threshold are considered, which is crucial for analyzing melted regions or phases.

3. **Execution and Radius Calculation**: 
   - The script is executed using the Python script modifier in OVITO. It calculates the radius required to encompass approximately 85% of the melted particles that meet the energy criterion established in the previous step. The radius is dynamically adjusted until the target percentage is met.

4. **Output**: 
   - The final radius that selects 85% of the melted particles can be exported using the Time Series Modifier in OVITO or printed directly on the screen. This output enables quantitative analysis of the size and distribution of the melted region, facilitating further scientific investigation and characterization of the material's behavior under specific high-temperature conditions.

### **Usage**
This script is ideal for researchers studying materials subjected to extreme temperatures, where understanding the behavior of melted regions is critical. It can be applied in fields such as material science, metallurgy, and engineering and high velocity impact where phase transitions and thermal stress analysis are vital.

### **Citation**
If you use this script in your research, please cite the following articles:

- DOI: [10.1016/j.jnucmat.2024.155289](https://doi.org/10.1016/j.jnucmat.2024.155289)
- DOI: [10.1016/j.jnucmat.2024.155042](https://doi.org/10.1016/j.jnucmat.2024.155042)

*Developed by Prashant Dwivedi.*

