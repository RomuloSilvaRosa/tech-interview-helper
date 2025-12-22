import streamlit as st
import pickle
from pillars_models import (
    PILLARS,
    PillarCharacteristic,
    PositivePillarCharacteristic,
    NegativePillarCharacteristic,
    CANDIDATE_TYPES,
    MANDATORY_PILLARS
)

'''TODO:
- Add job description input (from greenhouse)
- Add hour/time of generated report
- Codeshare link url
- Codeshare results
- Add questions to be asked:
- Ask an llm to pre-generate questions based on the pillars / CV of the candidate - At [company name], why you did this or that?
- Store questions in a json file
- Allow interviewer to add custom questions
- Allow interviewer to rate candidate answers to questions - assess sincerity in the answers
- Store all this data in the final report
Verify inconsistencies between interviewer evaluations and Talent feedback
'''

import json
from pathlib import Path
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)
import threading




POSSIBLE_GRADES = [1, 2, 3, 4, "NOT EVALUATED"]
# CANDIDATE_TYPES = ["DS", "MLE", "MLOps"]

def add_positive(i):
    st.session_state[f"extra_pos_{i}"].append(
        PositivePillarCharacteristic(description="")
    )

def add_negative(i):
    st.session_state[f"extra_neg_{i}"].append(
        NegativePillarCharacteristic(description="")
    )

def generate_report(report):
    md = "# Pillars\n\n"

    for r in report:
        md += f"## {r['name']}\n\n"
        md += f"{r['description']}\n\n"
        md += f"**Grade:** {r['grade']}/4\n\n"

        md += "**Positive:**\n"
        if r["positive"]:
            for x in r["positive"]:
                if x.checked:
                    md += f"\n(+) {str(x)}\n"
        else:
            md += "- None\n"

        md += "\n**Negative:**\n"
        if r["negative"]:
            for x in r["negative"]:
                if x.checked:
                    md += f"\n(-) {str(x)}\n"
        else:
            md += "- None\n"
        comments = r['comments'] or "No additional comments."
        md += f"\n**Overall interviewer notes:**\n{comments}\n"

        md += "\n---\n\n"
    md += "## Notes\n\n"
    other_notes_data = collect_other_notes()
    # print(other_notes_data)
    for key, value in other_notes_data.items():
        title = key.replace("_", " ").title()
        md += f"### {title}\n{value}\n\n"
    return md

def render_characteristic(char, key_prefix, editable=False):
    col_check, col_prompted, col_add = st.columns([6, 2, 2])

    with col_check:
        if editable:
            char.description = st.text_input(
                "",
                value=char.description,
                placeholder="Characteristic description",
                key=f"{key_prefix}_desc"
            )
            checked = st.checkbox(
                "Selected",
                key=f"{key_prefix}_checked"
            )
        else:
            checked = st.checkbox(
                char.description,
                key=f"{key_prefix}_checked"
            )

    with col_prompted:
        char.prompted = st.checkbox(
            "Prompted",
            value=char.prompted,
            key=f"{key_prefix}_prompted"
        )

    with col_add:
        if checked:
            # if st.button("Add comment", key=f"{key_prefix}_add_comment"):
            st.session_state[f"{key_prefix}_show_comment"] = True
    char.checked = checked
    if checked and st.session_state.get(f"{key_prefix}_show_comment", False):
        char.additional_commentary = st.text_area(
            "How it was evaluated (Optional)",
            value=char.additional_commentary,
            key=f"{key_prefix}_commentary",
            height=1
        )

    return checked
candidate_type = None

def collect_other_notes():
    _collected = {}
    for k, v in st.session_state.items():
        if k.startswith("notes_"):
            # print(k, v)
            _collected[k] = v
    return _collected

