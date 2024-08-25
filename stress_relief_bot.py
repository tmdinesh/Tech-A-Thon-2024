import random

class StressReliefBot:
    def __init__(self):
        self.context = []
        self.responses = {
            "greeting": [
                "Hello! I'm here to help you manage stress. How are you feeling today?",
                "Welcome to your stress relief session. What's on your mind?",
                "Hi there! I'm your virtual stress management assistant. How can I support you today?",
                "Good to see you! Let's work on reducing your stress. What would you like to focus on?"
            ],
            "general_stress": [
                "I'm sorry to hear you're feeling stressed. Remember, it's a normal reaction to challenging situations. Would you like to try a quick relaxation technique?",
                "Stress can be overwhelming, but you're not alone. Let's break down what's causing your stress and tackle it step by step. What's the main thing on your mind?",
                "It sounds like you're dealing with a lot right now. Have you tried any stress-relief methods that have worked for you in the past?",
                "Acknowledging your stress is a great first step. Now, let's work on some strategies to help you feel more in control. Are you open to trying a mindfulness exercise?"
            ],
            "work_stress": [
                "Work-related stress is common. Have you tried setting boundaries between work and personal time?",
                "It sounds like your job is causing you stress. Let's brainstorm some ways to make your work environment more manageable. What's the most challenging aspect of your work right now?",
                "Work stress can be draining. Have you considered talking to your supervisor about your workload or any specific issues?",
                "Remember, it's important to take breaks during your workday. Even a 5-minute walk can help reset your mind. Would you like some tips on quick stress-relief exercises you can do at work?"
            ],
            "academic_stress": [
                "Academic pressure can be intense. Have you tried breaking your study sessions into smaller, manageable chunks?",
                "Feeling stressed about school is normal. Let's work on a study schedule that includes regular breaks and self-care. How does that sound?",
                "Remember, perfection isn't the goal - progress is. Can you identify one small step you can take today towards your academic goals?",
                "It's great that you're committed to your studies, but balance is key. Have you made time for activities you enjoy outside of academics?"
            ],
            "relationship_stress": [
                "Relationship stress can be particularly challenging. Have you tried openly communicating your feelings with the person involved?",
                "It's important to maintain healthy boundaries in relationships. Would you like to discuss some strategies for setting and maintaining boundaries?",
                "Remember, it's okay to prioritize your own well-being in relationships. What do you think you need right now to feel more at ease?",
                "Conflicts in relationships are normal, but they can be stressful. Would you like to explore some conflict resolution techniques?"
            ],
            "financial_stress": [
                "Financial stress can feel overwhelming. Have you considered creating a budget to help manage your finances?",
                "Remember, many people face financial challenges. Would you like to discuss some strategies for financial planning or resources for financial advice?",
                "It's brave of you to address your financial stress. Small steps can make a big difference. Could we start by looking at one area where you might be able to reduce expenses?",
                "Financial worries can be all-consuming. Let's try to focus on what you can control right now. What's one small financial goal you could set for this week?"
            ],
            "health_stress": [
                "Health concerns can be a significant source of stress. Have you been able to discuss your worries with a healthcare professional?",
                "It's natural to feel stressed about health issues. Remember to be kind to yourself. Would you like to try a gentle relaxation exercise?",
                "Stress can impact our health, and health issues can cause stress. It's a cycle. Let's focus on small, healthy habits you can incorporate into your daily routine. What's one healthy change you'd like to make?",
                "Managing health-related stress often involves a holistic approach. Have you considered how factors like sleep, diet, and exercise might be affecting your overall well-being?"
            ],
            "social_stress": [
                "Social situations can be stressful for many people. Would you like to discuss some strategies for feeling more comfortable in social settings?",
                "It's okay to feel overwhelmed by social interactions. Remember, it's quality over quantity when it comes to relationships. Can you identify one or two key relationships you'd like to nurture?",
                "Social stress is common. Have you tried setting small, manageable goals for social interactions? We could work on that together.",
                "Remember, it's okay to take breaks from social activities when you need to recharge. How can you create a balance between social time and alone time that feels good for you?"
            ],
            "future_anxiety": [
                "Worrying about the future is very common. Let's try to focus on what you can control in the present moment. What's one thing you can do today to work towards your goals?",
                "It's natural to feel anxious about the unknown. Have you tried visualization techniques to imagine positive future scenarios?",
                "Anxiety about the future often stems from trying to predict outcomes. Let's work on accepting uncertainty and focusing on your strengths. What are some challenges you've successfully overcome in the past?",
                "Planning for the future is important, but so is living in the present. Could we try a mindfulness exercise to help you center yourself in the here and now?"
            ],
            "sleep_issues": [
                "Sleep problems can both cause and be caused by stress. Have you established a regular sleep routine?",
                "Difficulty sleeping can be frustrating. Let's discuss some relaxation techniques you can try before bed. Are you open to that?",
                "Sleep is crucial for managing stress. Have you considered creating a calm, device-free environment in your bedroom?",
                "Many people struggle with sleep issues. Would you like to explore some natural methods for improving sleep quality?"
            ],
            "self_esteem": [
                "Building self-esteem is an important part of managing stress. Can you tell me about a recent accomplishment, no matter how small?",
                "Remember, you are worthy and valuable, regardless of external achievements. Let's work on some positive self-talk exercises. How does that sound?",
                "Self-esteem fluctuations are normal. Have you tried keeping a journal of your positive qualities and achievements?",
                "It's important to be kind to yourself. Would you like to try a self-compassion exercise together?"
            ],
            "burnout": [
                "Burnout can be exhausting. It's important to recognize your limits. Have you been able to take any time off recently?",
                "Feeling burned out is a sign that you need to prioritize self-care. What's one small thing you could do today to recharge?",
                "Burnout often comes from prolonged stress. Let's work on identifying the key sources of your stress and brainstorm ways to address them.",
                "Remember, it's okay to ask for help when you're feeling burned out. Have you considered delegating some tasks or reaching out for support?"
            ],
            "mindfulness": [
                "Mindfulness can be a powerful tool for managing stress. Would you like to try a brief mindfulness exercise right now?",
                "Practicing mindfulness helps bring your attention to the present moment. Have you ever tried mindful breathing or body scan techniques?",
                "Mindfulness doesn't have to be complicated. It can be as simple as focusing on your senses right now. What do you see, hear, feel, smell, and taste in this moment?",
                "Regular mindfulness practice can help reduce overall stress levels. Would you be interested in learning about some apps or resources for guided mindfulness exercises?"
            ],
            "exercise": [
                "Physical activity is a great stress reliever. Have you been able to incorporate any exercise into your routine lately?",
                "Even small amounts of movement can help with stress. Would you like some ideas for quick, easy exercises you can do at home?",
                "Exercise releases endorphins, which are natural mood boosters. What type of physical activity do you enjoy most?",
                "Remember, the goal is to move your body in ways that feel good to you. This could be anything from a brisk walk to dancing in your living room. What sounds appealing to you?"
            ],
            "nutrition": [
                "Diet can have a big impact on how we handle stress. Have you noticed any connections between what you eat and how you feel?",
                "Staying hydrated and eating regular, balanced meals can help stabilize mood. Would you like some tips on stress-reducing foods?",
                "Sometimes stress can affect our eating habits. Have you found yourself eating more or less than usual when stressed?",
                "Certain foods can help support our body's stress response. Would you be interested in learning about some stress-busting superfoods?"
            ],
            "time_management": [
                "Feeling overwhelmed by tasks can be stressful. Have you tried breaking your to-do list into smaller, manageable steps?",
                "Time management is key to reducing stress. Would you like to explore some prioritization techniques?",
                "Sometimes, the Pomodoro Technique (working in focused 25-minute intervals) can help manage time and reduce stress. Have you heard of this method?",
                "Remember, it's okay to say no to non-essential tasks. How do you feel about setting boundaries around your time and commitments?"
            ],
            "relaxation_techniques": [
                "There are many relaxation techniques that can help manage stress. Would you like to try a progressive muscle relaxation exercise?",
                "Deep breathing is a simple but effective way to reduce stress. Shall we practice a deep breathing technique together?",
                "Visualization can be a powerful relaxation tool. Would you like to try imagining a peaceful, calming scene?",
                "Some people find calming music or nature sounds helpful for relaxation. Have you explored using audio for stress relief?"
            ],
            "positive_thinking": [
                "Shifting to more positive thinking patterns can help manage stress. Can you tell me about something positive that happened recently, no matter how small?",
                "Challenging negative thoughts is an important skill. Would you like to practice reframing a negative thought into a more balanced one?",
                "Gratitude can help shift our focus from stressors to positives. What are three things you're grateful for today?",
                "Positive affirmations can be helpful for some people. Would you like to create a personal positive affirmation together?"
            ],
            "support_system": [
                "Having a strong support system is crucial for managing stress. Do you have someone you can talk to about your feelings?",
                "Sometimes, talking to others who understand can be helpful. Have you considered joining a support group or online community?",
                "Remember, asking for help is a sign of strength, not weakness. How do you feel about reaching out to someone for support today?",
                "Supportive relationships are important for well-being. Can you think of ways to nurture your connections with supportive people in your life?"
            ]
        }

    def get_response(self, user_input):
        self.context.append(user_input.lower())
        
        # Check for specific keywords and return appropriate responses
        if any(word in user_input.lower() for word in ["work", "job", "career", "boss", "colleague"]):
            return random.choice(self.responses["work_stress"])
        elif any(word in user_input.lower() for word in ["school", "study", "exam", "homework", "grade"]):
            return random.choice(self.responses["academic_stress"])
        elif any(word in user_input.lower() for word in ["relationship", "partner", "friend", "family"]):
            return random.choice(self.responses["relationship_stress"])
        elif any(word in user_input.lower() for word in ["money", "finance", "debt", "bill"]):
            return random.choice(self.responses["financial_stress"])
        elif any(word in user_input.lower() for word in ["health", "sick", "illness", "doctor"]):
            return random.choice(self.responses["health_stress"])
        elif any(word in user_input.lower() for word in ["social", "party", "meetup", "gathering"]):
            return random.choice(self.responses["social_stress"])
        elif any(word in user_input.lower() for word in ["future", "uncertain", "worry about"]):
            return random.choice(self.responses["future_anxiety"])
        elif any(word in user_input.lower() for word in ["sleep", "insomnia", "tired", "fatigue"]):
            return random.choice(self.responses["sleep_issues"])
        elif any(word in user_input.lower() for word in ["confidence", "self-esteem", "self worth"]):
            return random.choice(self.responses["self_esteem"])
        elif any(word in user_input.lower() for word in ["burnout", "exhausted", "overwhelmed"]):
            return random.choice(self.responses["burnout"])
        elif any(word in user_input.lower() for word in ["mindful", "present", "awareness"]):
            return random.choice(self.responses["mindfulness"])
        elif any(word in user_input.lower() for word in ["exercise", "workout", "physical activity"]):
            return random.choice(self.responses["exercise"])
        elif any(word in user_input.lower() for word in ["food", "diet", "eating", "nutrition"]):
            return random.choice(self.responses["nutrition"])
        elif any(word in user_input.lower() for word in ["time", "schedule", "busy", "overwhelmed"]):
            return random.choice(self.responses["time_management"])
        elif any(word in user_input.lower() for word in ["relax", "calm", "peace", "tranquil"]):
            return random.choice(self.responses["relaxation_techniques"])
        elif any(word in user_input.lower() for word in ["positive", "optimism", "happy"]):
            return random.choice(self.responses["positive_thinking"])
        elif any(word in user_input.lower() for word in ["support", "help", "talk to someone"]):
            return random.choice(self.responses["support_system"])
        elif any(word in user_input.lower() for word in ["hello", "hi", "hey", "greetings"]):
            return random.choice(self.responses["greeting"])
        else:
            return random.choice(self.responses["general_stress"])

    def suggest_activity(self):
        activities = [
            "Let's try a quick breathing exercise. Inhale deeply for 4 counts, hold for 4, then exhale for 4. Repeat this 5 times.",
            "How about a gratitude practice? Can you list three things you're grateful for right now?",
            "Let's do a brief body scan. Start at your toes and slowly move up, relaxing each part of your body as you go.",
            "Try this grounding technique: Name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "Let's practice progressive muscle relaxation. Start by tensing and then relaxing each muscle group in your body, from your feet to your head.",
            "How about a quick mindfulness exercise? Focus on your breath for the next 60 seconds, observing each inhale and exhale without judgment.",
            "Try this visualization: Imagine a peaceful place where you feel completely relaxed. What do you see, hear, smell, and feel in this place?",
            "Let's do some gentle stretching. Can you slowly roll your shoulders, neck, and ankles to release any tension?",
            "How about a quick journaling session? Write down your current thoughts and feelings for the next 5 minutes without censoring yourself.",
            "Try this positive affirmation: 'I am capable of handling whatever comes my way.' Repeat it to yourself 5 times.",
            "Let's practice some self-compassion. Speak to yourself as you would to a dear friend who's going through a tough time.",
            "How about a brief nature connection? If possible, step outside or look out a window and observe the natural world for a few minutes.",
            "Try this quick stress-relief technique: Gently massage your temples and the back of your neck for a minute.",
            "Let's do a creativity exercise. Doodle or draw freely for the next 5 minutes without worrying about the result.",
            "How about some light physical activity? Do 10 jumping jacks or march in place for a minute to get your blood flowing."
        ]
        return random.choice(activities)