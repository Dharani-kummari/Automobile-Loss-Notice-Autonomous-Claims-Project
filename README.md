You can structure your repo like this:

AutomobileLossNotice/
│
├── backend/
│   ├── app.py
│   ├── extractor.py
│   ├── validator.py
│   ├── router.py
│   └── output/             # Auto-created when backend runs
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── auto.js
│
├── requirements.txt
└── README.md

2️⃣ README.md Content

Here’s a ready-to-copy README:

# Automobile Loss Notice & Autonomous Insurance Claims Processing

## Overview
This project is a complete system to automate **First Notice of Loss (FNOL)** processing for automobile insurance claims.  

Features:
- Manual claim form submission
- Raw ACORD form text parsing
- Automatic extraction of key fields:
  - Policy Information
  - Incident Information
  - Involved Parties
  - Asset Details
  - Claim Type, Attachments, Initial Estimate
- Routing to appropriate claim handling:
  - Fast-track
  - Specialist Queue
  - Investigation Flag
  - Manual Review
- JSON output saved automatically in `backend/output/`

---

## Project Structure


AutomobileLossNotice/
├── backend/ # Flask API backend
├── frontend/ # HTML/CSS/JS frontend
├── requirements.txt
└── README.md


---

## Backend
- **app.py** – Main Flask API  
- **extractor.py** – Extracts fields from JSON or ACORD text  
- **validator.py** – Checks for missing mandatory fields  
- **router.py** – Determines claim routing based on rules  

### How to Run
```bash
cd backend
python app.py


The backend runs on http://127.0.0.1:5000/.

Frontend

index.html – Manual form + ACORD text input

style.css – Styling

auto.js – Async JS to submit claims

How to Use

Open frontend/index.html with Live Server or browser.

Fill manual form or paste ACORD text.

Click Submit → JSON output displayed below the form.

Output saved in backend/output/result_TIMESTAMP.json.

Dependencies

Install dependencies with:

pip install -r requirements.txt


flask

flask-cors

Optional Demo

You can record a short 1–2 minute video demonstrating:

Filling the manual form

Pasting ACORD text

Submitting the claim

Viewing JSON output and saved file

Approach

Field Extraction:

Used regex to parse ACORD text for all mandatory fields.

Form input fields map directly to backend JSON.

Validation:

Mandatory fields checked before routing.

Routing Logic:

Fast-track for low estimated damage

Specialist Queue for injury claims

Investigation Flag for fraud keywords

Manual Review for incomplete or default cases

Frontend Interaction:

JavaScript uses async/await to submit data via fetch()

Handles both manual form and ACORD text asynchronously

Displays JSON output dynamically

Output Storage:

Auto-creates output/ folder if missing

Saves each claim as result_TIMESTAMP.json