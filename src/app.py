"""
Simple Final Exam Grade Calculator

Author: Wolf Paulus (wolf@paulus.com)
Author: Nikhil Dave
"""

import streamlit as st
from log import logger


def determine_minimum_final_grade(
    current_course_grade: float, final_weight: float, desired_grade: float
):
    """
    Get the grade required on a final exam to get a desired overall course grade

    All arguments should be expressed as ratios - 0 = 0%, 1 = 100%

    The math for the final grade only works with everything as a ratio, so all
    the grades must be converted

    Arguments:
        current_course_grade: The current grade in the course, excluding the
            final exam.
        final_weight: The weight of the final exam
        desired_grade: The desired grade in the course

    """
    try:
        required_grade = (
            desired_grade - (1 - final_weight) * current_course_grade
        ) / final_weight
    except ZeroDivisionError:
        required_grade = 0
        logger.debug(
            "0 passed as a final exam weight. Setting required_grade to 0")

    logger.info(f"Returning {required_grade}")
    return max(required_grade, 0)


# Value used to track how many Streamlit widgets can be created within a singular calculator UI
# Used to determine the base key for each UI
ST_WIDGETS_PER_UI = 10


def calculator_ui(course_name: str, base_key: int) -> None:
    """Generate a Final Grade calculator UI for a given course"""
    st.header(course_name)

    desired_grade = st.number_input(
        "Enter your desired grade (in percent)",
        min_value=0,
        value=90,
        format="%d",
        key=base_key,
    )
    current_grade = st.number_input(
        "Enter your current grade (in percent)", key=base_key + 1
    )
    final_weight = st.number_input(
        (
            "Enter the weight of the final exam (how "
            "much of the overall course grade is "
            "determined by the final exam) (in percent)"
        ),
        0,
        100,
        20,
        format="%d",
        key=base_key + 2,
    )

    final_grade = determine_minimum_final_grade(
        current_grade / 100, final_weight / 100, desired_grade / 100
    )

    # Round to 2 decimal places as a percent
    final_grade = round(final_grade * 100, 2)

    st.write(
        "To get a ",
        desired_grade,
        " in ",
        course_name,
        " you need a ",
        final_grade,
        " on the final exam.",
    )


def ui() -> None:
    st.title("Final Exam Grade Calculator")
    st.subheader(".. on Azure")

    num_courses = int(
        st.number_input(
            "Enter the number of courses",
            min_value=0,
            value=1,
            step=1,
            format="%d"
        )
    )

    course_names = [""] * num_courses

    # Streamlit needed me to provide widget keys (probably because of the for loop)
    # So, I provide the index of the array as the key
    for i in range(0, num_courses):
        course_names[i] = st.text_input("Course name: ", key=i)

    # The calculator UI has multiple widgets (it increments the key for each)
    # So, I have to ensure that a. the base key for that widget isn't 0, and
    # b. Each UI has enough keys available. This is what the (i + 1) *
    # ST_WIDGETS_PER_UI does
    for i in range(0, num_courses):
        if course_names[i]:
            calculator_ui(course_names[i], (i + 1) * ST_WIDGETS_PER_UI)


if __name__ == "__main__":
    logger.info("Starting App")
    ui()
