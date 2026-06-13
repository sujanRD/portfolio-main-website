from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ══════════════════════════════════════════════════════════════
#  PORTFOLIO DATA  — edit everything here to personalise
# ══════════════════════════════════════════════════════════════
DATA={ 
    "name":    "Sujan RD",
    "initial": "RD",          # first letter of your name for avatar
    "tagline": "CS Engineering Student · Builder · Problem Solver",
    "about":   (
        "I'm a first-year Computer Science Engineering student with a deep "
        "passion for building things that matter. I love exploring  "
        "web development, and turning ideas into real working projects. "
        "Currently levelling up my skills in Python, C and full-stack "
        "development — one project at a time."
    ),
    "email":    "sujanrdreddy@gmail.com",
    "github":   "https://github.com/sujanrd14",
    "linkedin": "https://linkedin.com/in/sujanrd14",
    "college":  "BMS college of Engineering",
    "degree":   "1st Year · B.E. Computer Science Engineering",

    "skills": [
        {"name": "Python",          "level": 90, "cat": "Languages"},
        {"name": "C ",         "level": 85, "cat": "Languages"},
        {"name": "HTML",            "level": 85, "cat": "Web"},
        {"name": "CSS",             "level": 82, "cat": "Web"},
        {"name": "Flask",           "level": 60, "cat": "Web"},
        {"name": "Git & GitHub",    "level": 72, "cat": "Tools"},
        {"name": "VS Code",         "level": 90, "cat": "Tools"},
        {"name": "Linux / CLI",     "level": 65, "cat": "Tools"},
        
    ],

    "projects": [
        {
            "id":    1,
            "icon":  "💻",
            "title": "This Portfolio Website",
            "desc":  (
                "A portfolio  "
                "pure HTML + CSS. Features mobile-first design, a working "
                "contact form, "
            ),
            "tech":   [ "HTML", "CSS"],
            "github": "https://github.com/sujanrd14",
            "live":   None,
            "status": "Completed",
            "year":   2026,
        },
        {
            "id":    2,
            "icon":  "🐍",
            "title": "Hackathon Entry pass generator",
            "desc":  (
                "python - HTML/CSS connected sucessfully by Flask,"
                "Takes input of user and generates pass, "
                "also generated my own QR code of project."
            ),
            "tech":   ["Python", "Flask","HTML-CSS"],
            "github": "https://github.com/sujanrd14",
            "live":   "https://full-stack-1st-project-3.onrender.com",
            "status": "Live",
            "year":   2026,
        },
        {
            "id":    3,
            "icon":  "⚙️",
            "title": "python projects",
            "desc":  (
                "student management system,bus ticket booking,supermarket-billing"
                "bank-menu-driven system,still more.."
                
            ),
            "tech":   ["python", "OOP"],
            "github": "https://github.com/sujanrd14",
            "live":   None,
            "status": "Completed",
            "year":   2026,
        },
        
    ],

    "certificates": [
        {
            "title":  "College Events",
            "issuer": "by BMS college",
            "date":   "2026",
            "link":   "/static/college_certificates.pdf",
        },
        {
            "title":  "Course completion",
            "issuer": "by Online Courses",
            "date":   "2026",
            "link":   "/static/online_certificates.pdf",
        },
        
    ],
}

# In-memory store for contact messages
MESSAGES = []

# ══════════════════════════════════════════════════════════════
#  ROUTES
# ══════════════════════════════════════════════════════════════

@app.route("/")
def home():
    return render_template("index.html", d=DATA, msg=None, ok=False)


@app.route("/contact", methods=["POST"])
def contact():
    name    = request.form.get("name",    "").strip()
    email   = request.form.get("email",   "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html", d=DATA, ok=False,
            msg="Please fill in your name, email and message."
        )

    MESSAGES.append({
        "name": name, "email": email,
        "subject": subject, "message": message,
        "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
    })

    return render_template(
        "index.html", d=DATA, ok=True,
        msg=f"Thanks {name}! Message received. I'll reply soon 🚀"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
