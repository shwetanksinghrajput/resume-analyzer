class ResumeMatcher:
    def calculate_match(self, resume_skills, jd_skills):
        if not jd_skills:
            return 0, set(), set()

    
        res_lowered = {s.lower() for s in resume_skills}
        jd_lowered = {s.lower() for s in jd_skills}

        
        matched_keys = res_lowered.intersection(jd_lowered)
        missing_keys = jd_lowered - res_lowered

        score = round((len(matched_keys) / len(jd_lowered)) * 100, 2)
        
        matched_display = {s for s in resume_skills if s.lower() in matched_keys}
        missing_display = {s for s in jd_skills if s.lower() in missing_keys}

        return score, missing_display, matched_display
