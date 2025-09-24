---
marp: true
theme: default
backgroundImage: url('zazmic.png')
paginate: true

---

![bg](main.png)

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
Build an AI-driven system to:  
- Analyze multi-dimensional sensor data in real time  
- Generate actionable insights & reports  
- Start with targeted POC use cases (e.g., cucumber downy mildew)  
- Enable scalable automation for future pest & nutrient management  

---

# 🛠 Use Cases

## Use Case 1:  
**Cucumber Downy Mildew Prediction**  
- Inputs: humidity, temperature, wind, spectrometry data (this is data we will be mocking/creating)
- Output: AI predicts disease susceptibility  
- Action: Recommend or trigger potassium application via irrigation  

---

## Use Case 2:  

redo this. it has to do with the cucumber case


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