def other_notes():
    global candidate_type
    candidate_type = st.radio(
                "candidate type",
                CANDIDATE_TYPES,
                horizontal=True,
                index=0,
                # index=None,
                key=f"candidate"
            )
    
    small_notes = ["Candidate Name", "Codeshare Link", "Codeshare Results", "Job Description Link"]
    col_pos, col_neg = st.columns([7, 7])
    len_small_notes = len(small_notes)
    with col_pos:
        for x in small_notes[:len_small_notes//2]:
            with st.expander(x, expanded=True):
                st.text_area(f"Enter {x}", key=f"notes_{x.lower().replace(' ', '_')}", height=100)
    with col_neg:
        for x in small_notes[len_small_notes//2:]:
            with st.expander(x, expanded=True):
                st.text_area(f"Enter {x}", key=f"notes_{x.lower().replace(' ', '_')}", height=100)
    overall_notes= ["Talent interviewer scoreboard", "Questions", "Notes", "Candidate CV", "Job Description"]
    for x in overall_notes:
        st.text_area(f"Enter {x}", key=f"notes_{x.lower().replace(' ', '_')}", height=100)

def pillars_page():
    st.set_page_config(layout="wide")
    other_notes()
    candidate_type = st.session_state.get("candidate", "MLE")
    st.title("Pillars Assessment -" + candidate_type )
    

    report = []
    all_graded = True

    for i, pillar in enumerate(PILLARS):
        pos_key = f"extra_pos_{i}"
        neg_key = f"extra_neg_{i}"

        st.session_state.setdefault(pos_key, [])
        st.session_state.setdefault(neg_key, [])
        expanded = True
        if pillar.shorten not in MANDATORY_PILLARS[candidate_type]:
            expanded = False

        with st.expander(pillar.name + (" (Mandatory)" if expanded else ""), expanded=expanded):
            st.markdown(pillar.description)

            col_pos, col_neg = st.columns([7, 7])

            with col_pos:
                st.markdown("### Positive")
                positives = []

                for j, p in enumerate(pillar.positive):
                    # st.markdown("**Characteristic**")
                    render_characteristic(p, f"p_{i}_{j}")
                    positives.append(p)

                for j, p in enumerate(st.session_state[pos_key]):
                    st.markdown("**Additional positive**")
                    render_characteristic(p, f"p_extra_{i}_{j}", True)
                    positives.append(p)

                st.button(
                    "➕ Add positive",
                    key=f"add_pos_{i}",
                    on_click=add_positive,
                    args=(i,)
                )

            with col_neg:
                st.markdown("### Negative")
                negatives = []

                for j, n in enumerate(pillar.negative):
                    # st.markdown("**Characteristic**")
                    render_characteristic(n, f"n_{i}_{j}",)
                    negatives.append(n)

                for j, n in enumerate(st.session_state[neg_key]):
                    st.markdown("**Additional negative**")
                    render_characteristic(n, f"n_extra_{i}_{j}", True)
                    negatives.append(n)

                st.button(
                    "➕ Add negative",
                    key=f"add_neg_{i}",
                    on_click=add_negative,
                    args=(i,)
                )

            pillar.grade = st.radio(
                "Grade",
                POSSIBLE_GRADES,
                horizontal=True,
                index=None,
                key=f"grade_{i}"
            )

            if pillar.grade is None:
                all_graded = False

            pillar.added_comments = st.text_area(
                "Overall comments from interviewer",
                value=pillar.added_comments,
                key=f"comments_{i}",
                height=1
            )

            report.append({
                "name": pillar.name,
                "description": pillar.description,
                "positive": positives,
                "negative": negatives,
                "grade": pillar.grade,
                "comments": pillar.added_comments
            })

    st.divider()
    def background_report():
        # other_notes_data = collect_other_notes()
        md = generate_report(report)

        candidate_name = (
            st.session_state["notes_candidate_name"]
            .replace(" ", "_")
            .lower()
        )
        if not candidate_name:
            return

        time_bucket = current_10min_bucket()
        safe_name = candidate_name.replace(" ", "_").lower()
        filename = f"notes_{safe_name}_{time_bucket}.md"
        filepath = REPORTS_DIR / filename

        filepath.write_text(md, encoding="utf-8")

        # st.success(f"Report saved as {filename}")

        # st.markdown(md)
    background_report()
    # threading.Thread(
    #     target=background_report,
    #     daemon=True
    # ).start()
    if st.button("Generate Markdown Report"):

        md = generate_report(report)

        st.markdown(md)
        st.download_button(
            "Download report",
            md,
            file_name="interview_evaluation.md"
        )
def current_10min_bucket():
    now = datetime.now()
    minute_bucket = (now.minute // 10) * 10
    return now.replace(minute=minute_bucket, second=0).strftime("%H%M")

if __name__ == "__main__":
    pillars_page()
