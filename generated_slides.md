---
marp: true
theme: default
backgroundImage: url('zazmic.png')
paginate: true
---

<!-- _class: lead -->
<!-- backgroundImage: url('main.png') -->
# 🌱 Diamond Sow Gardens  
AI-Powered Agricultural Monitoring & Action Automation  

---

# 📖 About  
Diamond Sow Gardens is a research-driven agricultural company focused on sustainable production and plant health optimization.  
They combine modern farming practices with advanced technology to improve crop yield, reduce risks, and support biodynamic agriculture.  

---

# 🔎 Current State  
- Ubibot sensors collect real-time data (temperature, humidity, voltage, etc.)  
- Basic automations already in place (e.g., greenhouse wall adjustments)  
- Infrared and spectrometry data planned for disease/deficiency detection  
- Key challenges:  
  - Lack of AI-driven interpretation of sensor data  
  - Difficulty correlating multiple environmental factors  
  - Limited predictive capabilities for disease management  

---

# 🎯 Goals  
- Build an AI-driven system to:  
  - Analyze multi-dimensional sensor data in real time  
  - Generate actionable insights & reports  
  - Start with targeted POC use cases (e.g., cucumber downy mildew)  
  - Enable scalable automation for future pest & nutrient management  
- Long-term: Fully automate corrective actions through IoT systems  

---

# 🛠 Use Cases (POC)  

## Use Case 1:  
**Cucumber Downy Mildew Prediction**  
- Inputs: humidity, temperature, wind, spectrometry data  
- Output: AI predicts disease susceptibility  
- Action: Recommend or trigger potassium application via irrigation  

---

## Use Case 2:  
**Nutrient Deficiency Detection (Infrared Analysis)**  
- Inputs: spectrometry (infrared), soil moisture, moonlight exposure  
- Output: Detect early nitrogen deficiency  
- Action: Alert agronomists with suggested organic interventions  

---

## Use Case 3:  
**Automated Environmental Optimization**  
- Inputs: Ubibot data (temperature, humidity, light exposure)  
- Output: Identify stress conditions for crops  
- Action: Suggest optimal greenhouse adjustments (ventilation, irrigation schedule)  

---

# 🏗 Architecture  

➡️ *Here should be the diagram "High-level AI Architecture"*  

- Sensor data ingestion (Ubibot, Davis Instruments)  
- Storage & processing: **BigQuery + Pub/Sub**  
- AI/ML: **Vertex AI**, TensorFlow, scikit-learn  
- Agent layer: LLM-based report generation & triggers  
- Outputs: Alerts (mobile/web), automated IoT actions  

---

# 📊 Estimate  

➡️ *Here should be the diagram "Agile Estimation Breakdown"*  

We will use **Scrum methodology** with sprints focusing on:  
- Data integration  
- AI model prototyping  
- Agent/report generation  
- Testing with cucumber mildew vertical  
- Scaling for nutrient analysis  

---

# 🚀 Next Steps  

1. **Define Triggers & Actions** for cucumber mildew scenario  
2. **Integrate Ubibot data pipeline** into GCP  
3. **Develop POC AI model** for mildew prediction  
4. **Create reporting & alerting dashboard**  
5. Validate with Diamond Sow agronomists 🌱  

---