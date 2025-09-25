## **Slide 1 – Title**

**Speech:**
“Diamond Sow Gardens is aiming to modernize agriculture with artificial intelligence.
Today, we’ll present a proof of concept that demonstrates how AI can support **real-time monitoring, intelligent recommendations, and early interventions**—bridging the gap between traditional farming and data-driven agriculture.”

---

## **Slide 2 – About**

**Speech:**
“Diamond Sow Gardens specializes in sustainable and biodynamic agriculture.
They combine deep farming knowledge with strong research partnerships, including Los Alamos National Labs.
Our role is to introduce **AI tools that complement their mission**, helping them interpret data more effectively and optimize production while staying true to sustainable practices.”

---

## **Slide 3 – Current State**

**Speech:**
“Currently, Diamond Sow collects environmental data in real time using sensors like Ubibot and Davis Instruments.
There is some basic automation—for example, temperature triggers for sidewall control.
But the pain points are clear:

* There’s no **AI-based analysis**,
* Multi-source data like humidity, moonlight, and wind is hard to correlate,
* And there’s no automated reporting or decision support.

As a result, valuable insights remain locked in raw data.”

---

## **Slide 4 – Goals**

**Speech:**
“The goal is to turn that raw sensor data into **actionable intelligence**.
We want to:

* Enable AI-driven monitoring for plant health,
* Trigger alerts and recommendations when conditions demand action,
* And begin with a very focused case: **predicting and preventing cucumber downy mildew**.

The vision is an agentic system that evolves from reporting, to recommending, and eventually to automating greenhouse operations.”

---

## **Slide 5 – Use Case 1**

**Speech:**
“Our first use case is **downy mildew prevention in cucumbers**.
By combining humidity, temperature, wind, and spectral data, the AI can predict the likelihood of mildew outbreaks.
When risk is high, the system alerts farmers and recommends preventive organic treatments.
This reduces crop loss and ensures interventions are timely and targeted.”

---

## **Slide 6 – Use Case 2**

**Speech:**
“The second use case is **nutrient deficiency detection**.

no estoy seguro de esto ya que aun no sabemos que tipo de adta tiene el cliente. 

Using infrared and spectrometry data, the AI identifies early signals of stress—before they’re visible to the human eye.
It then notifies agronomists with organic intervention suggestions, helping maintain healthy growth cycles.”

---

## **Slide 7 – Use Case 3**

**Speech:**
“The third use case focuses on **greenhouse optimization**.
By analyzing environmental data streams—temperature, humidity, wind, and light—the AI recommends or even automates adjustments.
For example, it could suggest venting, irrigation, or light control to keep conditions ideal for plant health.”

---

## **Slide 8 – Architecture**

**Speech:**
“Here’s the high-level architecture.
Sensor data is ingested into **Pub/Sub**, processed with **Dataflow**, and stored in **BigQuery** for correlation and analysis.
Models are trained and served with **Vertex AI** and TensorFlow, generating insights.
Finally, an **agentic layer** delivers reports, alerts, and potential IoT triggers back to the greenhouse.
This creates a full loop: from data → intelligence → action.”

---

## **Slide 9 – Estimate**

**Speech:**
“The POC is designed to run over a **two-month period**, using Scrum to structure delivery.
We’ll cover:

* Integration of sensors and pipelines,
* Modeling and training of mildew and nutrient predictors,
* Automated reporting and alert generation,
* And validation with Diamond Sow’s agronomists.
  The estimation details are provided in the CSV for transparency.”

---

## **Slide 10 – Next Steps**

**Speech:**
“The next steps are straightforward:

1. Confirm datasets and triggers for cucumber mildew,
2. Define success metrics for AI reports,
3. Build the first ingestion and analysis pipeline in GCP,
4. Deliver an initial prototype for validation,
5. And then expand to more crops and conditions.

This approach ensures that we start focused, deliver value quickly, and scale responsibly.”
