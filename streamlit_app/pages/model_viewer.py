import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Parameter extraction with defaults
CL_typ = float(24.0)  # L/h (per 70kg)
V_typ = float(43.7)  # L (per 70kg)
Ka_half_min = float(11.5)  # absorption half-life in minutes
Ka = np.log(2) / (Ka_half_min / 60)  # convert to 1/h
F = float(0.86)  # bioavailability

# Weight covariate adjustment
weight = st.sidebar.slider('Weight (kg)', 40, 120, 70, step=1)
CL_adj = CL_typ * (weight / 70) ** 0.75
V_adj = V_typ * (weight / 70) ** 1.0
# Ensure parameters are finite
if not np.isfinite(CL_adj):
    CL_adj = 5.0
if not np.isfinite(V_adj):
    V_adj = 50.0

# Dosing inputs
dose = st.sidebar.number_input('Dose (mg)', min_value=0.0, value=1000.0, step=100.0)
tau = st.sidebar.number_input('Interval (h)', min_value=1.0, value=12.0, step=1.0)
n_doses = st.sidebar.slider('Number of doses', 1, 20, 8)

# Time grid: 0 to last dose + 2*tau, 1000 points
last_dose_time = (n_doses - 1) * tau
total_time = last_dose_time + 2 * tau
time = np.linspace(0, total_time, 1000)

# Elimination rate constant
k = CL_adj / V_adj  # h^-1

# Simulate concentration (oral first-order absorption)
concentration = []
for t in time:
    c = 0.0
    for i in range(n_doses):
        t_i = i * tau
        if t >= t_i:
            delta_t = t - t_i
            numerator = F * dose * Ka
            denominator = V_adj * (Ka - k)
            if denominator != 0:
                term = (numerator / denominator) * (np.exp(-k * delta_t) - np.exp(-Ka * delta_t))
                c += term
    concentration.append(c)
concentration = np.array(concentration)

# Compute Cmax and Tmax
if dose == 0:
    cmax, tmax = 0.0, 0.0
else:
    cmax = np.max(concentration)
    tmax = time[np.argmax(concentration)]

# Create concentration-time plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=concentration, mode='lines', name='Concentration'))
# Add dose time vertical lines
for i in range(n_doses):
    t_i = i * tau
    fig.add_vline(x=t_i, line_width=1, line_dash='dash', line_color='red')
# Update layout and annotations
fig.update_layout(
    title='Acetaminophen Concentration-Time Curve',
    xaxis_title='Time (h)',
    yaxis_title='Concentration (mg/L)'
)
fig.add_annotation(
    x=tmax, y=cmax,
    text=f'Cmax: {cmax:.2f} mg/L<br>Tmax: {tmax:.2f} h',
    showarrow=True, arrowhead=1, ax=20, ay=-30
)

# Sidebar parameter table
st.sidebar.table({
    'Parameter': ['CL adjusted (L/h)', 'V adjusted (L)', 'Ka (1/h)', 'F'],
    'Value': [round(CL_adj, 4), round(V_adj, 4), round(Ka, 4), round(F, 4)]
})

# Display plot
st.plotly_chart(fig)