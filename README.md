
# 📦 AI Parcel Delivery Route Finder

## 🚀 Project Overview

This project is an **AI-based route optimization system** that finds the shortest delivery path between cities using the **A* (A-Star) Algorithm**.
It simulates a real-world parcel delivery system where users can select pickup and delivery locations and get the most efficient route.

---

## 🎯 Objective

* Implement the **A* search algorithm**
* Solve shortest path problems using AI
* Build a **user-friendly GUI using Streamlit**
* Demonstrate real-world application of AI in logistics

---

## 🧠 Key Concepts Used

* Artificial Intelligence (AI)
* Search Algorithms (A*)
* Heuristic Functions
* Graph Representation (Nodes & Edges)

---

## 🗂️ Project Structure

```
a-star-project/
│── app.py        # Streamlit GUI
│── astar.py      # A* Algorithm
│── cities.py     # Graph & heuristic data
│── requirements.txt
│── README.md
```

---

## ⚙️ How It Works

1. User selects:

   * 📍 Pickup Location
   * 📦 Delivery Location

2. The system:

   * Applies **A* algorithm**
   * Calculates shortest path using:

     * g(n): cost from start
     * h(n): estimated cost
     * f(n) = g(n) + h(n)

3. Displays:

   * 🚚 Delivery Route
   * 📏 Total Distance

---

## ▶️ How to Run the Project

### Step 1: Install dependencies

```
pip install -r requirements.txt
```

### Step 2: Run the application

```
streamlit run app.py
```

### Step 3: Open in browser

```
http://localhost:8501
```

---

## 📊 Example Output

**Input:**
Pickup: Delhi
Delivery: Chennai

**Output:**
Delhi → Jaipur → Indore → Bhopal → Nagpur → Hyderabad → Bangalore → Chennai
Distance: 2810 km

---

## 🎓 Course Relevance

This project directly applies concepts from the **Fundamentals of AI and ML course**, including:

* Intelligent Agents
* Search Algorithms (A*)
* Heuristic Optimization
* Graph-based Problem Solving

👉 *This project demonstrates practical implementation of A* algorithm taught in AI search techniques module.*

---

## 🚧 Challenges Faced

* Understanding A* algorithm logic
* Designing heuristic values
* Debugging Python module issues
* Converting terminal app to GUI

---

## 📚 Learning Outcomes

* Learned how A* works in real-world problems
* Improved problem-solving using AI
* Built GUI using Streamlit
* Understood graph-based algorithms

---

## 🔮 Future Scope

* Integrate real-time maps (Google Maps API)
* Add traffic-based routing
* Deploy as a web application
* Add visualization features

---

## 🏁 Conclusion

This project successfully demonstrates how **AI algorithms like A*** can be used for efficient route optimization in delivery systems, making it a practical and impactful application.

---

## 👨‍💻 Author

**Ansh Tomar**
Registration No: 25BAI11078
