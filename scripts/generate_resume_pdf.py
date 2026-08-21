#!/usr/bin/env python3
"""Generate Vaibhav Maheshwari resume PDF (ATS-optimized, Shatishay-style)."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT_PATH = "/workspace/resume/Vaibhav_Maheshwari_Resume.pdf"

CONTACT = (
    "+91-XXXXXXXXXX | vaibhav.maheshwari@example.com | "
    '<link href="https://linkedin.com/in/vaibhav-maheshwari">LinkedIn</link> | '
    '<link href="https://github.com/vaibhavmaheshwari15">GitHub</link>'
)

BLACK = colors.black


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=18,
            alignment=TA_CENTER,
            textColor=BLACK,
            spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "Title",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
            textColor=BLACK,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            alignment=TA_CENTER,
            textColor=BLACK,
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            textColor=BLACK,
            spaceBefore=6,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=BLACK,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            leftIndent=12,
            bulletIndent=0,
            textColor=BLACK,
            spaceAfter=2,
        ),
        "job_header": ParagraphStyle(
            "JobHeader",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12,
            textColor=BLACK,
            spaceAfter=1,
        ),
        "job_sub": ParagraphStyle(
            "JobSub",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9.5,
            leading=12,
            textColor=BLACK,
            spaceAfter=2,
        ),
        "job_meta": ParagraphStyle(
            "JobMeta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=BLACK,
            spaceAfter=3,
        ),
    }


def bullet(text, styles):
    return Paragraph(f"&bull; {text}", styles["bullet"])


def section(title, styles):
    return [
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=BLACK, spaceAfter=4),
    ]


def generate_pdf(output_path=OUTPUT_PATH):
    styles = build_styles()
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )
    story = []

    story.append(Paragraph("Vaibhav Maheshwari", styles["name"]))
    story.append(Paragraph("Full Stack Software Engineer", styles["title"]))
    story.append(Paragraph(CONTACT, styles["contact"]))

    story.extend(section("Professional Summary", styles))
    story.append(
        Paragraph(
            "Full Stack Software Engineer with experience building scalable goal-tracking "
            "platforms at D.E. Shaw using Node.js, React, MongoDB, and Redis. Shipped "
            "production AI features including LLM-powered check-in suggestions. Strong in "
            "performance optimization (SSR, Brotli, caching), event-driven architecture "
            "(Apache Kafka), RESTful API design, and React UI engineering—with measurable "
            "impact on latency, adoption, and user experience.",
            styles["body"],
        )
    )

    story.extend(section("Technical Skills", styles))
    story.append(
        Paragraph(
            "<b>Languages:</b> JavaScript / TypeScript (Primary), Python, SQL, Java<br/>"
            "<b>Frameworks:</b> Node.js, Express.js, React, RESTful APIs, Jest, Microservices<br/>"
            "<b>Databases:</b> MongoDB (aggregation, schema design), Redis (caching), SQLite, PostgreSQL<br/>"
            "<b>AI &amp; LLM Tools:</b> Gemini AI, OpenAI API, Google ADK, prompt engineering, LLM tool calling<br/>"
            "<b>Distributed Systems:</b> Apache Kafka, Redis pub/sub, event-driven architecture, async job processing<br/>"
            "<b>Performance:</b> Server-side rendering (SSR), Brotli compression, query optimization, memoization<br/>"
            "<b>Tools &amp; Cloud:</b> Git, Docker, CI/CD, Agile, Linux",
            styles["body"],
        )
    )

    story.extend(section("Work Experience", styles))
    story.append(
        Paragraph(
            "<b>The D.E. Shaw Group</b>&nbsp;&nbsp;&nbsp;&nbsp;Hyderabad, India",
            styles["job_header"],
        )
    )
    story.append(
        Paragraph(
            "<b>Software Engineer (Full Stack) — DESGoals</b>&nbsp;&nbsp;&nbsp;&nbsp;Aug 2024 – Present",
            styles["job_meta"],
        )
    )
    story.append(
        Paragraph(
            "<i>Node.js, React, TypeScript, MongoDB, Redis, Kafka</i>",
            styles["job_sub"],
        )
    )
    story.append(
        Paragraph(
            "Internal OKR and goal-tracking platform enabling teams to set objectives, track "
            "progress, and run structured check-ins across the organization.",
            styles["body"],
        )
    )

    des_bullets = [
        "Built a Redis caching layer for read-heavy goal dashboards, reducing p95 read latency "
        "from 340ms to under 95ms (72% improvement) and serving 2,000+ active users with "
        "sub-100ms reads on cached goal summaries.",
        "Implemented server-side rendering with Brotli compression for goal summary pages, "
        "cutting Time-to-Interactive from 2.8s to 1.1s (61% improvement) and reducing payload "
        "size by 48% on initial page load.",
        "Leading migration of the goal check-in notification pipeline to Apache Kafka, decoupling "
        "write events from API handlers—improving write-to-cache propagation to under 1 second "
        "for 95% of check-in updates and enabling parallel consumer scaling.",
        "Engineered React dashboards with virtualized lists, memoized selectors, and lazy-loaded "
        "modules—reducing unnecessary re-renders by 55% on large OKR tree views and improving "
        "scroll performance on dashboards with 500+ goals.",
        "Designed RESTful Node.js APIs backed by MongoDB aggregation pipelines for goal CRUD, "
        "check-ins, and progress rollups—maintaining 99.9% uptime during quarterly OKR cycles.",
        "Optimized MongoDB query patterns and added compound indexes on frequently filtered fields "
        "(owner, quarter, status)—cutting slow-query volume by 40% and improving write-path "
        "throughput during peak check-in windows.",
        "Built reusable React component library for forms, filters, and data tables with "
        "consistent loading/error states—reducing new dashboard delivery time by 30% and "
        "improving Lighthouse accessibility scores from 78 to 94.",
    ]
    for item in des_bullets:
        story.append(bullet(item, styles))

    story.extend(section("AI Products Shipped (Production)", styles))

    story.append(
        Paragraph(
            "<b>AI-Powered Check-in Suggestions</b>&nbsp;&nbsp;&nbsp;&nbsp;D.E. Shaw (DESGoals)",
            styles["job_header"],
        )
    )
    story.append(
        Paragraph(
            "<i>Node.js + Gemini AI + Prompt Engineering</i>&nbsp;&nbsp;&nbsp;&nbsp;2024 – Present",
            styles["job_sub"],
        )
    )
    ai_bullets = [
        "Built and shipped a production LLM suggestion engine for goal check-ins: ingests "
        "historical OKR progress, team context, and prior check-in notes to generate contextual "
        "prompts via Gemini—helping users complete check-ins faster with higher quality inputs.",
        "Reduced average check-in completion time by 35% (from 4.2 min to 2.7 min) and increased "
        "weekly check-in adoption by 22% across pilot teams within one OKR cycle.",
        "Processing 500+ AI suggestion requests/day in production with 99.5% service uptime; "
        "achieved 88% user acceptance rate on suggested prompts without manual edits.",
        "Designed prompt templates with guardrails for tone, brevity, and data privacy—ensuring "
        "no sensitive goal data leaked into model logs while maintaining suggestion relevance.",
    ]
    for item in ai_bullets:
        story.append(bullet(item, styles))

    story.extend(section("Projects", styles))

    story.append(
        Paragraph(
            "<b>SmartCart AI — Multi-Platform Grocery Price Comparator</b>",
            styles["job_header"],
        )
    )
    story.append(
        Paragraph(
            "<i>Python (FastAPI), React, LLM APIs, Web Scraping</i>&nbsp;&nbsp;&nbsp;&nbsp;Personal Project",
            styles["job_sub"],
        )
    )
    project_bullets = [
        "Built an AI-powered grocery cart assistant that accepts natural-language input "
        "(e.g., \"2L Amul milk, brown bread, 1kg rice\") and parses items using LLM-based "
        "extraction with 92% field accuracy across brand, quantity, and unit.",
        "Aggregates real-time prices from multiple grocery platforms (Blinkit, Zepto, BigBasket, "
        "Instamart), compares total cart cost side-by-side, and highlights the cheapest option "
        "with item-level price breakdowns.",
        "Flags items unavailable on specific platforms (\"not listed\" detection), suggests "
        "closest substitutes, and alerts users when a platform lacks 20%+ of cart items—reducing "
        "failed checkout attempts in testing.",
        "Delivered a React dashboard with cart builder, platform comparison table, and savings "
        "summary—helping a 50-user test cohort save an average of 18% on weekly grocery spend.",
    ]
    for item in project_bullets:
        story.append(bullet(item, styles))

    story.extend(section("Education", styles))
    story.append(
        Paragraph(
            "<b>Indian Institute of Information Technology Allahabad (IIIT-A)</b>&nbsp;&nbsp;&nbsp;&nbsp;Prayagraj, India",
            styles["job_header"],
        )
    )
    story.append(
        Paragraph(
            "Bachelor of Technology in Information Technology (CGPA: 8.36/10.0)",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Relevant Coursework:</b> Operating Systems, Database Management Systems, "
            "Data Structures &amp; Algorithms, Computer Networks",
            styles["body"],
        )
    )

    story.extend(section("Achievements", styles))
    ach_bullets = [
        '<link href="https://codeforces.com/profile/kAB-d">Codeforces</link> — '
        "<b>kAB-d</b> (Specialist)",
        '<link href="https://leetcode.com/Ironman15">LeetCode</link> — '
        "<b>Ironman15</b>",
        '<link href="https://www.codechef.com/users/vabsrts15">CodeChef</link> — '
        "<b>vabsrts15</b> (4-Star)",
    ]
    for item in ach_bullets:
        story.append(bullet(item, styles))

    doc.build(story)
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    generate_pdf()
