from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StaticPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "css" / "portal.css").read_text(encoding="utf-8")
        cls.js = (ROOT / "js" / "script.js").read_text(encoding="utf-8")

    def test_matches_required_final_content(self):
        required_text = [
            "InfoInfo",
            "Informatyka",
            "Rozwiązuj z nami swoje problemy ze sprzętem i oprogramowaniem.",
            "Budujemy społeczność programistów.",
            "Wiadomości",
            "Artykuły",
            "Testy",
            "Porady",
            "Tutoriale",
            "Recenzje",
            "Twórcy portalu",
            "Anna",
            "Piotr",
            "Czekamy na Twoją opinię.",
            "Płock, al. Kilińskiego 12",
            "+48 24 366 41 28",
            "informatyka@wlodkowic.pl",
            "SWPW",
        ]

        for text in required_text:
            with self.subTest(text=text):
                self.assertIn(text, self.html)

    def test_main_sections_are_in_screen_order(self):
        section_ids = [
            "header-section",
            "hero-section",
            "categories-section",
            "about-section",
            "contact-section",
            "map-section",
            "footer-section",
        ]
        positions = [self.html.index(f'id="{section_id}"') for section_id in section_ids]

        self.assertEqual(positions, sorted(positions))

    def test_layout_has_final_visual_system(self):
        required_css = [
            "--hero-bg: #414c8f",
            "--categories-bg: #a8b1dd",
            "--authors-bg: #e8ebfb",
            "--contact-bg: #6175dc",
            "position: sticky",
            ".category-item",
            ".carousel-author-image",
            ".contact-card",
            "@media (max-width: 575.98px)",
        ]

        for token in required_css:
            with self.subTest(token=token):
                self.assertIn(token, self.css)

        self.assertIsNone(re.search(r"#app section[^}]+border-radius", self.css))

    def test_script_supports_interactions_without_overwriting_static_footer_year(self):
        self.assertIn("current-year", self.js)
        self.assertIn("IntersectionObserver", self.js)
        self.assertIn("needs-validation", self.js)
        self.assertIn("!yearElement.textContent.trim()", self.js)


if __name__ == "__main__":
    unittest.main()
