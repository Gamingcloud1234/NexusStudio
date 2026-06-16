import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="Nexus Studio | Official",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a highly polished, clean light cinematic UI/UX
st.markdown("""
    <style>
    /* Main background and clean font styling */
    .stApp {
        background-color: #fcfbfe;
        color: #1f1a3a;
    }
    
    /* Light Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #f3f0fa !important;
        border-right: 1px solid #e1dbf0;
    }
    
    /* Custom Headers */
    .main-title {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 800;
        color: #2e1065;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .sub-title {
        color: #7c3aed;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    /* Cinematic Movie & Info Cards (Light Theme) */
    .movie-card {
        background: #ffffff;
        border: 1px solid #e2e0e8;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px 0 rgba(124, 58, 237, 0.05);
    }
    
    /* Text overrides inside dark containers if needed */
    .movie-card h2, .movie-card h4 {
        color: #2e1065 !important;
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 30px;
        font-size: 0.9rem;
        color: #6b7280;
        border-top: 1px solid #e5e7eb;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INITIALIZE PERSISTENT DATABASE (Session State)
# ==========================================
if 'applicants' not in st.session_state:
    # Seed data with dummy applications for demo purposes
    st.session_state.applicants = pd.DataFrame([
        {
            "ID": 101,
            "Date": "2026-06-14",
            "Name": "Arfeen Khan",
            "Age": 16,
            "Role Wanted": "Lead Protagonist",
            "Experience": "2 years in local theater groups.",
            "Contact": "03001234567",
            "Status": "Pending"
        },
        {
            "ID": 102,
            "Date": "2026-06-15",
            "Name": "Musab Ali",
            "Age": 17,
            "Role Wanted": "Voice Actor / Narrator",
            "Experience": "Amateur voice over work for animation clips.",
            "Contact": "03219876543",
            "Status": "Approved"
        }
    ])

# ==========================================
# SIDEBAR NAVIGATION & LOGO
# ==========================================
with st.sidebar:
    # Display Studio Logo
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.header("✨ NEXUS STUDIO")
        st.caption("⚠️ Upload 'logo.jpg' to GitHub to show image logo here.")
        
    st.markdown("---")
    page = st.radio("NAVIGATION", ["🏠 Home & Latest Release", "🎭 Audition Casting Call", "🔑 Studio Admin Panel"])
    st.markdown("---")
    
    st.markdown("### 📞 Contact Studio")
    st.caption("📧 NexusStudioOfficial0@gmail.com")
    st.caption("📱 03199263861")

# ==========================================
# PAGE 1: HOME & LATEST RELEASE
# ==========================================
if page == "🏠 Home & Latest Release":
    st.markdown("<h1 class='main-title'>NEXUS STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Where Imagination Meets Reality</p>", unsafe_allow_html=True)
    
    # Hero Movie Section
    st.markdown("### 🎬 Latest Blockbuster Release")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        try:
            st.image("thumbnail.jpg", caption="Now Streaming Worldwide", use_container_width=True)
        except:
            st.info("ℹ️ Upload 'thumbnail.jpg' to GitHub to show your movie poster here.")
            
    with col2:
        st.markdown("""
            <div class='movie-card'>
                <h2 style='margin-top:0;'>The Last Resistance</h2>
                <p><strong>Genre:</strong> Animated / Minecraft Cinematic Epic</p>
                <p><strong>Status:</strong> Official Trailer Out Now</p>
                <p style='color: #4b5563; line-height: 1.6;'>
                    Step into an expansive voxel world facing an unprecedented threat. 
                    As ancient fortresses crumble and shadow armies march across the Overworld, 
                    a disparate band of heroes must unite to stage <b>The Last Resistance</b>.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.button("▶ Watch Official Trailer", use_container_width=True)
        if st.button("🎭 Join the Cast of Next Project", type="primary", use_container_width=True):
            st.info("Switch to the 'Audition Casting Call' tab in the sidebar to apply!")

    # About Us Cards
    st.markdown("### 🌐 About Our Production House")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='movie-card'><h4>🚀 Our Vision</h4><p style='font-size:0.9rem; color:#4b5563;'>Pushing the absolute boundaries of digital storytelling, combining community building, unique lore, and crisp cinematic animations.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='movie-card'><h4>💻 Next-Gen CGI</h4><p style='font-size:0.9rem; color:#4b5563;'>Utilizing streamlined tools, advanced graphic fidelity, and specialized scripting pipelines to bring blocks and custom models to life.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='movie-card'><h4>🌟 Join the Team</h4><p style='font-size:0.9rem; color:#4b5563;'>We regularly scout for raw, talented actors, scriptwriters, and voice talent to feature in premium, serialized narrative events.</p></div>", unsafe_allow_html=True)

# ==========================================
# PAGE 2: AUDITION CASTING CALL
# ==========================================
elif page == "🎭 Audition Casting Call":
    st.markdown("<h1 class='main-title'>ONLINE AUDITION PORTAL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Submit your profile to be considered for our upcoming cinematic universes.</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='movie-card'>
            <h4 style='margin-top:0; color:#7c3aed;'>Submission Instructions</h4>
            <ul style='font-size:0.95rem; color:#4b5563; padding-left:20px;'>
                <li>Fill out all active fields accurately so our casting directors can parse your profile.</li>
                <li>Ensure your active mobile/WhatsApp contact is correct.</li>
                <li>The review team handles evaluations on a weekly rolling basis. Shortlisted candidates will receive callbacks.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("audition_form", clear_on_submit=True):
        st.subheader("Personal & Casting Details")
        
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            full_name = st.text_input("Full Name*", placeholder="e.g., Azan Farooq")
            age = st.number_input("Age*", min_value=5, max_value=100, value=15)
            contact_num = st.text_input("Contact Number (WhatsApp/Phone)*", placeholder="e.g., 03xxxxxxxxx")
            
        with f_col2:
            role_type = st.selectbox(
                "Target Role Type*", 
                ["Lead Protagonist", "Main Antagonist / Villain", "Supporting Character", "Comic Relief", "Voice Actor / Narrator", "Background Extra"]
            )
            experience = st.text_area("Prior Acting Experience / Short Bio", placeholder="Tell us about any previous voice lines, theater, video shorts, or why you want to act...")
            
        submitted = st.form_submit_button("🚀 Submit Audition Profile", type="primary")
        
        if submitted:
            if not full_name or not contact_num:
                st.error("❌ Please provide both your Name and Contact Number to apply.")
            else:
                # Append new data row securely
                new_id = st.session_state.applicants["ID"].max() + 1 if len(st.session_state.applicants) > 0 else 101
                new_row = {
                    "ID": new_id,
                    "Date": datetime.today().strftime('%Y-%m-%d'),
                    "Name": full_name,
                    "Age": int(age),
                    "Role Wanted": role_type,
                    "Experience": experience if experience else "None provided.",
                    "Contact": contact_num,
                    "Status": "Pending"
                }
                st.session_state.applicants = pd.concat([st.session_state.applicants, pd.DataFrame([new_row])], ignore_index=True)
                
                st.balloons()
                st.success(f"🎉 Success! Thank you {full_name}. Your profile has been locked in under Audition ID #{new_id}. Nexus Studio management will evaluate your profile.")

# ==========================================
# PAGE 3: STUDIO ADMIN PANEL
# ==========================================
elif page == "🔑 Studio Admin Panel":
    st.markdown("<h1 class='main-title'>STUDIO MANAGEMENT CORE</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Reviewing Applications & Casting Approvals</p>", unsafe_allow_html=True)
    
    # Secure Password Simulation
    st.sidebar.warning("🔒 Administrative access restricted.")
    password = st.sidebar.text_input("Enter Admin Password", type="password")
    
    if password != "nexus2026":
        st.info("💡 Please enter the valid Studio Admin Password via the sidebar to view incoming applications and manage applicant rosters.")
        st.caption("Tip for testing: Password is 'nexus2026'")
    else:
        st.success("🔓 Access Granted. Welcome, Studio Director.")
        
        # Metrics Row
        df = st.session_state.applicants
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Applicants", len(df))
        m2.metric("Pending Review", len(df[df["Status"] == "Pending"]))
        m3.metric("Approved Cast", len(df[df["Status"] == "Approved"]))
        m4.metric("Archived", len(df[df["Status"] == "Rejected"]))
        
        st.markdown("---")
        
        # Filter Layout
        st.subheader("📋 Registered Talent Pipeline")
        status_filter = st.selectbox("Quick Status Filter", ["All", "Pending", "Approved", "Rejected"])
        
        filtered_df = df if status_filter == "All" else df[df["Status"] == status_filter]
        
        if filtered_df.empty:
            st.warning("No applications found matching this status filter.")
        else:
            # Render a readable clean datatable
            st.dataframe(filtered_df, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.subheader("⚙️ Update Selection Verdict")
            
            # Form actions to change statuses
            with st.form("action_form"):
                select_id = st.selectbox("Select Applicant ID to evaluate", filtered_df["ID"].tolist())
                new_status = st.radio("Verdict Decision", ["Pending", "Approved", "Rejected"], horizontal=True)
                update_btn = st.form_submit_button("Save Casting Verdict")
                
                if update_btn:
                    st.session_state.applicants.loc[st.session_state.applicants["ID"] == select_id, "Status"] = new_status
                    st.success(f"Updated Profile Entry ID #{select_id} status to '{new_status}' successfully!")
                    st.rerun()

# ==========================================
# FOOTER COMPONENT
# ==========================================
st.markdown(f"""
    <div class='footer'>
        <p>© {datetime.now().year} <b>Nexus Studio Official</b>. All Rights Reserved.</p>
        <p style='font-size: 0.8rem;'>Contact: NexusStudioOfficial0@gmail.com | 03199263861</p>
    </div>
""", unsafe_allow_html=True)
                     

