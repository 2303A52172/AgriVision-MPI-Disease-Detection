# 🌱 AgriVision – MPI-Based Crop Disease Detection

A high-performance crop disease detection system using **MPI (Message Passing Interface)** and **OpenCV**.
This project analyzes crop images, detects disease patterns, and compares **serial vs parallel performance**.

---

## 🚀 Features

* 🌿 Crop disease detection using color analysis
* ⚡ Parallel processing using MPI (mpi4py)
* ⏱️ Serial vs Parallel time comparison
* 🖼️ Image processing using OpenCV
* 📊 Infection percentage calculation
* 🌽 Supports crops like Maize & Mirchi

---

## 🛠️ Technologies Used

* Python
* MPI (mpi4py)
* OpenCV
* NumPy

---

## 📂 Project Structure

AgriVision-MPI-Disease-Detection/
│
├── image_test.py
├── crop.jpg
├── serial_output.jpg
├── parallel_output.jpg
├── disease_classified.jpg
├── README.md

---

## ▶️ How to Run

### Step 1: Open Command Prompt

```bash
cd C:\MPI\src
```

### Step 2: Run using MPI (Parallel)

```bash
mpiexec -n 4 python image_test.py
```

---

## 📊 Results

### 🖼️ Input Image

![Input](crop.jpg)

---

### ⚙️ Serial Output

![Serial Output](serial_output.jpg)

---

### 🚀 Parallel Output (MPI)

![Parallel Output](parallel_output.jpg)

---

### 🦠 Disease Classification Output

![Disease Output](disease_classified.jpg)

---

## ⏱️ Performance Comparison

| Processing Type | Description                       |
| --------------- | --------------------------------- |
| Serial          | Normal execution                  |
| Parallel (MPI)  | Faster using multiple processes ⚡ |

---

## 🧠 Disease Detection Logic

The system detects diseases based on color patterns:

* 🟡 Yellow → Nutrient deficiency / Early infection
* 🟤 Brown → Leaf spot disease
* ⚫ Black → Fungal infection

---

## 📌 Output Example

Yellow Infection % : 0.18
Brown Infection %  : 0.00
Black Infection %  : 2.62

---

## 🎯 Conclusion

* MPI improves processing speed
* Parallel execution is faster than serial
* Useful for smart agriculture systems

---

## 🔮 Future Enhancements

* 🤖 AI-based disease detection
* 📱 Mobile app integration
* 🌐 Real-time monitoring

---

## 👩‍💻 Author

Shivani
AgriVision – High-Speed Crop Health Analysis Using MPI

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
