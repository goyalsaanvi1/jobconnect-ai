
def run_mock_chat(input_text):
    input_text = input_text.lower()

    if "software engineer" in input_text:
        return (
            "To become a software engineer, you'll want to build a strong foundation in Python or JavaScript, "
            "practice data structures and algorithms, and understand how web applications work end to end."
        )
    elif "resume" in input_text:
        return (
            "Make sure your resume highlights your technical skills, projects with real-world impact, "
            "and any internships or relevant coursework. Keep it concise and tailored to the job description."
        )
    elif "career switch" in input_text or "switch careers" in input_text:
        return (
            "Switching careers can be daunting, but totally doable! Start with free online courses, work on personal projects, "
            "and try to get involved in open source or freelancing to build credibility in the new field."
        )
    elif "internship" in input_text:
        return (
            "Start looking early, especially on LinkedIn and job boards. Apply widely, focus your resume on projects, "
            "and be ready to talk about what you’ve built — especially if it’s something like this chatbot!"
        )
    elif "linkedin" in input_text:
        return (
            "Your LinkedIn should mirror your resume, but with a more personal tone. Include a headline that reflects your goals, "
            "a concise About section, and make sure to list your projects and skills."
        )
    else:
        return (
            "That's a great question! While I'm still in mock mode, I'm built to answer career-related questions like:\n"
            "- How do I get an internship?\n"
            "- What skills are needed for data science?\n"
            "- How should I improve my resume?\n\n"
            "Try asking something like that!"
        )