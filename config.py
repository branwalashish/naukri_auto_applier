"""
 Naukri Automation Bot - Configuration File

This file controls:
- Login credentials
- Job search filters
- Application limits
- Screening answers (auto-fill)

⚠️ IMPORTANT:
👉 Before running the script, replace the below credentials with your actual Naukri login.
👉 Do NOT push your real credentials to GitHub.
"""

# ==============================
# 🔐 LOGIN CREDENTIALS
# ==============================

# 👉 Replace these before running the script
NAUKRI_EMAIL = "your_email_here"      # Example: abc@gmail.com
NAUKRI_PASSWORD = "your_password_here"  # Example: mypassword123


# ==============================
# APPLICATION SETTINGS
# ==============================

# Max applications per run (keep safe to avoid blocking)
MAX_APPLIES_PER_RUN = 15

# Max pages to search per keyword
MAX_PAGES_PER_KEYWORD = 3


# ==============================
# JOB SEARCH KEYWORDS
# ==============================

KEYWORDS = [
    "java developer",
    "spring boot developer",
    "backend developer",
    "software engineer",
    "java backend developer"
]


# ==============================
# SCREENING ANSWERS (REAL-TIME BASED)
# ==============================

"""
👉 These are common screening questions asked on Naukri.
👉 The bot tries to match keywords and auto-fill answers.

 You can customize based on your profile.
"""

SCREENING_ANSWERS = {

    # ======================
    # EXPERIENCE
    # ======================
    "total experience": "2",          # Example: 0 for fresher / 2 for 2 years
    "relevant experience": "2",       # Example: same as above or specific skill exp

    # ======================
    # LOCATION
    # ======================
    "current location": "Bangalore",  
    "preferred location": "Bangalore",

    # ======================
    # SALARY
    # ======================
    "current ctc": "3 LPA",           # Fresher → "0" or "NA"
    "expected ctc": "4 LPA",          # Example: 4 LPA or "As per company standards"

    # ======================
    # NOTICE PERIOD
    # ======================
    "notice period": "Immediate Joiner",  
    # Example:
    # "Immediate Joiner"
    # "15 Days"
    # "30 Days"

    # ======================
    # AVAILABILITY
    # ======================
    "available to join": "Yes",

    # ======================
    # EDUCATION
    # ======================
    "highest qualification": "B.Tech",
    "graduation year": "2023",

    # ======================
    # SKILLS (VERY COMMON)
    # ======================
    "java": "2 years",
    "spring boot": "1.5 years",
    "sql": "2 years",
    "rest api": "1.5 years",
    "microservices": "1 year",

    # ======================
    # WORK AUTHORIZATION
    # ======================
    "work authorization": "Yes",

    # ======================
    # WORK MODE
    # ======================
    "willing to relocate": "Yes",
    "willing to work from office": "Yes",

    # ======================
    # GENERAL HR QUESTIONS
    # ======================
    "why should we hire you": "I have strong backend development skills in Java and Spring Boot with hands-on project experience.",
    
    "reason for job change": "Looking for better growth opportunities and challenging work environment",

    "any offer in hand": "No",

    "comfortable with shifts": "Yes"
}


# ==============================
# EXAMPLE USAGE
# ==============================

"""
Example usage in code:

from config import SCREENING_ANSWERS

question = "What is your current CTC?"
for key in SCREENING_ANSWERS:
    if key in question.lower():
        print("Answer:", SCREENING_ANSWERS[key])

👉 Output:
Answer: 3 LPA
"""