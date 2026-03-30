import streamlit as st
from astar import a_star
from cities import graph, heuristic

st.set_page_config(page_title="AI Parcel Delivery System")

st.title(" AI Parcel Delivery Route Finder")

st.write("Find the best delivery route between cities using A* Algorithm")

cities = list(graph.keys())

# Dropdowns
start = st.selectbox(" Pickup Location (Parcel From)", cities)
goal = st.selectbox(" Delivery Location (Parcel To)", cities)

# Button
if st.button("Find Delivery Route"):
    
    if start == goal:
        st.warning("Pickup and delivery location cannot be same")
    else:
        path, cost = a_star(graph, heuristic, start, goal)

        if path:
            route = " → ".join(path)
            
            st.success("Route Found Successfully!")
            st.write(" Delivery Route:")
            st.write(route)

            st.write(" Total Distance:")
            st.write(f"{cost} km")
        else:
            st.error("No route found")