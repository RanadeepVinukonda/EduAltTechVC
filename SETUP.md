# Google Forms Connection Guide

This guide walks you through setting up a Google Form and mapping its fields to your refined, custom HTML landing pages.

---

## Step 1: Create Google Form

1. Go to [Google Forms](https://forms.google.com) → Click **Blank form**
2. Add these questions (use the `+` button, matching the types exactly):

| Question Label | Question Type | Custom HTML Mapping |
| :--- | :--- | :--- |
| **Full Name** | Short answer | Name |
| **Email** | Short answer | Email |
| **Phone** | Short answer | Phone |
| **Selected Service(s)** | Paragraph | Services (from Services tab) |
| **Selected Course(s)** | Paragraph | Courses (from Schools tab) |
| **Message** | Paragraph | Message / Details |

3. Click **Settings** (tab at the top) → **Responses** → Ensure **"Collect email addresses"** is set to **Do not collect**.

---

## Step 2: Find Form ID

Click the **Send** button in the top right, select the Link icon, and copy the URL. It looks like:
```
https://docs.google.com/forms/d/e/2ABCiEx...YfA/viewform
```
Extract the **Form ID** (the part between `/d/e/` and `/viewform`):
```
2ABCiEx...YfA
```
Keep this ID handy.

---

## Step 3: Find Entry IDs (Field Codes)

### Method A: Pre-filled Link (Recommended & Easiest)
1. In your form editor, click the three vertical dots (**⋮**) in the top right corner next to "Send".
2. Select **Get pre-filled link**.
3. In the pre-filled form that opens, type distinct dummy text in each field:
   - *Full Name* → type `TEST-NAME`
   - *Email* → type `TEST-EMAIL`
   - *Phone* → type `TEST-PHONE`
   - *Selected Service(s)* → type `TEST-SERVICES`
   - *Selected Course(s)* → type `TEST-COURSES`
   - *Message* → type `TEST-MESSAGE`
4. Click **Get Link** at the bottom, then click **Copy Link**.
5. Paste this link into a text editor. The URL will contain entry keys mapped to your test values:
   `?entry.1234567890=TEST-NAME&entry.1234567891=TEST-EMAIL&entry.1234567892=TEST-PHONE&entry.1234567893=TEST-SERVICES&entry.1234567894=TEST-COURSES&entry.1234567895=TEST-MESSAGE`
6. Note each `entry.XXXXXXXXX` number next to its field name.

### Method B: DevTools
1. Open your form and click the **Preview** (eye icon).
2. Press `F12` to open DevTools, and click the **Network** tab.
3. Submit dummy data in the form, and find the `formResponse` request in the network list.
4. Check the **Payload** (or Form Data) tab to copy each `entry.XXXXX` value.

---

## Step 4: Update Files

### For `index.html`:
Open [index.html](file:///d:/qr-form/index.html), find these lines at the top of the `<script>`:
```js
const FORM_ID = 'YOUR_FORM_ID';
const FIELD_MAP = {
  name: 'entry.1234567890',
  email: 'entry.1234567891',
  phone: 'entry.1234567892',
  services: 'entry.1234567893', // Replace with Services entry ID
  courses: 'entry.1234567894',  // Replace with Courses entry ID
  message: 'entry.1234567895'
};
```
Replace `YOUR_FORM_ID` and each `entry.XXXXX` with your real values.

### For `form.html`:
Same structure — update `FORM_ID` and the `name` attribute values on each input field inside [form.html](file:///d:/qr-form/form.html).

---

## Step 5: Test

Open `index.html` or `form.html` in a browser. Fill in:
- Name: `John Doe` (not `John123`)
- Email: `john@example.com` (must have `@` and `.`)
- Phone: select `+91` and enter `9876543210` (10 digits only)

Submit → check your Google Form's **Responses** tab.

---

## Step 6: Host & QR

Host the folder on GitHub Pages or Netlify (drag-drop the folder).

Generate QR:
```bash
python generate_qr.py
# Paste your hosted URL
```

Print `qr-code.png` to display at your counter/desk.

---

**Tip:** All submissions appear live in your Google Sheet (Forms → Responses → green Sheets icon).
