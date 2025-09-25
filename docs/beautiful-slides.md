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

# Diamond Sow Gardens 
# AI Workshop


---

# Solutions Workshop Agenda

- Overview
- Use Cases
- Architecture
- Estimate
- Next Steps


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
  - No AI-based analysis 
  - Difficulty correlating multi-source data (humidity, moonlight, temperature, wind)  
  - Lack of automated **report generation and recommendations**  

---

## Overview – Goals
- 📊 Build AI-driven monitoring for **plant health and production optimization**
- ⚡ Enable scheduled **trigger-based alerts and recommendations**  
- 🌿 Vertical focus: cucumber downy mildew prevention (review)
- 🤖 Develop an **agentic system**: from reporting → recommending → automating  

---

# 🎯 Use Cases
![alt text](image.png)

---

- **Generate AI Reports**  
  - Automatic interpretation of multi-sensor data  
  - Natural language summaries of plant health  

- **Predict Cucumber Downy Mildew**  
  - Combine humidity, temperature, wind & spectrometry  
  - Early alerts for treatment → reduce crop loss  

- **Receive Actionable Alerts**  
  - Recommendations via mobile/web  
  - Human-in-the-loop decision support  


---

# 🏗️ Architecture
![alt text](image-1.png)
- Ingest data streams with **Pub/Sub**  
- Process data with **Dataflow**  
- Store and correlate metrics in **BigQuery**  
- Generate recommendations with **Vertex AI**





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
5. Evaluate results and scale to additional crops  

---

# Thank you