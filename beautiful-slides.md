---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('zazmic.png')
---

<!-- Slide 1 -->
![bg](main.png)

---

# 🌱 Diamond Sow Gardens – AI Solution Proposal

---

## Overview – About
- Diamond Sow Gardens specializes in sustainable agriculture and research  
- Located in New Mexico, with partnerships including Los Alamos National Labs  
- Mission: advance **organic and biodynamic farming practices** using technology  

---

## Overview – Current State
- 🌡️ Sensor data (Ubibot, Davis Instruments) already collected in real time  
- ✅ Basic automation in place (temperature-based sidewall control)  
- ❌ Pain points:
  - No AI-based analysis of infrared spectrometry data  
  - Limited ability to **predict disease/deficiencies**  
  - Difficulty correlating multi-source data (humidity, moonlight, temperature, wind)  
  - Lack of automated **report generation and recommendations**  

---

## Overview – Goals
- 📊 Build AI-driven monitoring for **plant health and production optimization**  
- ⚡ Enable real-time **trigger-based alerts and recommendations**  
- 🌿 Vertical focus: cucumber downy mildew prevention  
- 🤖 Develop an **agentic system**: from reporting → to recommending → to automating actions  

---

# 🎯 Use Cases (POC Focus)

---

## Use Case 1 – AI Reports from Sensor Data
- **Problem:** Sensor data is raw and fragmented, difficult to interpret manually  
- **POC Solution:**  
  - Use GCP (BigQuery + Vertex AI) to process Ubibot data  
  - Train models to identify anomalies & generate **natural language reports**  
- **Outcome:** Automated, reliable reporting of plant health indicators  

---

## Use Case 2 – Cucumber Downy Mildew Prediction
- **Problem:** Disease prediction requires combining humidity, temperature, wind, and spectrometry  
- **POC Solution:**  
  - Develop ML classification model for mildew risk levels  
  - Trigger recommendations for potassium application  
- **Outcome:** Early warnings, optimized treatment timing, reduced crop loss  

---

## Use Case 3 – Actionable Alerts & Triggers
- **Problem:** Farmers need timely, actionable steps (not just raw data)  
- **POC Solution:**  
  - Build AI agents to recommend actions (alerts via mobile/web)  
  - Future-ready integration with irrigation automation systems  
- **Outcome:** Human-in-the-loop decision making → path toward automation  

---

# 🏗️ Architecture

---

## Proposed Architecture
Here should be the diagram `image_1_architecture`.

---

# 📊 Estimate

---

## Scrum-Based Estimation
Here should be a summary table of epics and stories.  
(Full CSV provided separately).  

---

# 🚀 Next Steps
1. Confirm cucumber downy mildew dataset and triggers  
2. Define success metrics for AI reports (precision, recall, farmer usability)  
3. Build initial pipeline in GCP (BigQuery + Vertex AI + Pub/Sub)  
4. Deliver **POC in 6–8 weeks**  
5. Evaluate results and scale to additional crops  

