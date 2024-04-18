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
            (desired_grade - (1 - final_weight) *
             current_course_grade) / final_weight
        )
    except ZeroDivisionError:
        required_grade = 0
        logger.info(
            "0 passed as a final exam weight. Setting required_grade to 0"
        )

    logger.info(f"Returning {required_grade}")
    return max(required_grade, 0)


def calculator_ui(course_name: str) -> None:
    """Generate a Final Grade calculator UI for a given course"""
    st.header(course_name)

    desired_grade = st.number_input(
        "Enter your desired grade (in percent)", min_value=0, value=90, format="%d")
    current_grade = st.number_input("Enter your current grade (in percent)")
    final_weight = st.number_input(
        (
            "Enter the weight of the final exam (how "
            "much of the overall course grade is "
            "determined by the final exam) (in percent)"
        ),
        0, 100, 20, format="%d"
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


if __name__ == "__main__":
    st.title("Final Exam Grade Calculator")
    st.subheader(".. on Azure")
    calculator_ui("test")
