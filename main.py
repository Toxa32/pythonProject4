from flask import Flask

from utils import load_json, get_all_candidates, format_candidate, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidate(candidates)
    result = '<pre>'

    for candidate in candidates:
        result += f"""
                {candidate["name"]}\n
                {candidate["position"]}\n
                {candidate["skills"]}\n
        """
    result += '</pre>'
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Поиск кандидатов по id"""
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidate([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Поиск кандидатов по навыку"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidate(candidates)
    return result


app.run()
