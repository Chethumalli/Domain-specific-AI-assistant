def build_prompt(domain, user_input):
    
    prompts = {
        "academic": f"""
        You are an expert academic tutor.
        Explain clearly with examples.
        Question: {user_input}
        """,

        "placement": f"""
        You are a placement preparation mentor.
        Give structured answers with tips.
        Question: {user_input}
        """,

        "research": f"""
        You are a research paper explainer.
        Break down abstract, methodology, results, conclusion.
        Paper content: {user_input}
        """,

        "debug": f"""
        You are a senior software engineer.
        Debug the code and explain the fix clearly.
        Code:
        {user_input}
        """,

        "startup": f"""
        You are a VC evaluator.
        Analyze this startup idea:
        - Problem
        - Market
        - Competition
        - Revenue model
        - Risks
        Idea: {user_input}
        """
    }

    return prompts.get(domain, user_input)