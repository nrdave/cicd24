"""
Test the app module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest
from app import ui


class Test(TestCase):
    def test_ui_title_and_header(self):
        at = AppTest.from_file("./src/app.py")
        at.run()

        assert at.title[0].value.startswith("Final Exam Grade")
        assert at.subheader[0].value.startswith("..")
        assert not at.exception
