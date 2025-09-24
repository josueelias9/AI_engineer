## content for the google slide

```markdown
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
```

---

## what should be said in each slide

```markdown
### Slide 1: Title
“Diamond Sow Gardens is looking to modernize agriculture with AI. Today we’ll walk you through a solution that focuses on real-time monitoring and intelligent action automation.”

### Slide 2: About
“Diamond Sow Gardens is committed to sustainable agriculture, combining traditional methods with modern technology. Our role is to help them harness AI to improve plant health and production.”

### Slide 3: Current State
“They already collect real-time data through Ubibot sensors, but they struggle to interpret multi-dimensional signals and automate decisions beyond basic temperature control.”

### Slide 4: Goals
“The main objective is to create AI systems that interpret complex data and provide actionable recommendations, starting with a cucumber mildew use case and expanding toward full automation.”

### Slide 5: Use Case 1
“This POC will predict cucumber downy mildew risk based on multiple environmental factors and trigger irrigation-based potassium application when needed.”

### Slide 6: Use Case 2
“We’ll use infrared analysis to detect nutrient deficiencies early. The AI will notify agronomists with recommended organic interventions.”

### Slide 7: Use Case 3
“By analyzing Ubibot environmental data, the AI can recommend or automate greenhouse adjustments for optimal growing conditions.”

### Slide 8: Architecture
“This architecture integrates Ubibot sensors with GCP tools like Pub/Sub and BigQuery, builds AI models on Vertex AI and TensorFlow, and adds an agent layer for reporting and IoT triggers.”

### Slide 9: Estimate
“We’ll approach this project using Scrum. The plan is broken into sprints that cover integration, modeling, reporting, and POC validation.”

### Slide 10: Next Steps
“Our immediate action is to clearly define the cucumber mildew triggers and actions, integrate the data, and build the first AI prototype. From there, we validate and expand.”
```

---

## the xml to create the diagrams in draw\.io

```image_1_architecture_high_level
<mxfile>
  <diagram id="arch1" name="High-level AI Architecture">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <mxCell id="2" value="Ubibot Sensors" style="shape=ellipse;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="50" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="3" value="Pub/Sub" style="shape=process;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="220" y="50" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="4" value="BigQuery" style="shape=process;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="380" y="50" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="5" value="Vertex AI / TensorFlow" style="shape=process;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="540" y="50" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="6" value="AI Agent Layer" style="shape=process;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="740" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="7" value="Alerts / IoT Actions" style="shape=ellipse;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="920" y="50" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="8" edge="1" source="2" target="3" parent="1"/>
        <mxCell id="9" edge="1" source="3" target="4" parent="1"/>
        <mxCell id="10" edge="1" source="4" target="5" parent="1"/>
        <mxCell id="11" edge="1" source="5" target="6" parent="1"/>
        <mxCell id="12" edge="1" source="6" target="7" parent="1"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

```image_2_estimation_breakdown
<mxfile>
  <diagram id="arch2" name="Agile Estimation Breakdown">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <mxCell id="2" value="Sprint 1: Data Integration" style="shape=rectangle;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="50" y="50" width="160" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="3" value="Sprint 2: AI Prototyping" style="shape=rectangle;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="250" y="50" width="160" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="4" value="Sprint 3: Agent & Reporting" style="shape=rectangle;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="450" y="50" width="180" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="5" value="Sprint 4: POC Validation" style="shape=rectangle;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="670" y="50" width="160" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="6" edge="1" source="2" target="3" parent="1"/>
        <mxCell id="7" edge="1" source="3" target="4" parent="1"/>
        <mxCell id="8" edge="1" source="4" target="5" parent="1"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## a csv that contains the estimation

```csv
EPIC,AS A,I WANT TO,SO THAT,SPs for BE,Assumptions and out of scope
Data Integration,Engineer,Ingest Ubibot sensor data into GCP Pub/Sub,We have a real-time streaming pipeline,5,Ubibot API credentials available
Data Integration,Engineer,Store raw sensor data in BigQuery,We can run historical queries and ML training,3,Schema agreed with client
AI Prototyping,Data Scientist,Build cucumber mildew prediction model,We can generate risk alerts based on humidity/temp/wind,8,Initial model is simple regression/classification
AI Prototyping,Data Scientist,Train nutrient deficiency model using infrared data,We can detect nitrogen stress early,8,Infrared dataset availability
Agent & Reporting,AI Engineer,Develop LLM-based reporting agent,We can generate human-readable recommendations,5,English-only reports at first
Agent & Reporting,Engineer,Integrate agent with alert system (mobile/web),Farmers receive timely notifications,5,Client provides preferred notification channel
POC Validation,QA,Test mildew prediction with real field data,We validate AI accuracy against agronomist expectations,3,Ground truth labels from agronomists
POC Validation,Engineer,Simulate automated irrigation trigger,We verify end-to-end automation,3,No real-world irrigation triggered in POC
```

---

Do you want me to also **add a risk/mitigation slide** (e.g., data availability, AI hallucination, IoT reliability) to strengthen the client-facing proposal?
