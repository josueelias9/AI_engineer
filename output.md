## content for the google slide

```markdown
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

---
```

---

## what should be said in each slide

```markdown
### Slide 1
Welcome everyone. Today we will present how AI can be leveraged to improve agricultural monitoring and automation at Diamond Sow Gardens.

### Slide 2
About Diamond Sow Gardens: a sustainable agriculture company in New Mexico, combining traditional farming practices with modern research. We aim to enhance plant health and production through advanced technologies.

### Slide 3
Currently, the farm already collects real-time data via Ubibot and Davis sensors, and has basic automation for greenhouse temperature. However, there are limitations: no advanced AI analysis, difficulty predicting diseases, and no automatic actionable reports.

### Slide 4
The goal is to move beyond simple monitoring, into AI-driven reporting and action recommendations. We will start with a vertical case: cucumber downy mildew. Long-term, the system should evolve into a fully agentic solution that can automate interventions.

### Slide 5
We identified three use cases for a proof-of-concept. These are designed to address the main pain points without committing to a full deployment.

### Slide 6
First use case: generating AI reports from sensor data. This will automate the interpretation of raw readings, giving farmers clear reports on health indicators.

### Slide 7
Second use case: cucumber downy mildew prediction. By combining environmental and spectrometry data, we can train an AI model to forecast mildew risk, enabling proactive treatment.

### Slide 8
Third use case: actionable alerts. AI agents will recommend concrete actions, starting with human-in-the-loop alerts, but designed for future automation with irrigation systems.

### Slide 9
Here is the proposed architecture. It shows how sensor data flows into GCP (Pub/Sub → BigQuery → Vertex AI), producing reports and recommendations. Agentic systems will deliver alerts, and in future phases, trigger automated irrigation or treatment.

### Slide 10
For estimation, we used Scrum methodology. Each epic and user story was broken into tasks. We ensured the plan is flexible enough for exploration while keeping delivery within 6–8 weeks for the POC.

### Slide 11
Next steps: confirm the cucumber dataset, define success metrics, set up GCP pipeline, and build the POC. After evaluation, we can scale to more crops and expand automation.
```

---

## the xml to create the diagrams in draw\.io

```image_1_architecture
<mxfile host="app.diagrams.net">
  <diagram id="architecture1" name="Architecture">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Sensors -->
        <mxCell id="2" value="Ubibot &amp; Davis Sensors" style="shape=ellipse;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="40" y="180" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pub/Sub -->
        <mxCell id="3" value="GCP Pub/Sub" style="shape=process;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="240" y="180" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <!-- BigQuery -->
        <mxCell id="4" value="BigQuery (Time Series Data)" style="shape=process;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="420" y="180" width="180" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Vertex AI -->
        <mxCell id="5" value="Vertex AI (ML Models)" style="shape=process;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="660" y="120" width="160" height="60" as="geometry"/>
        </mxCell>
        
        <!-- AI Agents -->
        <mxCell id="6" value="AI Agent Layer (Recommendations, Reports)" style="shape=process;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="660" y="240" width="220" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Farmers -->
        <mxCell id="7" value="Farmers (Mobile / Dashboard)" style="shape=ellipse;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="960" y="180" width="160" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Edges -->
        <mxCell id="8" edge="1" source="2" target="3" style="endArrow=block;strokeColor=#000000;" parent="1"/>
        <mxCell id="9" edge="1" source="3" target="4" style="endArrow=block;strokeColor=#000000;" parent="1"/>
        <mxCell id="10" edge="1" source="4" target="5" style="endArrow=block;strokeColor=#000000;" parent="1"/>
        <mxCell id="11" edge="1" source="4" target="6" style="endArrow=block;strokeColor=#000000;" parent="1"/>
        <mxCell id="12" edge="1" source="5" target="6" style="endArrow=block;strokeColor=#000000;" parent="1"/>
        <mxCell id="13" edge="1" source="6" target="7" style="endArrow=block;strokeColor=#000000;" parent="1"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## a csv that contains the estimation

```csv
EPIC,AS A,I WANT TO,SO THAT,SPs for BE,Assumptions and out of scope
Data Ingestion,Data Engineer,Ingest Ubibot & Davis sensor data via Pub/Sub,We can centralize time-series data in BigQuery,8,Assume API access is available and stable
Data Ingestion,Data Engineer,Normalize and clean incoming data,Models receive consistent inputs,5,Out of scope: building IoT firmware
Data Storage,AI Engineer,Design BigQuery schema for time-series data,We can efficiently query and train ML models,3,We assume current data volume is manageable in BigQuery
ML Model,ML Engineer,Build baseline anomaly detection on sensor data,We can identify outliers and patterns,8,Focus on humidity/temp data first
ML Model,ML Engineer,Develop cucumber mildew risk classifier,We can forecast and prevent outbreaks,13,Limited to one crop for POC
ML Model,ML Engineer,Integrate infrared spectrometry data,We can enhance prediction accuracy,8,Infrared dataset availability required
AI Reporting,AI Engineer,Generate natural language reports from data,Users can understand farm conditions,5,Out of scope: multilingual support
AI Reporting,AI Engineer,Build report templates for POC,Reports are standardized and actionable,3,Simple HTML/PDF only
Agentic Layer,AI Engineer,Implement alert system with recommended actions,Farmers get timely guidance,5,No automation of irrigation yet
Agentic Layer,AI Engineer,Design future-ready interface for IoT actions,We can later connect to irrigation system,3,Automation integration out of scope
Infrastructure,Cloud Engineer,Deploy models using Vertex AI pipelines,Ensure scalability and reproducibility,8,We assume project uses GCP only
Infrastructure,Cloud Engineer,Set up dashboards with Looker Studio,Farmers can visualize sensor data,5,Limited to POC sensors
Project Management,PO,Define success criteria with stakeholders,POC delivers measurable value,3,We assume cucumber mildew is the priority
Project Management,Scrum Master,Sprint planning and retrospectives,Team remains aligned and agile,5,---
```

---

Do you want me to also prepare **two additional supporting diagrams** (e.g., one for the cucumber mildew use case data flow, and another for the agentic alert system), so that the presentation has multiple visuals instead of just the general architecture?
