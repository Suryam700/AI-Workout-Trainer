import streamlit as st
from services.auth.login import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS

def main():
    st.set_page_config(
        page_title="AI Real-Time Workout Trainer",
        page_icon="🏋️",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    if not render_login_wall():
        return

    initial_session_defaults()

    with st.sidebar:
        st.title("🏋️ AI Training info...")
        if st.session_state["username"]:
            st.caption(f"👤 login as {st.session_state["username"]}")
        st.divider()

        st.subheader("Workout Plan")

        if not st.session_state["workout_started"]:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")
            st.number_input("Sets", min_value=1, key="plan_sets", step=1)
            st.number_input("Sets", min_value=1, key="plan_reps", step=1)

            st.space()

            if st.button("Start Session", width="stretch", key="start_session_button"):
                st.session_state["workout_started"] = True

            st.rerun()
        else:
            exercise = st.session_state["plan_exercise"]
            sets = st.session_state["plan_sets"]
            reps = st.session_state["plan_reps"]
            st.info(f"**{exercise}** -- {sets} Sets X {reps} Reps")

            if st.button("End Session", key="end_session_button", width="stretch"):
                st.session_state["workout_started"] = False
                st.rerun()

            if st.session_state["workout_started"]:
                st.divider()

                exercise = st.session_state.get("exercise_type")
                total_reps = st.session_state.get("reps")
                current_set_reps = st.session_state.get("current_set_reps")
                reps_per_set = st.session_state.get("plan_reps")
                sets_completed = st.session_state.get("sets_completed")
                target_sets = st.session_state.get("plan_sets")

                st.subheader("Progress")

                st.metric("Total Reps", f"{total_reps}")
                st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
                st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

                st.divider()

                if exercise == "Squats":
                    st.subheader("Squat Metrics")
                    st.metric("Knee Angle", f"{st.session_state.knee_angle}°")
                    st.metric("Back Angle", f"{st.session_state.back_angle}°")
                    st.metric("Depth Status", st.session_state.depth_status)

                elif exercise == "Push-ups":
                    st.subheader("Push-up Metrics")
                    st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                    st.metric("Body Alignment", st.session_state.body_alignment)
                    st.metric("Hip Position", st.session_state.hip_status)

                elif exercise == "Biceps Curls (Dumbbell)":
                    st.subheader("Curl Metrics")
                    st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                    st.metric("Shoulder Stability", st.session_state.shoulder_status)
                    st.metric("Swing Detection", st.session_state.swing_status)

                elif exercise == "Shoulder Press":
                    st.subheader("Shoulder Press Metrics")
                    st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                    st.metric("Arm Extension", st.session_state.extension_status)
                    st.metric("Back Arch", st.session_state.back_arch_status)

                elif exercise == "Lunges":
                    st.subheader("Lunge Metrics")
                    st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}°")
                    st.metric("Torso Angle", f"{st.session_state.torso_angle}°")
                    st.metric("Balance Status", st.session_state.balance_status)

if __name__ == "__main__":
    main()
