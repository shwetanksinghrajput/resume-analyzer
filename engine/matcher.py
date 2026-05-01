class ResumeMatcher:
    def calculate_match(self, resume_skills, jd_skills):
        if not jd_skills:
            return 0, set(), set()

        # Normalize everything to lowercase for the mathematical comparison
        res_lowered = {s.lower() for s in resume_skills}
        jd_lowered = {s.lower() for s in jd_skills}

        # Find the intersection and differences
        matched_keys = res_lowered.intersection(jd_lowered)
        missing_keys = jd_lowered - res_lowered

        # Calculate the Score
        score = round((len(matched_keys) / len(jd_lowered)) * 100, 2)
        
        # Map back to the original "Pretty" versions for the UI display
        # We prioritize the casing used in your provided skills list
        matched_display = {s for s in resume_skills if s.lower() in matched_keys}
        missing_display = {s for s in jd_skills if s.lower() in missing_keys}

        return score, missing_display, matched_display