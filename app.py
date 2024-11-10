import streamlit as st

# App Title
st.title("The Money Confidence Code")
st.subheader("Transform Your Finances and Build a Life You Love")

# Introduction
st.write("""
Welcome to *The Money Confidence Code*, a program based on the Confident Money Method. This guide will take you through seven pillars to help you define your values, boost self-worth, set meaningful goals, embrace abundance, prepare for challenges, establish boundaries, and take aligned action. Each chapter includes practical exercises to support your journey toward financial confidence and freedom.
""")

# Sidebar Navigation
chapters = [
    "Chapter 1: Define – Clarifying Your Money Values",
    "Chapter 2: Believe – Shifting Self-Worth Beliefs",
    "Chapter 3: Set – Creating Aligned Financial Goals",
    "Chapter 4: Embrace – Cultivating an Abundance Mindset",
    "Chapter 5: Prepare – Building a Resilience Plan",
    "Chapter 6: Establish – Setting Healthy Financial Boundaries",
    "Chapter 7: Act – Taking Consistent, Aligned Action"
]

selected_chapter = st.sidebar.selectbox("Select a Chapter", chapters)

# Chapter Content
if selected_chapter == "Chapter 1: Define – Clarifying Your Money Values":
    st.header("Define – Clarifying Your Money Values")
    st.write("""
    This chapter focuses on understanding what drives your financial decisions by defining your core money values.
    """)
    
    # Subchapters for Chapter 1
    st.subheader("Subchapter 1.1: Discovering What Truly Matters Financially")
    st.write("Explore what truly matters to you on a financial level.")
    
    st.subheader("Subchapter 1.2: Recognizing Values-Based Money Patterns")
    st.write("Identify patterns in your spending, saving, and investing that reflect your values.")
    
    st.subheader("Subchapter 1.3: Aligning Money Values with Life Goals")
    st.write("Learn to align your financial choices with your life goals for a cohesive vision.")
    
    st.subheader("Subchapter 1.4: Crafting Your Financial Values Statement")
    st.write("Create a values statement to summarize your core money principles.")
    
elif selected_chapter == "Chapter 2: Believe – Shifting Self-Worth Beliefs":
    st.header("Believe – Shifting Self-Worth Beliefs")
    st.write("""
    Build confidence in your financial worth by transforming limiting beliefs and adopting an empowered mindset.
    """)
    
    # Subchapters for Chapter 2
    st.subheader("Subchapter 2.1: Identifying Limiting Beliefs About Money")
    st.write("Explore and understand any negative beliefs around money.")
    
    st.subheader("Subchapter 2.2: Reframing Negative Self-Talk")
    st.write("Practice reframing unhelpful thoughts to build a positive mindset.")
    
    st.subheader("Subchapter 2.3: Building Self-Worth Beyond Finances")
    st.write("Strengthen your self-worth independently of financial success.")
    
    st.subheader("Subchapter 2.4: Creating Affirmations for Financial Empowerment")
    st.write("Create empowering affirmations to support your new mindset.")
    
elif selected_chapter == "Chapter 3: Set – Creating Aligned Financial Goals":
    st.header("Set – Creating Aligned Financial Goals")
    st.write("""
    Learn to set meaningful, achievable goals that align with your personal values and vision.
    """)
    
    # Subchapters for Chapter 3
    st.subheader("Subchapter 3.1: Goal-Setting with Purpose")
    st.write("Discover the purpose behind each financial goal.")
    
    st.subheader("Subchapter 3.2: Translating Life Goals Into Financial Milestones")
    st.write("Break down life aspirations into achievable financial goals.")
    
    st.subheader("Subchapter 3.3: The SMART Way to Set Financial Goals")
    st.write("Learn the SMART goal-setting method for clarity and focus.")
    
    st.subheader("Subchapter 3.4: Visualizing and Committing to Your Financial Future")
    st.write("Visualize your success and strengthen commitment to your goals.")
    
elif selected_chapter == "Chapter 4: Embrace – Cultivating an Abundance Mindset":
    st.header("Embrace – Cultivating an Abundance Mindset")
    st.write("""
    Embrace a mindset of growth and possibilities by developing an abundance mentality.
    """)
    
    # Subchapters for Chapter 4
    st.subheader("Subchapter 4.1: Understanding Scarcity vs. Abundance Mindsets")
    st.write("Identify and shift any scarcity-based thoughts.")
    
    st.subheader("Subchapter 4.2: Replacing Limiting Beliefs with Growth Beliefs")
    st.write("Develop growth-oriented beliefs around wealth and success.")
    
    st.subheader("Subchapter 4.3: Recognizing Opportunities for Wealth and Success")
    st.write("Learn to recognize wealth-building opportunities in everyday life.")
    
    st.subheader("Subchapter 4.4: Daily Practices for Cultivating Abundance")
    st.write("Incorporate daily practices to nurture an abundant mindset.")
    
elif selected_chapter == "Chapter 5: Prepare – Building a Resilience Plan":
    st.header("Prepare – Building a Resilience Plan")
    st.write("""
    Build a financial resilience plan to navigate challenges and unexpected events with confidence.
    """)
    
    # Subchapters for Chapter 5
    st.subheader("Subchapter 5.1: Identifying Potential Financial Roadblocks")
    st.write("Anticipate potential challenges that could hinder your goals.")
    
    st.subheader("Subchapter 5.2: Building Emergency Funds and Safety Nets")
    st.write("Understand the value of an emergency fund for security.")
    
    st.subheader("Subchapter 5.3: Strengthening Financial Flexibility")
    st.write("Build financial flexibility for uncertain times.")
    
    st.subheader("Subchapter 5.4: Developing a Support System for Success")
    st.write("Create a support system for encouragement and accountability.")
    
elif selected_chapter == "Chapter 6: Establish – Setting Healthy Financial Boundaries":
    st.header("Establish – Setting Healthy Financial Boundaries")
    st.write("""
    Protect your financial health by establishing and maintaining clear boundaries.
    """)
    
    # Subchapters for Chapter 6
    st.subheader("Subchapter 6.1: The Role of Boundaries in Financial Success")
    st.write("Understand how financial boundaries support your success.")
    
    st.subheader("Subchapter 6.2: Boundaries in Spending, Saving, and Giving")
    st.write("Set boundaries in spending, saving, and sharing resources.")
    
    st.subheader("Subchapter 6.3: Navigating Boundaries in Relationships")
    st.write("Navigate boundaries with friends, family, and colleagues.")
    
    st.subheader("Subchapter 6.4: Staying Committed to Your Boundaries")
    st.write("Learn practical strategies for upholding your boundaries.")
    
elif selected_chapter == "Chapter 7: Act – Taking Consistent, Aligned Action":
    st.header("Act – Taking Consistent, Aligned Action")
    st.write("""
    The final chapter focuses on putting everything into action, creating lasting financial change.
    """)
    
    # Subchapters for Chapter 7
    st.subheader("Subchapter 7.1: The Power of Consistency in Financial Growth")
    st.write("Explore the importance of consistent action.")
    
    st.subheader("Subchapter 7.2: Developing a Financial Action Plan")
    st.write("Create a step-by-step plan for your financial journey.")
    
    st.subheader("Subchapter 7.3: Building Accountability and Momentum")
    st.write("Learn to stay accountable and maintain momentum.")
    
    st.subheader("Subchapter 7.4: Celebrating Milestones and Adjusting the Journey")
    st.write("Celebrate successes and adjust your plans as needed.")
